# boidolr.github.io

Code for my minimal personal page.


## Setup

Steps to create a new GitHub Pages site:

```
brew install ruby
# add ruby to $PATH
gem install bundler jekyll
mkdir docs && cd docs
jekyll new --skip-bundle .
# update Gemfile
bundle install
# update _config.yml
```

## Local testing

```
JEKYLL_GITHUB_TOKEN="ghp_..." bundle exec jekyll serve --safe
```
