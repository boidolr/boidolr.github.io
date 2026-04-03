import datetime


FIRSTNAME = "Raphael"
AUTHOR = "Raphael Boidol"
SITE_DOMAIN = "boidol.dev"
HERO_TITLE = "Crafting Digital Experiences"
TAGLINE = "Passionate software engineer and designer specializing in building clean, efficient, and elegant digital solutions. Combining code and creativity to create meaningful user experiences. Based in the digital world."
SITENAME = AUTHOR
SITEURL = ""

THEME = "theme"
PATH = "content"
DIRECT_TEMPLATES = ["index"]

TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

# Custom config
GITHUB_USER = "boidolr"
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["gh_repos", "cssmin", "jsmin"]
JINJA_GLOBALS = {"now": lambda: datetime.datetime.now(datetime.UTC)}
JINJA_TESTS = {
    "repo_check": lambda repo_name: any(
        (
            part in repo_name
            for part in ("actions", "cookiecutter", "pelican", "pre-commit", "pytest")
        )
    )
}
THEME_CONFIG = {
    "light_theme": "#f2f2f2",
    "dark_theme": "#11191f",
}
SOCIAL_CONFIG = [
    {"title": "GitHub", "class": "github", "url": "https://github.com/boidolr"},
    {
        "title": "LinkedIn",
        "class": "linkedin",
        "url": "https://www.linkedin.com/in/boidol",
    },
]
