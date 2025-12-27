import streamlit as st
from typing import Any, Callable, Optional


class FieldType:
    STRING = "string"
    INT = "int"
    DOUBLE = "double"
    DATE = "date"
    SELECT = "select"
    BOOLEAN = "boolean"


class Field:
    def __init__(
        self,
        name: str,
        label: str,
        field_type: str,
        required: bool = True,
        default: Any = None,
        options: list[Any] | None = None,
        validator: Optional[Callable[[Any], bool]] = None,
        help_text: Optional[str] = None,
    ):
        self.name = name
        self.label = label
        self.field_type = field_type
        self.required = required
        self.default = default
        self.options = options
        self.validator = validator
        self.help_text = help_text

    def render(self, key_prefix: str) -> Any:
        key = f"{key_prefix}_{self.name}"

        if self.field_type == FieldType.STRING:
            value = st.text_input(self.label, value=self.default or "", key=key)

        elif self.field_type == FieldType.INT:
            value = st.number_input(self.label, value=self.default or 0, step=1, key=key)

        elif self.field_type == FieldType.DOUBLE:
            value = st.number_input(self.label, value=self.default or 0.0, key=key)

        elif self.field_type == FieldType.DATE:
            value = st.date_input(self.label, value=self.default, key=key)

        elif self.field_type == FieldType.SELECT:
            value = st.selectbox(self.label, self.options or [], key=key)

        elif self.field_type == FieldType.BOOLEAN:
            value = st.checkbox(self.label, value=bool(self.default), key=key)

        else:
            raise ValueError(f"Unsupported field type: {self.field_type}")

        if self.help_text:
            st.caption(self.help_text)

        return value
