#  EduMind: Mental Health Educational Content Generator

EduMind is a generative AI application that creates professional, supportive educational content focused on mental health topics.  
It leverages Retrieval-Augmented Generation (RAG) and prompt engineering to deliver contextually accurate outputs through an interactive Streamlit application.

---

##  Key Features

- Retrieve relevant information from a curated mental health knowledge base.
- Dynamically generate task-specific prompts.
- Produce educational outputs using the Gemini 1.5 Flash model via API.
- Provide three types of educational content:
  - Generate Class Notes
  - Generate 5 Practice Questions
  - Generate Mini Lectures
- Interactive and user-friendly Streamlit interface.
- Deployed online via Streamlit Cloud for real-time access.

---

##  Project Structure

```
/EduMind
├── app.py                    # Streamlit front-end with tabs (Project Overview + Generator)
├── logic.py                  # Core retrieval and generation logic
├── kb.csv                    # Knowledge base (mental health content)
├── requirements.txt          # Python dependency list
├── README.md                 # Project documentation
├── EduMind_ Documentation.pdf # Full project report (architecture, metrics, future improvements)
├── Example Outputs.txt       # Sample generated outputs for different tasks
├── testing scripts/
│   └── 7375Notebook.ipynb    # Annotated version of logic.py with detailed explanations and three different test cases
```



##  Setup Instructions

1. Clone this repository:

2. Install the dependencies:

   pip install -r requirements.txt

3. Run the application locally:

   streamlit run app.py

