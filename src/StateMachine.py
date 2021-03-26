from ReadStateMachine import ReadStateMachineFile
from State import State
from Event import Event
import logging

class StateMachine:
    def __init__(self, xml_file : str):
        self.xml_file = xml_file
        self.states = None
        self.current_state = ""
        self.context = {}
        logging.basicConfig(filename=xml_file.split(sep=".xml")[0] + '.log',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    def __CheckConditions(self,conditions):
        all_conditions_satisfied = True
        if(conditions != None):
            _conditions = conditions.conditions
            for condition in _conditions:
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
                    logging.error("No Found Condition Expression %s in Context", condition.expression)
                    all_conditions_satisfied = False      
        else:
            logging.info("No Condition")
        return all_conditions_satisfied

    def __ExecActions(self,actions):
        all_action_executed = True
        if(actions != None):
            _actions = actions.actions
            for action in _actions:
                if action.expression in self.context:
                    func = self.context[action.expression]                    
                    if callable(func):
                        #print("Call ",action.expression)
                        func()
                    else:
                        func 
                else:
                    logging.error("No Found Action Expression %s in Context", action.expression)
                    all_action_executed = False;                
        else:
            logging.info("No Action")        
        return all_action_executed

    def get_current_state(self):
        return self.current_state

    def LoadStateMachine(self):
        if (self.states != None):
            logging.error("State Machine already loaded")
        else:    
            self.xml_file
            self.states , self.current_state = ReadStateMachineFile(self.xml_file)
            logging.info('State Machine Loaded')

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
            all_pre_conditions_satisfied = self.__CheckConditions(handled_event.pre_conditions)
            if(all_pre_conditions_satisfied):
                ## Preactions
                all_pre_actions_executed = self.__ExecActions(handled_event.pre_actions)
                if(all_pre_actions_executed):
                    ## Transition
                    logging.debug("Transition %s ------> %s", self.current_state, handled_event.to_state)
                    self.current_state = handled_event.to_state
                    ## Postactions
                    ## Postconditions
            else:
                logging.error("Not all PreConditions satisfied")
        else:
            logging.error("Not a possible event")

    
        


