import streamlit as st

from src.custom_form.response import CustomFormResponse
from src.final_response.render import FinalForm
from src.final_response.response import FinalFormResponse


def main():
    if 'custom_form_response' not in st.session_state:
        st.error("Please generate custom form first.")
        return

    custom_form_response: CustomFormResponse = st.session_state.custom_form_response

    final_form: FinalForm = FinalForm(custom_form_response)
    final_form_response: FinalFormResponse = final_form.render()

    if final_form_response is not None:
        print("FFR", final_form_response.personal_information_response.first_name.value)
        print("FFR2", final_form_response.employment_information_response.manual_response[0].employer_name.value)
        st.success("Form submitted successfully!")

if __name__ == "__main__":
    main()