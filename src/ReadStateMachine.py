from Condition import Condition
from Conditions import Conditions
from Actions import Actions
from Action import Action
from Event import Event
from State import State
import xml.etree.ElementTree as ET


def ReadStateMachineFile(xml_file : str):
    states = {}
    initial_state = ""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for states_child in root:
        #print(states_child.tag, states_child.attrib)
        # States Element
        if states_child.tag == "State" :
            #print("State element")
            # State Element
            state_name = ""
            events = {}
            for state_child in states_child:
                #print(state_child.tag, state_child.attrib)
                if state_child.tag == "Event":
                    #print("Event element")
                    # State->Event Element
                    event_name = ""
                    to_state = ""
                    pre_conditions = None # dummy
                    post_conditions = None # dummy
                    pre_actions = None #dummy
                    post_actions = None #dummy
                    
                    for event_child in state_child:
                                                
                        #print(event_child.tag, event_child.attrib)
                        if event_child.tag == "Name":
                            #print("Name element = ", event_child.text)
                            # State->Event->Name Element
                            event_name = event_child.text
                        elif event_child.tag == "ToState":
                            #print("ToState element = ", event_child.text)
                            # State->Event->ToState Element
                            to_state = event_child.text
                        elif event_child.tag == "PreConditions":
                            # State->Event->PreConditions Element
                            pre_condition_elements = []
                            for preconditions_child in event_child:
                                #print(preconditions_child.text)
                                # State->Event->PreConditions->Condition Element
                                if preconditions_child.tag == "Condition":
                                    expression = ""
                                    result = ""
                                    for condition_child in preconditions_child:
                                        if condition_child.tag == "Expression":
                                            expression = condition_child.text
                                        elif condition_child.tag == "Result":
                                            result = condition_child.text
                                    pre_condition_elements.append(Condition(expression,result))
                            pre_conditions = Conditions(pre_condition_elements)
                        elif event_child.tag == "PostConditions":
                            # State->Event->PostConditions Element
                            for postconditions_child in event_child:
                                #print(postconditions_child.text)
                                # State->Event->PostConditions->Condition Element
                                None
                        elif event_child.tag == "PreActions":
                            # State->Event->PreActions Element
                            pre_action_elements = []
                            for preactions_child in event_child:
                                #print(preactions_child.text)
                                # State->Event->PreActions->Action Element
                                if preactions_child.tag == "Action":
                                    expression = ""                                   
                                    for action_child in preactions_child:
                                        if action_child.tag == "Expression":
                                            expression = action_child.text
                                    pre_action_elements.append(Action(expression))
                            pre_actions = Actions(pre_action_elements)

                        elif event_child.tag == "PostActions":
                            # State->Event->PostActions Element
                            for postactions_child in event_child:
                                #print(postactions_child.text)
                                # State->Event->PostActions->Action Element
                                None
                    events[event_name] = Event(event_name,to_state,pre_conditions,post_conditions,pre_actions,post_actions)
                    #print(event.to_string())
                elif state_child.tag == "Name":
                    #print("Name element = ", state_child.text)
                    # State->Name Element
                    state_name = state_child.text
                    
            states[state_name] = State(state_name, events)
        
        elif states_child.tag == "Initial_State" :
            #print ("Initial_State element = ", states_child.text)
            # Initial_State Element
            initial_state = states_child.text    
    
    return states, initial_state