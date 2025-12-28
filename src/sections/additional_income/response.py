from typing import List

from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.sections.response_template import UploadedEntryResponse
from utils.file_input import FileInput


class AdditionalIncomeUploadedResponse(UploadedEntryResponse):
    context: str | None
    response: UploadedFile | None

    def __init__(self):
        super().__init__()
        self.context = None
        self.response = None


    @staticmethod
    def get_streamlit_fields(key_prefix: str) -> FileInput:
        fields = FileInput(
            name="additional_income_upload",
            label="Upload Additional Income Document",
            context_help_string="Write Context about the additional income here.",
            key_prefix=key_prefix,
            allowed_types=["pdf"],
            required=True,
            help_text="Please upload a PDF copy.",
            multiple=False,
        )

        return fields


class AdditionalIncomeResponse:
    uploaded_response: List[AdditionalIncomeUploadedResponse]  # Streamlit UploadedFile

    def custom_init(self, upload_entry_count: int):
        self.uploaded_response = [AdditionalIncomeUploadedResponse() for _ in range(upload_entry_count)]