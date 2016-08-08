from django import forms
from talk.models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'id': 'post-text', 'required': True, 'rows':8, 'cols':8,'placeholder': 'Dump your text here...'}
            ),
        }

    def save(self):
        post = super().save(commit=False)
        post.entry = self.entry
        post.save()
        return post

    #custom python cleaning function
    # def clean_text(self):
    #     text = self.cleaned_data.get['text']
    #     matches = []
    #     for match in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", text):
    #         clean = re.findall(r'\d+', match.group())
    #         matches.append(clean)
    #     text = [''.join([str(b) for b in a]) for a in matches]
    #     return text
