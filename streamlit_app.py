import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    default=True
)
project_1_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot"
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(
    {
       "Info": [about_page],
       "Projects": [project_1_page]
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.text("Made by Divan 💻")

# logo sizing and placement
st.html("""
  <style>
    [alt=Logo] {
      height: 6rem;
    }
  </style>
    """)

st.logo("assets/logo.png")
# --- RUN NAVIGATION ---
pg.run()