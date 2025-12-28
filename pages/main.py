import streamlit as st

from src.custom_form.response import CustomFormResponse
from src.final_response.render import FinalForm
from src.final_response.response import FinalFormResponse
from utils.switch_page import switch_to_verification, switch_to_custom_form


def main():
    if 'custom_form_response' not in st.session_state:
        st.error("Please generate custom form first.")
        switch_to_custom_form()
        return

    if 'final_form_response' in st.session_state:
        st.info("You have already submitted the final form.")
        switch_to_verification()
        return

    custom_form_response: CustomFormResponse = st.session_state.custom_form_response

    final_form: FinalForm = FinalForm(custom_form_response)
    final_form_response: FinalFormResponse = final_form.render()

    if final_form_response is not None:
        st.session_state['final_form_response'] = final_form_response
        st.success("Form submitted successfully!")
        switch_to_verification()
        return

if __name__ == "__main__":
    main()