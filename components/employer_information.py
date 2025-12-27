from utils.field import Field, FieldType
from utils.file_input import  FileInput
import streamlit as st

class EmployerInformation:
    def __init__(self, manual_entry_count, file_upload_count):
        self.manual_entry_count = manual_entry_count
        self.file_upload_count = file_upload_count
        self.employer_fields = []

        print("Class Initialized")


    @staticmethod
    def _get_manual_entry(index: int):
        """
        Single employer form.
        index is used to keep keys unique when multiple employers exist.
        """
        fields = [
            Field(
                "employer_name",
                "Name of Employer",
                FieldType.STRING,
                f"{index}"
            ),

            Field(
                "employer_address",
                "Address of Employer",
                FieldType.STRING,
                f"{index}"
            ),

            Field(
                "employment_income",
                "Employment Income (Amount in Column 14)",
                FieldType.DOUBLE,
                f"{index}"
            ),

            Field(
                "cpp_contribution",
                "CPP (Amount in Column 16)",
                FieldType.DOUBLE,
                f"{index}"
            ),

            Field(
                "ei_contribution",
                "EI (Amount in Column 24)",
                FieldType.DOUBLE,
                f"{index}"
            ),

            Field(
                "column_18_amount",
                "Amount in Column 18",
                FieldType.DOUBLE,
                f"{index}"
            ),

            Field(
                "column_26_amount",
                "Amount in Column 26",
                FieldType.DOUBLE,
                f"{index}"
            ),
        ]

        return fields


    @staticmethod
    def _get_file_upload_entry(index: int):
        form = FileInput(
            name=f"t4_slip_{index}",
            label=f"Upload T4 Slip for Employer",
            key_prefix=f"{index}",
            allowed_types=["pdf"],
            required=True,
            help_text="Please upload a PDF copy of your T4 slip.",
            multiple=False,
        )
        return form


    def _process(self, index, is_manual_entry: bool):
        st.title(f"Employer Information {index + 1}")

        if is_manual_entry:
            all_fields = self._get_manual_entry(index)
            self.employer_fields.extend(all_fields)
        else:
            all_fields = self._get_file_upload_entry(index)
            self.employer_fields.append(all_fields)


    def get_all_fields(self):
        total_entries = self.manual_entry_count + self.file_upload_count

        index = 0
        while index < total_entries:
            print("Total Entries:", total_entries)
            print("Current Fields Length:", len(self.employer_fields))
            print("Index:", index)
            is_manual_entry = index < self.manual_entry_count
            self._process(index, is_manual_entry)
            index += 1


        return self.employer_fields