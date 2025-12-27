from components.employer_information import EmployerInformation
from components.personal_information import personal_information_form
from typing import Optional

class FinalResponse:

    def __init__(
            self,
            manual_entry_count: int,
            file_upload_count: int
    ):
        self.manual_entry_count = manual_entry_count
        self.file_upload_count = file_upload_count

        self.all_fields = []


    def _add_personal_information(self):
        fields = personal_information_form("personal_info")

        self.all_fields.append(*fields)

    def _add_employer_information(self):
        fields = EmployerInformation(
            self.manual_entry_count,
            self.file_upload_count
        ).get_all_fields()

        self.all_fields.append(*fields)

    def clear(self):
        self.all_fields = []


    def render_form(self):
        self._add_personal_information()
        self._add_employer_information()

        for field in self.all_fields:
            field.render()
