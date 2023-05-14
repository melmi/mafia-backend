from typing import Iterable

from ...domain.application.trigger import Trigger



class StateMachine:
    def __init__(self, states: list[str], triggers: list[Trigger], initial_state: str):
        self._states: set[str] = set(states)

        for trigger in triggers:
            if trigger.from_state not in self._states:
                raise Exception(
                    f'trigger {trigger.name} from_state {trigger.from_state} was not in states')
            if trigger.to_state not in self._states:
                raise Exception(
                    f'trigger {trigger.name} to_state {trigger.to_state} was not in states')
        self._triggers: set[Trigger] = set(triggers)
        for trigger in self._triggers:
            same_triggers_count = len(list(self._get_matching_triggers(
                trigger.from_state, trigger.name)))
            if same_triggers_count > 1:
                raise Exception(
                    f'there are more than one of trigger {trigger} with the same from_state {trigger.from_state}')

        if initial_state not in self._states:
            raise Exception(
                f'initial_state({initial_state}) did not exist in states!')
        self._state: str = initial_state

    @property
    def state(self) -> str:
        return self._state

    def _get_matching_triggers(self, state: str, trigger_name: str) -> Iterable[Trigger]:
        return (t for t in self._triggers if t.name == trigger_name and t.from_state == state)

    def evolve(self, trigger_name: str):
        matching_triggers = list(
            self._get_matching_triggers(self._state, trigger_name))
        if not matching_triggers:
            return
        trigger = matching_triggers[0]
        self._state = trigger.to_state
