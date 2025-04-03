# AI-Powered Text Editing Tool

This project provides an AI-powered text editing tool capable of refining text based on various prompts. The tool can handle tasks such as clarity enhancement, coherence improvement, grammatical error correction (GEC), neutrality adjustment, paraphrasing, and simplification.

## Features
- **Clarity Enhancement** – Rewrite sentences for better readability.
- **Coherence Improvement** – Ensure logical flow in text.
- **Grammar Error Correction (GEC)** – Fix grammatical mistakes.
- **Neutralization** – Adjust the tone to be more neutral.
- **Paraphrasing** – Reword sentences while maintaining meaning.
- **Simplification** – Make complex text more understandable.
- **Default GEC Mode** – By default, the model will perform grammatical error correction if no specific prompt is provided.

## Setup

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
2. **Access the web interface:**
   Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Usage Examples

### Clarity Enhancement
**Prompt:** Rewrite this sentence clearly:  
*The method was not able to utilize the available huge amount of monolingual data because of the inability of models to differentiate between the authentic and synthetic parallel data.*  
**Output:**  
*The method was not able to utilize the available huge amount of monolingual data because of the inability of models to differentiate between the authentic and synthetic parallel data during training.*  

### Neutralization
**Prompt:** Make this text more neutral:  
*Chloroform "the molecular lifesaver" an article at Oxford University providing interesting facts about chloroform.*  
**Output:**  
*Chloroform "the molecular lifesaver" an article at Oxford University providing facts about chloroform.*  

### Paraphrasing
**Prompt:** Reword this text:  
*She stopped when she saw his expression.*  
**Output:**  
*Seeing the look on his face, she paused.*  

### Simplification
**Prompt:** Write a simpler version for the sentence:  
*There's one other brave person I know.*  
**Output:**  
*I know another brave person here too.*  

### Grammar Error Correction (GEC)
**Prompt:** Remove all grammatical errors from this text:  
*For example, countries with a lot of deserts can terraform their desert to increase their habitable land and using irrigation to provide clean water to the desert.*  
**Output:**  
*For example, countries with a lot of deserts can transform their desert to increase their habitable land and use irrigation to provide clean water to the desert.*  

### Default Mode (Grammar Error Correction)
If no specific prompt is provided, the model will automatically correct grammatical errors in the input text.

## Model Information
This application utilizes the grammar correction model `sumitraut7/gec_coedit_c4200m` from Hugging Face.


---

This tool enables users to improve their writing effortlessly with AI-powered refinements. Feel free to contribute, raise issues, or suggest improvements!

