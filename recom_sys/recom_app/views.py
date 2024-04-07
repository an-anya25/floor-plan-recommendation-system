
# Create your views here.

from django.shortcuts import render, redirect
from .forms import FloorPlanRecommendationForm
from .recommendation import recommend_floor_plans
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import os


def recommend_floor_plans_view(request):
    recommended_plan_names = []
    print("1")
    if request.method == 'POST':
        print("3")
        form = FloorPlanRecommendationForm(request.POST)
        if form.is_valid():
            print("2")
            user_input = {
                "no_of_rooms": form.cleaned_data['no_of_rooms'],
                "attached_required": form.cleaned_data['attached_required'] == 'yes',
                "garage_required": form.cleaned_data['garage_required'] == 'yes',
                "porch_required": form.cleaned_data['porch_required'] == 'yes'
            }


            # Construct the path to data.json relative to the app directory
            app_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file (views.py)
            data_file_path = os.path.join(app_dir, 'data.json')
            print("app_dir", app_dir)
            print("data file path", data_file_path)
            # Load floor plans data from JSON file
            with open(data_file_path, "r") as file:
                floor_plans = json.load(file)["floor_plans"]

            # Get the top two recommended floor plan names
            recommended_plan_names = recommend_floor_plans(user_input, floor_plans)
            print(recommended_plan_names)
            # return show_results_view(request, recommended_plan_names)
            # return redirect('show_results', recommended_plan_names=recommended_plan_names)
            # Redirect to show_results view with recommended_plan_names as query parameter
            # return HttpResponseRedirect(reverse('show_results') + f"?recommended_plan_names={','.join(recommended_plan_names)}")
            # return redirect('show_results')
            redirect_url = reverse('show_results')  + f"?recommended_plan_names={','.join(recommended_plan_names)}"
            return HttpResponseRedirect(redirect_url)
        # else:
        #     print("form not valid")
    else:
        form = FloorPlanRecommendationForm()

    return render(request, 'user_input_form.html', {'form': form})


def show_results_view(request):
    # Retrieve recommended_plan_names from query parameter
    recommended_plan_names = request.GET.get('recommended_plan_names', '').split(',')
    print(request.GET)
    # Pass the list of recommended plan names to the template
    context = {'recommended_plan_names': recommended_plan_names}
    return render(request, 'show_results.html', context)




#     return render(request, 'user_input_form.html', {'form': form, 'recommended_plan_names': recommended_plan_names})


# def show_results_view(request, recommended_plan_names):
#     # Pass the list of recommended plan names to the template
#     context = {'recommended_plan_names': recommended_plan_names}
#     return render(request, 'show_results.html', context)






def landing(request):
    return render(request, 'index.html')