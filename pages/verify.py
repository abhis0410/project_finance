from components.final_response import FinalResponse
from utils.functions import render_dict
import streamlit as st



def render_final_response(final_response: FinalResponse):
    # Render Personal Information
    personal_information = final_response.personal_information
    render_dict(personal_information, "Personal Information")

    # Render Employer Information
    for i, employer_info in enumerate(final_response.employer_information):
        render_dict(employer_info, f"Employer Information {i+1}")

    # Render....


def main():
    if 'final_response' not in st.session_state:
        st.error("Please go to the main page first & submit details to verify")
        return

    final_response: FinalResponse = st.session_state['final_response']
    render_final_response(final_response)


    if st.button("Submit Final Response"):
        st.success("Final response submitted successfully!")
        st.session_state.pop('final_response', None)


if __name__ == "__main__":
    main()