from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "the title":
    #         raise forms.ValidationError("This tittle is taken.")
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "the title":
            self.add_error("title", "This title is taken.")
        if "tricky" in content or "tricky" in title.lower():
            self.add_error("content", "tricky can not be in the content.")
            raise forms.ValidationError("tricky is not allowed")
        return cleaned_data