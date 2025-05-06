import google.generativeai as genai
from config import MODEL_NAME

def refine_inputs(user_responses):
    """
    Generate clarifying questions based on user inputs.
    
    Args:
        user_responses (str): User's initial travel preferences
        
    Returns:
        str: Generated clarifying questions
    """
    questions_prompt = f"""
    Based on the user's inputs, generate clarifying questions for:
    - Location (e.g., specific areas, neighborhoods, or regions they want to visit)
    - Interests (e.g., specific types of activities, cultural experiences, or local experiences they're interested in)
    - Additional requirements (e.g., dietary restrictions, mobility concerns, or specific preferences)

    User Inputs:
    {user_responses}
    """
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(questions_prompt)
    return response.text

def generate_itinerary(location, duration, budget, interests, accommodation, additional_notes):
    """
    Generate a detailed travel itinerary based on user preferences.
    
    Args:
        location (str): Travel destination
        duration (int): Trip duration in days
        budget (str): Budget category
        interests (str): User's interests
        accommodation (str): Preferred accommodation type
        additional_notes (str): Any additional requirements
        
    Returns:
        str: Generated travel itinerary
    """
    itinerary_prompt = f"""
    Create a travel itinerary for:
    - Location: {location}
    - Duration: {duration} days
    - Budget: {budget}
    - Interests: {interests}
    - Accommodation Preferences: {accommodation}
    - Additional Notes: {additional_notes}

    Provide a detailed day-by-day itinerary with:
    - Morning, afternoon, and evening activities.
    - Dining recommendations.
    - Suggestions for accommodation.
    """
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(itinerary_prompt)
    return response.text 