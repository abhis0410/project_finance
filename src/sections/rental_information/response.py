from typing import List

from src.field_value import StringField, IntField, DoubleField
from utils.field import StreamlitFieldType, StreamlitField


class RentalInformationManualEntryResponse:
    address: StringField
    months_stayed: IntField
    rent_per_month: DoubleField

    def __init__(self):
        self.address = StringField(
            title="Rental Property Address",
            required=True,
        )
        self.months_stayed = IntField(
            title="Number of Months Stayed",
            required=True,
            min_value=0,
            max_value=12
        )
        self.rent_per_month = DoubleField(
            title="Rent Paid Per Month ($)",
            required=True,
        )

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

    def get_streamlit_fields(self, key_prefix: str) -> dict[str, StreamlitField]:
        fields = {
            "address": StreamlitField(
                "address",
                self.address.title,
                StreamlitFieldType.STRING,
                key_prefix,
            ),
            "months_stayed": StreamlitField(
                "months_stayed",
                self.months_stayed.title,
                StreamlitFieldType.INT,
                key_prefix,
            ),
            "rent_per_month": StreamlitField(
                "rent_per_month",
                self.rent_per_month.title,
                StreamlitFieldType.DOUBLE,
                key_prefix,
            ),
        }
        return fields


class RentalInformationResponse:
    manual_response: List[RentalInformationManualEntryResponse]

    def custom_init(self, manual_entry_count: int):
        self.manual_response = [RentalInformationManualEntryResponse() for _ in range(manual_entry_count)]