from peewee import CharField

from crawler.core.db.models import BaseModel


class UrlRecord(BaseModel):
    url = CharField()
