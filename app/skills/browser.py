"""
JarvisOS Browser Skill

Responsible for:

- Opening websites
- Opening direct URLs
- Google search
- YouTube search
- GitHub search

Every public method returns:

(message: str, handled: bool)
"""

import subprocess
import urllib.parse
import webbrowser

from app.registry.registry import registry


class BrowserSkill:

    def __init__(self):
        pass

    # =====================================================
    # Browser Path
    # =====================================================

    def _browser_path(self):

        browser_name = registry.default_browser()

        app = registry.get_app(browser_name)

        if not app:
            return None

        return app.get("path")

    # =====================================================
    # Launch URL
    # =====================================================

    def open_url(self, url: str) -> bool:

        if not url:
            return False

        browser = self._browser_path()

        try:

            if browser:
                subprocess.Popen([browser, url])

            else:
                webbrowser.open(url)

            return True

        except Exception as e:

            print(f"[BrowserSkill] {e}")

            return False

    # =====================================================
    # Open Website
    # =====================================================

    def open(self, command):

        target = (command.target or "").strip()

        if not target:

            return (
                "Which website would you like me to open?",
                True,
            )

        # ---------------------------------------
        # Direct URL
        # ---------------------------------------

        if registry.is_url(target):

            url = registry.normalize_url(target)

            if self.open_url(url):

                return (
                    f"Opening {url}.",
                    True,
                )

            return (
                "I couldn't open that website.",
                True,
            )

        # ---------------------------------------
        # Registry Website
        # ---------------------------------------

        url = registry.get_website_url(target)

        if url:

            if self.open_url(url):

                title = registry.get_website(target)["title"]

                return (
                    f"Opening {title}.",
                    True,
                )

            return (
                f"I couldn't open {target}.",
                True,
            )

        # ---------------------------------------
        # Unknown Website
        # ---------------------------------------

        return (
            f"I don't know the website '{target}'.",
            True,
        )

    # =====================================================
    # Google Search
    # =====================================================

    def search(self, command):

        query = (command.target or command.query or "").strip()

        if not query:

            return (
                "What would you like me to search for?",
                True,
            )

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(query)
        )

        if self.open_url(url):

            return (
                f"Searching Google for {query}.",
                True,
            )

        return (
            "Google search failed.",
            True,
        )

    # =====================================================
    # YouTube Search
    # =====================================================

    def youtube_search(self, query):

        if not query:

            return (
                "What would you like me to search on YouTube?",
                True,
            )

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote_plus(query)
        )

        if self.open_url(url):

            return (
                f"Searching YouTube for {query}.",
                True,
            )

        return (
            "YouTube search failed.",
            True,
        )

    # =====================================================
    # GitHub Search
    # =====================================================

    def github_search(self, query):

        if not query:

            return (
                "What would you like me to search on GitHub?",
                True,
            )

        url = (
            "https://github.com/search?q="
            + urllib.parse.quote_plus(query)
        )

        if self.open_url(url):

            return (
                f"Searching GitHub for {query}.",
                True,
            )

        return (
            "GitHub search failed.",
            True,
        )