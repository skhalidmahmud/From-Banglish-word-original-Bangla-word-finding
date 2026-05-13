import os
import sys
import subprocess

def install_dependencies():
    print("Checking dependencies...")
    try:
        import fastapi
        import uvicorn
    except ImportError:
        print("Installing required packages (fastapi, uvicorn)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    install_dependencies()
    
    print("\n" + "="*50)
    print("Banglish-to-Bangla Smart Converter is starting!")
    print("API & UI will be available at: http://localhost:8000")
    print("="*50 + "\n")
    
    # Run the FastAPI app
    try:
        import uvicorn
        uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")

if __name__ == "__main__":
    main()
