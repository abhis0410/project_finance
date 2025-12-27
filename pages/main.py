import streamlit as st
from components.final_response import FinalResponse

def render_final_response():

    if 'final_response' not in st.session_state:
        with st.form("employer_count_form"):
            manual_entry_count = st.number_input(
                "Number of Employers with manual entry", 0, 10, 1
            )
            file_upload_count = st.number_input(
                "Number of Employers with form entry", 0, 10, 0
            )
            submitted = st.form_submit_button("Continue")

            if submitted:
                final_response = FinalResponse(manual_entry_count, file_upload_count)
                st.session_state['final_response'] = final_response
            else:
                return


    final_response: FinalResponse = st.session_state.final_response

    final_response.render_form()



def main():
    render_final_response()



if __name__ == "__main__":
    main()
