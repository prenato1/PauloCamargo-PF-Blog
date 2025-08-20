from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label="Destinatário")

    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['recipient'].queryset = User.objects.exclude(pk=user.pk)
