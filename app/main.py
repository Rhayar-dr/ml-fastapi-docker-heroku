from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline, translate_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


class TranslationOut(BaseModel):
    translation: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

@app.post("/translation", response_model=TranslationOut)
def translation(payload: TextIn):
    translation = translate_pipeline(payload.text)
    return {"translation": translation}
