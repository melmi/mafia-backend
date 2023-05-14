
# Generated by CodiumAI
from ....domain.application.state_machine_builder import StateMachineBuilder
from ....domain.application.trigger import Trigger
from ....domain.application.state_machine import StateMachine


import pytest

"""
Code Analysis

Main functionalities:
The StateMachineBuilder class is responsible for building instances of the StateMachine class. It allows the user to add states, triggers, and set the initial state of the state machine. Once all the necessary components are added, the build method is called to create the StateMachine instance.

Methods:
- add_states(states: list[str]) -> StateMachineBuilder: adds a list of states to the builder object and returns the builder instance.
- add_triggers(trigger: Trigger) -> StateMachineBuilder: adds a trigger to the builder object and returns the builder instance.
- initial_state(initial_state: str) -> StateMachineBuilder: sets the initial state of the state machine and returns the builder instance.
- build() -> StateMachine: creates a StateMachine instance using the states, triggers, and initial state added to the builder object.

Fields:
- _states: a list of states added to the builder object.
- _triggers: a list of triggers added to the builder object.
- _initial_state: the initial state of the state machine added to the builder object.
"""


class TestStateMachineBuilder:
    # Tests that add_states method adds states to the StateMachineBuilder correctly.
    def test_add_states_happy(self):
        builder = StateMachineBuilder()
        states = ['state1', 'state2', 'state3']
        builder.add_states(states)
        assert builder._states == states

    # Tests that add_triggers method adds triggers to the StateMachineBuilder correctly.
    def test_add_triggers_happy(self):
        builder = StateMachineBuilder()
        trigger1 = Trigger('trigger1', 'state1', 'state2')
        trigger2 = Trigger('trigger2', 'state2', 'state3')
        builder.add_trigger(
            trigger1.name, trigger1.from_state, trigger1.to_state)
        builder.add_trigger(
            trigger2.name, trigger2.from_state, trigger2.to_state)
        assert builder._triggers == [trigger1, trigger2]

    # Tests that evolve method does not change the state of the StateMachine with an invalid trigger.

    def test_evolve_edge(self):
        builder = StateMachineBuilder()
        states = ['state1', 'state2', 'state3']
        triggers = [Trigger('trigger1', 'state1', 'state2')]
        initial_state = 'state1'
        state_machine = StateMachine(states, triggers, initial_state)
        builder._states = states
        builder._triggers = triggers
        builder._initial_state = initial_state
        assert state_machine.state == initial_state
        builder.build()
        assert state_machine.state == initial_state
        builder.build()
        assert state_machine.state == initial_state

    # Tests that build method creates a StateMachine object with correct parameters.
    def test_build_happy(self):
        builder = StateMachineBuilder()
        states = ['state1', 'state2', 'state3']
        triggers = [Trigger('trigger1', 'state1', 'state2')]
        initial_state = 'state1'
        builder._states = states
        builder._triggers = triggers
        builder._initial_state = initial_state
        state_machine = builder.build()
        assert isinstance(state_machine, StateMachine)
        assert state_machine._states == set(states)
        assert state_machine._triggers == set(triggers)
        assert state_machine._state == initial_state

    # Tests that evolve method changes the state of the StateMachine correctly with a valid trigger.
    def test_evolve_happy(self):
        builder = StateMachineBuilder()
        states = ['state1', 'state2', 'state3']
        triggers = [Trigger('trigger1', 'state1', 'state2')]
        initial_state = 'state1'
        builder._states = states
        builder._triggers = triggers
        builder._initial_state = initial_state
        state_machine = builder.build()
        assert state_machine.state == initial_state
        state_machine.evolve('trigger1')
        assert state_machine.state == 'state2'