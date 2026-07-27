import ollama


class JarvisBrain:
    def __init__(self):
        self.model = "qwen2.5:3b"

    def think(self, message: str) -> str:
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are JARVIS, the AI assistant created by Ashish Tripathi. "
                            "Always answer in plain English. "
                            "Do not use Markdown. "
                            "Do not use LaTeX. "
                            "Do not use bullet points unless the user requests them. "
                            "Keep answers concise unless the user asks for a detailed explanation. "
                            "If you mention equations, write them in normal text, for example: "
                            "'Voltage = Current × Resistance' instead of mathematical notation."
                        ),
                    },
                    {
                        "role": "user",
                        "content": message,
                    },
                ],
            )

            return response["message"]["content"]

        except Exception as e:
            return f"Error: {e}"