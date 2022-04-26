from solve import *
from config import *
import threading


def binary():
    cp = ConfigBinary(8)
    csp = SolveBinary(cp)
    csp.solve_bt()
    csp.print_board(csp.solutions[0])
    print(f"Solutions: {len(csp.solutions)}")


def futoshiki():
    cf = ConfigFutoshiki(6)
    sf = SolveFutoshiki(cf)
    sf.solve_btfc()
    sf.end()
    print(f'Solutions: {len(sf.solutions)}')


def futoshiki2():
    cf = ConfigFutoshiki(4)
    sf = SolveFutoshiki(cf)
    sf.solve_btfc()
    print("BTFC")
    sf.print_board()
    print(sf.step_count)


def multi():
    t1 = threading.Thread(target=futoshiki())
    t2 = threading.Thread(target=futoshiki2())
    t1.start()
    t2.start()


if __name__ == '__main__':
    futoshiki()
