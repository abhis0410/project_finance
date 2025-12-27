from components.employer_information import EmployerInformation
from components.personal_information import personal_information_form
import streamlit as st
from typing import Dict, Optional

class FinalResponse:

    def __init__(
            self,
            manual_entry_count: int,
            file_upload_count: int
    ):
        self.manual_entry_count = manual_entry_count
        self.file_upload_count = file_upload_count

        self.personal_form = None
        self.employer_form: Optional[Dict] = None


    def _populate_personal_information(self):
        form = personal_information_form("personal_info")

        self.personal_form = form

    def _populate_employer_information(self):
        form = EmployerInformation(
            self.manual_entry_count,
            self.file_upload_count
        ).get_all_fields()

        self.employer_form = form


    def render_form(self):
        # Personal Information
        self._populate_personal_information()

        with st.container(border=True):
            st.title("Personal Information")
            for field in self.personal_form:
                field.render()

        # Main Employer Information
        self._populate_employer_information()
        for title, form in self.employer_form.items():
            with st.container(border=True):
                st.title(title.replace("_", " ").title())
                for field in form:
                    field.render()




    def clear(self):
        self.personal_form = None
        self.employer_form = None