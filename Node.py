class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.child = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.child + self.pr


