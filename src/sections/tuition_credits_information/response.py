from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.field_value import StringField, IntField, DoubleField
from utils.constants import Strings
from utils.field import StreamlitField, StreamlitFieldType
from utils.file_input import FileInput


class TuitionCreditsManualEntryResponse:
    institution_name: StringField
    institution_address: StringField
    months_full_time: IntField
    months_part_time: IntField
    tuition_fees_paid: DoubleField

    def __init__(self):
        self.institution_name = StringField(
            title="Name of Educational institution",
            required=True,
        )
        self.institution_address = StringField(title="Institution address",required=True)
        self.months_full_time = IntField(
            title="Months studied full-time",
            required=True,
            min_value=0,
            max_value=100
        )
        self.months_part_time = IntField(
            title="Months studied part-time",
            required=True,
            min_value=0,
            max_value=100
        )
        self.tuition_fees_paid = DoubleField(
            title="Tuition fees paid ($)",
            required=True,
        )

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

    def get_streamlit_fields(self, key_prefix: str) -> dict[str, StreamlitField]:
        fields = {
            "institution_name": StreamlitField(
                "institution_name",
                self.institution_name.title,
                StreamlitFieldType.STRING,
                key_prefix,
            ),
            "institution_address": StreamlitField(
                "institution_address",
                self.institution_address.title,
                StreamlitFieldType.STRING,
                key_prefix,
            ),
            "months_full_time": StreamlitField(
                "months_full_time",
                self.months_full_time.title,
                StreamlitFieldType.INT,
                key_prefix,
            ),
            "months_part_time": StreamlitField(
                "months_part_time",
                self.months_part_time.title,
                StreamlitFieldType.INT,
                key_prefix,
            ),
            "tuition_fees_paid": StreamlitField(
                "tuition_fees_paid",
                self.tuition_fees_paid.title,
                StreamlitFieldType.DOUBLE,
                key_prefix,
            ),
        }
        return fields


class TuitionCreditsUploadedEntryResponse:
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
            name="tuition_form_upload",
            label="Upload TT2202 from college",
            context_help_string="Enter your institution name/context here",
            key_prefix=key_prefix,
            allowed_types=["pdf"],
            required=True,
            help_text="Please upload a PDF copy of your TT2202 from college",
            multiple=False,
        )

        return fields


class TuitionCreditsInformationResponse:
    response_manual: TuitionCreditsManualEntryResponse
    response_uploaded: TuitionCreditsUploadedEntryResponse

    def custom_init(self, mode: str):
        if mode == "manual":
            self.response_manual = TuitionCreditsManualEntryResponse()
        elif mode == "upload":
            self.response_uploaded = TuitionCreditsUploadedEntryResponse()