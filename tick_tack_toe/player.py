class Player:
    def __init__(self, name, player_type, sign):
        self.name = name
        self.type = player_type
        self.sign = sign

    @staticmethod
    def do_move():
        retries = 3
        for attempt in range(retries):
            try:
                line = int(input("Please enter desired line:"))
                raw = int(input("Please enter desired row: "))
                if not (0 <= line < 3 and 0 <= raw < 3):
                    raise ValueError
                return [line, raw]
            except ValueError as error:
                if attempt < retries:
                    attempt += 1
                    print("Error, line and row must be integers!")
                else:
                    raise error
