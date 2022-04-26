import matplotlib.pyplot as plt
from CONSTANTS import *
from config import *
from graph.observator import *


class Graph:
    graph_id = 1
    graph_style = GRAPH_STYLE

    def __init__(self, observators: 'list[Observator]', config: Config):
        self.observators = observators
        self.config = config
        self.field_graph = list(range(0, len(observators)))
        self.notify_times = []
        self.visited_nodes = []
        self.__get_data()

    def __get_data(self):
        for elem in self.observators:
            self.notify_times.append(elem.measured_time)
            self.visited_nodes.append(elem.node_count)

    def setting(self):
        plt.clf()
        self.graph_name = f"Graph nr_{self.graph_id}"
        plt.title(self.graph_name)
        plt.style.use(self.graph_style)
        # plt.xlim(xmin=0)
        # plt.ylim(ymin=0)

    def make_graph_1(self):
        # plt.figtext(.15, .76, 'details')
        self.setting()
        plt.plot(self.field_graph, self.visited_nodes, label='Nodes')
        if GRAPH_SAVE:
            plt.savefig(f'{self.graph_name}.png')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        self.graph_id += 1

    def make_graph_2(self):
        self.setting()
        plt.plot(self.field_graph, self.notify_times, label='Time')
        if GRAPH_SAVE:
            plt .savefig(f'{self.graph_name}.png')
        plt.legend()
        plt.grid(True)
        # plt.tight_layout()
        plt.show()
        self.graph_id += 1


class Graph2:
    graph_id = 1
    graph_style = GRAPH_STYLE

    def __init__(self, observators1: 'list[Observator]', observators2: 'list[Observator]'):
        self.observators_1 = observators1
        self.observators_2 = observators2
        self.field_graph_1 = list(range(0, len(observators1)))
        self.field_graph_2 = list(range(0, len(observators2)))
        self.notify_times_1 = []
        self.visited_nodes_1 = []
        self.notify_times_2 = []
        self.visited_nodes_2 = []
        self.__get_data()

    def __get_data(self):
        for elem in self.observators_1:
            self.notify_times_1.append(elem.measured_time)
            self.visited_nodes_1.append(elem.node_count)
        for elem in self.observators_2:
            self.notify_times_2.append(elem.measured_time)
            self.visited_nodes_2.append(elem.node_count)

    def setting(self, name=''):
        plt.clf()
        self.graph_name = f"Graph - porownanie metod sprawdzania {name}"
        plt.title(self.graph_name)
        plt.style.use(self.graph_style)
        # plt.xlim(xmin=0)
        # plt.ylim(ymin=0)

    def make_graph_nodes(self, name=''):
        self.setting(f'{name} Nodes')
        plt.plot(self.field_graph_1, self.visited_nodes_1, label='Nodes-FC', color='b')
        plt.plot(self.field_graph_2, self.visited_nodes_2, label='Nodes-BT', color='r')
        plt.legend()
        plt.grid(True)
        if GRAPH_SAVE:
            plt.savefig(f'{self.graph_name}.png')
        plt.show()
        self.graph_id += 1

    def make_graph_time(self, name=''):
        self.setting(f'{name} Time')
        plt.plot(self.field_graph_1, self.notify_times_1, label='Time-FC', color='b')
        plt.plot(self.field_graph_2, self.notify_times_2, label='Time-BT', color='r')
        plt.legend()
        plt.grid(True)
        plt.show()
        self.graph_id += 1

    def make_graph_heuristic(self):
        plt.clf()
        plt.title('Graph - Heurystyki wybory zmiennej Futoshiki 4x4')
        plt.style.use(self.graph_style)
        plt.plot(self.field_graph_1, self.visited_nodes_1, label='Nodes-Find_first_empty', color='b')
        plt.plot(self.field_graph_2, self.visited_nodes_2, label='Nodes-Find_random_empty', color='r')
        plt.legend()
        plt.grid()
        plt.show()
