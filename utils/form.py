import streamlit as st
from utils.field import Field


class Form:
    def __init__(self, form_id: str, title: str, fields: list[Field]):
        self.form_id = form_id
        self.title = title
        self.fields = fields

    def render(self):
        st.subheader(self.title)

        data = {}
        errors = {}

        for field in self.fields:
            value = field.render(self.form_id)

            if field.required and (value is None or value == ""):
                errors[field.name] = "Required field"

            if field.validator and value not in (None, ""):
                if not field.validator(value):
                    errors[field.name] = "Invalid value"

            data[field.name] = value

        return data, errors
