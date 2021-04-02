import Actions
import Conditions


class Event:
    def __init__(self, name: str, to_state: str, pre_conditions: Conditions, post_conditions: Conditions, pre_actions: Actions, post_actions: Actions):
        self.name = name
        self.to_state = to_state
        self.pre_conditions = pre_conditions
        self.post_conditions = post_conditions
        self.pre_actions = pre_actions
        self.post_actions = post_actions

    def to_string(self):
        result_s = "Event: \n"
        result_s += "\tName: " + self.name + "\n"
        result_s += "\tToState: " + self.to_state + "\n"
        result_s += "\tPreConditions: " + self.pre_conditions.to_string() + "\n"
        result_s += "\tPostConditions: " + self.post_conditions.to_string() + "\n"
        result_s += "\tPreActions: " + self.pre_actions.to_string() + "\n"
        result_s += "\tPostActions: " + self.post_actions.to_string() + "\n"
        return result_s
