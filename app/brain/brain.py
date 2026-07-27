from pathlib import Path

import ollama


class JarvisBrain:
    """
    JarvisOS Brain

    Responsible only for communicating with the LLM.
    """

    def __init__(self):

        # --------------------------------------------------
        # Model Configuration
        # --------------------------------------------------

        self.model = "qwen2.5:3b"

        self.temperature = 0.3

        # --------------------------------------------------
        # Load System Prompt
        # --------------------------------------------------

        self.system_prompt = self._load_system_prompt()

    # ======================================================
    # Prompt Loader
    # ======================================================

    def _load_system_prompt(self):

        try:

            prompt_path = (
                Path(__file__)
                .parent.parent
                / "prompts"
                / "system.txt"
            )

            with open(
                prompt_path,
                "r",
                encoding="utf-8",
            ) as file:

                return file.read().strip()

        except Exception:

            return (
                "You are JARVIS, a professional AI assistant."
            )

    # ======================================================
    # Message Builder
    # ======================================================

    def build_messages(
        self,
        prompt,
        history=None,
    ):

        messages = [

            {
                "role": "system",
                "content": self.system_prompt,
            }

        ]

        if history:

            messages.extend(history)

        # Prevent duplicate user message
        if (
            not history
            or history[-1]["role"] != "user"
            or history[-1]["content"] != prompt
        ):

            messages.append(

                {
                    "role": "user",
                    "content": prompt,
                }

            )

        return messages

    # ======================================================
    # Clean Response
    # ======================================================

    def clean_response(self, text):

        if not text:

            return (
                "I'm sorry, I couldn't generate a response."
            )

        text = text.strip()

        while "\n\n\n" in text:

            text = text.replace(
                "\n\n\n",
                "\n\n",
            )

        return text

    # ======================================================
    # Think
    # ======================================================

    def think(
        self,
        prompt,
        history=None,
    ):

        try:

            messages = self.build_messages(
                prompt,
                history,
            )

            response = ollama.chat(

                model=self.model,

                messages=messages,

                options={
                    "temperature": self.temperature,
                },

            )

            return self.clean_response(

                response["message"]["content"]

            )

        except Exception as error:

            return (
                "I'm having trouble communicating with my AI model.\n"
                f"Error: {error}"
            )

    # ======================================================
    # Configuration
    # ======================================================

    def set_model(self, model):

        self.model = model

    def get_model(self):

        return self.model

    def set_temperature(self, temperature):

        self.temperature = temperature

    def get_temperature(self):

        return self.temperature

    # ======================================================
    # Prompt Management
    # ======================================================

    def reload_prompt(self):

        self.system_prompt = self._load_system_prompt()

    def set_prompt(self, prompt):

        self.system_prompt = prompt

    def get_prompt(self):

        return self.system_prompt

    # ======================================================
    # Future Features
    # ======================================================

    def think_stream(
        self,
        prompt,
        history=None,
    ):
        """
        Reserved for streaming responses.

        Will be implemented in a future version.
        """
        raise NotImplementedError

    def think_with_tools(
        self,
        prompt,
        history=None,
    ):
        """
        Reserved for Tool Calling.

        Future JarvisOS versions will execute
        tools through this method.
        """
        raise NotImplementedError