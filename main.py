from rich.console import Console
from app.brain.brain import JarvisBrain
from app.voice.speak import speak

console = Console()
brain = JarvisBrain()

console.print("[bold cyan]==================================[/bold cyan]")
console.print("[bold green]       JARVIS AI v0.1[/bold green]")
console.print("[bold cyan]==================================[/bold cyan]")

while True:
    user = input("\nYou: ")

    if user.lower() in ["exit", "quit"]:
        speak("Goodbye, Ashish!")
        break

    response = brain.think(user)
    speak(response)