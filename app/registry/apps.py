"""
JarvisOS Application Registry

Every desktop application known by Jarvis
is defined here.
"""

APPS = {

    # =====================================================
    # Browsers
    # =====================================================

    "brave": {
        "name": "Brave Browser",
        "exe": "brave.exe",
        "path": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "category": "browser",
    },

    "chrome": {
        "name": "Google Chrome",
        "exe": "chrome.exe",
        "path": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "category": "browser",
    },

    "edge": {
        "name": "Microsoft Edge",
        "exe": "msedge.exe",
        "path": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "category": "browser",
    },

    # =====================================================
    # Development
    # =====================================================

    "vscode": {
        "name": "Visual Studio Code",
        "exe": "Code.exe",
        "path": r"C:\Users\ASHISH\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "category": "development",
    },

    # =====================================================
    # Gaming
    # =====================================================

    "steam": {
        "name": "Steam",
        "exe": "steam.exe",
        "path": r"C:\Program Files (x86)\Steam\steam.exe",
        "category": "gaming",
    },

    # =====================================================
    # Communication
    # =====================================================

    "discord": {
        "name": "Discord",
        "exe": "Discord.exe",
        "path": None,
        "category": "communication",
    },

    # =====================================================
    # Music
    # =====================================================

    "apple_music": {
        "name": "Apple Music",
        "exe": "AppleMusic.exe",
        "path":r"C:\Program Files\WindowsApps\AppleInc.AppleMusicWin_1.1540.23042.0_x64__nzyj5cx40ttqa\AppleMusic.exe",
        "category": "music",
    
    },

    "spotify": {
        "name": "Spotify",
        "exe": "Spotify.exe",
        "path": None,
        "category": "music",
    },

    # =====================================================
    # Windows
    # =====================================================

    "notepad": {
        "name": "Notepad",
        "exe": "notepad.exe",
        "path": None,
        "category": "system",
    },

    "calculator": {
        "name": "Calculator",
        "exe": "calc.exe",
        "path": None,
        "category": "system",
    },

    "paint": {
        "name": "Paint",
        "exe": "mspaint.exe",
        "path": None,
        "category": "system",
    },

}