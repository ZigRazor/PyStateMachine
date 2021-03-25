import sys
sys.path.append('../src')

from StateMachine import StateMachine

def main():
    
    sm = StateMachine("../sample/sample1.xml")

    sm.LoadStateMachine()
    
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
    
    
if __name__ == "__main__":
    main()