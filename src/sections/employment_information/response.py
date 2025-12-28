from src.field_value import StringField, DoubleField, FieldValue
from typing import List, Any
from dataclasses import dataclass

@dataclass
class EmployerManualEntryResponse:
    employer_name: StringField = StringField(
        title="Name of Employer",
        required=True,
    )

    employer_address: StringField = StringField(
        title="Address of Employer",
        required=True,
    )

    employment_income: DoubleField = DoubleField(
        title="Employment Income (Amount in Column 14)",
        required=True,
    )

    cpp_contribution: DoubleField = DoubleField(
        title="CPP (Amount in Column 16)",
        required=False,
    )

    ei_contribution: DoubleField = DoubleField(
        title="EI (Amount in Column 24)",
        required=False,
    )

    column_18_amount: DoubleField = DoubleField(
        title="Amount in Column 18",
        required=False,
    )

    column_26_amount: DoubleField = DoubleField(
        title="Amount in Column 26",
        required=False,
    )





@dataclass
class EmploymentResponse:
    manual_employers: List[EmployerManualEntryResponse]
    uploaded_t4s: List[Any]  # Streamlit UploadedFile
