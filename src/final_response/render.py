from typing import Any

from src.custom_form.response import CustomFormResponse
from src.final_response.response import FinalFormResponse

import streamlit as st

from utils.field import StreamlitField
from utils.file_input import FileInput


class FinalForm:
    custom_form_response: CustomFormResponse
    final_form_response: FinalFormResponse

    def __init__(self, custom_form_response: CustomFormResponse):
        self.custom_form_response = custom_form_response
        self.final_form_response = FinalFormResponse()

    @staticmethod
    def __render_single_form(title: str, fields: dict[Any, StreamlitField]):
        d = {}
        with st.container(border=True):
            st.subheader(title.replace("_", " ").title())
            for key, streamlit_field in fields.items():
                d[key] = streamlit_field.render()
        return d

    @staticmethod
    def __render_file_upload_form(title: str, field: FileInput):
        d = {}

        with st.container(border=True):
            st.subheader(title.replace("_", " ").title())
            context, response = field.render()
            print("context: ", context)
            print("response: ", response)
            d['context'] = context
            d['response'] = response

        return d

    def _render_personal_information(self):
        conf = self.final_form_response.personal_information_response
        title = "personal_information"

        d = self.__render_single_form(
            title,
            conf.get_streamlit_fields(title)
        )
        conf.setter(**d)

    def _render_employment_information(self):
        meta_inputs = self.custom_form_response.employment_config
        if not meta_inputs.enabled.value:
            return

        conf = self.final_form_response.employment_information_response
        conf.custom_init(
            manual_entry_count=meta_inputs.manual_count.value,
            upload_entry_count=meta_inputs.upload_count.value
        )

        index = 0
        for x in conf.manual_response:
            title = f"employment_information_{index+1}"
            d = self.__render_single_form(
                title,
                x.get_streamlit_fields(title)
            )
            x.setter(**d)
            index += 1

        for x in conf.uploaded_response:
            title = f"employment_information_{index+1}"
            d = self.__render_file_upload_form(
                title,
                x.get_streamlit_fields(title)
            )
            x.setter(**d)
            index += 1

    def _render_additional_income_information(self):
        meta_inputs = self.custom_form_response.additional_income_config

        if not meta_inputs.enabled.value:
            return

        conf = self.final_form_response.additional_income_information_response
        conf.custom_init(
            upload_entry_count=meta_inputs.income_count.value
        )
        index = 0
        for x in conf.uploaded_response:
            title = f"addition_income_{index+1}"
            d = self.__render_file_upload_form(
                title,
                x.get_streamlit_fields(title)
            )
            x.setter(**d)
            index += 1

    def _render_tuition_credits_information(self):
        meta_inputs = self.custom_form_response.tuition_config
        conf = self.final_form_response.tuition_credits_information_response
        conf.custom_init(
            mode=meta_inputs.mode.value
        )
        title = "tuition_credits_information"
        if meta_inputs.mode.value == "manual":
            d = self.__render_single_form(
                title,
                conf.manual_response.get_streamlit_fields(title)
            )
            conf.manual_response.setter(**d)

        elif meta_inputs.mode.value == "upload":
            d = self.__render_file_upload_form(
                title,
                conf.uploaded_response.get_streamlit_fields(title)
            )
            conf.uploaded_response.setter(**d)

    def _render_rental_information(self):
        meta_inputs = self.custom_form_response.rental_config
        if not meta_inputs.enabled.value:
            return
        conf = self.final_form_response.rental_information_response
        conf.custom_init(
            meta_inputs.address_count.value
        )

        index = 0
        for x in conf.manual_response:
            title = f"rental_information_{index+1}"
            d = self.__render_single_form(
                title,
                x.get_streamlit_fields(title)
            )
            x.setter(**d)
            index += 1

    def render(self):
        self._render_personal_information()
        self._render_employment_information()
        self._render_additional_income_information()
        self._render_tuition_credits_information()
        self._render_rental_information()

        if st.button("Submit"):
            self.final_form_response.is_rendered = True
            return self.final_form_response

        return None