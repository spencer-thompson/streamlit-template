"""
How to run:
streamlit run app.py

Hello cs club
"""
import streamlit as st

def clear_form():
    st.session_state["user_text"] = ""
    st.session_state["user_pragraph"] = ""

st.title("Hello World")

col1, col2 = st.columns(2)

fillerText = """
<div style="width:100%">"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam feugiat odio non elit blandit vehicula. In hac habitasse platea dictumst. Vivamus tincidunt, justo vel posuere consectetur, odio augue vestibulum sapien, a convallis elit tortor eget justo. Sed at risus nec justo interdum dapibus. Sed placerat lacinia elit, eu fermentum velit fermentum id. Praesent non odio ut leo dictum elementum eu at purus. Fusce at nisl eu dui auctor vulputate a ac sapien. Fusce vestibulum purus sit amet urna posuere, id iaculis leo mattis. Integer id nisi sed ligula posuere tincidunt. In hac habitasse platea dictumst. Etiam luctus augue ac erat rhoncus, id bibendum quam eleifend.</div>
"""

with col1:
    st.markdown(fillerText, unsafe_allow_html=True)

with col2:
    st.image("fillerImage.png")

st.title("Example Form:")

col1, col2 = st.columns(2)
selected_button = None
with col1:
    short_entry = st.text_input("Short Entry", key="user_text")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    colx, coly, colz = st.columns(3)
    with colx:
        checkbox1 = st.checkbox("button 1")
    with coly:
        checkbox2 = st.checkbox("button 2")
    with colz:
        checkbox3 = st.checkbox("button 3")

paragraph_entry = st.text_area("User Paragraph", key = "user_paragraph")

if st.button("Submit"):
    short_entry_value = short_entry
    paragraph_entry_value = paragraph_entry
    checkbox = (checkbox1, checkbox2, checkbox3)
    print(short_entry_value, paragraph_entry_value, checkbox)
