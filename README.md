## Dumroo.ai - Admin AI Query System
This is my solution for the Dumroo.ai developer assignment.
It’s a simple AI-powered web app where different admins can query a student dataset using plain English questions.
The main focus of the project is to implement Role-Based Access Control (RBAC) so that each admin only sees the data they’re allowed to access.

# Overview
The app uses Streamlit for the UI and LangChain (with a Pandas DataFrame Agent) to connect the data with an OpenAI model.
Admins can ask questions like:
“Which students haven’t submitted their homework yet?”
“What’s the average quiz score for Grade 8?”
The app filters the dataset before sending it to the AI — meaning each role only interacts with its own subset of data.
For example, a “Grade 8 Admin” will never see other grades’ data, even indirectly through the model.

# Tech Stack
Python 3.10+
Streamlit – for building the interactive dashboard
Pandas – for handling and filtering data
LangChain (Experimental) – for connecting the AI model to the DataFrame
OpenAI API – as the language model backend

# Key Highlights
RBAC in Action: Each role (Grade 8 Admin, Regional Admin, Super Admin, etc.) only sees specific filtered data.
Natural Language Queries: Instead of writing SQL or pandas code, admins can just ask questions in plain English.
Interactive UI: Clean, minimal Streamlit interface that’s easy to test and demonstrate.
Modular Design: The logic for loading data, filtering by role, and querying via AI is clearly separated — so it’s easy to extend or connect to a real database later.

# Setup Guide
1) Clone the repo
git clone https://github.com/<your-username>/dumroo-ai-assignment
cd dumroo-ai-assignment

2) Create and activate a virtual environment
python -m venv venv

2) a. for Windows
venv\Scripts\activate

2) b. for macOS/Linux
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Run the Streamlit app
streamlit run app.py
Open your browser at http://localhost:8501

# How It Works:
Enter your OpenAI API key in the sidebar (the app doesn’t store it).
Choose your Admin Role — this determines which part of the dataset you can see.
Type a question in the input box (e.g., “Show all Grade 8 students with pending homework”).
The AI will answer based only on your filtered dataset.

# Example Queries:-
Grade 8 Admin:
“Who hasn’t submitted homework yet?”
“Average quiz score for my students?”
“How many students are in Section A?”

# Region South Admin:
“Show me the Grade 9 performance data.”
“List students who missed assignments.”

# Super Admin:
“Total number of students?”
“Compare quiz averages between Grade 8 and Grade 10.”
“List all students from the North region.”

# Notes:
The dataset used here (data.csv) is mock data for demonstration purposes.
The app is designed to easily connect to a real database or API later.
The .env file (for your OpenAI key) should not be committed — it’s already in .gitignore.