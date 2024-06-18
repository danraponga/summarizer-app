A simple web application that integrates an AI-powered text summarization service using FastAPI and Hugging Face.

## SetUp

Install dependencies:
```
pip install -r requirements.txt
```
Run the project:

```
python -m src.main
```

Then navigate to `http://127.0.0.1:8000/docs` and use /summarize endpoint

**or**

Make the request:

 `curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d '{"text": "<Your text here>"}'`

