from datetime import date
from typing import Dict, Any

from src.field_value import StringField
from utils.field import StreamlitField, StreamlitFieldType


class PersonalInformationResponse:
    first_name: StringField
    last_name: StringField
    sin: StringField
    date_of_birth: StringField
    province: StringField
    marital_status: StringField
    street: StringField
    city: StringField
    address_province: StringField
    postal_code: StringField
    home_phone: StringField
    email: StringField

    def __init__(self):
        self.first_name = StringField(title="First name", required=True)
        self.last_name = StringField(title="Last name", required=True)
        self.sin = StringField(title="Social Insurance Number", required=True)
        self.date_of_birth = StringField(title="Date of birth", required=True)
        self.province = StringField(
            title="Province of residence",
            required=True,
        )
        self.marital_status = StringField(
            title="Marital status",
            required=True,
        )
        self.street = StringField(title="Street address", required=True)
        self.city = StringField(title="City", required=True)
        self.address_province = StringField(title="Province", required=True)
        self.postal_code = StringField(title="Postal code", required=True)
        self.home_phone = StringField(title="Home phone number", required=False)
        self.email = StringField(title="Email address", required=True)

    def setter(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                getattr(self, key).set_value(value)

    def get_streamlit_fields(self, key_prefix: str) -> dict[Any, StreamlitField]:
        fields = {
            "first_name": StreamlitField("first_name", self.first_name.title, StreamlitFieldType.STRING, key_prefix),
            "last_name": StreamlitField("last_name", self.last_name.title, StreamlitFieldType.STRING, key_prefix),
            "sin": StreamlitField("sin", self.sin.title, StreamlitFieldType.STRING, key_prefix),
            "date_of_birth": StreamlitField(
                "date_of_birth",
                self.date_of_birth.title,
                StreamlitFieldType.DATE,
                key_prefix,
                default=date(1990, 1, 1),
            ),
            "province": StreamlitField(
                "province",
                self.province.title,
                StreamlitFieldType.STRING,
                key_prefix,
            ),
            "marital_status": StreamlitField(
                "marital_status",
                self.marital_status.title,
                StreamlitFieldType.SELECT,
                key_prefix,
                options=["Single", "Married", "Common-law", "Divorced", "Widowed"],
            ),
            "street": StreamlitField("street", self.street.title, StreamlitFieldType.STRING, key_prefix),
            "city": StreamlitField("city", self.city.title, StreamlitFieldType.STRING, key_prefix),
            "address_province": StreamlitField("address_province", self.address_province.title, StreamlitFieldType.STRING, key_prefix),
            "postal_code": StreamlitField("postal_code", self.postal_code.title, StreamlitFieldType.STRING, key_prefix),
            "home_phone": StreamlitField(
                "home_phone",
                self.home_phone.title,
                StreamlitFieldType.STRING,
                key_prefix,
                required=False,
            ),
            "email": StreamlitField("email", self.email.title, StreamlitFieldType.STRING, key_prefix),
        }
        return fields
