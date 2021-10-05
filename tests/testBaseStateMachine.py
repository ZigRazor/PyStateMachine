from StateMachine import StateMachine
import sys
import unittest
sys.path.append('../src')

test = 2


def everFalse():
    """Return false"""

    return False


def everTrue():
    """Return false"""

    return True


def testPrint():
    """Return Test"""

    print("Test")


def setTestTo3():
    """Sets Test to 3"""

    global test    # Needed to modify global copy of globvar
    print(test)
    test = 3
    print(test)


def printTest():
    """Print Test"""

    print("Test: ", test)


class TestBaseStateMachine(unittest.TestCase):
    """Test state machine using various samples"""

    def test1(self):
        """Test Statemachine"""
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
        """Second Test for Statemachine"""

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
        """Test 3 for State Machine"""

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
        """Test 4 for state machine"""

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
        """Test 5 for state machine"""

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
        """Test 6 for state machine"""

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
