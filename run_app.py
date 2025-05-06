import os
import sys
import streamlit.web.cli as stcli

# Add the src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.append(src_path)

# Run the Streamlit application
if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "src/app.py"]
    sys.exit(stcli.main()) 