import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from pyspark.sql.types import StructType, StructField, FloatType

nltk.download('vader_lexicon')

def initialize_vader():
    return SentimentIntensityAnalyzer()

def vader_sentiment(text, sid):
    if not isinstance(text, str) or text.strip() == "":
        return {"compound": 0.0, "pos": 0.0, "neu": 0.0, "neg": 0.0}
    return sid.polarity_scores(text)

vader_schema = StructType([
    StructField("compound", FloatType(), nullable=True),
    StructField("pos", FloatType(), nullable=True),
    StructField("neu", FloatType(), nullable=True),
    StructField("neg", FloatType(), nullable=True)
])

def initialize_finbert():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert", use_fast=True)
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)
    return pipeline(
        task="sentiment-analysis",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1,
        torch_dtype=torch.float16,
        return_all_scores=True,
        truncation=True,
        padding=True,
        max_length=512,
        batch_size=32
    )

def analyze_finbert(text, pipeline):
    chunks = [text[i:i+510] for i in range(0, len(text), 510)]
    if not chunks or all(not c.strip() for c in chunks):
        return "neutral", 0.0, 0.0, {"positive": 0.0, "neutral": 1.0, "negative": 0.0}
    results = pipeline(chunks)
    cumulative = {"positive": 0.0, "neutral": 0.0, "negative": 0.0}
    count = 0
    for r in results:
        for entry in r:
            label = entry["label"].lower()
            cumulative[label] += entry["score"]
        count += 1
    avg_scores = {k: v / count for k, v in cumulative.items()}
    polarity = avg_scores["positive"] - avg_scores["negative"]
    return "neutral" if abs(polarity) < 0.15 else ("positive" if polarity > 0 else "negative"), polarity, max(r["score"] for r in results) / count, avg_scores