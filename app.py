from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from converter import BanglishConverter
import os

app = FastAPI(title="Banglish-to-Bangla API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the converter
converter = BanglishConverter()

class TranslationRequest(BaseModel):
    text: str

@app.post("/convert")
async def convert_text(request: TranslationRequest):
    if not request.text:
        return {"original": "", "converted": ""}
    
    try:
        converted = converter.convert_sentence(request.text)
        return {
            "original": request.text,
            "converted": converted
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats():
    return {
        "known_mappings": len(converter.b2b_map),
        "generator_rules": len(converter.generator_map),
        "dictionaries_loaded": len(converter.word_lists),
        "total_words_in_dict": sum(len(wlist) for wlist in converter.word_lists)
    }

# Serve static files (Frontend)
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
