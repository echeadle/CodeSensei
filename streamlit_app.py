import streamlit as st
import json
import os
from openai_utils import generate_code, explain_code, debug_code, optimize_code

# Directory to store code snippets
SNIPPETS_DIR = "saved_snippets"

# Ensure the saved_snippets directory exists
os.makedirs(SNIPPETS_DIR, exist_ok=True)

def save_code_snippet(name, content):
    """
    Save a code snippet as an individual JSON file named <name>.json.
    """
    file_path = os.path.join(SNIPPETS_DIR, f"{name}.json")
    with open(file_path, "w") as f:
        json.dump({"name": name, "content": content}, f, indent=4)

def load_snippet_files():
    """
    List all snippet files in the saved_snippets directory.
    """
    files = [f for f in os.listdir(SNIPPETS_DIR) if f.endswith(".json")]
    return files

def load_snippet_content(file_name):
    """
    Load the content of a selected snippet JSON file.
    """
    file_path = os.path.join(SNIPPETS_DIR, file_name)
    with open(file_path, "r") as f:
        snippet = json.load(f)
    return snippet.get("content", "")

# Streamlit page config
st.set_page_config(page_title="CodeSensei", layout="wide")
st.title("👨‍🏫 CodeSensei")
st.subheader("Your Python Coding Assistant")
st.write("""
Welcome to **CodeSensei**, your friendly Python programming assistant powered by OpenAI and Streamlit.
Use this app to generate, debug, explain, or optimize Python code effortlessly.
""")

# Tabs for main functionalities
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Code Generation", "🧐 Code Explanation", "🐛 Debugging Assistance", "⚡ Code Optimization"])

# Sidebar for saving/loading snippets
st.sidebar.header("💾 Code Snippet Manager")
snippet_name = st.sidebar.text_input("Snippet File Name", placeholder="Enter a name for your snippet (no spaces)")
if st.sidebar.button("Save Snippet"):
    if snippet_name:
        current_code = st.session_state.get("current_code", "")
        if current_code:
            save_code_snippet(snippet_name, current_code)
            st.sidebar.success(f"Snippet '{snippet_name}.json' saved successfully!")
        else:
            st.sidebar.warning("No code to save. Generate or paste code first.")
    else:
        st.sidebar.warning("Please enter a snippet name.")

# Load and display saved snippets
st.sidebar.subheader("📂 Load Saved Snippets")
snippet_files = load_snippet_files()
selected_file = st.sidebar.selectbox("Select a snippet to load:", [""] + snippet_files)
if selected_file:
    if st.sidebar.button("Load Snippet"):
        snippet_content = load_snippet_content(selected_file)
        st.session_state["current_code"] = snippet_content
        st.sidebar.info(f"Loaded snippet from '{selected_file}'")
        st.code(snippet_content, language="python")

# Tab 1: Code Generation
with tab1:
    st.header("🚀 Code Generation")
    prompt = st.text_area("Enter your prompt for code generation:", placeholder="e.g., Write a function to calculate factorial.")
    if st.button("Generate Code"):
        if prompt.strip():
            st.info("Generating code... Please wait.")
            result = generate_code(prompt)
            st.session_state["current_code"] = result  # Store generated code
            st.code(result, language="python")
        else:
            st.warning("Please enter a prompt.")

# Tab 2: Code Explanation
with tab2:
    st.header("🧐 Code Explanation")
    code_to_explain = st.text_area("Paste your Python code here:", placeholder="e.g., def add(a, b): return a + b")
    if st.button("Explain Code"):
        if code_to_explain.strip():
            st.info("Explaining the code... Please wait.")
            explanation = explain_code(code_to_explain)
            st.write("### Explanation:")
            st.write(explanation)
        else:
            st.warning("Please paste your Python code.")

# Tab 3: Debugging Assistance
with tab3:
    st.header("🐛 Debugging Assistance")
    code_to_debug = st.text_area("Paste your Python code here:", placeholder="e.g., def divide(a, b): return a / b")
    if st.button("Debug Code"):
        if code_to_debug.strip():
            st.info("Analyzing code for errors... Please wait.")
            debug_suggestions = debug_code(code_to_debug)
            st.write("### Debugging Suggestions:")
            st.write(debug_suggestions)
        else:
            st.warning("Please paste your Python code.")

# Tab 4: Code Optimization
with tab4:
    st.header("⚡ Code Optimization")
    code_to_optimize = st.text_area("Paste your Python code here:", placeholder="e.g., for i in range(len(arr)): print(arr[i])")
    if st.button("Optimize Code"):
        if code_to_optimize.strip():
            st.info("Optimizing code... Please wait.")
            optimization = optimize_code(code_to_optimize)
            st.write("### Optimization Suggestions:")
            st.write(optimization)
        else:
            st.warning("Please paste your Python code.")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Developed with ❤️ using [Streamlit](https://streamlit.io) and [OpenAI](https://openai.com).")
