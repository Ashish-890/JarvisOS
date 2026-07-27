import os

COMMON_LOCATIONS = [

    r"C:\Program Files",

    r"C:\Program Files (x86)",

    r"C:\Users\ASHISH\AppData\Local",

    r"C:\Users\ASHISH\AppData\Local\Programs",

    r"D:\\",

]

KNOWN_EXECUTABLES = {

    "brave.exe": "brave",

    "chrome.exe": "chrome",

    "Code.exe": "vscode",

    "steam.exe": "steam",

    "Discord.exe": "discord",

    "AppleMusic.exe": "apple_music",

    "Spotify.exe": "spotify",

    "notepad.exe": "notepad",

    "calc.exe": "calculator",

    "mspaint.exe": "paint",

}


class AppScanner:

    def scan(self):

        discovered = {}

        for root in COMMON_LOCATIONS:

            if not os.path.exists(root):

                continue

            for path, _, files in os.walk(root):

                for file in files:

                    if file in KNOWN_EXECUTABLES:

                        key = KNOWN_EXECUTABLES[file]

                        if key not in discovered:

                            discovered[key] = os.path.join(path, file)

        return discovered