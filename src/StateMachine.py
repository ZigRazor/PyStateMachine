from ReadStateMachine import ReadStateMachineFile
import logging


class StateMachine:
    """
    This is a class defines state machine operations.

    Attributes:
        xml_file (str): The name of the xml that defines the state machine.
        states (list): list of possible states of the machine.
        current_state (str): the current state of the machine.
        context (dict): dictionary that contains the imported module 
            at runtime for state machine operations.
        saved_state (list): list of variables for restore state in case of rollback.
    """
    def __init__(self, xml_file: str):
        """
        The constructor for StateMachine class.

        Parameters:
           xml_file (str): The name of the xml that defines the state machine.
        """
        self.xml_file = xml_file
        self.states = None
        self.current_state = ""
        self.context = {}
        self.saved_state = None
        logging.basicConfig(
            filename=xml_file.split(sep=".xml")[0] + '.log',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.DEBUG
        )

    def __CheckConditions(self, conditions):
        """
        This Function checks the conditions passed as argument

        Parameters:
           conditions (list): List of condition to check.
        Returns:
            all_conditions_satisfied: 
                a boolean that indicates if all conditions are satisfied
        """
        all_conditions_satisfied = True
        if conditions is not None:
            _conditions = conditions.conditions_list
            for condition in _conditions:
                module, expression = self.__PrepareExpression(
                    condition.expression)
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
                    except AttributeError:
                        logging.error(
                            "Not Found Expression %s in Context", condition.expression)
                        all_conditions_satisfied = False
                else:
                    logging.error("Not Found Module %s in Context", module)
                    all_conditions_satisfied = False
        else:
            logging.info("No Condition")
        return all_conditions_satisfied

    def __ExecActions(self, actions):
        """
        This Function executes the actions passed as argument

        Parameters:
           actions (list): List of actions to execute.
        Returns:
            all_action_executed: a boolean that indicates if all actions are executed
        """
        all_action_executed = True
        if actions is not None:
            _actions = actions.actions_list
            for action in _actions:
                module, expression = self.__PrepareExpression(
                    action.expression)
                if module in self.context:
                    mod = self.context[module]
                    try:
                        func = getattr(mod, expression)
                        if callable(func):
                            func()
                    except AttributeError:
                        logging.error(
                            "Not Found Expression %s in Context", action.expression)
                        all_action_executed = False
                else:
                    logging.error("Not Found Module %s in Context", module)
                    all_action_executed = False
        else:
            logging.info("No Action")
        return all_action_executed

    def __SaveState(self):
        """
        This Function saves internal state
        """
        self.saved_state = [self.current_state, self.context]

    def __RestoreState(self):
        """
        This Function restores the saved state
        """
        self.current_state = self.saved_state[0]
        self.context = self.saved_state[1]

    @staticmethod
    def __PrepareExpression(expression):
        """
        This Function split expression in module and expression

        Parameters:
           expression (str): complete expression.
        Returns:
            module (str): module string
            expression (str): expression string
        """
        module_expression = expression.rsplit('.', 1)
        return module_expression[0], module_expression[1]

    def get_current_state(self):
        """
        This Function return current state

        Returns:
            current_state (str): current state
        """
        return self.current_state

    def LoadStateMachine(self):
        """
        This Function load state machine configuration
        """
        if self.states is not None:
            logging.error("State Machine already loaded")
        else:
            self.states, self.current_state = ReadStateMachineFile(
                self.xml_file)
            logging.info('State Machine Loaded')

    def addModuleToContext(self, module: str):
        """
        This Function adds a module to the context of state machine

        Parameters:
           module (str): The module to add.
        """
        mod = __import__(module)
        self.context[module] = mod

    def InjectEvent(self, event: str):
        """
        This Function execute the event injected

        Parameters:
           event (str): Event injected
        """
        my_state = self.states[self.current_state]
        possible_events = my_state.events
        if event in possible_events:
            handled_event = possible_events[event]
            # Save Old State
            self.__SaveState()
            # Preconditions
            all_pre_conditions_satisfied = self.__CheckConditions(
                handled_event.pre_conditions)
            if all_pre_conditions_satisfied:
                logging.debug("PreConditions satisfied")
                # Preactions
                all_pre_actions_executed = self.__ExecActions(
                    handled_event.pre_actions)
                if all_pre_actions_executed:
                    logging.debug("PreActions Executed")
                    # Transition
                    logging.debug("Transition %s ------> %s",
                                  self.current_state, handled_event.to_state)
                    self.current_state = handled_event.to_state
                    # Postactions
                    all_post_actions_executed = self.__ExecActions(
                        handled_event.post_actions)
                    if all_post_actions_executed:
                        logging.debug("PostActions Executed")
                        # Postconditions
                        all_post_conditions_satisfied = self.__CheckConditions(
                            handled_event.post_conditions)
                        if all_post_conditions_satisfied:
                            logging.debug("PostConditions Satisfied")
                        else:
                            logging.error(
                                "Not all PostConditions satisfied, restore saved state")
                            self.__RestoreState()
                    else:
                        logging.error(
                            "Not all PostActions Executed, restore saved state")
                        self.__RestoreState()
                else:
                    logging.error(
                        "Not all PretActions Executed, restore saved state")
                    self.__RestoreState()
            else:
                logging.error("Not all PreConditions satisfied")
        else:
            logging.error("Not a possible event")
