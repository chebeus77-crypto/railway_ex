"""
네이버 뉴스 검색 API 서비스
"""

import html
import re

import requests
from django.conf import settings


def clean_html(text: str) -> str:
    """HTML 태그 및 엔티티 제거"""
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def search_news(query: str, display: int = 20) -> list[dict]:
    """
    네이버 뉴스 검색 API로 기사 목록 반환

    Args:
        query: 검색 키워드
        display: 가져올 기사 수 (최대 100)

    Returns:
        기사 딕셔너리 리스트 [{title, link, description, pubDate}, ...]
    """
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": settings.NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": settings.NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": display,
        "sort": "date",  # 최신순
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    items = response.json().get("items", [])
    return [
        {
            "title": clean_html(item.get("title", "")),
            "link": item.get("link", ""),
            "description": clean_html(item.get("description", "")),
            "pub_date": item.get("pubDate", ""),
            "original_link": item.get("originallink", ""),
        }
        for item in items
    ]
