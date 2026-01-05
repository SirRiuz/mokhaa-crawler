from peewee import Model

from crawler.core.db.connection import get_database_instance


class BaseModel(Model):
    """
    Base model class used for creating all database models
    """

    class Meta:
        database = get_database_instance()
