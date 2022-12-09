from django import forms
from django.utils.translation import gettext_lazy as _


class MailFeedbackForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    message = forms.CharField(
        widget=forms.Textarea,
        help_text=_("Enter your message"),
        label=_("Message"),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields["user_id"].initial = user.pk