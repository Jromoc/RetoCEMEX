from transformers import BertModel, BertTokenizer
from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex
import glob
import os
import fitz

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

inputA = st.text_input()

st.write(inputA)



