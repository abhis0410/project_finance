# employer_information.py
import streamlit as st
from utils.field import Field, FieldType
from utils.form import Form
from utils.file_input import FileInput


def employer_information_form_manual_entry(index: int):
    """
    Single employer form.
    index is used to keep keys unique when multiple employers exist.
    """
    fields = [
        Field(
            "employer_name",
            "Name of Employer",
            FieldType.STRING,
        ),

        Field(
            "employer_address",
            "Address of Employer",
            FieldType.STRING,
        ),

        Field(
            "employment_income",
            "Employment Income (Amount in Column 14)",
            FieldType.DOUBLE,
        ),

        Field(
            "cpp_contribution",
            "CPP (Amount in Column 16)",
            FieldType.DOUBLE,
        ),

        Field(
            "ei_contribution",
            "EI (Amount in Column 24)",
            FieldType.DOUBLE,
        ),

        Field(
            "column_18_amount",
            "Amount in Column 18",
            FieldType.DOUBLE,
        ),

        Field(
            "column_26_amount",
            "Amount in Column 26",
            FieldType.DOUBLE,
        ),
    ]

    form = Form(
        form_id=f"employer_information_{index}",
        title=f"Employer #{index + 1}",
        fields=fields,
    )

    return form.render()


def employer_information_form_file_upload(index: int):
    form = FileInput(
        name = f"t4_slip_{index}",
        label = f"Upload T4 Slip for Employer",
        allowed_types = ["pdf"],
        required = True,
        help_text = "Please upload a PDF copy of your T4 slip.",
        multiple = False,
    )
    return form.render(f"{index}")



def main(index: int=0, is_manual_entry: bool=True):
    st.title(f"Employer Information {index + 1}")


    if is_manual_entry:
        data, errors = employer_information_form_manual_entry(index)
    else:
        data = employer_information_form_file_upload(index)
        errors = None

    if st.button("Submit"):
        if errors:
            st.error("Please fix the highlighted errors.")
            st.json(errors)
        else:
            return data

    return None
