from app.agents.summary_agent import SummaryAgent
from app.agents.qa_agent import QAAgent
from app.agents.ner_agent import NERAgent
from app.agents.classification_agent import ClassificationAgent
from app.agents.fallback_agent import FallbackAgent

from sentence_transformers import SentenceTransformer, util


class AgentRouter:
    def __init__(self):
        self.agents = {
            "summary": SummaryAgent(),
            "qa": QAAgent(),
            "ner": NERAgent(),
            "classifier": ClassificationAgent(),
            "fallback": FallbackAgent()
        }

        self.model = SentenceTransformer("snunlp/KR-SBERT-V40K-klueNLI-augSTS")

        # task_templates
        self.task_templates = {
            "summary" : [
                "이 문장을 요약해줘", "간단히 정리해줘", "핵심만 말해줘"],
            "qa" : [
                "이 문장에 대해 궁금한 점에 답해줘", "정보를 알려줘", "답변해줘", "무엇인지 설명해줘"],
            "ner" : [
                "이 문장에서 주요 키워드를 추출해줘", "핵심어를 뽑아줘"],
            "classifier" : [
                "이 문장을 어떤 카테고리에 속하는지 분류해줘", "이 문장의 주제는 뭐야?"]
        }

        self.task_embeddings = {
            task: [self.model.encode(temp, convert_to_tensor=True) for temp in temps]
            for task, temps in self.task_templates.items()
        }
    
    def classify_task(self, user_input: str) -> str:
        # """룰 기반 시작 -> 분류 모델 기반으로 변경하거나 임베딩 유사도 기반으로 변경 예정"""
        """Rule-based 1차 처리"""
        q_words = ["무엇", "왜", "어디", "누가", "언제", "어떻게", "얼마", "몇", "?"]
        if any(q in user_input for q in q_words):
            return "qa"
        elif "요약" in user_input:
            return "summary"
        elif "키워드" in user_input:
            return "ner"
        elif "분류" in user_input or "카테고리" in user_input:
            return "classifier"
        # else:
        #     return "fallback"  # fallback

        """다중 템플릿 기반 임베딩 유사도 계산 2차 처리"""
        input_embedding = self.model.encode(user_input, convert_to_tensor=True)

        similarities = {}
        for task, embeds in self.task_embeddings.items():
            scores = [util.cos_sim(input_embedding, e).item() for e in embeds]
            similarities[task] = max(scores)

        # print(f"[Router] Similarities: {similarities}")

        best_task = max(similarities, key=similarities.get)
        # return best_task
        if similarities[best_task] > 0.3:
            return best_task
        else:
            return "fallback"

        print(f"[Router] Similarities: {similarities}, Best: {best_task}, Score: {similarities[best_task]}")
       
        # print(f"[Router] User input: {user_input}") 

    def route(self, user_input: str):
        """입력에 따라 적절한 에이전트를 선택"""
        task_type = self.classify_task(user_input)
        # return self.agents.get(task_type, self.agents["fallback"]).run(user_input)
        return self.agents[task_type].run(user_input)

router = AgentRouter()

def route_query(user_input: str):
    return router.route(user_input)