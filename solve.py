import time

from config import *
from point import *
import CONSTANTS
import numpy as np


class Solve:
    def __init__(self, config: Config):
        self.config = config
        self.board = config.board
        self.step_count = 0

    def solve_bt(self):
        self.step_count += 1

    def solve_btfc(self):
        self.step_count += 1

    def get_empty_squares(self):
        empty_squares: 'list[Point]'= []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'x':
                    empty_squares.append(Point(row, col))
        return empty_squares

    def _check_unique_row_and_col(self, position):
        row, col = position

        # Check Row unique
        unique_row: list = self.board[row]
        for i in range(row):
            if unique_row == self.board[i]:
                return False

        # Check Col unique
        board_copy = np.array(list(self.board))
        board_copy = board_copy.transpose()
        unique_col = board_copy[col]
        for i in range(col):
            if list(unique_col) == list(board_copy[i]):
                return False
        return True

    def print_board(self, board=None):
        if board is None:
            board = self.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=" ")
            print()
        print("\n")

    def find_fist_empty(self) -> (int, int):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'x':
                    return row, col
        return None

    def find_min_possibility(self) -> (int, int):
        min: Point = self.find_list_of_min_possibilities()[0]
        return min.row, min.col


    def find_list_of_min_possibilities(self) -> list:
        transpose_borad = list(map(list, zip(*self.board)))
        res: 'list[Point]' = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'x':
                    row_possibilities = self.board[row].count('x')
                    col_possibilities = transpose_borad[col].count('x')
                    res.append(Point(
                        row=row,
                        col=col,
                        dependent_values=row_possibilities + col_possibilities
                    ))
        res = sorted(res)
        return res


class SolveBinary(Solve):
    def __init__(self, config: ConfigBinary):
        super().__init__(config)

    def __check_rows_and_columns(self, val: int, position) -> bool:
        row, col = position

        if CONSTANTS.GENERAL_IF_PRINT_STEPS:
            self.print_board()

        # Chceck Row
        nr_of_same_values = 0
        for i in range(row - 2, row + 3):
            if nr_of_same_values >= CONSTANTS.GAME_BP_MAX_SAME_VAL_IN_ROW:
                return False
            if 0 <= i < self.config.width:
                if i == row:
                    nr_of_same_values += 1
                elif self.board[i][col] == val or self.board[i][col] == str(val):
                    nr_of_same_values += 1
                else:
                    nr_of_same_values = 0
        if nr_of_same_values >= CONSTANTS.GAME_BP_MAX_SAME_VAL_IN_ROW:
            return False

        # Check Col
        nr_of_same_values = 0
        for i in range(col - 2, col + 3):
            if nr_of_same_values >= CONSTANTS.GAME_BP_MAX_SAME_VAL_IN_ROW:
                return False
            if 0 <= i < self.config.height:
                if i == col:
                    nr_of_same_values += 1
                elif self.board[row][i] == val or self.board[row][i] == str(val):
                    nr_of_same_values += 1
                else:
                    nr_of_same_values = 0
        if nr_of_same_values >= CONSTANTS.GAME_BP_MAX_SAME_VAL_IN_ROW:
            return False

        return True

    def __check_uniformity_of_list(self, array: list) -> bool:
        if not array:
            return True
        uni_val = array[0]
        for elem in array:
            if elem != uni_val:
                return False
        return True

    def __same_amount_of_val(self, position):
        pass

    def __valid(self, val: int, position) -> bool:
        if not self._check_unique_row_and_col(position):
            return False
        if not self.__same_amount_of_val(position):
            return False
        if not self.__check_rows_and_columns(val, position):
            return False

        return True

    def __get_possible_values_by_valid(self, position) -> list:
        possible_values = []
        for val in CONSTANTS.GAME_BP_AVAILABLE_VALUES:
            if self.__valid(val, position):
                possible_values.append(val)
        return possible_values

    def __get_available_values_by_comapre(self, position) -> list:
        row, col = position
        possible_values: list = list(CONSTANTS.GAME_BP_AVAILABLE_VALUES)
        for val in self.board[row]:
            if val in possible_values:
                possible_values.remove(val)

        transpose_board = list(map(list, zip(*self.board)))
        for val in transpose_board[col]:
            if val in possible_values:
                possible_values.remove(val)
        return possible_values


    def __fill_squares_without_dependencies(self, possibilities: 'list[Point]') -> bool:
        flag = False
        for elem in possibilities:
            if elem.dependent_values == 0:
                self.board[elem.row][elem.col] = self.__get_possible_values_by_valid((elem.row, elem.col))[0]
                flag = True
        return flag


    def solve_btfc(self):
        possibilities: 'list[Point]' = self.find_list_of_min_possibilities()
        if not possibilities:
            return True
        self.step_count += 1

        while self.__fill_squares_without_dependencies(possibilities):
            possibilities = self.find_list_of_min_possibilities()
            if not possibilities:
                return True
            self.__fill_squares_without_dependencies(possibilities)

        row, col = possibilities[0].row, possibilities[0].col

        for i in CONSTANTS.GAME_BP_AVAILABLE_VALUES:
            if self.__valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve_btfc():
                    return True
                self.board[row][col] = 'x'
            if CONSTANTS.GENERAL_IF_PRINT_STEPS:
                self.print_board()


    def solve_bt(self):
        find = self.find_fist_empty()
        if not find:
            return True
        self.step_count += 1
        row, col = find

        for i in CONSTANTS.GAME_BP_AVAILABLE_VALUES:
            if self.__valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve_bt():
                    return True
                self.board[row][col] = 'x'
        if CONSTANTS.GENERAL_IF_PRINT_STEPS:
            self.print_board()


class SolveFutoshiki(Solve):

    def __init__(self, config: ConfigFutoshiki):
        self.config = config
        self.board = config.board
        self.board_sign_horizontal = config.board_sign_horizontal
        self.board_sign_vertical = config.board_sign_vertical
        self.avalaible_numbers: list = [i for i in range(1, self.config.width + 1)]
        self.step_count = 0

    def __check_equalities(self, val, position):
        row, col = position

        # Check Row
        if col - 1 >= 0:
            if self.board_sign_horizontal[row][col - 1] == '>' and self.__check_is_number(row, col - 1):
                if not self.board[row][col - 1] > val:
                    return False
            elif self.board_sign_horizontal[row][col - 1] == '<' and self.__check_is_number(row, col - 1):
                if not self.board[row][col - 1] < val:
                    return False
        if col + 1 < self.config.width:
            if self.board_sign_horizontal[row][col] == '>' and self.__check_is_number(row, col + 1):
                if not val > self.board[row][col + 1]:
                    return False
            elif self.board_sign_horizontal[row][col] == '<' and self.__check_is_number(row, col + 1):
                if not val < self.board[row][col + 1]:
                    return False

        # Check Col
        if row - 1 >= 0:
            if self.board_sign_vertical[row - 1][col] == '>' and self.__check_is_number(row - 1, col):
                if not self.board[row - 1][col] > val:
                    return False
            elif self.board_sign_vertical[row - 1][col] == '<' and self.__check_is_number(row - 1, col):
                if not self.board[row - 1][col] < val:
                    return False
        if row + 1 < self.config.height:
            if self.board_sign_vertical[row][col] == '>' and self.__check_is_number(row + 1, col):
                if not val > self.board[row + 1][col]:
                    return False
            elif self.board_sign_vertical[row][col] == '<' and self.__check_is_number(row + 1, col):
                if not val < self.board[row + 1][col]:
                    return False
        return True

    def __check_unique_val_in_row_and_col(self, val: int, position):
        row, col = position

        # Check Row value unique
        if val in self.board[row]:
            return False

        if row == 0 and col == 2 and val == 3:
            pass

        # Check Col value unique
        board_copy = np.array(list(self.board))
        board_copy = board_copy.transpose()
        lista: list = list(board_copy[col])
        if str(val) in lista:
            return False
        return True

    def __check_is_number(self, row, col):
        return self.board[row][col] in self.avalaible_numbers

    def __valid(self, val: int, position):
        if not self.__check_unique_val_in_row_and_col(val, position):
            return False
        if not self._check_unique_row_and_col(position):
            return False
        if not self.__check_equalities(val, position):
            return False
        return True

    def __get_possible_values_by_valid(self, position) -> list:
        possible_values = []
        for val in self.avalaible_numbers:
            if self.__valid(val, position):
                possible_values.append(val)
        return possible_values

    def __get_possible_values_bu_compare(self, position) -> list:
        row, col = position
        possible_values: list = list(self.avalaible_numbers)
        for val in self.board[row]:
            if val in possible_values:
                possible_values.remove(val)

        transpose_board = list(map(list, zip(*self.board)))
        for val in transpose_board[col]:
            if val in possible_values:
                possible_values.remove(val)
        return possible_values

    def __fill_squares_without_dependencies(self, possibilities):
        flag = False
        for elem in possibilities:
            if elem.dependent_values == 0:
                self.board[elem.row][elem.col] = self.__get_possible_values_by_valid((elem.row, elem.col))[0]
                flag = True
        return flag


    def solve_btfc(self):
        possibilities: 'list[Point]' = self.find_list_of_min_possibilities()
        if not possibilities:
            return True
        self.step_count += 1

        while self.__fill_squares_without_dependencies(possibilities):
            possibilities = self.find_list_of_min_possibilities()
            if not possibilities:
                return True
        row, col = possibilities[0].row, possibilities[0].col

        for i in self.__get_possible_values_by_valid((row, col)):
            if self.__valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve_btfc():
                    return True
                self.board[row][col] = 'x'

        if CONSTANTS.GENERAL_IF_PRINT_STEPS:
            print(f"Step: {self.step_count}")
            self.print_board()


    def solve_bt(self):
        find = self.find_fist_empty()
        if not find:
            return True
        self.step_count += 1
        row, col = find

        for i in self.avalaible_numbers:
            if self.__valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve_bt():
                    return True
                self.board[row][col] = 'x'
        if CONSTANTS.GENERAL_IF_PRINT_STEPS:
            print(f"Step: {self.step_count}")
            self.print_board()
