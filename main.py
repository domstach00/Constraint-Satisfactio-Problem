from solve import *
from config import *
from graph.graph import Graph2


def binary(size):
    cp = ConfigBinary(size)
    csp = SolveBinary(cp)
    csp.solve_bt()
    obs1 = csp.get_observators()
    csp2 = SolveBinary(cp)
    csp2.solve_btfc()
    obs2 = csp2.get_observators()
    g = Graph2(obs1, obs2)
    g.make_graph_nodes(f'Binary {size}x{size}')
    g.make_graph_time(f'Binary {size}x{size}')
    print(f"Solutions: {len(csp.solutions)} {len(csp2.solutions)}")


def futoshiki(size):
    cf = ConfigFutoshiki(size)
    sf = SolveFutoshiki(cf)
    sf.solve_bt()
    obs1 = sf.get_observators()
    # sf.end()
    sf2 = SolveFutoshiki(cf)
    sf2.solve_btfc()
    obs2 = sf2.get_observators()
    g = Graph2(obs1, obs2)
    g.make_graph_nodes(f'Futoshiki {size}x{size}')
    g.make_graph_time(f'Futoshiki {size}x{size}')
    print(f'Solutions: {len(sf.solutions)} {len(sf2.solutions)}')


def futoshiki_heuristic():
    cf = ConfigFutoshiki(4)
    sf = SolveFutoshiki(cf)
    sf.solve_bt()
    obs1 = sf.get_observators()
    # sf.end()
    CONSTANTS.GENERAL_IF_FIND_RANDOM = True
    sf2 = SolveFutoshiki(cf)
    sf2.solve_btfc()
    obs2 = sf2.get_observators()
    g = Graph2(obs1, obs2)
    g.make_graph_heuristic()
    print(f'Solutions: {len(sf.solutions)} {len(sf2.solutions)}')


if __name__ == '__main__':
    futoshiki(5)
