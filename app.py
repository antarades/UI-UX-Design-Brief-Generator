# import streamlit as st
# import random
# from generator import generate_design_brief  

# def load_css(file_name: str):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# load_css("style.css")

# industries = [
#     "Random", "Healthcare", "Fashion", "Education", "Sports",
#     "Transportation", "Real Estate", "Travel", "Finance",
#     "Food & Beverage", "Technology", "Entertainment"
# ]
# difficulties = ["Beginner", "Intermediate", "Hard"]
# brief_types = ["Short", "Long"]
# design_types = ["UI", "UX"]

# st.title("UI/UX Design Brief Generator")

# col1, col2 = st.columns([1, 2])

# with col1:
#     st.markdown("<div class='input-card'>", unsafe_allow_html=True)
#     industry = st.selectbox("Industry:", industries)
#     difficulty = st.selectbox("Difficulty:", difficulties)
#     brief_type = st.selectbox("Brief Type:", brief_types)
#     design_type = st.selectbox("Design Type:", design_types)
#     generate_clicked = st.button("Generate Brief")
#     st.markdown(
#     """
#     <div class="social-icons">
        
#     </div>
#     """,
#     unsafe_allow_html=True
# )
# with col2:
#     if "brief" not in st.session_state:
#         st.session_state.brief = None

#     if generate_clicked:
#         if industry == "Random":
#             industry_choice = random.choice(industries[1:])
#         else:
#             industry_choice = industry

#         brief = generate_design_brief(
#             design_type=design_type,
#             industry=industry_choice,
#             difficulty=difficulty.lower(),
#             brief_type=brief_type.lower(),
#             include_branding=True,
#             include_user_story=True
#         )

#         lines = brief.splitlines()
#         if lines and lines[0].startswith("#"):
#             brand_name = lines[0].lstrip("#").strip()
#             lines[0] = f"<h1 class='brand-title'>{brand_name}</h1>"
#             brief = "\n".join(lines)

#         st.session_state.brief = brief

#     if st.session_state.brief:
#         content = st.session_state.brief
#     else:
#         content = """ <h1 class='brand-title'>About Us !</h1>
        
#         <p>
#         Welcome to the <span class='accent'>UI/UX Design Brief Generator</span> — 
#         your practice space for creating portfolio-ready design projects!  
#         </p>

#         <p>
#         Choose an <b>industry</b>, pick a <b>difficulty level</b>, and decide whether 
#         you want a <b>UI</b> or <b>UX</b> project.  
#         In seconds, you'll get a professionally-structured brief complete with 
#         brand identity, project goals, and user stories.
#         </p>

#         <p>
#         This tool is designed to help beginners and intermediate designers 
#         learn how real client briefs are written — without the overwhelm of 
#         inventing them from scratch.
#         </p>
#         """

#     st.markdown(
#         f"""
#         <div class="brief-box fade-in">
#             {content}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     if st.session_state.brief:
#         st.download_button(
#         label="Export Brief",  
#         data=st.session_state.brief,
#         file_name="design_brief.txt",
#         mime="text/plain",
#         key="download-btn"
#     )
import streamlit as st
import random
from generator import generate_design_brief  

def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Initialize session state
if "brief" not in st.session_state:
    st.session_state["brief"] = None

# Dropdown options
industries = [
    "Random", "Healthcare", "Fashion", "Education", "Sports",
    "Transportation", "Real Estate", "Travel", "Finance",
    "Food & Beverage", "Technology", "Entertainment"
]
difficulties = ["Beginner", "Intermediate", "Hard"]
brief_types = ["Short", "Long"]
design_types = ["UI", "UX"]

# Main Title
st.title("UI/UX Design Brief Generator")

# Two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    industry = st.selectbox("Industry:", industries)
    difficulty = st.selectbox("Difficulty:", difficulties)
    brief_type = st.selectbox("Brief Type:", brief_types)
    design_type = st.selectbox("Design Type:", design_types)

    generate_button = st.button("Generate Brief")

    # Social icons
    st.markdown(
        """
        <div class="social-icons">
            <a href="https://github.com/antarades" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" />
            </a>
            <a href="https://linkedin.com/in/antara-srivastava-344670196/" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" />
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    if generate_button:
        if industry == "Random":
            industry_choice = random.choice(industries[1:])
        else:
            industry_choice = industry

        brief = generate_design_brief(
            design_type=design_type,
            industry=industry_choice,
            difficulty=difficulty.lower(),
            brief_type=brief_type.lower(),
            include_branding=True,
            include_user_story=True
        )
        lines = brief.splitlines()
        if lines and lines[0].startswith("#"):
            brand_name = lines[0].lstrip("#").strip()
            lines[0] = f"<h1 class='brand-title'>{brand_name}</h1>"
            brief = "\n".join(lines)

        # Save to session state
        st.session_state["brief"] = brief

    if st.session_state.brief:
        # Show brief inside styled box
        st.markdown(
            f"""
            <div class="brief-container">
                <div class="brief-box fade-in">
                    {st.session_state.brief}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Export button aligned with brief box
        st.markdown(
            """
            <div class="export-container">
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            label="Export Brief",
            data=st.session_state.brief,
            file_name="design_brief.txt",
            mime="text/plain",
            key="download-btn"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        # Default about section before generating
        st.markdown(
            """
            <div class="brief-box fade-in">
                <h1 class="brand-title">About This Tool</h1>
                <p>
                    Welcome to the <span class='accent'>UI/UX Design Brief Generator</span> — 
                    your practice space for creating portfolio-ready design projects!
                </p>
                <p>
                    Choose an <b>industry</b>, pick a <b>difficulty level</b>, and decide whether 
                    you want a <b>UI</b> or <b>UX</b> project.  
                    In seconds, you'll get a professionally-structured brief complete with 
                    brand identity, project goals, and user stories.
                </p>
                <p>
                    This tool is designed to help beginners and intermediate designers 
                    learn how real client briefs are written — without the overwhelm of 
                    inventing them from scratch.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
