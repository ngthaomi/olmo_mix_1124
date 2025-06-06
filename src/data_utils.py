import re
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, substring
from pyspark.sql.types import StringType, ArrayType, IntegerType
from nltk.tokenize import word_tokenize
from emoji import demojize

def create_spark_session():
    return SparkSession.builder \
        .appName("Olmo Mix 1124 Sentiment Analysis") \
        .master("local[*]") \
        .config("spark.driver.memory", "16g") \
        .config("spark.executor.memory", "8g") \
        .config("spark.sql.shuffle.partitions", "4") \
        .getOrCreate()

def load_data(spark, path):
    return spark.read.parquet(path)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[\\n\\r]', ' ', text)
    text = re.sub(r'[^\\w\\s]', '', text.lower())
    text = re.sub(r'\\d+', '', text)
    text = re.sub(r'\\s+', ' ', text).strip()
    text = demojize(text)
    text = re.sub(r'[^\\w\\s:]', '', text.lower())
    return text

def tokenize_text(text):
    if not isinstance(text, str) or text.strip() == "":
        return []
    return word_tokenize(text)

clean_udf = udf(clean_text, StringType())
tokenize_udf = udf(tokenize_text, ArrayType(StringType()))

def extract_domain(url):
    from urllib.parse import urlparse
    if not isinstance(url, str):
        return ""
    parsed = urlparse(url)
    return parsed.netloc or ""