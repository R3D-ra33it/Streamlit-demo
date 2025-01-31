import streamlit as st

api_key = st.secrets["API_KEY"]
st.write(api_key)


st.set_page_config(
    page_title="AIS AI Coding Assistant",
        layout="centered"
)

st.title('AIS AI Coding Assistant')

prompt = st.chat_input('Ask anything...')

if "chats" not in st.session_state:
    st.session_state.chats = []

if prompt:
    st.session_state.chats.append({
        "role": "user",
        "content": prompt
    })


for chat in st.session_state.chats:
    st.chat_message(chat['role']).markdown(chat['content'])
