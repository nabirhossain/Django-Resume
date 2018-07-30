from django import forms

class contact_form(forms.Form):
    contact_name = forms.CharField(label='Your Name', max_length=255)
    contact_email = forms.CharField(label='Your Email',max_length=255)
    contact_message = forms.CharField(label='Write Message',
        required=True,
        widget=forms.Textarea
    )