import re
import time
import traceback

from rich.console import Console

from app.actions.dispatcher import Dispatcher
from app.brain.brain import JarvisBrain
from app.config import settings
from app.memory.context import ConversationContext
from app.router.router import Router
from app.voice.listen import listen
from app.voice.speak import speak
from app.voice.wakeword import WakeWordDetector


class Jarvis:

    VERSION = "v0.8.0"

    EXIT_WORDS = {
        "exit",
        "quit",
        "bye",
        "goodbye",
        "shutdown jarvis",
        "stop jarvis",
    }

    def __init__(self):

        self.console = Console()

        self.detector = WakeWordDetector()
        self.router = Router()
        self.dispatcher = Dispatcher()
        self.brain = JarvisBrain()

        self.context = ConversationContext()

    # =====================================================
    # Startup
    # =====================================================

    def startup(self):

        self.console.print()

        self.console.rule(
            f"[bold cyan]JARVIS OS {self.VERSION}"
        )

        self.console.print()

        speak("Hello Ashish. Jarvis is online.")

    # =====================================================
    # Shutdown
    # =====================================================

    def shutdown(self):

        self.console.print()

        self.console.print(
            "[bold red]Shutting down...[/bold red]"
        )

        speak("Goodbye Ashish.")

    # =====================================================
    # Sleep
    # =====================================================

    def sleep(self):

        self.console.print(
            "[blue]Sleeping...[/blue]"
        )

        self.context.clear()

        speak("Going back to sleep.")

        time.sleep(1)

    # =====================================================
    # Helpers
    # =====================================================

    def should_exit(self, text: str) -> bool:

        cleaned = re.sub(
            r"[^\w\s]",
            "",
            text.lower(),
        ).strip()

        return cleaned in self.EXIT_WORDS

    def debug(self, command):

        if not getattr(settings, "DEBUG", False):
            return

        self.console.print(
            f"[magenta]Intent:[/magenta] {command.intent.value}"
        )

        self.console.print(
            f"[dim]{command}[/dim]"
        )

    # =====================================================
    # AI
    # =====================================================

    def ask_brain(self, user: str) -> str:

        self.console.print(
            "[yellow]Thinking...[/yellow]"
        )

        try:

            reply = self.brain.think(user)

            if not isinstance(reply, str):

                return str(reply)

            return reply

        except Exception as e:

            self.console.print(
                f"[red]Brain Error:[/red] {e}"
            )

            if getattr(settings, "DEBUG", False):

                traceback.print_exc()

            return (
                "Sorry, I had trouble thinking about that."
            )

    # =====================================================
    # Process
    # =====================================================

    def process(self, user: str):

        self.context.add(
            "user",
            user,
        )

        command = self.router.route(user)

        self.debug(command)

        try:

            reply, handled = self.dispatcher.dispatch(
                command
            )

        except Exception as e:

            self.console.print(
                f"[red]Dispatcher Error:[/red] {e}"
            )

            if getattr(settings, "DEBUG", False):

                traceback.print_exc()

            reply = None

            handled = False

        # ------------------------------------------
        # AI fallback
        # ------------------------------------------

        if not handled:

            reply = self.ask_brain(user)

        # ------------------------------------------
        # Safety
        # ------------------------------------------

        if reply is None:

            reply = "I'm not sure how to respond."

        elif not isinstance(reply, str):

            reply = str(reply)

        self.context.add(
            "assistant",
            reply,
        )

        self.console.print()

        self.console.print(
            f"[green]Jarvis:[/green] {reply}"
        )

        speak(reply)

    # =====================================================
    # Conversation
    # =====================================================

    def conversation(self):

        speak("Yes Ashish?")

        while True:

            user = listen()

            if not user:

                self.sleep()

                return

            self.console.print()

            self.console.print(
                f"[cyan]You:[/cyan] {user}"
            )

            if self.should_exit(user):

                raise KeyboardInterrupt

            try:

                self.process(user)

            except Exception as e:

                self.console.print()

                self.console.print(
                    f"[bold red]Conversation Error:[/bold red] {e}"
                )

                if getattr(settings, "DEBUG", False):

                    traceback.print_exc()

                speak(
                    "Something went wrong."
                )

    # =====================================================
    # Main Loop
    # =====================================================

    def run(self):

        self.startup()

        while True:

            try:

                self.detector.wait_for_wake_word()

                self.conversation()

            except KeyboardInterrupt:

                self.shutdown()

                break

            except Exception as e:

                self.console.print()

                self.console.print(
                    f"[bold red]Fatal Error:[/bold red] {e}"
                )

                if getattr(settings, "DEBUG", False):

                    traceback.print_exc()

                speak(
                    "A fatal error occurred."
                )

                time.sleep(1)