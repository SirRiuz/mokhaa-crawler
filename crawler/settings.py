# Entry point URL for the crawler
# The crawler starts from this URL, extracts all links from the page,
# and begins mapping the site structure
ENTRY_POINT_URL = "https://es.wikipedia.org/wiki/C%C3%A9lula"

# Database configuration
# SQLite database file settings
DATABASE = {
    "NAME": "my_database.db"
}

# Model mappings
# All models that should be used must be registered in this list.
# This allows Peewee to detect them and create the corresponding database tables.
# If a model is not specified in this list, Peewee will not create its table,
# so any models you want to use must be mapped here.

# TODO: This should be done automatically, similar to Django's
# INSTALLED_APPS auto-discovery mechanism.
MAPPED_MODELS = []

