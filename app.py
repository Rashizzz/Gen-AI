from langchain.llms import Cohere
import streamlit as st
# CohereAPIError is no longer directly imported from cohere
# It's generally not needed to be explicitly caught for basic use.
# from cohere import CohereAPIError

# Directly set the API key (be cautious in production environments)
COHERE_API_KEY = "qYHxQkFz5RuqGoviOoaSQEFMb3zsZFnpCJV8WGKU" # Replace with your actual API key

def get_cohere_response(question):
    """
    Retrieves a response from the Cohere language model.

    Args:
        question (str): The question to ask the model.

    Returns:
        str: The model's response, or an error message if the request fails.
    """
    try:
        llm = Cohere(model="command", temperature=0.5, cohere_api_key=COHERE_API_KEY) # Changed model name
        response = llm(question)
        return response
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input:")  # Changed variable name to avoid shadowing
submit = st.button("Ask the question")

if submit and input_text:
    response = get_cohere_response(input_text)
    st.subheader("The Response is")
    st.write(response)
