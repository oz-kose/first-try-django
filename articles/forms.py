from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs_t = Article.objects.filter(title__icontains=title)
        qs_c = Article.objects.filter(title__icontains=title)

        if qs_t.exists():
            self.add_error("title", f"\"{title}\" is already in use.")
        if qs_c.exists():
            self.add_error("content", "This content is duplicated.")
        return data
