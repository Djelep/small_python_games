import sys


class Game:
    def __init__(self, player_x, player_o):
        self.player_x = player_x
        self.player_o = player_o
        self.field = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]

    def play(self):
        turn = 1
        self.show_field()
        while turn < 9:
            if turn % 2 == 1:
                self.ask_for_move(self.player_x)
                self.show_field()
            else:
                self.ask_for_move(self.player_o)
                self.show_field()
            if turn > 4:
                if self.check_if_position_is_winning():
                    print(f"Player {self.player_x.name} is winner")
                    sys.exit()
            turn += 1
        print("It's a draw")

    def check_if_position_is_winning(self):
        winning_lines = [self.field[0],
                         self.field[1],
                         self.field[2],
                         [self.field[0][0],
                         self.field[1][0],
                         self.field[2][0]],
                         [self.field[0][1],
                         self.field[1][1],
                         self.field[2][1]],
                         [self.field[0][2],
                          self.field[1][2],
                          self.field[2][2]],
                         [self.field[0][0],
                          self.field[1][1],
                          self.field[2][2]],
                         [self.field[0][2],
                          self.field[1][1],
                          self.field[2][0]],
                         ]
        for i in winning_lines:
            signs_in_line = set(i)
            if len(signs_in_line) == 1 and "_" not in signs_in_line:
                return True

    def check_if_move_is_valid(self, cell):
        return self.field[cell[0]][cell[1]] == "_"

    def ask_for_move(self, player):
        tries = 3
        for i in range(tries):
            cell = player.do_move()
            if self.check_if_move_is_valid(cell):
                self.field[cell[0]][cell[1]] = player.sign
                break
            else:
                print("Sorry this cell is populated")
                tries -= 1
                continue
        else:
            print(f"Sorry player {player.name} is a moron ")

    def show_field(self):
        for i in self.field:
            print(f"{i}\n")
