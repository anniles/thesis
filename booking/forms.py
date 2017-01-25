from django import forms


TYPE_CHOICES = (
    ('RO', 'Room only'),
    ('BB', 'Bed & Breakfast'),
    ('HB', 'Half Board (Breakfast and Dinner)'),
    ('FB', 'Full Board (Beakfast, Lunch and Dinner)'),
    ('AI', 'All Inclusive'),
)


class SearchRoom(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    hotel_name = forms.CharField(default='Any')
    check_in = forms.DateField(input_formats=['%Y-%m-%d'], initial=date.today)
    check_out = forms.DateField()
    guests = forms.IntegerField(default=2)
    roomtype = forms.MultipleChoiceField(
        required=False,
        choices=TYPE_CHOICES,
    )
