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
        if title.lower().strip() == "the title":
            self.add_error("title", "This title is taken.")