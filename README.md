# Dumroo.ai - AI Admin Query Assignment

This project is a solution for the Dumroo.ai developer assignment. It demonstrates an AI-powered system that allows admins to query a student database using natural language, with a key focus on implementing Role-Based Access Control (RBAC).

The system is built using **Python**, **Streamlit**, **Pandas**, and **LangChain** (with the Pandas DataFrame Agent).

## 🛡️ Key Features

* **Natural Language Queries:** Admins can ask questions like "Which students haven't submitted homework?" instead of writing complex SQL.
* **Role-Based Access Control (RBAC):** The core requirement. The system uses a Streamlit dropdown to simulate an admin logging in. The data (a Pandas DataFrame) is **pre-filtered based on the admin's role** *before* being passed to the AI. This ensures the AI (LangChain agent) literally cannot see or access data outside its permitted scope (e.g., a "Grade 8 Admin" can only see data for Grade 8).
* **Bonus: Interactive UI:** A simple web interface built with **Streamlit** allows for easy interaction and demonstration.
* **Bonus: Modular Code:** The data loading and agent creation logic are separated, making it easy to swap the CSV for a real database connection in the future.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit:** For the interactive web UI
* **Pandas:** For data manipulation
* **LangChain (`langchain-experimental`):** To create the Pandas DataFrame Agent
* **OpenAI:** As the LLM backbone for the agent

## ⚙️ Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [Your-GitHub-Repo-URL]
    cd [repository-folder]
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get an OpenAI API Key:**
    * You will need an API key from [OpenAI](https://platform.openai.com/).
    * The application will ask for this key in the sidebar (it is not stored).

## 🚀 How to Run

1.  Ensure your terminal is in the project's root directory.
2.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3.  A new tab will open in your browser at `http://localhost:8501`.
4.  Enter your OpenAI API Key in the sidebar.
5.  Select an Admin Role to test the RBAC.
6.  Type your query in the text box and press "Get Answer".

## 🧪 Example Queries to Try

* **Role: Admin - Grade 8**
    * "Which students haven't submitted their homework yet?"
    * "What is the average quiz score for my students?"
    * "How many students are in section A?"
    * "List all upcoming quizzes scheduled for next week" (The AI will correctly parse 'next week' from today's date)

* **Role: Admin - Region South**
    * "Show me performance data for Grade 9"
    * "Which students missed their homework?"

* **Role: Super Admin (Platform-Wide)**
    * "How many students are there in total?"
    * "Compare the average quiz score of Grade 8 and Grade 10"
    * "List all students from the West region."