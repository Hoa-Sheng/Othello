import random
import copy

# Classe du Bot
class XxScl4ve_DestroyerxX:
    def __init__(self):
        self.name = "Scl4ve"
   
    # BOT FUNCTIONS

    def check_valid_moves(self, toto, anus):
        tour = (anus.score_black + anus.score_white) - 4
        fourretout = []
        max_score = -999
        matricedebut = [
        50, -10, 10, 5, 5, 10, -10, 50,
        -10, -25, -6, -6, -6, -6, -25, -10,
        10, -6, 50, 10, 10, 50, -6, 10,
        5, -6, 10, 0, 0, 10, -6, 5,
        5, -6, 10, 0, 0, 10, -6, 5,
        10, -6, 50, 10, 10, 50, -6, 10,
        -10, -25, -6, -6, -6, -6, -25, -10,
        50, -10, 10, 5, 5, 10, -10, 50
        ]
        matricemilieu = [
        50, -10, 10, 5, 5, 10, -10, 50,
        -10, -25, -10, -6, -6, -10, -25, -10,
        15, -10, 5, 1, 1, 5, -6, 15,
        5, -6, 1, 0, 0, 1, -6, 5,
        5, -6, 1, 0, 0, 1, -6, 5,
        15, -6, 5, 1, 1, 50, -6, 15,
        -10, -25, -10, -6, -6, -10, -25, -10,
        50, -10, 10, 5, 5, 10, -10, 50
        ]
        compteur=0
        for tile_index in toto.board:
            ff=0
            tour = anus.score_black + anus.score_white - 4
            prout = toto.is_legal_move( tile_index.x_pos, tile_index.y_pos, anus.active_player)
            if prout != False:
                if tour <= 15:
                    ff += matricedebut[compteur]
                elif tour > 15:
                    ff += matricemilieu[compteur]
                for zizi in prout:
                    ff += zizi[0]


                ff -= self.prediction(tile_index, toto, anus)


                if ff > max_score:
                    max_score = ff
                    fourretout = []
                    fourretout.append([tile_index.x_pos, tile_index.y_pos])
                elif ff == max_score:
                    fourretout.append([tile_index.x_pos, tile_index.y_pos])
            compteur += 1           
        return random.choice(fourretout)
    
    def prediction(self, tile, board, game):
        my_board = copy.deepcopy(board)
        my_game = copy.deepcopy(game)
        my_game.place_pawn(tile.x_pos, tile.y_pos, my_board, my_game.active_player)
        return self.get_score(my_board, my_game)

    def get_score(self, toto, anus):
        tour = (anus.score_black + anus.score_white) - 4
        max_score = -999
        matricedebut = [
        50, -10, 10, 5, 5, 10, -10, 50,
        -10, -25, -6, -6, -6, -6, -25, -10,
        10, -6, 50, 10, 10, 50, -6, 10,
        5, -6, 10, 0, 0, 10, -6, 5,
        5, -6, 10, 0, 0, 10, -6, 5,
        10, -6, 50, 10, 10, 50, -6, 10,
        -10, -25, -6, -6, -6, -6, -25, -10,
        50, -10, 10, 5, 5, 10, -10, 50
        ]
        matricemilieu = [
        50, -10, 10, 5, 5, 10, -10, 50,
        -10, -25, -10, -6, -6, -10, -25, -10,
        15, -10, 5, 1, 1, 5, -6, 15,
        5, -6, 1, 0, 0, 1, -6, 5,
        5, -6, 1, 0, 0, 1, -6, 5,
        15, -6, 5, 1, 1, 50, -6, 15,
        -10, -25, -10, -6, -6, -10, -25, -10,
        50, -10, 10, 5, 5, 10, -10, 50
        ]
        compteur=0
        for tile_index in toto.board:
            ff=0
            tour = anus.score_black + anus.score_white - 4
            prout = toto.is_legal_move( tile_index.x_pos, tile_index.y_pos, anus.active_player)
            if prout != False:
                if tour <= 15:
                    ff += matricedebut[compteur]
                elif tour > 15:
                    ff += matricemilieu[compteur]
                for zizi in prout:
                    ff += zizi[0]
                if ff > max_score:
                    max_score = ff
            compteur += 1 
                 
        return max_score
    

# Création du Bot
croto_bot = XxScl4ve_DestroyerxX()

# Exécution du Bot
move_coordinates = croto_bot.check_valid_moves(othello_board, othello_game)