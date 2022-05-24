import base64

import streamlit as st
from pkg_resources import resource_filename


def streamlit_custom_page():
    # Page layout config
    logo_path = resource_filename("pr_streamlit_template", "assets/images/logo_coe.png")
    st.set_page_config(
        page_title="", page_icon=logo_path, layout="wide", initial_sidebar_state="auto"
    )

    # CoE logo on the sidebar
    st.sidebar.image(logo_path)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Set custom PR css template
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Background image
    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = (
            """
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s") !important;
        background-size: cover;
        }
        </style>
        """
            % bin_str
        )

        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

    set_png_as_page_bg(
        resource_filename("pr_streamlit_template", "assets/images/background_image.png")
    )

    # Call the css PR template
    local_css(resource_filename("pr_streamlit_template", "assets/css/streamlit_PR.css"))
