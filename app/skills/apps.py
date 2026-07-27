"""
JarvisOS App Skill

Responsible for opening desktop applications.

Every skill returns:

(message: str, handled: bool)
"""

import shutil
import subprocess

from app.registry.registry import registry


class AppSkill:

    def __init__(self):
        pass

    # ==========================================================
    # Execute
    # ==========================================================

    def execute(self, command):

        if not command.target:

            return (
                "Which application would you like me to open?",
                True,
            )

        success = self.open(command.target)

        if success:

            return (
                f"Opening {command.target}.",
                True,
            )

        return (
            f"I couldn't find {command.target}.",
            True,
        )

    # ==========================================================
    # Open Application
    # ==========================================================

    def open(self, app_name: str):

        print("\n========== APP DEBUG ==========")

        print("Input:", app_name)

        app_name = registry.resolve_alias(app_name)

        print("Resolved:", app_name)

        app = registry.get_app(app_name)

        print("Registry:", app)

        if not app:

            print("Application not found.")

            print("================================\n")

            return False

        # -----------------------------------------
        # Try Full Path
        # -----------------------------------------

        path = app.get("path")

        if path:

            print("Trying path:", path)

            try:

                subprocess.Popen([path])

                print("SUCCESS: Opened using full path.")

                print("================================\n")

                return True

            except Exception as e:

                print("Path launch failed:", e)

        # -----------------------------------------
        # Try Executable Name
        # -----------------------------------------

        exe = app.get("exe")

        if exe:

            print("Trying executable:", exe)

            try:

                executable = shutil.which(exe)

                if executable:

                    subprocess.Popen([executable])

                    print("SUCCESS: Opened using shutil.which().")

                    print("================================\n")

                    return True

            except Exception as e:

                print("Executable lookup failed:", e)

            try:

                subprocess.Popen(exe, shell=True)

                print("SUCCESS: Opened using shell=True.")

                print("================================\n")

                return True

            except Exception as e:

                print("Shell launch failed:", e)

        print("FAILED TO OPEN APPLICATION")

        print("================================\n")

        return False