import streamlit as st

from components.personal_information import main as personal_information_form
from components.final_response import FinalResponse


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


def main():
    if 'final_response' not in st.session_state:
        st.session_state['final_response'] = FinalResponse()

    final_response: FinalResponse = st.session_state.final_response

    render_personal_information(final_response)
    st.divider()


    if final_response.ready_for_verification() and st.button("Go to Verification Page"):
        st.session_state['final_response'] = final_response
        st.switch_page('pages/verify.py')




if __name__ == "__main__":
    main()
