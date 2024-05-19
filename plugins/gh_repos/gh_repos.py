# Adapted from
# https://github.com/kura/pelican-githubprojects/blob/2ee75cdebde1c6e5a836e32bfb85a7e0207fe5a4/pelican_githubprojects/github.py
# Copyright (c) 2014 Kura
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json
import logging
import os

from urllib.request import HTTPError
from urllib.request import urlopen


from pelican import signals


logger = logging.getLogger(__name__)
GITHUB_API = "https://api.github.com/users/{username}/repos?type={user_type}&sort={sort_by}&direction={direction}"


class GithubProjects(object):
    def __init__(self, generator):
        self.repositories = []
        # Params supported at
        # https://developer.github.com/v3/repos/#list-user-repositories
        username = generator.settings["GITHUB_USER"]
        user_type = generator.settings.get("GITHUB_USER_TYPE", "owner")
        sort_by = generator.settings.get("GITHUB_SORT_BY", "full_name")
        direction = generator.settings.get(
            "GITHUB_DIRECTION", "asc" if sort_by == "full_name" else "desc"
        )

        github_url = GITHUB_API.format(
            username=username, user_type=user_type, sort_by=sort_by, direction=direction
        )
        try:
            with urlopen(github_url, timeout=2) as f:
                encoding = f.headers.get_content_charset()
                response = f.read().decode(encoding)
        except HTTPError:
            logger.warning(f"unable to open {github_url}")
            return
        self.repositories = json.loads(response)

    def process(self):
        logger.info(f"Found {len(self.repositories)} repos")
        return [
            {
                "name": repo["name"],
                "description": repo["description"],
                "github_url": repo["html_url"],
                "stars": repo["stargazers_count"],
            }
            for repo in self.repositories
            if not repo["private"] and not repo["fork"]
        ]


def initialize(generator):
    if "GITHUB_USER" not in generator.settings:
        logger.warning("GITHUB_USER not set")
    else:
        instance = GithubProjects(generator)
        generator.context["github_projects"] = instance.process()


def register():
    signals.article_generator_init.connect(initialize)
