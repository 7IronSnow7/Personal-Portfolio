import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Divan De Bruin.jpg", width=230)
with col2:
    st.title("Divan De Bruin",  anchor="False")
    st.write("Developer in the Making")
    if st.button("✉ Contact Me"):
        show_contact_form()
        
# --- SHORT INTRO ---
st.write("\n")
st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
        text-justify: inter-word; /* Improves justification, especially in some browsers */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.write(
    """
    <div class="justified-text">
    Passionate and results-driven individual with a demonstrated history of unwavering work ethic and ambitious pursuits. 
    Recognized for outstanding time management and organizational skills, 
    I seamlessly contribute to collaborative team efforts. 
    My unwavering commitment to excellence, proactive initiative, 
    and relentless pursuit of professional growth position me as a valuable asset to any organisation.
    </div>
    """,
    unsafe_allow_html=True,
)

# --- EXPERIENCE AND QUALIFICATIONS
st.write("\n")
st.subheader("Experience", anchor=False)
st.write(
    """
    - Server | Ocean Reef (KEY LARGO)| December 2023 - Present
    - Project Lead | Sebonack (NYC) | June 2023 – November 2023
    - Server | Woodfield CC (BOCA RATON) | February 2022 – May 2023
    - Project Coordinator | AMS Attorneys Inc (KZN) | Aug 2019 - Jan 2022 
    """
)
st.write("\n")
st.subheader("Qualifications", anchor=False)
st.write(
    """
    
    """
)
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    
    """
)