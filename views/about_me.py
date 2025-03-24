import streamlit as st
from forms.contact import contact_form

st.write(f"Streamlit version: {st.__version__}")

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

with st.expander("Project Lead | Sebonack (NYC) | June 2023 – Present"):
    st.write(
        """
        • Led the planning and organization of enterprise events, ensuring
          seamless execution through effective scheduling, logistics
          management, and on-site coordination.\n
        • Streamlined team operations by assigning tasks, setting clear
          priorities, and optimizing workflows to enhance efficiency and
          overall event success.\n
        • Maintained direct oversight of event setup and execution,
          proactively addressing challenges to ensure smooth operations and
          a high-quality guest experience.\n
        • Fostered a collaborative and motivated team environment,
          ensuring all members were aligned and working efficiently to meet
          event objectives.\n
        • Applied strong problem-solving skills to anticipate and resolve
          operational issues, ensuring every event met the organization’s
          professional standards.
          
        """
    )

with st.expander("Supervisor | Woodfield CC (BOCA RATON) | February 2022 – May 2023"):
    st.write(
        """
        • Acted as a key point of contact for team coordination, ensuring
          seamless communication and quick decision-making in a fast-paced
          environment.\n
        • Led and coordinated a team, delegating tasks effectively while
          maintaining a high level of organization and productivity.\n
        • Trained and mentored new team members, reinforcing best
          practices and fostering a collaborative, high-performance work
          environment.\n
        • Leveraged strong analytical and logical thinking to anticipate
          challenges, implement effective solutions, and enhance service
          efficiency.\n
        • Managed service logistics, proactively resolving operational issues
          to maintain efficiency and uphold organizational standards.
        """
    )

with st.expander("Project Coordinator | AMS Attorneys Inc (KZN) | Aug 2019 - Jan 2022"):
    st.write(
        """
        • Led strategic marketing and public relations initiatives within the conveyancing industry,
          enhancing brand visibility and strengthening client engagement.\n
        • Spearheaded campaign planning and execution, ensuring consistent messaging and alignment
          with business objectives.\n
        • Coordinated cross-functional efforts to streamline communication, keeping clients and
          stakeholders informed on key project updates and milestones.\n
        • Applied analytical thinking to assess marketing performance, identify growth opportunities,
          and implement data-driven improvements.\n
        • Developed and maintained strong client relationships, fostering trust and long-term business
          partnerships.
        """
    )
st.write("\n")
st.subheader("Qualifications", anchor=False)
st.markdown("**Bachelor of Commerce – Marketing Management** | IIE Varsity College Durban North | 2015 – 2017")
st.write("• Developed a solid foundation in marketing, business principles, and strategic communication.")

st.markdown("**Honors in Management & Leadership** | IIE Varsity College Durban North | 2018")
st.write("• Explored advanced concepts in leadership, organizational management, and decision-making strategies.")

st.markdown("**C# and JavaScript Bootcamp** | School of IT - Bootcamp | 2023")
st.write("• Explored advanced concepts in leadership, organizational management, and decision-making strategies.")

st.markdown("**Foundational C# with Microsoft** | Microsoft - Online | 2024")
st.write("• Gained foundational expertise in C# for .NET development, with a focus on efficient design, code optimization, and debugging techniques.")

st.markdown("**Python for Computer Science (CS50)** | Harvard University - Online | Ongoing")
st.write("• Engaging in a comprehensive study of Python programming, covering core concepts in algorithms, data structures, and software engineering practices. Focused on building practical, real-world applications and problem-solving skills.")

st.write("\n")
st.subheader("Skills", anchor=False)
st.markdown("<u>**Project Management & Leadership**</u>", unsafe_allow_html=True)
st.write("• Strong problem-solving and logical thinking skills to optimize workflows and improve efficiency.")
st.write("• Team coordination and leadership, ensuring seamless collaboration and task execution.")
st.write("• Strategic planning and resource management to drive successful project outcomes.")
st.write("\n")
st.markdown("<u>**Software Development & Technical Skill**</u>", unsafe_allow_html=True)
st.write("• **Programming Languages:** C# (.NET Framework), Python, JavaScript")
st.write("• **Web Development:** Responsive Web Design, Frontend & Backend Development")
st.write("• **Software Engineering Principles:** Object-Oriented Programming (OOP), Functional Programming")
st.write("• **Technical Problem-Solving:** Debugging, optimizing performance, and implementing scalable solutions")
st.write("• **Version Control:** Git, including branching, merging and managing repositories to streamline development processes")
st.write("\n")

st.markdown("---")
st.markdown(f"""
<p align="center">
    Full Project Source Code Found Here: <a href="https://github.com/7IronSnow7/Personal-Portfolio/blob/master/views/scanner_ui.py" target="_blank">GitHub</a>.
</p>
""", unsafe_allow_html=True)
