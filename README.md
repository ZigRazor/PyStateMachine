# PyStateMachine
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>  Python State Machine 

[![CodeFactor](https://www.codefactor.io/repository/github/zigrazor/pystatemachine/badge)](https://www.codefactor.io/repository/github/zigrazor/pystatemachine)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/17ca07f67ba44089bf28af37ba368e1b)](https://www.codacy.com/gh/ZigRazor/PyStateMachine/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ZigRazor/PyStateMachine&amp;utm_campaign=Badge_Grade)

[![DeepSource](https://deepsource.io/gh/ZigRazor/PyStateMachine.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/ZigRazor/PyStateMachine/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/ZigRazor/PyStateMachine.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/ZigRazor/PyStateMachine/?ref=repository-badge)

## Introduction
**PyStateMachine** is a Framework that support state machines in **Python**

## Requirements
- Python3

### How to Run

How do we import the framework?

1. Insure that Python3 is installed:
   - https://www.python.org/downloads/

2. Install the PyStateMachines framework
   - pip3 install PyStateMachines

## Example
After framework is installed, import and create a small example.
Create xml file from sample with the State machine states.

myStateMachine.xml

```
<?xml version="1.0"?>
<x:States xmlns:x="pystatemachine:sm">
    <State>
        <Name>State1</Name>
        <Event>
            <Name>ToState2</Name>
            <ToState>State2</ToState>
        </Event>
    </State>
    <State>
        <Name>State2</Name>
        <Event>
            <Name>ToState3</Name>
            <ToState>State3</ToState>
        </Event>
    </State>
    <State>
        <Name>State3</Name>
        <Event>
            <Name>ToState1</Name>
            <ToState>State1</ToState>
        </Event>
    </State>
    <Initial_State>State1</Initial_State>
</x:States>
```

Create Python Script to run state machine
pyStateMachine.py
```
# importing necessary packages
from StateMachine import StateMachine

"""Test StateMachine"""
sm = StateMachine("myStateMachine.xml")
sm.LoadStateMachine()

# print initial state
print(sm.get_current_state())  # current_state == State1

sm.InjectEvent("ToState2")
print(sm.get_current_state())  # current_state == State2

sm.InjectEvent("ToState3")
print(sm.get_current_state())  # current_state == State3

sm.InjectEvent("ToState1")
print(sm.get_current_state())  # current_state == State1

```
run Python script to execute state machine
```
python pyStateMachine.py
```
pyStateMachineUnitTest.py
```
## Test Suite
#  importing necessary packages
from StateMachine import StateMachine
import unittest


class TestBaseStateMachine(unittest.TestCase):
    """Test state machine using various samples"""

# test all valid state transitions
    def test1(self):
        """Test Statemachine"""
        sm = StateMachine("myStateMachine.xml")
        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")
        # OK Event
        sm.InjectEvent("ToState2")
        self.assertEqual(sm.get_current_state(), "State2", "Should be State2")
        # OK Event
        sm.InjectEvent("ToState3")
        self.assertEqual(sm.get_current_state(), "State3", "Should be State3")
        # OK Event
        sm.InjectEvent("ToState1")
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")

# test invalid State1 transitions
    def test2(self):
        """Test Statemachine"""
        sm = StateMachine("myStateMachine.xml")
        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")
        # Invalid transition
        sm.InjectEvent("ToState3")
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")

# test invalid State2 transitions
    def test3(self):
        """Test Statemachine"""
        sm = StateMachine("myStateMachine.xml")
        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")
        # OK Event
        sm.InjectEvent("ToState2")
        self.assertEqual(sm.get_current_state(), "State2", "Should be State2")
        # Invalid transition
        sm.InjectEvent("ToState1")
        self.assertEqual(sm.get_current_state(), "State2", "Should be State2")

# test invalid State3 transitions
    def test4(self):
        """Test Statemachine"""
        sm = StateMachine("myStateMachine.xml")
        sm.LoadStateMachine()
        self.assertEqual(sm.get_current_state(), "State1", "Should be State1")
        # OK Event
        sm.InjectEvent("ToState2")
        self.assertEqual(sm.get_current_state(), "State2", "Should be State2")
        # OK Event
        sm.InjectEvent("ToState3")
        self.assertEqual(sm.get_current_state(), "State3", "Should be State3")
        # Invalid transition
        sm.InjectEvent("ToState2")
        self.assertEqual(sm.get_current_state(), "State3", "Should be State3")
        
if __name__ == '__main__':
    unittest.main()
```
run unit tests
```
python pyStateMachineUnitTest.py
```


## How to contribute [![GitHub contributors](https://img.shields.io/github/contributors/ZigRazor/PyStateMachine.svg)](https://GitHub.com/ZigRazor/PyStateMachine/graphs/contributors/)
Read the [CONTRIBUTING GUIDE](https://github.com/ZigRazor/PyStateMachine/blob/main/CONTRIBUTING.md)

## Hacktoberfest

We are pleased to inform you that this repository is participating in the **#Hacktoberfest**!

Happy Coding!

## Contact
E-Mail : zigrazor@gmail.com

[GitHub Profile](https://github.com/ZigRazor) ![Profile views](https://gpvc.arturio.dev/ZigRazor)

![ZigRazor's github stats](https://github-readme-stats.vercel.app/api?username=ZigRazor&show_icons=true&theme=tokyonight)

## Support
To support me just add ***Star*** the project  [![GitHub stars](https://img.shields.io/github/stars/ZigRazor/PyStateMachine.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/ZigRazor/PyStateMachine/stargazers/) or ***follow me***  [![GitHub followers](https://img.shields.io/github/followers/ZigRazor.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/ZigRazor?tab=followers)

To get updated ***watch*** the project  [![GitHub watchers](https://img.shields.io/github/watchers/ZigRazor/PyStateMachine.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/ZigRazor/PyStateMachine/watchers/)

## Project Info

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=ZigRazor&repo=PyStateMachine)](https://github.com/ZigRazor/PyStateMachine)


