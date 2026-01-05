import asyncio

from crawl4ai import *

from crawler.core.db.connection import database_conect
from crawler.manager.url_record_manager import UrlRecords
from crawler.utils.enty_point import save_entry_point_urls


from crawler.utils.urls import extract_urls
from crawler.libs.call import make_crawler_request


async def main() -> None:

    if not UrlRecords.objects.has_records():
        # Initialize database with URLs from the entry point
        # These seed URLs will be crawled first
        await save_entry_point_urls()

    # Main loop that runs while there are records in the database.
    # During execution, URLs are processed and new records are added
    # dynamically. The crawler stops automatically when there are no
    # more records to process.
    while UrlRecords.objects.has_records():
        records_batch = UrlRecords.objects.get_records_batch()
        for record in records_batch:

            result = await make_crawler_request(record.url)
            result_urls = extract_urls(result)

            # TODO: Extract all urls from record and store in db
            # TODO: Extract images and video content
            # TODO: Process and call index service


if __name__ == "__main__":
    # Initialize database connection
    database_conect()

    # Run the async main function that starts the crawler
    asyncio.run(main())
