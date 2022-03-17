# -*- coding: utf-8 -*-
from pathlib import Path
from dotenv import load_dotenv
from flaskapp import create_app
import os

try:
    load_dotenv(Path(__file__).resolve().parent / ".flaskenv")
except FileNotFoundError:
    pass

app = create_app()

if __name__ == "__main__":
    app.run(
        host=str(os.environ.get("FLASK_IP", "127.0.0.1")), 
        port=int(os.environ.get("FLASK_PORT", 5000)), 
        debug=bool(os.environ.get("FLASK_DEBUG", False))
    )
