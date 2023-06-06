from django.shortcuts import render

def game_view(request):
    if request.method == 'POST':
        goal = get_goals(request.POST)
        total_scores = (get_largest_blocks(request.POST) + get_goal_scores(request.POST)) - get_roads(request.POST)

        if total_scores >= goal:
            result = 'You Win.'
        else:
            result = 'You Lose.'

        return render(request, 'game/game.html', {'goal': goal, 'total_scores': total_scores, 'result': result})

    return render(request, 'game/game.html')

def get_goals(data):
    goals = []
    for i in range(3):
        goal = int(data.get(f"goal_{i+1}"))
        goals.append(goal)
    return sum(goals)

def get_largest_blocks(data):
    block_types = ['Park', 'Residential', 'Commercial', 'Industrial']
    blocks = []
    for block_type in block_types:
        block = int(data.get(f"block_{block_type.lower()}"))
        blocks.append(block)
    return sum(blocks)

def get_goal_scores(data):
    goal_scores = []
    for i in range(3):
        goal_score = int(data.get(f"goal_score_{i+1}"))
        goal_scores.append(goal_score)
    return sum(goal_scores)

def get_roads(data):
    roads = int(data.get('roads'))
    return roads
