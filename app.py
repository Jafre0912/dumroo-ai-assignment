import streamlit as st
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import os
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="Dumroo.ai Admin AI",
    page_icon="🛡️",
    layout="wide"
)

# --- Helper Function for RBAC ---
def get_filtered_dataframe(df, role):
    """Filters the dataframe based on the selected admin role."""
    if role == "Admin - Grade 8":
        return df[df['grade'] == 8].copy()
    elif role == "Admin - Region South":
        return df[df['grade'] == 9].copy() # Assuming 9 is south for this demo
    elif role == "Admin - Region North":
        return df[df['region'] == 'North'].copy()
    elif role == "Super Admin (Platform-Wide)":
        return df.copy() # Super admin sees all
    else:
        return pd.DataFrame() # Return empty if no role

# --- Main Application ---
st.title(" Dumroo.ai Admin Panel AI Query")
st.write("""
This demo shows how an AI assistant can answer questions about student data 
while respecting **Role-Based Access Control (RBAC)**.
""")

# --- 1. Load Data ---
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    st.error("Error: `data.csv` file not found. Please make sure it's in the same directory.")
    st.stop()

# --- 2. API Key and Role Selection (Sidebar) ---
with st.sidebar:
    st.header("Settings")
    
    # Get OpenAI API Key
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    
    # Role-Based Access Control
    admin_role = st.selectbox(
        "Select Your Admin Role:",
        (
            "Admin - Grade 8", 
            "Admin - Region North",
            "Admin - Region South",
            "Super Admin (Platform-Wide)"
        ),
        index=0
    )
    st.info(f"You are logged in as: **{admin_role}**")

# --- 3. Filter Data Based on Role ---
df_filtered = get_filtered_dataframe(df, admin_role)

with st.expander("View Your Accessible Data (Based on Your Role)"):
    st.write(f"The AI can only see and query the following **{len(df_filtered)} rows**:")
    st.dataframe(df_filtered)

# --- 4. AI Query Interface ---
st.header("Ask the AI Assistant")
query = st.text_area("Enter your question in plain English:", 
                     placeholder="e.g., Which students haven't submitted their homework yet?")

if st.button("Get Answer"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key in the sidebar to proceed.")
    elif not query:
        st.warning("Please enter a question to ask.")
    elif df_filtered.empty:
        st.error("No data available for your selected role.")
    else:
        # --- 5. Initialize LangChain Agent ---
        try:
            # Initialize the LLM
            llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0,
                api_key=openai_api_key
            )
            
            # Create the Pandas Agent
            # We pass allow_dangerous_code=True because the agent executes Python code
            agent = create_pandas_dataframe_agent(
                llm,
                df_filtered,
                verbose=True,
                allow_dangerous_code=True, # Required for pandas agent
                handle_parsing_errors=True
            )
            
            # --- 6. Run the Query ---
            with st.spinner("The AI is thinking..."):
                # Add a prefix to guide the AI to only use the provided dataframe
                prefix = """
                You are an AI assistant for an admin panel. 
                You must answer questions based *only* on the dataframe provided.
                Do not make up information.
                When asked for a list of students, show their names.
                """
                
                # Use agent.invoke for the latest LangChain version
                full_query = f"{prefix}\n\nQuestion: {query}"
                response = agent.invoke({"input": full_query})
                
                # Display the answer
                st.subheader("Answer:")
                st.write(response.get('output', 'No answer found.'))

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("Please check your API key and permissions.")

