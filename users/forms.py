from django import forms


from .models import news


class ImageForm(forms.ModelForm):
    class Meta:
        model = news
        fields = ['logo', 'vedio','text']
