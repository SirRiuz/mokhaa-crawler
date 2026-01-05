from peewee import SqliteDatabase


def get_database_instance() -> SqliteDatabase:

    from crawler.settings import DATABASE
    from crawler.constants.messages import DatabaseConfiguration
    from crawler.exceptions.db import DatabaseConfigurationError

    DATABASE_NAME = DATABASE.get("NAME")

    if not DATABASE_NAME:
        raise DatabaseConfigurationError(
            DatabaseConfiguration.DB_NAME_NOT_CONFIGURED_ERROR,
        )

    db = SqliteDatabase(DATABASE_NAME)
    return db


def database_conect() -> None:

    from crawler.settings import MAPPED_MODELS

    db = get_database_instance()
    db.connect()
    db.create_tables(MAPPED_MODELS)
