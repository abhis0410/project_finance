import streamlit as st
import time
from components.final_response import  FinalResponse


def generate_custom_form():
    with st.form("employer_count_form"):
        manual_entry_count = st.number_input(
            "Number of Employers with manual entry", 0, 10, 1
        )
        file_upload_count = st.number_input(
            "Number of Employers with form entry", 0, 10, 0
        )

        submitted = st.form_submit_button("Continue")
        if submitted:
            with st.spinner("Generating Tailor-made form for you..."):
                time.sleep(2)
                return FinalResponse(manual_entry_count, file_upload_count)
        else:
            return None



def main():
    if 'final_response' not in st.session_state:
        final_response = generate_custom_form()
        if final_response:
            st.session_state['final_response'] = final_response
            st.switch_page("pages/main.py")
        else:
            return

    else:
        st.error("You have already generated the custom form. Please go to the Fill Form page to view it.")
        st.error("If you want to generate a new form, please restart the app.")


if __name__ == "__main__":
    main()