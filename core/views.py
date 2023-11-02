from django.shortcuts import render
from django.http import HttpResponse


def game_view(request):
    if request.method == "POST":
        try:
            goal = get_goals(request.POST)
            total_scores = calculate_total_scores(request.POST)
            result = "You Win." if total_scores >= goal else "You Lose."
            context = {"goal": goal, "total_scores": total_scores, "result": result}
            return render(request, "game/home.html", context)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return HttpResponse(error_message, status=500)
    return render(request, "game/home.html")


def tutorial_view(request):
    return render(request, "game/tutorial.html")


def overview_view(request):
    return render(request, "game/overview.html")


def get_goals(data):
    goals = [int(data.get(f"goal_{i+1}")) for i in range(3)]
    return sum(goals)


def calculate_total_scores(data):
    block_types = ["Park", "Residential", "Commercial", "Industrial"]
    blocks = [
        int(data.get(f"block_{block_type.lower()}")) for block_type in block_types
    ]
    goal_scores = [int(data.get(f"goal_score_{i+1}")) for i in range(3)]
    roads = int(data.get("roads"))
    return sum(blocks) + sum(goal_scores) - roads
