# ECHO BOT
import openai
import streamlit as st

st.title("Echo Bot")

st.markdown("### 👋 What's This Echo Bot Thing?")
st.info("""
Think of this as a super simple chat where I just repeat what you say! 🗣️

You type something in the box, and BAM! I show it right back to you. It's like talking to a friendly parrot (a digital one, of course!). 🦜

**Why is it so basic?**

You might see some code stuff about something called 'openai'. That's a cool tool for making really smart chatbots, the kind that can actually understand and talk with you. I was playing around with it, but those smart bots can cost money to use. 💸

So, for now, this is just a straightforward echo. It's a simple way to see how basic chat stuff can be built with code. Maybe someday it'll get smarter! 😉
""")

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
    
st.markdown("---")
st.markdown(f"""
    <p align="center">
        Check out the source code for this Echo Bot on <a href="https://github.com/7IronSnow7/Personal-Portfolio/blob/master/views/chatbot.py" target="_blank">GitHub</a>.
    </p>
    """, unsafe_allow_html=True)

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
