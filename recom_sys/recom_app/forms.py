from django import forms

class FloorPlanRecommendationForm(forms.Form):
    no_of_rooms = forms.IntegerField(label='Number of Rooms')
    attached_required = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Attached Rooms Required')
    garage_required = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Garage Required')
    porch_required = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Porch Required')
