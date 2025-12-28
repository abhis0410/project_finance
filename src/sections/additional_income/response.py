from typing import List

from streamlit.runtime.uploaded_file_manager import UploadedFile

from utils.file_input import FileInput


class AdditionalIncomeUploadedResponse:
    context: str
    response: UploadedFile

    def __init__(self):
        pass

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

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