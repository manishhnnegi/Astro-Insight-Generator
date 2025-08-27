import json, os
from config.config import Config


class Cache:
    """
    A simple file-based caching system for storing and retrieving data.

    This class uses a JSON file as persistent storage to maintain a cache.
    It automatically loads the cache from disk when initialized and saves
    changes whenever a new entry is added or updated.

    Attributes:
        _cache (dict): Internal dictionary to hold cached data in memory.
        CACHE_FILE (str): File path for the cache JSON file.
    """

    def __init__(self):
        """
        Initialize the Cache object.

        - Loads existing cache data from the configured cache file.
        - If the file does not exist, creates an empty JSON file.
        """

        self._cache = {}
        self.CACHE_FILE = Config.CACHE_FILE
        self.load()

    def load(self):
        """
        Load the cache from the JSON file.

        - If the cache file does not exist, create an empty one.
        - If the cache file exists, load its contents into memory.
        - If the file contains invalid JSON, reset the cache to an empty dictionary.
        """

        if not os.path.exists(self.CACHE_FILE):
            with open(self.CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

        if os.path.exists(self.CACHE_FILE):
            try:
                with open(self.CACHE_FILE, "r", encoding="utf-8") as f:
                    self._cache = json.load(f)
            except json.JSONDecodeError:
                self._cache = {}

    def save(self):
        """
        Save the current state of the cache to the JSON file.

        Ensures the cache dictionary is always written in a human-readable format.
        """

        with open(self.CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(self._cache, f, ensure_ascii=False, indent=2)

    def get(self, key: str):
        """
        Retrieve a value from the cache using the provided key.

        Args:
            key (str): The cache key to look up.

        Returns:
            dict or None: The cached entry if found, otherwise None.
        """

        return self._cache.get(key)

    def set(self, key: str, zodiac: str, insight: str, language: str):
        """
        Insert or update a value in the cache and persist it to disk.

        Args:
            key (str): Unique identifier for the cached entry.
            zodiac (str): The zodiac sign associated with the entry.
            insight (str): The insight or prediction text.
            language (str): The language code of the cached insight.

        Returns:
            None
        """

        self._cache[key] = {"zodiac": zodiac, "insight": insight, "language": language}
        self.save()
