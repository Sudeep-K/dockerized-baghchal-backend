import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.baghchal import Board
from .utils.mcts import *
from .tasks import easybot, mediumbot, hardbot

#                 {"task_id": result.task_id, "status": "Task submitted successfully!"},
#                 status=200,


@csrf_exempt
def get_best_move(request):
    request_body = json.loads(request.body)

    game_mode = request_body["game_mode"]

    if game_mode == "easy":
        ai_moved_board = easybot.delay(request.body)
    elif game_mode == "medium":
        ai_moved_board = mediumbot.delay(request.body)
    else:
        ai_moved_board = hardbot.delay(request.body)
    # return HttpResponse(ai_moved_board.get())
    return JsonResponse(ai_moved_board.get(), status=200, safe=False)
