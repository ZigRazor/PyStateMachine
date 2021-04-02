class Conditions:
    def __init__(self, conditions = None ):
        if conditions is None:
            conditions = []
        self.conditions = conditions

    @staticmethod
    def to_string():
        result_s = ""
        return result_s