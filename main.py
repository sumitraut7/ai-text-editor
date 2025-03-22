from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('grammar_correction.log')
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Dictionary to store models and tokenizers
models = {}
tokenizers = {}

def load_model_and_tokenizer(model_name):
    """Load model and tokenizer if not already loaded"""
    if model_name not in models:
        logger.info(f"Loading tokenizer for model: {model_name}")
        tokenizers[model_name] = AutoTokenizer.from_pretrained(model_name)
        logger.info(f"Loading model: {model_name}")
        models[model_name] = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        logger.info(f"Model {model_name} loaded successfully")

# Load default model at startup
DEFAULT_MODEL = "sumitraut7/gec_coedit_c4200m"
load_model_and_tokenizer(DEFAULT_MODEL)

def get_corrections_for_model(text, model_name):
    """Get corrections using specified model"""
    if model_name not in models:
        load_model_and_tokenizer(model_name)
    
    logger.info(f"Processing text with model {model_name}")
    tokenizer = tokenizers[model_name]
    model = models[model_name]
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=512)
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    logger.info(f"Generated correction : {corrected_text}")
    
    # Find differences between original and corrected text
    original_words = text.split()
    corrected_words = corrected_text.split()
    
    suggestions = []
    i = 0
    j = 0
    
    while i < len(original_words) and j < len(corrected_words):
        if original_words[i] != corrected_words[j]:
            suggestions.append({
                'original': original_words[i],
                'suggestion': corrected_words[j],
                'index': i
            })
            logger.info(f"Found correction: '{original_words[i]}' -> '{corrected_words[j]}'")
        i += 1
        j += 1
    
    logger.info(f"Total suggestions found: {len(suggestions)}")
    return suggestions

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/correct")
async def correct(text: str = Form(...), model: str = Form(DEFAULT_MODEL)):
    logger.info(f"Received correction request using model: {model}")
    suggestions = get_corrections_for_model(text, model)
    logger.info("Completed correction request")
    return {"suggestions": suggestions} 