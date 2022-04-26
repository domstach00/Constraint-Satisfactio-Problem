import CONSTANTS


class Config:
    def __init__(self, width: int):
        self.width = width
        self.height = width
        self.board = None

    def read_file(self):
        pass

    def print_board(self, board: 'list[list]' = None):
        if board is None:
            board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=" ")
            print()
        print("\n\n")

    def print_list(self, array: list):
        print("\nPrinting list")
        for elem in array:
            print(elem)


class ConfigBinary(Config):
    def __init__(self, width: int):
        super().__init__(width)
        self.width = width
        self.height = width
        self.path = f'dane/binary_{width}x{width}'
        self.board = None
        self.read_file()

    def read_file(self):
        lista = []
        with open(self.path) as file:
            for line in file.read().splitlines():
                new_row = []
                for val in line:
                    new_row.append(val)
                lista.append(new_row)
        self.board = lista


class ConfigFutoshiki(Config):
    def __init__(self, width: int):
        super().__init__(width)
        self.width = width
        self.height = width
        self.path = f'dane/futoshiki_{width}x{width}'
        self.board = None
        self.board_sign_vertical = None
        self.board_sign_horizontal = None
        self.read_file()

    def read_file(self):
        lista = []
        lista_znakow_pion = []
        lista_znakow_poziom = []

        with open(self.path) as file:
            line_nr = 0
            for line in file.read().splitlines():
                new_row = []
                new_znaki_pion = []
                new_znaki_poziom = []
                for val in line:
                    if line_nr % 2 == 1:
                        new_znaki_pion.append(val)
                    elif val in CONSTANTS.GAME_FP_SIGNS_LIST:
                        new_znaki_poziom.append(val)
                    else:
                        if val != 'x':
                            new_row.append(int(val))
                        else:
                            new_row.append(val)
                line_nr += 1
                if new_row != []:
                    lista.append(new_row)
                if new_znaki_poziom != []:
                    lista_znakow_poziom.append(new_znaki_poziom)
                if new_znaki_pion != []:
                    lista_znakow_pion.append(new_znaki_pion)

        self.board = lista
        self.board_sign_horizontal = lista_znakow_poziom
        self.board_sign_vertical = lista_znakow_pion
