
# Create your views here.

from django.shortcuts import render
from .forms import FloorPlanRecommendationForm
from .recommendation import recommend_floor_plans
import json
import os

def recommend_floor_plans_view(request):
    form = FloorPlanRecommendationForm(request.POST or None)
    recommended_plan_names = []

    if request.method == 'POST' and form.is_valid():
        user_input = {
            "no_of_rooms": form.cleaned_data['no_of_rooms'],
            "attached_required": form.cleaned_data['attached_required'] == 'yes',
            "garage_required": form.cleaned_data['garage_required'] == 'yes',
            "porch_required": form.cleaned_data['porch_required'] == 'yes'
        }

        # # Load floor plans data from JSON file or database
        # with open("data.json", "r") as file:
        #     floor_plans = json.load(file)["floor_plans"]

        # Construct the path to data.json relative to the app directory
        app_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file (views.py)
        data_file_path = os.path.join(app_dir, 'data.json')

        # Load floor plans data from JSON file
        with open(data_file_path, "r") as file:
            floor_plans = json.load(file)["floor_plans"]

        # Get the top two recommended floor plan names
        recommended_plan_names = recommend_floor_plans(user_input, floor_plans)
        print(recommended_plan_names)

    return render(request, 'user_input_form.html', {'form': form, 'recommended_plan_names': recommended_plan_names})



def landing(request):
    return render(request, 'index.html')