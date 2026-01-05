from crawl4ai.models import CrawlResult


def extract_urls(crawler_result: CrawlResult) -> list:
    """
    Extracts all URLs from the crawler result.
    """
    entry_point_url = []
    request_url = crawler_result.url
    result_links = crawler_result.links

    for key in result_links.keys():
        links = result_links[key]
        for link in links:
            url = link.get("href")
            if url and url != request_url:
                entry_point_url.append(url)

    return entry_point_url
