import streamlit as st
from openai_utils import generate_code, explain_code, debug_code, optimize_code

# Streamlit page config
st.set_page_config(page_title="CodeSensei", layout="wide")
st.title("👨‍🏫 CodeSensei")
st.subheader("Your Python Coding Assistant")
st.write("""
Welcome to **CodeSensei**, your friendly Python programming assistant powered by OpenAI and Streamlit.
Use this app to generate, debug, explain, or optimize Python code effortlessly.
""")

# Tabs for the main functionalities
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Code Generation", "🧐 Code Explanation", "🐛 Debugging Assistance", "⚡ Code Optimization"])

# Tab 1: Code Generation
with tab1:
    st.header("🚀 Code Generation")
    prompt = st.text_area("Enter your prompt for code generation:", placeholder="e.g., Write a function to calculate factorial.")
    if st.button("Generate Code"):
        if prompt.strip():
            st.info("Generating code... Please wait.")
            result = generate_code(prompt)
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
