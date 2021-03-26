import sys
sys.path.append('../src')

from StateMachine import StateMachine

test = 2

def main():
    
    sm = StateMachine("../sample/sample3.xml")

    sm.LoadStateMachine()

    sm.addVariableToContext("test3", "everFalse")
    sm.addVariableToContext("test3", "test")
    sm.addVariableToContext("test3", "testPrint")
    
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

def testPrint():
    print("Test")
    
    
if __name__ == "__main__":
    main()