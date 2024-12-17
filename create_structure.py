import os

# Define the project structure
project_structure = {
    "streamlit_app.py": "Main Streamlit application file.",
    "openai_utils.py": "Wrapper for OpenAI API integration.",
    "code_analysis.py": "Functions for code debugging and optimization.",
    "prompts/": {
        "default.json": "{}",
        "optimization.json": "{}",
        "debugging.json": "{}"
    },
    "saved_snippets/": {},  # Empty folder for code snippets
    "requirements.txt": "# Python dependencies\nstreamlit\nopenai\n",
    "README.md": "# CodeSensei\n\nYour Python coding assistant powered by Streamlit and OpenAI.",
    ".env": "# Add your OpenAI API key here\nOPENAI_API_KEY=your-api-key",
    "assets/": {
        "CodeSensei_logo.png": None  # Placeholder for logo file
    }
}

def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        
        # If content is a dictionary, create a folder
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"Created folder: {path}")
            create_project_structure(path, content)
        else:
            # Create a file with content
            with open(path, "w") as f:
                if content:
                    f.write(content)
                print(f"Created file: {path}")

if __name__ == "__main__":
    base_path = os.getcwd()  # Assumes you are in the CodeSensei directory
    print("Creating CodeSensei project structure...\n")
    create_project_structure(base_path, project_structure)
    print("\nProject structure created successfully!")

