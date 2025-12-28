from sqlite3 import adapt

from src.custom_form.response import CustomFormResponse

import streamlit as st


class CustomForm:
    def __init__(self, title: str):
        self.title = title
        self.config: CustomFormResponse = CustomFormResponse()


    def _render_personal_information_section(self):
        conf = self.config.personal_information_config
        conf.setter(enabled=True)

    def _render_employment_section(self):
        conf = self.config.employment_config

        st.subheader(conf.title)

        employment_enabled = st.checkbox(conf.enabled.title)
        manual_count = 0
        upload_count = 0

        if employment_enabled:
            manual_count = st.number_input(
                conf.manual_count.title,
                min_value=conf.manual_count.min_value,
                max_value=conf.manual_count.max_value,
                step=1,
                key="manual_count",
            )

            upload_count = st.number_input(
                conf.upload_count.title,
                min_value=conf.upload_count.min_value,
                max_value=conf.upload_count.max_value,
                step=1,
                key="upload_count",
            )

        conf.setter(
            enabled=employment_enabled,
            manual_count=manual_count,
            upload_count=upload_count,
        )
        self.config.employment_config = conf

    def _render_additional_income_section(self):
        conf = self.config.additional_income_config

        st.subheader(conf.title)
        st.info(conf.disclaimer)

        enabled = st.checkbox(
            conf.enabled.title
        )

        income_count = None
        if enabled:
            income_count = st.number_input(
                conf.income_count.title,
                min_value=conf.income_count.min_value,
                max_value=conf.income_count.max_value,
                step=1,
                key="income_count",
            )

        conf.setter(enabled=enabled, income_count=income_count)

    def _render_tuition_section(self):
        conf = self.config.tuition_config
        st.subheader(conf.title)

        enabled = st.checkbox(conf.enabled.title)

        mode = None
        if enabled:
            selected = st.radio(
                conf.mode.title,
                options=[
                    ("Manual Entry", "manual"),
                    ("Upload T2202", "upload"),
                ],
                format_func=lambda x: x[0],
                horizontal=True,
            )
            mode = selected[1]
            conf.mode.set_value(selected[1])

        conf.setter(
            enabled=enabled,
            mode=mode
        )

    def _render_rent_info_section(self):
        conf = self.config.rental_config
        st.subheader(conf.title)
        st.info(conf.disclaimer)

        enabled = st.checkbox(
            conf.enabled.title
        )

        address_count = None
        if enabled:
            address_count = st.number_input(
                conf.address_count.title,
                min_value=conf.address_count.min_value,
                max_value=conf.address_count.max_value,
                step=1,
                key="address_count",
            )

        conf.setter(enabled=enabled, address_count=address_count)

    def render(self) -> CustomFormResponse | None:
        st.header(self.title)

        self._render_personal_information_section()

        with st.container(border=True):
            self._render_employment_section()

        with st.container(border=True):
            self._render_additional_income_section()

        with st.container(border=True):
            self._render_tuition_section()

        with st.container(border=True):
            self._render_rent_info_section()

        if st.button("Continue"):
            return self.config

        return None