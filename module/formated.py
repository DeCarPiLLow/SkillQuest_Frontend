import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

class Title(object):
    """"
    Update title and favicon of each page
    ⚠️ IMPORTANT: Must call page_config() as first function in script 
    """
    def __init__(self):
        pass
    
    def page_config(self, title):
        self.title = title
        st.set_page_config(page_title=self.title)

