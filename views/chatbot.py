# ECHO BOT
import openai
import streamlit as st

st.title("Echo Bot")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
prompt = st.chat_input("Hello!")
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = f"Echo: {prompt}"
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant
    st.session_state.messages.append({"role": "assistant", "content": response})

# FOR OPEN AI
#_________________________________________________
# import streamlit as st
# from openai import OpenAI

# st.title("Wish me luck")
# client = OpenAI(api_key=st.secrets["ACE"])

# if "messages" not in st.session_state:
#     st.session_state.messages = []
    
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
# prompt = st.chat_input("Say something")
# if prompt:
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     st.session_state.messages.append({"role": "user", "content": prompt})
    
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=st.session_state.messages
#     ).choices[0].message.content
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     st.session_state.messages.append({"role": "assisstant", "content": response})