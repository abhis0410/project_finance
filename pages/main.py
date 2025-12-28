import streamlit as st

from src.custom_form.response import CustomFormResponse
from src.final_response.render import FinalForm
from src.final_response.response import FinalFormResponse
from temp import print_all


def main():
    if 'custom_form_response' not in st.session_state:
        st.error("Please generate custom form first.")
        return

    custom_form_response: CustomFormResponse = st.session_state.custom_form_response

    final_form: FinalForm = FinalForm(custom_form_response)
    final_form_response: FinalFormResponse = final_form.render()

    if final_form_response is not None:
        st.success("Form submitted successfully!")

        print_all(final_form_response)

if __name__ == "__main__":
    main()