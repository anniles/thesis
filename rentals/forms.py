from django import forms
from .models import Car

CAR_CATEGORY = (
    ('SUV', 'SUV'),
    ('Truck', 'Truck'),
    ('Sedan', 'Sedan'),
    ('Van', 'Van'),
    ('Coupe/Compact', 'Coupe/Compact'),
    ('Wagon', 'Wagon'),
    ('Convertible', 'Convertible'),
    ('Sports Car', 'Sports Car'),
    ('Diesel', 'Diesel'),
    ('Crossover', 'Crossover'),
    ('Luxury Car', 'Luxury Car'),
    ('Hybrid/Electric', 'Hybrid/Electric'),
    ('Hatchback', 'Hatchback'),
)

CC_CATEGORY = (
    # ((url)value) , label)
    ('0-1000', '0 - 1000'),
    ('1000-1100', '1000 - 1100'),
    ('1100-1300', '1100 - 1300'),
    ('1300-1600', '1300 - 1600'),
    ('1600-2000', '1600 - 2000'),
    ('2000', 'Bigger than 2000'),
)

BIKE_CATEGORY = (
    ('Standard', 'Standard'),
    ('Cruiser', 'Cruiser'),
    ('Sport bike', 'Sport bike'),
    ('Touring', 'Touring'),
    ('Sport touring', 'Sport touring'),
    ('Dual-sport', 'Dual-sport'),
    ('Scooters', 'Scooters'),
    ('Off-road', 'Off-road'),
    ('Enclosed', 'Enclosed'),
    ('Utility', 'Utility'),
    ('Tricycles', 'Tricycles'),
)

BCC_CATEGORY = (
    # ((url)value) , label)
    ('', 'Clear'),
    ('0-100', '100 cc And Below'),
    ('100-150', '100 cc To 150 cc'),
    ('150-200', '150 cc To 200 cc'),
    ('200-250', '200 cc To 250 cc'),
    ('250', '250 cc And Above'),
)

class CarFilterForm(forms.Form):

    t = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CAR_CATEGORY,
    )

    cc = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=CC_CATEGORY,
    )


class BikeFilterForm(forms.Form):

    c = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BIKE_CATEGORY,
    )

    cc = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=BCC_CATEGORY,
    )


