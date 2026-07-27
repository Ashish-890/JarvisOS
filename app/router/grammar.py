"""
JarvisOS Grammar

Defines the natural language vocabulary understood by Jarvis.

The classifier imports these groups instead of hardcoding
dozens of regexes.
"""

# ==========================================================
# OPEN
# ==========================================================

OPEN_WORDS = {
    "open",
    "launch",
    "start",
    "run",
}

# ==========================================================
# CLOSE
# ==========================================================

CLOSE_WORDS = {
    "close",
    "quit",
    "terminate",
    "kill",
    "exit",
    "stop",
}

# ==========================================================
# SEARCH
# ==========================================================

SEARCH_WORDS = {
    "search",
    "find",
    "lookup",
    "look up",
    "google",
}

# ==========================================================
# YOUTUBE
# ==========================================================

YOUTUBE_WORDS = {
    "youtube",
    "watch",
    "watch on youtube",
    "search youtube",
    "find on youtube",
}

# ==========================================================
# GITHUB
# ==========================================================

GITHUB_WORDS = {
    "github",
    "search github",
    "find on github",
}

# ==========================================================
# MUSIC
# ==========================================================

PLAY_WORDS = {
    "play",
    "resume",
}

PAUSE_WORDS = {
    "pause",
    "stop music",
}

NEXT_WORDS = {
    "next",
    "next song",
    "skip",
}

PREVIOUS_WORDS = {
    "previous",
    "previous song",
    "back",
}

# ==========================================================
# FILES
# ==========================================================

FILE_WORDS = {
    "open folder",
    "find file",
    "documents",
    "downloads",
    "desktop",
}

# ==========================================================
# SYSTEM
# ==========================================================

SYSTEM_WORDS = {
    "shutdown",
    "restart",
    "lock",
    "sleep",
    "volume",
    "brightness",
    "screenshot",
}

# ==========================================================
# MEMORY
# ==========================================================

MEMORY_WORDS = {
    "remember",
    "forget",
    "recall",
}