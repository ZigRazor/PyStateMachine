from StateMachine import StateMachine
import sys
import unittest
sys.path.append('../src')

test = 2


def everFalse():
    return False


def everTrue():
    return True


def testPrint():
    print("Test")


def setTestTo3():
    global test    # Needed to modify global copy of globvar
    print(test)
    test = 3
    print(test)


def printTest():
    print("Test: ", test)


class TestBaseStateMachine(unittest.TestCase):
"""Test state machine using various samples"""

    def test1(self):

        sm = StateMachine("../sample/sample1.xml")

        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # OK Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Possible Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # OK Event
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # Not Possible Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # OK Event (same state)
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")

    def test2(self):

        sm = StateMachine("../sample/sample2.xml")

        sm.LoadStateMachine()

        sm.addModuleToContext("testBaseStateMachine")

        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # Precondition Verified
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

    def test3(self):
        sm = StateMachine("../sample/sample3.xml")

        sm.LoadStateMachine()

        sm.addModuleToContext("testBaseStateMachine")

        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # Precondition Verified / Execute PreAction
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Precondition Not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

    def test4(self):
        sm = StateMachine("../sample/sample4.xml")

        sm.LoadStateMachine()

        sm.addModuleToContext("testBaseStateMachine")

        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # Precondition Verified / Execute PreAction
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

        # Precondition Verified /Execute Post Action
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # Precondition Verified /Execute Post Action
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")

    def test5(self):
        sm = StateMachine("../sample/sample5.xml")

        sm.LoadStateMachine()

        sm.addModuleToContext("testBaseStateMachine")

        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # Precondition Verified / Execute PreAction
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

        # Precondition Verified /Execute Post Action /Post Conditions Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")
        # Precondition Verified /Execute Post Action
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Null", "Should be Null")

    def test6(self):
        global test
        test = 2
        sm = StateMachine("../sample/sample6.xml")

        sm.LoadStateMachine()

        sm.addModuleToContext("testBaseStateMachine")

        self.assertEqual(sm.get_current_state(), "Enter", "Should be Enter")
        # Precondition Verified / Execute PreAction
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")

        # Precondition Verified /Execute Post Action /Post Conditions not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Not Valid Event
        sm.InjectEvent("ToExit")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")
        # Precondition Verified /Execute Post Action /Post Conditions not Verified
        sm.InjectEvent("ToNull")
        self.assertEqual(sm.get_current_state(), "Exit", "Should be Exit")


if __name__ == '__main__':
    unittest.main()
