import streamlit as st


def render_dict(d: dict, title: str):
    """Render a dictionary in a clean, boxed layout."""
    with st.container(border=True):
        st.markdown(f"### {title}")

        if not d:
            st.caption("No data available")
            return

        for key, value in d.items():
            col_key, col_val = st.columns([1, 2])
            with col_key:
                st.markdown(f"**{key.replace('_', ' ').title()}**")
            with col_val:
                st.write(value)
