from django import forms

class Feedbackform(forms.Form):
    email = forms.EmailField(label='enter your email address',max_length=100, required=True)
    name=forms.CharField(label='enter the name',max_length=200)
    feedback=forms.CharField(label='enter feedback',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Feedbackform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    