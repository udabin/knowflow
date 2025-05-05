from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from typing import List, Dict

class NERAgent:
    def __init__(self):
        model_name = "monologg/koelectra-base-v3-discriminator"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")

    def run(self, text: str) -> Dict:
        """NER 추출 실행"""
        entities = self.nlp(text)
        simplified = [
            {"text": ent["word"], "label": ent["entity_group"], 
            "score": round(float(ent["score"]), 3)}
            for ent in entities
        ]
        return {
            "input": text,
            "entities": simplified
        }