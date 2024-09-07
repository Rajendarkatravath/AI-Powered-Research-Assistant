# Project Title

AI-Powered Research Assistant
## Overview

The **AI-Powered Research Assistant** is a web-based application built with Streamlit that leverages advanced language models like Llama 3 to assist users in exploring research topics. Users can input a research question or topic, and the assistant can generate summaries, answer questions, provide relevant citations, and suggest related topics for further exploration. The assistant is powered by the LangChain library, the Llama 3 model via the Groq API, and integrated into a Streamlit interface.

## Features

- **Generate Summary**: Provides a detailed summary of the entered research topic.
- **Answer Question**: Answers specific research questions with detailed explanations.
- **Generate Citations**: Suggests relevant citations for the provided topic.
- **Suggest Related Topics**: Recommends related topics for further exploration.
- **User-Friendly Interface**: Simple and attractive UI built with Streamlit.

## Installation

### Prerequisites

- **Python 3.12.4**: Make sure you have Python 3.12.4 installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Set Up a Virtual Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-powered-research-assistant.git
   cd ai-powered-research-assistant

2.Create a Virtual Environment: Create a virtual environment named venv for the project:
```bash
  python3.12 -m venv venv
3.Activate the Virtual Environment:
On Windows:
```bash
venv\Scripts\activate

On macOS and Linux:
```bash
source venv/bin/activate

4.Install Dependencies: Install all required packages using pip:
```bash
pip install -r requirements.txt

Environment Variables
To access the Llama 3 model via the Groq API, you need to set up your API key. Create a .env file in the root directory of the project and add the following:
```bash
GROQ_API_KEY=your_groq_api_key_here

Replace your_groq_api_key_here with your actual Groq API key.

##Usage
Run the Streamlit Application: Start the Streamlit server and open the application in your default web browser:
```bash
streamlit run app.py

2.Interact with the Application:

Enter a research question or topic in the input field.
Choose a task (Generate Summary, Answer Question, Generate Citations, or Suggest Related Topics).
View the results directly on the page.

File Structure

.
├── app.py                    # Main Streamlit application file
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
├── .env.example              # Example environment variables file
├── venv/                     # Virtual environment directory
└── ... (other files and folders as needed)


