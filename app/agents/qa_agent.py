from core.generator import generate_answer

class QAAgent:
    def run(self, query: str, docs=None):
        # return f"[QAAgent] 질의응답 처리: {query}"
        try:
            answer = generate_answer(query)
            return answer
        except Exception as e:
            return f"[QAAgent] 오류 발생: {str(e)}"