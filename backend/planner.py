class Planner:
    def __init__(self):
        pass

    def plan(self, question):
        q = question.lower()

        if any(word in q for word in ["what does", "overview", "project", "purpose"]):
            return {
                "top_k": 5,
                "mode": "broad"
            }
        
        if any(word in q for word in ["file", "function", "class", "how does"]):
            return {
                "top_k": 3,
                "mode": "focused"
            }
        
        return {
            "top_k": 3,
            "mode": "default"
        }
    
if __name__ == "__main__":
    planner = Planner()

    questions = [
        "What does this project do?",
        "Explain loader.py",
        "How does the retriever work?"
    ]

    for q in questions:
        print(q, "->", planner.plan(q))