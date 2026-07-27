import re
import time

from rich.console import Console

from app.brain.brain import JarvisBrain
from app.voice.listen import listen
from app.voice.speak import speak
from app.voice.wakeword import WakeWordDetector


class Jarvis:

    def __init__(self):

        self.console = Console()

        self.brain = JarvisBrain()
        self.detector = WakeWordDetector()

        self.exit_words = {
            "exit",
            "quit",
            "goodbye",
            "bye",
            "shutdown jarvis",
        }

    def should_exit(self, text: str) -> bool:

        command = re.sub(r"[^\w\s]", "", text.lower()).strip()

        return any(word in command for word in self.exit_words)

    def startup(self):

        self.console.print("[bold cyan]====================================[/bold cyan]")
        self.console.print("[bold green]        JARVIS AI v0.5[/bold green]")
        self.console.print("[bold cyan]====================================[/bold cyan]")

        speak("Hello Ashish. JARVIS is online.")

    def sleep(self):

        speak("Going back to sleep.")

        # Give Windows a moment to release the microphone
        time.sleep(1)

    def run(self):

        self.startup()

        while True:

            # -----------------------------
            # WAIT FOR WAKE WORD
            # -----------------------------
            self.detector.wait_for_wake_word()

            speak("Yes Ashish?")

            # -----------------------------
            # CONVERSATION LOOP
            # -----------------------------
            while True:

                try:

                    user = listen()

                    # Nobody spoke
                    if not user:

                        self.sleep()

                        break

                    self.console.print(f"\n[cyan]You:[/cyan] {user}")

                    # Exit
                    if self.should_exit(user):

                        speak("Goodbye Ashish.")

                        return

                    self.console.print("[yellow]Thinking...[/yellow]")

                    reply = self.brain.think(user)

                    if not reply.strip():

                        speak("I didn't quite understand that.")

                        continue

                    self.console.print(f"\n[green]Jarvis:[/green] {reply}")

                    speak(reply)

                except KeyboardInterrupt:

                    speak("Goodbye Ashish.")

                    return

                except Exception as e:

                    self.console.print(f"[red]Error:[/red] {e}")

                    speak("Something went wrong.")

                    break