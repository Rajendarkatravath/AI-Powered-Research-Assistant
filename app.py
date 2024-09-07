import streamlit as st
from langchain import LLMChain, PromptTemplate
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# GROQ API key
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize Llama 3 model using ChatGroq with the GROQ API
llama3_model = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

# Set up Streamlit UI with a custom theme and wide layout
st.set_page_config(page_title="AI-Powered Research Assistant", layout="wide")

# Customize the sidebar
st.sidebar.title("AI-Powered Research Assistant")
st.sidebar.write("Leverage advanced AI to explore research topics, generate summaries, answer questions, suggest related topics, and more.")

# Header section with custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: red;  /* Changed color to red */
            text-align: center;
            margin-bottom: 0.5em;
        }
        .subheader {
            font-size: 1.5em;
            color: red;  /* Changed color to red */
            margin-top: 1em;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #888888;
            margin-top: 3em;
        }
        .input-section {
            margin-left: 2em;
            width: 90%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">AI-Powered Research Assistant</h1>', unsafe_allow_html=True)

# Research Question Input section with left alignment and full-width style
st.markdown('<h2 class="subheader">Enter Your Research Question or Topic Below</h2>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
research_question = st.text_input("", placeholder="Type your research question or topic here...")
st.markdown('</div>', unsafe_allow_html=True)

if research_question:
    # Define prompt templates for different tasks
    summary_template = """Summarize the following research topic in a detailed manner:
    Topic: {topic}
    Summary:"""

    question_answer_template = """Provide a detailed answer to the following research question:
    Question: {question}
    Answer:"""

    citation_template = """Provide some relevant citations for the following topic:
    Topic: {topic}
    Citations:"""

    related_topics_template = """Suggest some related topics for further exploration on the following topic:
    Topic: {topic}
    Related Topics:"""

    # Create prompt templates using LangChain
    summary_prompt = PromptTemplate(template=summary_template, input_variables=["topic"])
    question_answer_prompt = PromptTemplate(template=question_answer_template, input_variables=["question"])
    citation_prompt = PromptTemplate(template=citation_template, input_variables=["topic"])
    related_topics_prompt = PromptTemplate(template=related_topics_template, input_variables=["topic"])

    # Create LLM Chains using ChatGroq LLM and templates
    summary_chain = LLMChain(llm=llama3_model, prompt=summary_prompt)
    question_answer_chain = LLMChain(llm=llama3_model, prompt=question_answer_prompt)
    citation_chain = LLMChain(llm=llama3_model, prompt=citation_prompt)
    related_topics_chain = LLMChain(llm=llama3_model, prompt=related_topics_prompt)

    # Task selection section
    st.markdown('<h2 class="subheader">Select a Task to Perform</h2>', unsafe_allow_html=True)
    task = st.selectbox("Choose a task:", ["Generate Summary", "Answer Question", "Generate Citations", "Suggest Related Topics"])

    if task == "Generate Summary":
        with st.spinner("Generating summary..."):
            summary = summary_chain.run({"topic": research_question})
            st.subheader("Detailed Summary")
            st.write(summary)

    elif task == "Answer Question":
        with st.spinner("Finding answer..."):
            answer = question_answer_chain.run({"question": research_question})
            st.subheader("Answer to Your Question")
            st.write(answer)

    elif task == "Generate Citations":
        with st.spinner("Generating citations..."):
            citations = citation_chain.run({"topic": research_question})
            st.subheader("Suggested Citations")
            st.write(citations)

    elif task == "Suggest Related Topics":
        with st.spinner("Suggesting related topics..."):
            related_topics = related_topics_chain.run({"topic": research_question})
            st.subheader("Related Topics for Further Exploration")
            st.write(related_topics)
