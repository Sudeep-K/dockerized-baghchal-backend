import json
from celery import shared_task
from .utils.baghchal import Board
from .utils.mcts import *


@shared_task(queue="easybot")
def easybot(board_status):
    board = Board()

    request_body = json.loads(board_status)
    board.position = request_body["position"]
    board.player_turn = request_body["player_turn"]
    board.goats["onHand"] = request_body["goats_onhand"]
    board.goats["killed"] = request_body["goats_killed"]
    board.tigers["trapped"] = request_body["tigers_trapped"]

    mcts = MCTS()
    best_move = mcts.search(board, 10)
    ai_moved_board = best_move.board
    response_board_status = {
        "position": ai_moved_board.position,
        "player_turn": ai_moved_board.player_turn,
        "goats_onhand": ai_moved_board.goats["onHand"],
        "goats_killed": ai_moved_board.goats["killed"],
        "tigers_trapped": ai_moved_board.tigers["trapped"],
    }
    # return board_status
    return response_board_status
    # return json.dumps(response_board_status)


@shared_task(queue="mediumbot")
def mediumbot(board_status):
    board = Board()

    request_body = json.loads(board_status)
    board.position = request_body["position"]
    board.player_turn = request_body["player_turn"]
    board.goats["onHand"] = request_body["goats_onhand"]
    board.goats["killed"] = request_body["goats_killed"]
    board.tigers["trapped"] = request_body["tigers_trapped"]

    mcts = MCTS()
    best_move = mcts.search(board, 100)
    ai_moved_board = best_move.board
    response_board_status = {
        "position": ai_moved_board.position,
        "player_turn": ai_moved_board.player_turn,
        "goats_onhand": ai_moved_board.goats["onHand"],
        "goats_killed": ai_moved_board.goats["killed"],
        "tigers_trapped": ai_moved_board.tigers["trapped"],
    }
    # return json.dumps(response_board_status)
    return response_board_status


@shared_task(queue="hardbot")
def hardbot(board_status):
    board = Board()

    request_body = json.loads(board_status)
    board.position = request_body["position"]
    board.player_turn = request_body["player_turn"]
    board.goats["onHand"] = request_body["goats_onhand"]
    board.goats["killed"] = request_body["goats_killed"]
    board.tigers["trapped"] = request_body["tigers_trapped"]

    mcts = MCTS()
    best_move = mcts.search(board, 1000)
    ai_moved_board = best_move.board
    response_board_status = {
        "position": ai_moved_board.position,
        "player_turn": ai_moved_board.player_turn,
        "goats_onhand": ai_moved_board.goats["onHand"],
        "goats_killed": ai_moved_board.goats["killed"],
        "tigers_trapped": ai_moved_board.tigers["trapped"],
    }
    return json.dumps(response_board_status)
