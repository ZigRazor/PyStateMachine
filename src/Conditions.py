class Conditions:
    """Define Conditions"""

    def __init__(self, conditions=None):
        if conditions is None:
            conditions = []
        self.conditions_list = conditions

    @staticmethod
    def to_string():
        result_s = ""
        return result_s
