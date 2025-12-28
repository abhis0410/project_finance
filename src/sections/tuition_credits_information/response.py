from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.field_value import StringField, IntField, DoubleField
from src.sections.response_template import ManualEntryResponse, UploadedEntryResponse
from utils.streamlit_field import StreamlitField, StreamlitFieldType
from utils.file_input import FileInput


class TuitionCreditsManualEntryResponse(ManualEntryResponse):
    institution_name: StringField
    institution_address: StringField
    months_full_time: IntField
    months_part_time: IntField
    tuition_fees_paid: DoubleField

    def __init__(self):
        super().__init__()
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


class TuitionCreditsUploadedEntryResponse(UploadedEntryResponse):
    context: str | None
    response: UploadedFile | None

    def __init__(self):
        super().__init__()
        self.context = None
        self.response = None


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
    manual_response: TuitionCreditsManualEntryResponse | None
    uploaded_response: TuitionCreditsUploadedEntryResponse | None

    def custom_init(self, mode: str):
        self.manual_response = None
        self.uploaded_response = None

        if mode == "manual":
            self.manual_response = TuitionCreditsManualEntryResponse()
        elif mode == "upload":
            self.uploaded_response = TuitionCreditsUploadedEntryResponse()

    def get_all(self) -> dict:
        if self.manual_response:
            return self.manual_response.get_all()

        if self.uploaded_response:
            return self.uploaded_response.get_all()

        return {}