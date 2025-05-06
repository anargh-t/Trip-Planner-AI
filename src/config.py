import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key from environment variable or use the default
API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyC4RQOc7G96569C-0FowyyzYCG1i-P5uso')

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

# System prompt for the travel assistant
SYSTEM_PROMPT = """
You are an intelligent travel assistant. Your role is to help users create personalized travel itineraries. 
Follow these steps:
1. Ask relevant follow-up questions to gather detailed user input.
2. Refine user inputs to address missing or unclear details.
3. Generate a structured, day-by-day travel itinerary.
Include:
- Attractions and activities aligned with preferences.
- Dining options and local experiences.
- Suggested accommodations and travel tips.
"""

# Model configuration
MODEL_NAME = "gemini-1.5-pro-latest" 