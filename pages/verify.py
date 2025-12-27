


import streamlit as st
from utils.functions import render_dict
from src.final_submission import main as final_submission_component
import time

def render_verification_page():
    final_data = st.session_state['final_data']

    render_dict(final_data, "")

    disclaimer = "Further Processing will be done on email after verification. "
    disclaimer += "In case of any correction, please reload the page and resubmit the details."
    disclaimer += "Or you can correct on mail after submission."

    st.markdown("If everything looks good, click the button below to confirm and submit your details")
    if st.button("Confirm and Submit"):
        final_submission_component(final_data)

        with st.spinner("Processing your submission..."):
            time.sleep(3)

        st.success("Your details have been submitted successfully!")



def main():
    st.title("Final Verification Page")
    if 'final_data' not in st.session_state:
        st.error("No data available for verification. Please complete the previous steps.")
        return

    render_verification_page()


if __name__ == "__main__":
    main()
