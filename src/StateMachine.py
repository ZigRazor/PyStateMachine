from ReadStateMachine import ReadStateMachineFile
from State import State
from Event import Event

class StateMachine:
    def __init__(self, xml_file : str):
        self.xml_file = xml_file
        self.states = None
        self.current_state = ""

    def get_current_state(self):
        return self.current_state

    def LoadStateMachine(self):
        if (self.states != None):
            print("State Machine already loaded")
        else:    
            self.xml_file
            self.states , self.current_state = ReadStateMachineFile(self.xml_file)
        
    def InjectEvent(self, event : str):
        my_state = self.states[self.current_state]
        possible_events = my_state.get_events()
        if event in possible_events:
            handled_event = possible_events[event]
            ## Preconditions
            ## Preactions
            print("Transition ", self.current_state, " ------> ", handled_event.get_to_state())
            self.current_state = handled_event.get_to_state()
            ## Postactions
            ## Postconditions
        else:
            print("Not a possible event")

