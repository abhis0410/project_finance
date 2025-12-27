from datetime import date
from utils.field import Field, FieldType
from typing import List


def personal_information_form(key_prefix: str) -> List[Field]:
    fields = [
        Field("first_name", "First name", FieldType.STRING, key_prefix),
        Field("last_name", "Last name", FieldType.STRING, key_prefix),

        Field(
            "sin",
            "Social Insurance Number",
            FieldType.STRING,
            key_prefix,
            help_text="9-digit number",
        ),

        Field(
            "date_of_birth",
            "Date of birth",
            FieldType.DATE,
            key_prefix,
            default=date(1990, 1, 1),
        ),

        Field(
            "province_2025",
            "Province of residence on December 31, 2025",
            FieldType.STRING,
            key_prefix,
        ),

        Field(
            "marital_status_2025",
            "Marital status on December 31, 2025",
            FieldType.SELECT,
            key_prefix,
            options=["Single", "Married", "Common-law", "Divorced", "Widowed"],
        ),

        Field("street", "Street address", FieldType.STRING, key_prefix),
        Field("city", "City", FieldType.STRING, key_prefix),
        Field("address_province", "Province", FieldType.STRING, key_prefix),
        Field("postal_code", "Postal code", FieldType.STRING, key_prefix),

        Field("home_phone", "Home phone number", FieldType.STRING, key_prefix, required=False),
        Field("email", "Email address", FieldType.STRING, key_prefix),
    ]

    return fields