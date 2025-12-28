


import streamlit as st

from src.final_response.response import FinalFormResponse
from utils.functions import render_dict
from src.final_submission import main as final_submission_component
import time

from utils.switch_page import switch_to_main, switch_to_custom_form


def render_verification_page(final_form_response: FinalFormResponse):

    st.markdown("###### If everything looks good, click the button below to confirm and submit your details")
    if st.button("Confirm and Submit"):
        # final_submission_component(final_data)

        with st.spinner("Processing your submission..."):
            time.sleep(3)

        st.success("Your details have been submitted successfully!")


def main():
    if 'custom_form_response' not in st.session_state:
        st.error("Please generate custom form first.")
        switch_to_custom_form()
        return

    if 'final_form_response' not in st.session_state:
        st.error("No final form response found. Please complete the previous steps.")
        switch_to_main()
        return

    final_form_response: FinalFormResponse = st.session_state.final_form_response
    st.info(
        "Further processing will be done on email after verification.\n\n"
        "In case of any correction, please reload the page and resubmit the details.\n\n"
        "Or you can correct on mail after submission."
    )

    with st.container(border=True):
        render_verification_page(final_form_response)


if __name__ == "__main__":
    main()
