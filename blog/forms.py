from django import forms
from blog.models import Comment


class PreviewImageInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None):
        html = super(PreviewImageInput, self).render(name, value, attrs)
        # value 가 InMemoryUploadedFile 인스턴스일 경우, url 이 없다.
        if value and hasattr(value, 'url'):
            image_html = '''
                <a href="{}" target="_blank" style="float:right;">
                    <img src="{}" style="max-width: 200px; max-height: 100px;" />
                </a>
                '''.format(value.url, value.url)
            html = image_html + html
        return html


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'photo']
        widgets = {
            'photo': PreviewImageInput,
        }
