import streamlit as st

from src.custom_form.render import CustomForm
from src.custom_form.response import CustomFormResponse


def main():
    if 'custom_form_response' in st.session_state:
        st.error("You have already generated the custom form. Please go to the Fill Form page to view it.")
        st.error("If you want to generate a new form, please restart the app.")
        return

    custom_form = CustomForm(title="")
    custom_form_response: CustomFormResponse = custom_form.render()

    if custom_form_response:
        st.session_state["custom_form_response"] = custom_form_response
        st.switch_page("pages/main.py")

if __name__ == "__main__":
    main()