import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def render_dict(d: dict, title: str, level: int = 0):
    """Render a dictionary in a clean, boxed layout."""
    if not d:
        return

    with st.container(border=True):
        if len(title) > 0:
            title = "###" + "#" * level + " " + title
            st.markdown(title)

        for key, value in d.items():
            if type(value) is dict:
                render_dict(value, title=key.replace('_', ' ').title(), level=level + 1)
                continue

            col_key, col_val = st.columns([1, 2])
            with col_key:
                st.markdown(f"**{key.replace('_', ' ').title()}**")
            with col_val:
                if type(value) is UploadedFile:
                    st.write(value.name)
                    continue

                st.write(value)
