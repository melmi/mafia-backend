from __future__ import annotations
from ...domain.application.state_machine import StateMachine
from ...domain.application.trigger import Trigger


class StateMachineBuilder:
    def __init__(self) -> None:
        self._states = []
        self._triggers = []
        self._initial_state = None

    def add_states(self, states: list[str]) -> StateMachineBuilder:
        self._states.extend(states)
        return self

    def add_trigger(self, name: str, from_state: str, to_state: str) -> StateMachineBuilder:
        trigger = Trigger(name, from_state, to_state)
        self._triggers.append(trigger)
        return self

    def initial_state(self, initial_state: str) -> StateMachineBuilder:
        self._initial_state = initial_state
        return self

    def build(self) -> StateMachine:
        return StateMachine(self._states, self._triggers, self._initial_state)
