from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn, os

from utils import translate 

# Initialize the app 
app = FastAPI(title='Neural machine translation')
class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    translation: str

@app.get('/')
async def home():
    return {'Hello I am youssef kamel'}

@app.post("/translate/", response_model=TranslationResponse)
async def translate2(request: TranslationRequest):
    translated_sentence = translate(request.text)
    return TranslationResponse(translation=translated_sentence)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
