from datetime import date
from utils.field import StreamlitField, StreamlitFieldType
from typing import List


def personal_information_form(key_prefix: str) -> List[StreamlitField]:
    streamlit_fields = [
        StreamlitField("first_name", "First name", StreamlitFieldType.STRING, key_prefix),
        StreamlitField("last_name", "Last name", StreamlitFieldType.STRING, key_prefix),

        StreamlitField(
            "sin",
            "Social Insurance Number",
            StreamlitFieldType.STRING,
            key_prefix,
            help_text="9-digit number",
        ),

        StreamlitField(
            "date_of_birth",
            "Date of birth",
            StreamlitFieldType.DATE,
            key_prefix,
            default=date(1990, 1, 1),
        ),

        StreamlitField(
            "province_2025",
            "Province of residence on December 31, 2025",
            StreamlitFieldType.STRING,
            key_prefix,
        ),

        StreamlitField(
            "marital_status_2025",
            "Marital status on December 31, 2025",
            StreamlitFieldType.SELECT,
            key_prefix,
            options=["Single", "Married", "Common-law", "Divorced", "Widowed"],
        ),

        StreamlitField("street", "Street address", StreamlitFieldType.STRING, key_prefix),
        StreamlitField("city", "City", StreamlitFieldType.STRING, key_prefix),
        StreamlitField("address_province", "Province", StreamlitFieldType.STRING, key_prefix),
        StreamlitField("postal_code", "Postal code", StreamlitFieldType.STRING, key_prefix),

        StreamlitField("home_phone", "Home phone number", StreamlitFieldType.STRING, key_prefix, required=False),
        StreamlitField("email", "Email address", StreamlitFieldType.STRING, key_prefix),
    ]

    return streamlit_fields