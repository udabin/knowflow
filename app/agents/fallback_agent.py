class FallbackAgent:
    def run(self, query: str):
        return f"[FallbackAgent] 처리할 수 없는 요청: {query}"