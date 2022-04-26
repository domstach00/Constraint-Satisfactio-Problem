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