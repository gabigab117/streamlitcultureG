import json
import streamlit as st

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def reset():
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.feedback = None
    st.rerun()
