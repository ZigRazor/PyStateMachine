from ReadStateMachine import ReadStateMachineFile
from State import State
from Event import Event

class StateMachine:
    def __init__(self, xml_file : str):
        self.xml_file = xml_file
        self.states = None
        self.current_state = ""
        self.context = {}

    def __CheckCondition(self,conditions):
        all_conditions_satisfied = True
        if(conditions != None):
            conditions = conditions.conditions
            for condition in conditions:
                if condition.expression in self.context:
                    func = self.context[condition.expression]
                    result = None
                if callable(func):
                    result = func()
                else:
                    result = func
                if str(result) != condition.result:
                    all_conditions_satisfied = False
                    break
        else:
            print("No Precondition")
        return all_conditions_satisfied

    def get_current_state(self):
        return self.current_state

    def LoadStateMachine(self):
        if (self.states != None):
            print("State Machine already loaded")
        else:    
            self.xml_file
            self.states , self.current_state = ReadStateMachineFile(self.xml_file)

    def addVariableToContext(self, module : str, variable : str):
        mod = __import__(module)
        func = getattr(mod, variable)
        self.context[module+"."+variable] = func
        
    def InjectEvent(self, event : str):
        my_state = self.states[self.current_state]
        possible_events = my_state.events
        if event in possible_events:
            handled_event = possible_events[event]
            ## Preconditions
            all_pre_conditions_satisfied = self.__CheckCondition(handled_event.pre_conditions)
            if(all_pre_conditions_satisfied):
                ## Preactions
                ## Transition
                print("Transition ", self.current_state, " ------> ", handled_event.to_state)
                self.current_state = handled_event.to_state
                ## Postactions
                ## Postconditions
            else:
                print("Not all PreConditions satisfied")
        else:
            print("Not a possible event")

    
        


