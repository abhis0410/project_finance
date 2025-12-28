# import streamlit as st
# from dataclasses import dataclass
#
#
# @dataclass
# class EmploymentConfig:
#     enabled: bool
#     manual_count: int = 0
#     upload_count: int = 0
#
#
# @dataclass
# class TuitionConfig:
#     enabled: bool
#     mode: str | None = None  # manual | upload
#
#
# @dataclass
# class CustomFormConfig:
#     personal_information: bool
#     employment: EmploymentConfig
#     additional_income: bool
#     tuition: TuitionConfig
#     rent_information: bool
#     hst_message: bool
#
#
# class CustomForm:
#     def __init__(self, title: str):
#         self.title = title
#         self.config: CustomFormConfig | None = None
#
#     @staticmethod
#     def _section(title:str, fn):
#         with st.container(border=True):
#             st.subheader(title)
#             return fn()
#
#     @staticmethod
#     def _render_personal_information_section():
#         return True  # Always enabled
#
#     @staticmethod
#     def _render_employment_section():
#         employment_enabled = st.checkbox("I have employment income")
#
#         manual_count = 0
#         upload_count = 0
#
#         if employment_enabled:
#             manual_count = st.number_input(
#                 "Number of Employers for Manual Filling- T4 form",
#                 min_value=0,
#                 max_value=10,
#                 step=1,
#                 key="manual_count",
#             )
#
#             upload_count = st.number_input(
#                 "Number of Employers for Manual Filling- T4 form",
#                 min_value=0,
#                 max_value=10,
#                 step=1,
#                 key="upload_count",
#             )
#
#             if manual_count + upload_count > 10:
#                 st.error("Total employers cannot exceed 10")
#
#         return EmploymentConfig(
#             enabled=employment_enabled,
#             manual_count=manual_count,
#             upload_count=upload_count,
#         )
#
#     @staticmethod
#     def _render_additional_income_section():
#         additional_income = st.checkbox("I have additional income to report")
#         return additional_income
#
#     @staticmethod
#     def _render_tuition_section():
#         tuition_enabled = st.checkbox("I want to claim tuition credits")
#
#         tuition_mode = None
#         if tuition_enabled:
#             tuition_mode = st.radio(
#                 "How will you provide tuition details?",
#                 ["Manual Entry", "Upload T2202"],
#                 horizontal=True,
#             )
#             tuition_mode = "manual" if tuition_mode == "Manual Entry" else "upload"
#
#         return TuitionConfig(
#             enabled=tuition_enabled,
#             mode=tuition_mode,
#         )
#
#     @staticmethod
#     def _render_rent_info_section():
#         rent_information = st.checkbox(
#             "I paid rent during Jan–Dec 2025 (non-cash)"
#         )
#         return rent_information
#
#     @staticmethod
#     def _render_hst_section():
#         hst_message = st.checkbox(
#             "I want to leave a message for HST filing (separate charges)"
#         )
#         return hst_message
#
#     def render(self) -> CustomFormConfig | None:
#         st.header(self.title)
#
#         personal_information = self._render_personal_information_section()
#
#         employment_config = self._section(
#             "Employment Information",
#             self._render_employment_section,
#         )
#
#         additional_income = self._section(
#             "Additional Income",
#             self._render_additional_income_section,
#         )
#
#         tuition_config = self._section(
#             "Tuition Credits (T2202)",
#             self._render_tuition_section,
#         )
#
#         rent_information = self._section(
#             "Rent Tenant Information",
#             self._render_rent_info_section,
#         )
#
#         hst_message = self._section(
#             "HST Filing",
#             self._render_hst_section,
#         )
#
#         if st.button("Continue"):
#             self.config = CustomFormConfig(
#                 personal_information=personal_information,
#                 employment=employment_config,
#                 additional_income=additional_income,
#                 tuition=tuition_config,
#                 rent_information=rent_information,
#                 hst_message=hst_message,
#             )
#             return self.config
#
#         return None
#
