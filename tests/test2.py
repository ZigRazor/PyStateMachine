import sys
sys.path.append('../src')

from StateMachine import StateMachine

test = 2

def main():
    
    sm = StateMachine("../sample/sample2.xml")

    sm.LoadStateMachine()

    sm.addVariableToContext("test2", "everFalse")
    sm.addVariableToContext("test2", "test")
    
    print(sm.get_current_state())
    sm.InjectEvent("ToExit")
    print(sm.get_current_state())
    sm.InjectEvent("ToExit")
    print(sm.get_current_state())
    sm.InjectEvent("ToNull")
    print(sm.get_current_state())
    sm.InjectEvent("ToExit")
    print(sm.get_current_state())
    sm.InjectEvent("ToNull")

def everFalse():
    return False
    
    
if __name__ == "__main__":
    main()