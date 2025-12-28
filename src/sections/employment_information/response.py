from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.field_value import StringField, DoubleField
from utils.constants import Strings
from utils.streamlit_field import StreamlitField, StreamlitFieldType
from typing import List, Any

from utils.file_input import FileInput


class EmployerManualEntryResponse:
    employer_name: StringField
    employer_address: StringField
    employment_income: DoubleField
    cpp_contribution: DoubleField
    ei_contribution: DoubleField
    column_18_amount: DoubleField
    column_26_amount: DoubleField


    def __init__(self):
        self.employer_name: StringField = StringField(
            title="Name of Employer",
            required=True,
        )

        self.employer_address: StringField = StringField(
            title="Address of Employer",
            required=True,
        )

        self.employment_income: DoubleField = DoubleField(
            title="Employment Income (Amount in Column 14)",
            required=True,
        )

        self.cpp_contribution: DoubleField = DoubleField(
            title="CPP (Amount in Column 16)",
            required=False,
        )

        self.ei_contribution: DoubleField = DoubleField(
            title="EI (Amount in Column 24)",
            required=False,
        )

        self.column_18_amount: DoubleField = DoubleField(
            title="Amount in Column 18",
            required=False,
        )

        self.column_26_amount: DoubleField = DoubleField(
            title="Amount in Column 26",
            required=False,
        )

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

    def get_streamlit_fields(self, key_prefix: str) -> dict[Any, Any]:
        fields = {
            "employer_name": StreamlitField("employer_name", self.employer_name.title, StreamlitFieldType.STRING, key_prefix),
            "employer_address": StreamlitField("employer_address", self.employer_address.title, StreamlitFieldType.STRING, key_prefix),
            "employment_income": StreamlitField("employment_income", self.employment_income.title, StreamlitFieldType.DOUBLE, key_prefix),
            "cpp_contribution": StreamlitField("cpp_contribution", self.cpp_contribution.title, StreamlitFieldType.DOUBLE, key_prefix),
            "ei_contribution": StreamlitField("ei_contribution", self.ei_contribution.title, StreamlitFieldType.DOUBLE, key_prefix),
            "column_18_amount": StreamlitField("column_18_amount", self.column_18_amount.title, StreamlitFieldType.DOUBLE, key_prefix),
            "column_26_amount": StreamlitField("column_26_amount", self.column_26_amount.title, StreamlitFieldType.DOUBLE, key_prefix),
        }
        return fields


class EmployerUploadedEntryResponse:
    context: str | None
    response: UploadedFile | None

    def __init__(self):
        self.context = None
        self.response = None

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                continue

    @staticmethod
    def get_streamlit_fields(key_prefix: str) -> FileInput:
        fields = FileInput(
            name="employer_file_upload",
            label="Upload T4 Slip for Employer",
            context_help_string=Strings.EmployerFileUploadContext,
            key_prefix=key_prefix,
            allowed_types=["pdf"],
            required=True,
            help_text="Please upload a PDF copy of your T4 slip.",
            multiple=False,
        )

        return fields


class EmploymentResponse:
    manual_response: List[EmployerManualEntryResponse]
    uploaded_response: List[EmployerUploadedEntryResponse]  # Streamlit UploadedFile

    def custom_init(self, manual_entry_count: int, upload_entry_count: int):
        self.manual_response = [EmployerManualEntryResponse() for _ in range(manual_entry_count)]
        self.uploaded_response = [EmployerUploadedEntryResponse() for _ in range(upload_entry_count)]