


import streamlit as st
from utils.functions import render_dict
from components.final_submission import main as final_submission_component


def render_verification_page():
    final_data = st.session_state['final_data']

    render_dict(final_data, "")

    disclaimer = "Further Processing will be done on email after verification. "
    disclaimer += "In case of any correction, please reload the page and resubmit the details."
    disclaimer += "Or you can correct on mail after submission."

    st.markdown("If everything looks good, click the button below to confirm and submit your details")
    if st.button("Confirm and Submit"):
        st.success("Your details have been submitted successfully!")
        final_submission_component(final_data)
        # Here you can add code to process the final_data as needed


    pass



def main():
    st.title("Final Verification Page")
    if 'final_data' not in st.session_state:
        st.error("No data available for verification. Please complete the previous steps.")
        return

    render_verification_page()


if __name__ == "__main__":
    main()
