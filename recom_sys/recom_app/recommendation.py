import json

def calculate_similarity(user_input, floor_plan):
    similarity_score = 0
    
    if user_input["attached_required"] == (floor_plan["no_of_attached"] > 0):
        similarity_score += 1
    
    if user_input["garage_required"] == (floor_plan["garage"] == "yes"):
        similarity_score += 1
    
    if user_input["porch_required"] == (floor_plan["porch"] == "yes"):
        similarity_score += 1
    
    return similarity_score

def recommend_floor_plans(user_input, floor_plans):
    if user_input["attached_required"]:
        filtered_floor_plans = [plan for plan in floor_plans if plan["no_of_rooms"] == user_input["no_of_rooms"] and plan["no_of_attached"] > 0]
    else:
        filtered_floor_plans = [plan for plan in floor_plans if plan["no_of_rooms"] == user_input["no_of_rooms"]]
    
    for floor_plan in filtered_floor_plans:
        floor_plan["similarity_score"] = calculate_similarity(user_input, floor_plan)

    sorted_floor_plans = sorted(filtered_floor_plans, key=lambda x: x["similarity_score"], reverse=True)

    return [plan['name'] for plan in sorted_floor_plans[:2]]  # Return names of top 2 floor plans
