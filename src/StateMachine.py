from ReadStateMachine import ReadStateMachineFile
import logging

class StateMachine:
    def __init__(self, xml_file : str):
        self.xml_file = xml_file
        self.states = None
        self.current_state = ""
        self.context = {}
        self.saved_state = None
        logging.basicConfig(filename=xml_file.split(sep=".xml")[0] + '.log',format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    def __CheckConditions(self,conditions):
        all_conditions_satisfied = True
        if(conditions is not None):
            _conditions = conditions.conditions
            for condition in _conditions:
                module,expression = self.__PrepareExpression(condition.expression)
                if module in self.context:                    
                    mod = self.context[module]
                    try:  
                        func = getattr(mod, expression) 
                        result = None
                        if callable(func):
                            result = func()
                        else:
                            result = func
                        if str(result) != condition.result:
                            all_conditions_satisfied = False
                            break
                    except:
                        logging.error("Not Found Expression %s in Context", condition.expression)
                        all_conditions_satisfied = False  
                else:
                    logging.error("Not Found Module %s in Context", module)
                    all_conditions_satisfied = False      
        else:
            logging.info("No Condition")
        return all_conditions_satisfied

    def __ExecActions(self,actions):
        all_action_executed = True
        if(actions is not None):
            _actions = actions.actions
            for action in _actions:
                module,expression = self.__PrepareExpression(action.expression)
                if module in self.context:                    
                    mod = self.context[module]
                    try:  
                        func = getattr(mod, expression) 
                        if callable(func):
                            func()
                        else:
                            func
                    except:
                        logging.error("Not Found Expression %s in Context", action.expression)
                        all_action_executed = False;
                else:
                    logging.error("Not Found Module %s in Context", module)
                    all_action_executed = False;                
        else:
            logging.info("No Action")        
        return all_action_executed

    def __SaveState(self):
        self.saved_state = [self.current_state, self.context]

    def __RestoreState(self):
        self.current_state = self.saved_state[0]
        self.context = self.saved_state[1]

    @staticmethod
    def __PrepareExpression(expression):
        module_expression=expression.rsplit('.',1)
        return module_expression[0],module_expression[1]

    def get_current_state(self):
        return self.current_state

    def LoadStateMachine(self):
        if (self.states is not None):
            logging.error("State Machine already loaded")
        else:    
            self.xml_file
            self.states , self.current_state = ReadStateMachineFile(self.xml_file)
            logging.info('State Machine Loaded')

    def addModuleToContext(self, module : str):
        mod = __import__(module)        
        self.context[module] = mod
        
    def InjectEvent(self, event : str):
        my_state = self.states[self.current_state]
        possible_events = my_state.events
        if event in possible_events:
            handled_event = possible_events[event]
            ## Save Old State
            self.__SaveState()
            ## Preconditions
            all_pre_conditions_satisfied = self.__CheckConditions(handled_event.pre_conditions)
            if(all_pre_conditions_satisfied):
                logging.debug("PreConditions satisfied") 
                ## Preactions
                all_pre_actions_executed = self.__ExecActions(handled_event.pre_actions)
                if(all_pre_actions_executed):
                    logging.debug("PreActions Executed")                    
                    ## Transition
                    logging.debug("Transition %s ------> %s", self.current_state, handled_event.to_state)
                    self.current_state = handled_event.to_state
                    ## Postactions
                    all_post_actions_executed = self.__ExecActions(handled_event.post_actions)
                    if(all_post_actions_executed):
                        logging.debug("PostActions Executed")
                        ## Postconditions
                        all_post_conditions_satisfied = self.__CheckConditions(handled_event.post_conditions)
                        if(all_post_conditions_satisfied):
                            logging.debug("PostConditions Satisfied")
                        else:
                            logging.error("Not all PostConditions satisfied, restore saved state")
                            self.__RestoreState()
                    else:
                        logging.error("Not all PostActions Executed, restore saved state")
                        self.__RestoreState()
                else:
                    logging.error("Not all PretActions Executed, restore saved state")
                    self.__RestoreState()                    
            else:
                logging.error("Not all PreConditions satisfied")
        else:
            logging.error("Not a possible event")

    
        


