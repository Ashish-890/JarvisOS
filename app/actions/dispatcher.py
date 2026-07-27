"""
JarvisOS Dispatcher

Routes Commands to the appropriate Skill.

The Dispatcher never performs work itself.
It simply forwards Commands to the correct Skill.

Every skill MUST return:

(message: str | None, handled: bool)
"""

from app.router.intent import Intent

from app.skills.apps import AppSkill
from app.skills.browser import BrowserSkill


class Dispatcher:

    def __init__(self):

        # ==========================================
        # Skills
        # ==========================================

        self.app_skill = AppSkill()

        self.browser_skill = BrowserSkill()

    # ==================================================
    # Dispatch
    # ==================================================

    def dispatch(self, command):

        if command is None:

            return (
                "I couldn't understand that.",
                True,
            )

        intent = command.intent

        # ==================================================
        # APPLICATIONS
        # ==================================================

        if intent == Intent.OPEN_APP:

            return self.app_skill.execute(command)

        # ==================================================
        # WEBSITES
        # ==================================================

        if intent == Intent.OPEN_WEBSITE:

            return self.browser_skill.open(command)

        # ==================================================
        # GOOGLE SEARCH
        # ==================================================

        if intent == Intent.GOOGLE_SEARCH:

            return self.browser_skill.search(command)

        # ==================================================
        # YOUTUBE SEARCH
        # ==================================================

        if intent == Intent.YOUTUBE_SEARCH:

            return self.browser_skill.youtube_search(
                command.target
            )

        # ==================================================
        # GITHUB SEARCH
        # ==================================================

        if intent == Intent.GITHUB_SEARCH:

            return self.browser_skill.github_search(
                command.target
            )

        # ==================================================
        # MEMORY
        # ==================================================

        if intent == Intent.SAVE_MEMORY:

            return (
                "Memory support is under development.",
                True,
            )

        if intent == Intent.RECALL_MEMORY:

            return (
                "Memory recall is under development.",
                True,
            )

        # ==================================================
        # UNKNOWN
        # ==================================================

        return (
            None,
            False,
        )