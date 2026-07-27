from collections import deque


class ConversationContext:
    """
    Stores the current conversation history.

    This history is sent to the AI so it can remember
    what has already been discussed during the current
    conversation.

    The history is cleared whenever Jarvis goes back
    to sleep.
    """

    def __init__(self, max_history=20):

        self.history = deque(maxlen=max_history)

    # =====================================================
    # Add Message
    # =====================================================

    def add(self, role: str, content: str):

        self.history.append(

            {
                "role": role,
                "content": content,
            }

        )

    # =====================================================
    # Conversation
    # =====================================================

    def conversation(self):

        return list(self.history)

    # =====================================================
    # Helpers
    # =====================================================

    def last_user(self):

        for message in reversed(self.history):

            if message["role"] == "user":

                return message["content"]

        return None

    def last_assistant(self):

        for message in reversed(self.history):

            if message["role"] == "assistant":

                return message["content"]

        return None

    # =====================================================
    # Reset
    # =====================================================

    def clear(self):

        self.history.clear()

    # =====================================================
    # Length
    # =====================================================

    def __len__(self):

        return len(self.history)

    # =====================================================
    # Debug
    # =====================================================

    def __str__(self):

        return f"ConversationContext(messages={len(self.history)})"