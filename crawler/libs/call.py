from crawl4ai.models import CrawlResult
from crawl4ai import AsyncWebCrawler


async def make_crawler_request(url: str) -> CrawlResult:
    """
    Performs an asynchronous web crawling request to a specific URL.

    This function creates an AsyncWebCrawler instance, executes the crawling
    process on the provided URL, and returns the crawling result.

    The crawler uses an asynchronous context manager to ensure that resources
    are properly released after the operation completes, even if an error
    occurs during the process.

    Args:
        url (str): The complete URL of the website to crawl.
                   Must be a valid URL with http:// or https:// format.

    Returns:
        CrawlResult: Object containing the crawling results, including:
                     - Extracted HTML content
                     - Page metadata
                     - Found links
                     - Any other information collected during crawling

    Raises:
        Exception: May raise exceptions related to:
                   - Invalid or inaccessible URLs
                   - Network errors or timeouts
                   - Issues during the crawling process

    Example:
        >>> result = await make_crawler_request("https://example.com")
        >>> print(result.html)
    """
    async with AsyncWebCrawler() as crawler:
        return await crawler.arun(url=url)
