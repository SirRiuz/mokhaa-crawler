from typing import Optional

from crawl4ai.models import CrawlResult

from crawler.utils.urls import extract_urls
from crawler.settings import ENTRY_POINT_URL
from crawler.constants import CrawlerMessages
from crawler.models.url_record import UrlRecord
from crawler.libs.call import make_crawler_request
from crawler.exceptions.crawling import EntryPointLinkExtractionError


async def get_entry_point() -> Optional[CrawlResult]:
    """
    Retrieves the initial links from the entry point.
    """
    result = await make_crawler_request(ENTRY_POINT_URL)
    if result.success:
        return result


async def get_entry_point_urls() -> list:
    """
    Retrieves a list of URLs from the entry point by making an HTTP request
    and extracting all available URLs.
    """
    result = await get_entry_point()

    if not result:
        raise EntryPointLinkExtractionError(
            CrawlerMessages.FAILED_TO_EXTRACT_LINKS % ENTRY_POINT_URL,
        )

    # Extract all available URLs from the entry point
    entry_point_url = extract_urls(result)
    return entry_point_url


async def save_entry_point_urls() -> None:
    """
    Fetch entry point URLs and save them to the database.

    This function retrieves all entry point URLs asynchronously, creates
    UrlRecord objects for each URL, and performs a bulk insert operation
    to save them to the database.

    Raises:
        Exception: If there's an error during URL retrieval or database insertion.
    """
    # Initialize list to store URL record objects
    records_objects = []

    # Fetch all entry point URLs asynchronously
    entry_point_urls = await get_entry_point_urls()

    # Create a UrlRecord object for each entry point URL
    for url in entry_point_urls:
        records_objects.append(UrlRecord(url=url))

    # Bulk insert all URL records into the database
    UrlRecord.bulk_create(records_objects)
