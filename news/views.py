"""
AI 기반 뉴스 필터링 및 요약 뷰
"""

import os
from typing import List

import json
from django.conf import settings
from django.shortcuts import render
from django.views import View

from .forms import NewsSearchForm
from .services.naver_api import search_news

# OpenAI 사용 안함 (선택 사항)


def filter_and_summarize(articles: List[dict], filter_prompt: str) -> List[dict]:
    """필터링 프롬프트는 현재 무시하고, 처음 3개의 기사만 반환합니다. 출처와 날짜를 포함합니다."""
    selected = articles[:3]
    results = []
    for a in selected:
        results.append({
            "title": a.get("title", ""),
            "link": a.get("link", ""),
            "summary": a.get("description", "")[:200],
            "pub_date": a.get("pub_date", "")
        })
    return results


class NewsSearchView(View):
    template_name = "news/search.html"

    def get(self, request):
        form = NewsSearchForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = NewsSearchForm(request.POST)
        results = []
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            filter_prompt = form.cleaned_data["filter_prompt"]
            articles = search_news(keyword, display=20)
            results = filter_and_summarize(articles, filter_prompt)
        return render(request, self.template_name, {"form": form, "results": results})
