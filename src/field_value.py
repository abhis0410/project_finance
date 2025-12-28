from typing import Generic, TypeVar, Optional, Iterable

T = TypeVar("T")

class FieldValue(Generic[T]):
    title: str
    value: Optional[T] = None
    required: bool = False

    def __init__(self, title: str, required: bool = False):
        self.title = title
        self.required = required
        self.value = None

    def set_value(self, value):
        self.value = value


# Specialized field types

class BoolField(FieldValue[bool]):
    def __init__(self, title: str, required: bool):
        super().__init__(title, required)


class StringField(FieldValue[str]):
    def __init__(self, title: str, required: bool):
        super().__init__(title, required)


class IntField(FieldValue[int]):
    min_value: int | None = None
    max_value: int | None = None

    def __init__(self, title: str, required: bool, min_value: int | None = None, max_value: int | None = None):
        super().__init__(title, required)
        self.min_value = min_value
        self.max_value = max_value


class DoubleField(FieldValue[float]):
    min_value: float | None = None
    max_value: float | None = None

    def __init__(self, title: str, required: bool, min_value: int | None = None, max_value: int | None = None):
        super().__init__(title, required)
        self.min_value = min_value
        self.max_value = max_value


class ListField(FieldValue[list[T]]):
    max_length: int | None = None

    def __init__(self, title: str, required: bool, max_length: int | None = None):
        super().__init__(title, required)
        self.max_length = max_length


class OptionField(FieldValue[T]):
    options: Iterable[T]

    def __init__(
        self,
        title: str,
        options: Iterable[T],
        required: bool = False,
    ):
        super().__init__(title, required)
        self.options = list(options)

        if not self.options:
            raise ValueError("OptionField must have at least one option")

    def set_value(self, value: T):
        if value is not None and value not in self.options:
            raise ValueError(
                f"Invalid value '{value}' for {self.title}. "
                f"Allowed values: {self.options}"
            )
        self.value = value