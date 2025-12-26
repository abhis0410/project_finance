import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import utils.constants as CONSTANTS

def sidebar_contact():
    with st.sidebar:
        with st.container(border=True):
            st.markdown("## 📬 Contact")
            st.markdown(
                f"""
                    **✉️** [{CONSTANTS.ContactInfo.EMAIL}](mailto:{CONSTANTS.ContactInfo.EMAIL})  
                    **📞** {CONSTANTS.ContactInfo.CONTACT_NUMBER}  
                    [LinkedIn]({CONSTANTS.URL.LINKEDIN_URL}) ·
                    [Instagram]({CONSTANTS.URL.INSTAGRAM_URL})
                """
            )

def main():
    st.set_page_config(layout="wide")
    sidebar_contact()

    nav = get_nav_from_toml()
    pg = st.navigation(nav)
    add_page_title(pg)
    pg.run()


if __name__ == "__main__":
    main()