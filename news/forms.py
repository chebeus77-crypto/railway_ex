from django import forms

class NewsSearchForm(forms.Form):
    keyword = forms.CharField(label="검색 키워드", max_length=100, required=True)
    filter_prompt = forms.CharField(
        label="필터링 프롬프트",
        widget=forms.Textarea(attrs={"rows": 3}),
        required=True,
        help_text="AI가 기사 선별에 사용할 프롬프트 예: 'AI와 기술 관련 기사만'",
    )
