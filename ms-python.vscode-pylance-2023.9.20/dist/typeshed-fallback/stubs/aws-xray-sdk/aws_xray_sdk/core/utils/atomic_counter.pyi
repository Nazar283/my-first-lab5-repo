from typing import Any

class AtomicCounter:
    value: Any
    def __init__(self, initial: int = 0) -> None: ...
    def increment(self, num: int = 1): ...
    def decrement(self, num: int = 1): ...
    def get_current(self): ...
    def reset(self): ...