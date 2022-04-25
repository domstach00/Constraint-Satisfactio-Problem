class Observator:
    def __init__(self, measured_time, node_count: int, solutions: int, game_name: str, search_type: str):
        self.measured_time = measured_time
        self.node_count = node_count
        self.solutions = solutions
        self.game_name = game_name
        self.search_type = search_type
