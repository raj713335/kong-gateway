import uvicorn
from fastapi import FastAPI
from typing import Dict
#Use the below command to create virtual environment and install dependencies
# python3 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && pip install fastapi uvicorn[standard] && pip freeze > requirements.txt && python -c "import fastapi, uvicorn; print('fastapi', fastapi.__version__); print('uvicorn', uvicorn.__version__)"

app = FastAPI(title="Kong Gateway Mock")

@app.get("/healthy")

def health_check() -> Dict[str, str]:
    return {"status": "Healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
