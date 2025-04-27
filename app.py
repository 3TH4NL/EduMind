# app.py
import streamlit as st
from logic import generate_content

st.set_page_config(page_title="EduMind - Mental Health Educational Content Generator", page_icon="🎓")


tab1, tab2 = st.tabs(["🏠 Project Overview", "📝 Educational Content Generator"])


with tab1:
    st.title("🎓 EduMind: Project Overview")
    st.markdown("---")
    st.write("""
    Welcome to EduMind, a mental health educational content generator that leverages RAG (Retrieval-Augmented Generation) and prompt engineering to deliver high-quality outputs.
    """)

    st.header("🔍 Key Features")
    st.write("""
    - Retrieve relevant information from a curated mental health knowledge base.  
    - Dynamically generate task-specific prompts.  
    - Produce clear and supportive educational content using the Gemini model.  
    - Interactive and user-friendly Streamlit interface.
    """)

    st.markdown("---")
    st.header("🔗 Project Links")
    st.write("""
    - [GitHub Repository](https://github.com/your-username/your-repo-name)  
    - [Project Documentation (PDF)](https://github.com/your-username/your-repo-name/blob/main/EduMind_Documentation.pdf)
    """)

    st.markdown("---")
    st.header("🌟 How It Works")
    st.write("""
    1. Enter a mental health-related keyword (e.g., anxiety, mindfulness).  
    2. Select the type of content you want to generate.  
    3. Click "Generate Content" to receive customized educational material.
    """)


with tab2:
    st.title("📝 Educational Content Generator")
    st.write("Enter a mental health topic and select the type of educational content you'd like to generate.")
    st.markdown("---")

    keyword = st.text_input("Enter a mental health topic (e.g., anxiety, depression, PTSD):")

    task_type = st.selectbox(
        "Select the type of content you want to generate:",
        ("Generate Class Notes", "Generate 5 Practice Questions", "Generate Mini Lecture")
    )

    if st.button("Generate Content"):
        if not keyword.strip():
            st.error("Please enter a valid topic!")
        else:
            with st.spinner("Generating content..."):
                output = generate_content(keyword, task_type)
            st.success("Here is your generated educational content:")
            st.write(output)
