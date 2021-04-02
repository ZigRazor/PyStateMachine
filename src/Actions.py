class Actions:
    def __init__(self, actions = None):
        if actions is None:
            actions = []
        self.actions = actions
    @staticmethod
    def to_string():
        result_s = ""
        return result_s