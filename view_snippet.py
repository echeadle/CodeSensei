import os
import json

def pretty_print_snippet(file_path):
    """
    Pretty prints the contents of a JSON file containing a code snippet.

    Args:
        file_path (str): Path to the JSON file containing the snippet.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    try:
        # Open and load the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Extract name and content fields
        name = data.get("name", "Unnamed Snippet")
        content = data.get("content", "")
        
        print(f"\n{'='*40}")
        print(f"📄 Snippet Name: {name}")
        print(f"{'='*40}\n")
        print("🧾 Code Content:\n")
        print(content)
        print(f"\n{'='*40}\n")
    
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file. {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Define the directory where snippets are stored
    SNIPPETS_DIR = "saved_snippets"
    
    # List available snippet files
    print("Available Snippet Files:")
    if not os.path.exists(SNIPPETS_DIR):
        print(f"Error: Directory '{SNIPPETS_DIR}' does not exist.")
        exit(1)
    
    files = [f for f in os.listdir(SNIPPETS_DIR) if f.endswith(".json")]
    if not files:
        print("No snippet files found.")
        exit(0)
    
    for i, file in enumerate(files):
        print(f"[{i+1}] {file}")
    
    # Prompt user to select a file
    try:
        choice = int(input("\nEnter the number of the file to display: "))
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            file_path = os.path.join(SNIPPETS_DIR, selected_file)
            
            # Pretty print the selected snippet
            pretty_print_snippet(file_path)
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
