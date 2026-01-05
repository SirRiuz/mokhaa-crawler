from crawler.models.url_record import UrlRecord


class AbstractUrlRecordManager:

    def has_records(self) -> bool:
        """
        Check if there are any URL records in the database.

        Returns:
            bool: True if at least one URL record exists, False otherwise.
        """
        return UrlRecord.select().exists()

    def get_records_batch(self, page: int = 1) -> list:
        """
        Get URL records in batches of 50.

        Args:
            page (int): Page number (starting from 1). Default is 1.

        Returns:
            list: List of UrlRecord objects (maximum 50 records per call).
        """
        batch_size = 50
        offset = (page - 1) * batch_size
        return list(UrlRecord.select().limit(batch_size).offset(offset))


class UrlRecords:
    objects = AbstractUrlRecordManager()
