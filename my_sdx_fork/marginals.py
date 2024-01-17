from .common import ColumnType, Value
from .tree import Node
from .forest import Forest

class Marginal:
    def __init__(self, root: Node) -> None:
        pass

class Marginals:
    # All one-dimensional trees must be already built
    def __init__(self, forest: Forest) -> None:
        self.safe_values = set()

    def add_safe_value(self, value: float) -> None:
        if self.column_type == ColumnType.STRING:
            self.safe_values.add(value)

    def is_value_safe(self, value: float) -> bool:
        return value in self.safe_values
