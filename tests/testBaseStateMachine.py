import sys
import unittest
sys.path.append('../src')

from StateMachine import StateMachine

test = 2

def everFalse():
    return False

def testPrint():
    print("Test")
    

class TestBaseStateMachine(unittest.TestCase):   
    
    def test1(self):
    
        sm = StateMachine("../sample/sample1.xml")

        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(),"Enter", "Should be Enter")
        # OK Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Not Possible Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # OK Event
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Null", "Should be Null")
        # Not Possible Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Null", "Should be Null")
        # OK Event (same state)
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Null", "Should be Null")

    
    def test2(self):

        sm = StateMachine("../sample/sample2.xml")

        sm.LoadStateMachine()

        sm.addVariableToContext("testBaseStateMachine", "everFalse")
        sm.addVariableToContext("testBaseStateMachine", "test")
    
        self.assertEqual(sm.get_current_state(),"Enter", "Should be Enter")
        # Precondition Verified
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")

    def test3(self):
        sm = StateMachine("../sample/sample3.xml")

        sm.LoadStateMachine()

        sm.addVariableToContext("testBaseStateMachine", "everFalse")
        sm.addVariableToContext("testBaseStateMachine", "test")
        sm.addVariableToContext("testBaseStateMachine", "testPrint")
    
        self.assertEqual(sm.get_current_state(),"Enter", "Should be Enter")
        # Precondition Verified / Execute PreAction
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(),"Exit", "Should be Exit")

    
    
if __name__ == '__main__':
    unittest.main()