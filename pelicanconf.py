import datetime


AUTHOR = "Raphael Boidol"
EMAIL = "boidolr@users.noreply.github.com"
TAGLINE = "Software consultant with a passion for automation."
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

# Custom config
PLUGIN_PATHS = ["plugins", "plugins/gh_repos"]
PLUGINS = ["gh_repos", "cssmin", "jsmin"]
JINJA_GLOBALS = {"now": datetime.datetime.utcnow}
GITHUB_USER = "boidolr"
THEME_CONFIG = {
    "light_theme": "#f2f2f2",
    "dark_theme": "#11191f",
}
JINJA_TESTS = {
    "repo_check": lambda repo_name: any(
        (
            part in repo_name
            for part in ("actions", "cookiecutter", "pelican", "pre-commit")
        )
    )
}
SOCIAL_CONFIG = [
    {"title": "GitHub", "class": "github", "url": "https://github.com/boidolr"},
    {
        "title": "Xing",
        "class": "xing",
        "url": "https://www.xing.com/profile/Raphael_Boidol/cv",
    },
    {
        "title": "LinkedIn",
        "class": "linkedin",
        "url": "https://www.linkedin.com/in/boidol",
    },
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
