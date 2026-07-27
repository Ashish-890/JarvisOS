import os
import shutil
import subprocess

from app.registry.registry import registry


class AppSkill:
    """
    Desktop Application Skill

    Responsible for opening desktop applications.
    """

    def __init__(self):
        pass

    # =====================================================
    # Execute
    # =====================================================

    def execute(self, command):

        target = command.target

        if not target:
            return False, "I don't know which application to open."

        success = self.open(target)

        if success:
            return True, f"Opening {target}."

        return True, f"I couldn't find {target}."

    # =====================================================
    # Open Application
    # =====================================================

    def open(self, app_name):

        app_name = registry.resolve_alias(app_name)

        app = registry.get_app(app_name)

        if not app:
            return False

        # --------------------------------------------
        # 1. Launch from configured path
        # --------------------------------------------

        path = app.get("path")

        if path and os.path.exists(path):

            try:
                subprocess.Popen(path)

                return True

            except Exception:
                pass

        # --------------------------------------------
        # 2. Launch executable from PATH
        # --------------------------------------------

        exe = app.get("exe")

        if exe:

            try:

                if shutil.which(exe):

                    subprocess.Popen(exe)

                    return True

            except Exception:

                pass

        # --------------------------------------------
        # 3. Try shell launch
        # --------------------------------------------

        try:

            subprocess.Popen(exe, shell=True)

            return True

        except Exception:

            return False