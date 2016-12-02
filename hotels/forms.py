from django import forms
from .models import Hotel

STARS_CATEGORY = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


class HotelFilterForm(forms.Form):

    c = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=STARS_CATEGORY,
    )
