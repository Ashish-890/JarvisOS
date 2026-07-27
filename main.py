from rich.console import Console

from app.brain.brain import JarvisBrain
from app.voice.listen import listen
from app.voice.speak import speak

console = Console()
brain = JarvisBrain()

console.print("[bold cyan]====================================[/bold cyan]")
console.print("[bold green]        JARVIS AI v0.3[/bold green]")
console.print("[bold cyan]====================================[/bold cyan]")

speak("Hello Ashish. JARVIS is online.")

while True:

    user = listen()

    console.print(f"\n[cyan]You:[/cyan] {user}")

    if user.lower() in ["exit", "quit", "goodbye"]:
        speak("Goodbye Ashish.")
        break

    console.print("[yellow]Thinking...[/yellow]")

    reply = brain.think(user)

    console.print(f"\n[green]Jarvis:[/green] {reply}")

    speak(reply)