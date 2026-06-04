import requests

from logger import *

def fetch_announcements(url):

    try:
        logger.info(f"Probing endpoint: {url}")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        logger.success("Announcements fetched successfully")
        return response.json()

    except requests.exceptions.Timeout:
        logger.exception(f"Request timeout probing endpoint: {url}")
        return []

    except requests.exceptions.HTTPError as e:
        logger.exception(f"HTTP error while probing endpoint {url}: {e.response.status_code}")
        return []

    except requests.exceptions.RequestException as e:
        logger.exception(f"Request failed probing endpoint {url}: {e}")
        return []

    except ValueError as e:
        logger.exception(f"Invalid JSON response probing endpoint {url}: {e}")
        return []
