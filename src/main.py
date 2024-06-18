import uvicorn
from fastapi import FastAPI
from transformers import pipeline

from src.schemas import TextInput, SummaryResponse


# You can choose another LLM following this link - https://huggingface.co/docs/transformers/index
summarizer = pipeline(task="summarization", model="google-t5/t5-small")
app = FastAPI()

 
@app.post("/summarize")
async def summarize(input: TextInput) -> SummaryResponse:
    summary_text = summarizer(input.text)[0]["summary_text"]
    return SummaryResponse(summary=summary_text)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
