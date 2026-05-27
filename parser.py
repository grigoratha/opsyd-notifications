import re

from bs4 import BeautifulSoup


def sanitize_date(html):
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)

    match = re.search(r"\d{1,2}/\d{1,2}/\d{4}", text)

    return match.group(0) if match else text


def sanitize_html(html):
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)

    text = re.sub(r"\s+", " ", text)

    return text.strip()