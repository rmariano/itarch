"""Mutable objects as class attributes."""
import logging

logger = logging.getLogger(__name__)


class Query:
    PARAMETERS = {"limit": 100, "offset": 0}

    def run_query(self, query, limit=None, offset=None):
        if limit is not None:
            self.PARAMETERS.update(limit=limit)
        if offset is not None:
            self.PARAMETERS.update(offset=offset)
        return self._run(query, **self.PARAMETERS)

    @staticmethod
    def _run(query, limit, offset):
        logger.info("running %s [%s, %s]", query, limit, offset)
