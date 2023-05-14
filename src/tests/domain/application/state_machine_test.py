from ....domain.application.state_machine import StateMachine, Trigger
import pytest

# Tests that the class initializes correctly with valid states, triggers, and initial state. 
def test_initialization_with_valid_input():
    states = ['A', 'B', 'C']
    triggers = [Trigger('t1', 'A', 'B'), Trigger('t2', 'B', 'C')]
    initial_state = 'A'
    sm = StateMachine(states, triggers, initial_state)
    assert sm.state == initial_state

# Tests that the class raises an exception when evolved with a trigger that has an invalid from_state or to_state. 
def test_evolve_with_invalid_from_or_to_state():
    states = ['A', 'B', 'C']
    triggers = [Trigger('t1', 'A', 'D'), Trigger('t2', 'D', 'C')]
    initial_state = 'A'
    with pytest.raises(Exception):
        StateMachine(states, triggers, initial_state)

# Tests that the class raises an exception when initialized with an empty list of states or triggers. 
def test_initialization_with_empty_list_of_states_or_triggers():
    states = []
    triggers = []
    initial_state = 'A'
    with pytest.raises(Exception):
        StateMachine(states, triggers, initial_state)

# Tests that the class raises an exception when initialized with a non-existent initial state. 
def test_initialization_with_nonexistent_initial_state():
    states = ['A', 'B', 'C']
    triggers = [Trigger('t1', 'A', 'B'), Trigger('t2', 'B', 'C')]
    initial_state = 'D'
    with pytest.raises(Exception):
        StateMachine(states, triggers, initial_state)

# Tests that the class does not change state when evolved with an invalid trigger name. 
def test_evolve_with_invalid_trigger_name():
    states = ['A', 'B', 'C']
    triggers = [Trigger('t1', 'A', 'B'), Trigger('t2', 'B', 'C')]
    initial_state = 'A'
    sm = StateMachine(states, triggers, initial_state)
    sm.evolve('t3')
    assert sm.state == initial_state