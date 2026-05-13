const banglishInput = document.getElementById('banglish-input');
const banglaOutput = document.getElementById('bangla-output');
const charCount = document.getElementById('char-count');
const clearBtn = document.getElementById('clear-btn');
const copyBtn = document.getElementById('copy-btn');
const toast = document.getElementById('toast');
const statWords = document.getElementById('stat-words');
const statKnown = document.getElementById('stat-known');

const voiceBtn = document.getElementById('voice-btn');

const historyList = document.getElementById('history-list');

let debounceTimer;

// History Logic
function saveToHistory(banglish, bangla) {
    if (!banglish || !bangla) return;
    let history = JSON.parse(localStorage.getItem('banglish_history') || '[]');
    // Remove if already exists (to move to top)
    history = history.filter(item => item.banglish !== banglish);
    history.unshift({ banglish, bangla, time: new Date().toISOString() });
    history = history.slice(0, 10); // Keep last 10
    localStorage.setItem('banglish_history', JSON.stringify(history));
    renderHistory();
}

function renderHistory() {
    if (!historyList) return;
    const history = JSON.parse(localStorage.getItem('banglish_history') || '[]');
    historyList.innerHTML = history.map(item => `
        <div class="history-item" onclick="loadHistory('${item.banglish}')">
            <span class="h-banglish">${item.banglish}</span>
            <span class="h-bangla">${item.bangla}</span>
        </div>
    `).join('');
}

window.loadHistory = (text) => {
    banglishInput.value = text;
    charCount.textContent = `${text.length} characters`;
    convertText(text);
};

// Voice Input (Web Speech API)
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US'; // English script for Banglish
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
        voiceBtn.classList.add('recording');
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        banglishInput.value += (banglishInput.value ? ' ' : '') + transcript;
        charCount.textContent = `${banglishInput.value.length} characters`;
        convertText(banglishInput.value);
    };

    recognition.onend = () => {
        voiceBtn.classList.remove('recording');
    };

    recognition.onerror = () => {
        voiceBtn.classList.remove('recording');
    };

    voiceBtn.addEventListener('click', () => {
        if (voiceBtn.classList.contains('recording')) {
            recognition.stop();
        } else {
            recognition.start();
        }
    });
} else {
    voiceBtn.style.display = 'none';
}

// Fetch stats on load
async function fetchStats() {
    try {
        const response = await fetch('/stats');
        const data = await response.json();
        statWords.textContent = data.total_words_in_dict.toLocaleString();
        statKnown.textContent = data.known_mappings.toLocaleString();
    } catch (error) {
        console.error('Error fetching stats:', error);
    }
}

// Convert text via API
async function convertText(text) {
    if (!text.trim()) {
        banglaOutput.value = '';
        return;
    }

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        banglaOutput.value = data.converted;
        
        // Save to history only if it's a short phrase (to avoid clutter)
        if (text.length < 100) {
            saveToHistory(text, data.converted);
        }
    } catch (error) {
        console.error('Conversion error:', error);
    }
}

// Event Listeners
banglishInput.addEventListener('input', (e) => {
    const text = e.target.value;
    charCount.textContent = `${text.length} characters`;

    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        convertText(text);
    }, 300); // 300ms debounce
});

clearBtn.addEventListener('click', () => {
    banglishInput.value = '';
    banglaOutput.value = '';
    charCount.textContent = '0 characters';
    banglishInput.focus();
});

copyBtn.addEventListener('click', () => {
    if (!banglaOutput.value) return;
    
    navigator.clipboard.writeText(banglaOutput.value).then(() => {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    });
});

// Initial load
fetchStats();
// Refresh stats periodically
setInterval(fetchStats, 10000);
