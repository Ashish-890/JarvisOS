<div align="center">

# 🤖 JarvisOS

### An Offline AI Operating System inspired by J.A.R.V.I.S.

Voice-controlled • Private • Local • Modular

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local_AI-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

</div>

---

# 📖 About

JarvisOS is an offline AI assistant built entirely in Python.

Inspired by Tony Stark's J.A.R.V.I.S., the goal of this project is to create a fully featured AI operating system capable of understanding voice commands, controlling the computer, remembering conversations, seeing the screen, and assisting with everyday tasks—all while running locally.

Unlike cloud-based assistants, JarvisOS prioritizes:

- 🔒 Privacy
- ⚡ Speed
- 📴 Offline operation
- 🧩 Modular architecture

---

# ✨ Current Features

## 🧠 AI Brain

- Ollama integration
- Qwen 2.5 Language Model
- Completely offline responses
- Natural conversations

---

## 🎙 Voice Assistant

- Wake Word Detection ("Hey Jarvis")
- Speech-to-Text using Faster Whisper
- Text-to-Speech
- Continuous conversations
- Automatic silence detection
- Sleep mode after inactivity

---

## ⚙ Core System

- Modular architecture
- Error handling
- Clean project structure
- Git version control

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Ollama | Local LLM runtime |
| Qwen 2.5 | AI model |
| Faster Whisper | Speech recognition |
| OpenWakeWord | Wake word detection |
| pyttsx3 | Text-to-Speech |
| SoundDevice | Audio input |
| NumPy | Audio processing |
| Rich | Terminal UI |

---

# 📂 Project Structure

```text
JarvisOS/
│
├── app/
│   ├── brain/
│   ├── voice/
│   ├── actions/
│   ├── memory/
│   ├── vision/
│   └── utils/
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Ashish-890/JarvisOS.git

cd JarvisOS
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download from:

https://ollama.com/

---

## 5. Download the AI model

```bash
ollama pull qwen2.5:3b
```

---

## 6. Run JarvisOS

```bash
python main.py
```

---

# 🎤 Example

```
You:
Hey Jarvis

Jarvis:
Yes Ashish?

You:
What is Ohm's Law?

Jarvis:
Ohm's Law states that Voltage equals Current multiplied by Resistance.
```

---

# 🗺 Roadmap

## ✅ v0.5

- Offline AI
- Wake Word
- Whisper
- Text-to-Speech
- Continuous Conversations

---

## 🚧 v0.6

Desktop Automation

- Open Chrome
- Open VS Code
- Search Google
- Open folders
- Lock computer
- Launch applications

---

## 🚧 v0.7

Memory System

- Long-term memory
- User preferences
- Conversation history
- Personal knowledge base

---

## 🚧 v0.8

Vision

- Screenshot understanding
- OCR
- Image analysis
- Webcam support

---

## 🚧 v0.9

Internet & Agents

- Web Search
- File Management
- Coding Assistant
- Terminal Control

---

## 🎯 v1.0

JarvisOS

- Fully offline AI Operating System
- Desktop Automation
- Memory
- Vision
- Internet Tools
- Coding Assistant
- Plugin System

---

# 🤝 Contributing

Contributions, ideas, and feature requests are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 👨‍💻 Author

**Ashish Tripathi**

Electrical Engineering Student

AI Developer

GitHub:
https://github.com/Ashish-890

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

<div align="center">

### JarvisOS

*"Sometimes you gotta run before you can walk."*

— Tony Stark

</div>
