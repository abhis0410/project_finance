import streamlit as st

from components.personal_information import main as personal_information_form
from components.employment_information import main as employer_information_form
from components.final_response import FinalResponse

from utils.employer_information import EmployerInformation


def render_personal_information(final_response: FinalResponse):
    # Render the form
    if final_response.personal_information is not None:
        st.info("Personal information already provided.")
        return

    data = personal_information_form()

    # Persist only when user submits valid data
    if data is not None:
        final_response.personal_information = data
        st.success("Personal information saved.")
        return

def render_employer_information(final_response: FinalResponse):
    if len(final_response.employer_information) > 0:
        st.info("Employer information already provided.")
        return

    with st.form("employer_count_form"):
        manual_entry_count = st.number_input(
            "Number of Employers with manual entry", 0, 10, 1
        )
        form_entry_count = st.number_input(
            "Number of Employers with form entry", 0, 10, 0
        )
        submitted = st.form_submit_button("Continue")

    if not submitted:
        return

    data = employer_information_form()


def main():
    if 'final_response' not in st.session_state:
        st.session_state['final_response'] = FinalResponse()

    final_response: FinalResponse = st.session_state.final_response

    x = """
    render_personal_information(final_response)
    st.divider()

    if final_response.personal_information is None:
        return
    """
    render_employer_information(final_response)
    st.divider()

    # Final verification step
    if final_response.ready_for_verification() and st.button("Go to Verification Page"):
        st.session_state['final_response'] = final_response
        st.switch_page('pages/verify.py')




if __name__ == "__main__":
    main()
