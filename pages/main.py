import streamlit as st
from components.final_response import FinalResponse
import time

def render_final_response():
    if 'final_response' not in st.session_state:
        st.error("Please generate custom form first.")
        return

    final_response: FinalResponse = st.session_state.final_response
    result = final_response.render_form()

    if result is None:
        return

    st.success("Form submitted successfully!")
    with st.spinner("Moving forward for final verification..."):
        time.sleep(2)
        st.session_state['final_data'] = result
        st.switch_page("pages/verify.py")


def main():
    render_final_response()


if __name__ == "__main__":
    main()
