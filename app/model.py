from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=-1  # force CPU
)

def analyze(text: str):
    result = sentiment_model(text[:512])[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"] * 100, 2)
    }