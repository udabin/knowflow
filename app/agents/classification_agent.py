from sentence_transformers import SentenceTransformer, util

class ClassificationAgent:
    def __init__(self):
        self.model = SentenceTransformer("snunlp/KR-SBERT-V40K-klueNLI-augSTS")

        # 예시 카테고리
        self.categories = {
            "정치" : "이 문장은 정치와 관련 있어",
            "경제" : "이 문장은 경제와 관련 있어",
            "과학" : "이 문장은 과학에 대한 내용이야",
            "기술" : "이 문장은 기술에 대한 내용이야",
            "기타" : "이 문장은 일반적인 내용이야"
        }

        self.category_embeddings = {
            k: self.model.encode(v, convert_to_tensor=True)
            for k, v in self.categories.items()
        }

    def run(self, query: str):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        similarities = {
            cat: util.cos_sim(query_embedding, emb).item()
            for cat, emb in self.category_embeddings.items()
        }
        best_category = max(similarities, key=similarities.get)

        # return f"[ClassificationAgent] 분류 처리: {query}"
        return f"[Classificat6ionAgent] 예측된 카테고리: {best_category} (유사도: {similarities[best_category]:.3f})"
    