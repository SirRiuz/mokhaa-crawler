from peewee import SqliteDatabase, Model

# from crawler.settings import DATABASE
# from crawler.constants.messages import DatabaseConfiguration
# from crawler.exceptions.db import DatabaseConfigurationError


# DATABASE_NAME = DATABASE.get("NAME")

# if not DATABASE_NAME:
#     raise DatabaseConfigurationError(
#         DatabaseConfiguration.DB_NAME_NOT_CONFIGURED_ERROR,
#     )


def get_sqllite_db_instance() -> SqliteDatabase:
    db = SqliteDatabase("my_database.db")
    return db


def sqllite_conect() -> None:
    # Inportando desde dentro para evitar importaciones ciclicas
    from crawler.settings import MAPPED_MODELS

    db = get_sqllite_db_instance()
    db.connect()
    db.create_tables(MAPPED_MODELS)


class BaseModel(Model):
    """
    Base model class used for creating all database models
    """

    class Meta:
        database = get_sqllite_db_instance()
