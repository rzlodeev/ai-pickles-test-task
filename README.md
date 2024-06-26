# FastAPI Text Summarizer

## Setup

1. Create virtual environment:

`python -m venv env

source env/bin/activate`  

# On Windows use `env\Scripts\activate`

2. Install dependencies:

`pip install -r requirements.txt`

3. Run application:

`cd src/backend

fastapi run app.py`

4. Usage:

 - Send a POST request to `http://127.0.0.1:8000/summarize` with JSON body in a following format:

`{
    "input_text": "Text to summarize."
}`
