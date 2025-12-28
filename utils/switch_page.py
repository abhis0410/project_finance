import streamlit as st
import time


def switch_to_verification(title = None):
    if not title:
        title = "Proceeding for verification..."
    with st.spinner(title):
        time.sleep(3)
        st.switch_page('pages/verify.py')


def switch_to_main(title = None):
    if not title:
        title = "Proceeding to main form..."
    with st.spinner(title):
        time.sleep(3)
        st.switch_page('pages/main.py')


def switch_to_custom_form(title = None):
    if not title:
        title = "Proceeding to custom form..."
    with st.spinner(title):
        time.sleep(3)
        st.switch_page('pages/custom_form.py')