
# Create your views here.

from django.shortcuts import render, redirect
from .forms import FloorPlanRecommendationForm
from .recommendation import recommend_floor_plans
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import os




def recommend_floor_plans_view(request):
    if request.method == 'POST':
        form = FloorPlanRecommendationForm(request.POST)
        if form.is_valid():
            user_input = {
                "no_of_rooms": form.cleaned_data['no_of_rooms'],
                "attached_required": form.cleaned_data['attached_required'] == 'yes',
                "garage_required": form.cleaned_data['garage_required'] == 'yes',
                "porch_required": form.cleaned_data['porch_required'] == 'yes'
            }
            app_dir = os.path.dirname(os.path.abspath(__file__))
            data_file_path = os.path.join(app_dir, 'data.json')
            with open(data_file_path, "r") as file:
                floor_plans = json.load(file)["floor_plans"]
            recommended_plan_names = recommend_floor_plans(user_input, floor_plans)
            return HttpResponseRedirect(reverse('show_results') + f"?recommended_plan_names={','.join(recommended_plan_names)}")
    else:
        form = FloorPlanRecommendationForm()
    return render(request, 'user_input_form.html', {'form': form})

def show_results_view(request):
    recommended_plan_names = request.GET.get('recommended_plan_names', '').split(',')
    context = {'recommended_plan_names': recommended_plan_names}
    return render(request, 'show_results.html', context)





#     return render(request, 'user_input_form.html', {'form': form, 'recommended_plan_names': recommended_plan_names})


# def show_results_view(request, recommended_plan_names):
#     # Pass the list of recommended plan names to the template
#     context = {'recommended_plan_names': recommended_plan_names}
#     return render(request, 'show_results.html', context)






def landing(request):
    return render(request, 'index.html')