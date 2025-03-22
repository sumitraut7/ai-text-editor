# Grammar Correction Tool

This is a web application that uses a Hugging Face transformer model to provide grammar correction suggestions for text input.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

## Usage

1. Enter your text in the text box
2. Click "Show Corrections" to get grammar suggestions
3. For each suggestion:
   - Click "Accept" to apply the correction
   - Click "Decline" to ignore the suggestion

## Model Information

This application uses the grammar correction model `sumitraut7/gec_coedit_c4200m` from Hugging Face. 