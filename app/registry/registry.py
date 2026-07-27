"""
JarvisOS Registry Service

The Registry is the single source of truth for:

• Applications
• Websites
• User Preferences
• Aliases

Every module should communicate ONLY with this service.
"""

from app.registry.aliases import ALIASES
from app.registry.apps import APPS
from app.registry.preferences import (
    DEFAULT_AI_WEBSITE,
    DEFAULT_BROWSER,
    DEFAULT_CODE_EDITOR,
    DEFAULT_EMAIL,
    DEFAULT_MUSIC_PLAYER,
    DEFAULT_SEARCH_ENGINE,
    DEFAULT_TERMINAL,
    USER_NAME,
    ASSISTANT_NAME,
)

from app.registry.websites import WEBSITES


class Registry:

    # ==========================================================
    # ALIASES
    # ==========================================================

    def resolve_alias(self, value: str):

        if not value:
            return None

        value = value.lower().strip()

        return ALIASES.get(value, value)

    # ==========================================================
    # APPLICATIONS
    # ==========================================================

    def get_app(self, name: str):

        name = self.resolve_alias(name)

        return APPS.get(name)

    def app_exists(self, name: str):

        return self.get_app(name) is not None

    def list_apps(self):

        return list(APPS.keys())

    # ==========================================================
    # WEBSITES
    # ==========================================================

    def get_website(self, name: str):

        name = self.resolve_alias(name)

        return WEBSITES.get(name)

    def website_exists(self, name: str):

        return self.get_website(name) is not None

    def get_website_url(self, name: str):

        website = self.get_website(name)

        if not website:
            return None

        return website.get("url")

    def get_website_title(self, name: str):

        website = self.get_website(name)

        if not website:
            return None

        return website.get("title")

    def get_website_category(self, name: str):

        website = self.get_website(name)

        if not website:
            return None

        return website.get("category")

    def list_websites(self):

        return list(WEBSITES.keys())

    def list_categories(self):

        categories = set()

        for website in WEBSITES.values():

            category = website.get("category")

            if category:

                categories.add(category)

        return sorted(categories)

    # ==========================================================
    # URL HELPERS
    # ==========================================================

    def is_url(self, text: str):

        if not text:
            return False

        text = text.strip().lower()

        if text.startswith("http://"):

            return True

        if text.startswith("https://"):

            return True

        if "." in text and " " not in text:

            return True

        return False

    def normalize_url(self, url: str):

        if not url:
            return None

        if url.startswith("http://"):

            return url

        if url.startswith("https://"):

            return url

        return f"https://{url}"

    # ==========================================================
    # SEARCH
    # ==========================================================

    def search_url(self, query: str):

        query = query.replace(" ", "+")

        engines = {

            "google":
                f"https://www.google.com/search?q={query}",

            "bing":
                f"https://www.bing.com/search?q={query}",

            "duckduckgo":
                f"https://duckduckgo.com/?q={query}",
        }

        return engines.get(

            DEFAULT_SEARCH_ENGINE,

            engines["google"],

        )

    def youtube_search(self, query: str):

        query = query.replace(" ", "+")

        return f"https://www.youtube.com/results?search_query={query}"

    def github_search(self, query: str):

        query = query.replace(" ", "+")

        return f"https://github.com/search?q={query}"

    # ==========================================================
    # USER PREFERENCES
    # ==========================================================

    def default_browser(self):

        return DEFAULT_BROWSER

    def default_search_engine(self):

        return DEFAULT_SEARCH_ENGINE

    def default_music_player(self):

        return DEFAULT_MUSIC_PLAYER

    def default_email(self):

        return DEFAULT_EMAIL

    def default_code_editor(self):

        return DEFAULT_CODE_EDITOR

    def default_terminal(self):

        return DEFAULT_TERMINAL

    def default_ai(self):

        return DEFAULT_AI_WEBSITE

    # ==========================================================
    # USER INFO
    # ==========================================================

    def user_name(self):

        return USER_NAME

    def assistant_name(self):

        return ASSISTANT_NAME


registry = Registry()