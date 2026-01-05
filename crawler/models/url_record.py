from peewee import CharField

from crawler.core.db import BaseModel
from crawler.core.db import BaseModel


class UrlRecord(BaseModel):
    url = CharField()
