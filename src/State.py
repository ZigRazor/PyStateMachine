class State:
    def __init__(self, name: str, events = None):
        if events is None:
            events = {}
        self.name = name
        self.events = events
      
    def to_string(self):
        result_s = "State:\n"
        result_s += "  Name: " + self.name + "\n"
        result_s += "  Events: \n"
        for event in self.events.items():
            result_s += "    " + event[1].to_string() + "\n"
        return result_s