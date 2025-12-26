import streamlit as st
from datetime import date
from components.field import Field, FieldType
from components.form import Form


def personal_information_form():
    fields = [
        Field("first_name", "First name", FieldType.STRING),
        Field("last_name", "Last name", FieldType.STRING),

        Field(
            "sin",
            "Social Insurance Number",
            FieldType.STRING,
            help_text="9-digit number",
        ),

        Field(
            "date_of_birth",
            "Date of birth",
            FieldType.DATE,
            default=date(1990, 1, 1),
        ),

        Field(
            "province_2025",
            "Province of residence on December 31, 2025",
            FieldType.STRING,
        ),

        Field(
            "marital_status_2025",
            "Marital status on December 31, 2025",
            FieldType.SELECT,
            options=["Single", "Married", "Common-law", "Divorced", "Widowed"],
        ),

        Field("street", "Street address", FieldType.STRING),
        Field("city", "City", FieldType.STRING),
        Field("address_province", "Province", FieldType.STRING),
        Field("postal_code", "Postal code", FieldType.STRING),

        Field("home_phone", "Home phone number", FieldType.STRING, required=False),
        Field("email", "Email address", FieldType.STRING),
    ]

    form = Form(
        form_id="personal_information",
        title="Personal Information",
        fields=fields,
    )

    return form.render()


def main():
    st.title("Tax Information Form")

    data, errors = personal_information_form()

    if st.button("Submit"):
        if errors:
            st.error("Please fix the highlighted errors.")
            st.json(errors)
        else:
            return data

    return None