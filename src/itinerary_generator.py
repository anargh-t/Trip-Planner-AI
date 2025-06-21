import google.generativeai as genai
from config import MODEL_NAME, API_KEY
import time
import random

def refine_inputs(user_responses):
    """
    Generate clarifying questions based on user inputs.
    
    Args:
        user_responses (str): User's initial travel preferences
        
    Returns:
        str: Generated clarifying questions or error message
    """
    if not API_KEY:
        return """
        ⚠️ **API Key Not Configured**
        
        Please add your Google Gemini API key to the .env file:
        GOOGLE_API_KEY=your_api_key_here
        
        Get your API key from: https://makersuite.google.com/app/apikey
        """
    
    questions_prompt = f"""
    Based on the user's inputs, generate clarifying questions for:
    - Location (e.g., specific areas, neighborhoods, or regions they want to visit)
    - Interests (e.g., specific types of activities, cultural experiences, or local experiences they're interested in)
    - Additional requirements (e.g., dietary restrictions, mobility concerns, or specific preferences)

    User Inputs:
    {user_responses}
    """
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(questions_prompt)
        return response.text
    except Exception as e:
        error_msg = str(e)
        
        if "quota" in error_msg.lower() or "429" in error_msg or "rate" in error_msg.lower():
            return """
            ⚠️ **API Rate Limit Reached**
            
            We've hit the Google Gemini API rate limits. This can happen when:
            - Too many requests are made in a short time
            - Daily quota is exceeded
            - Free tier limits are reached
            
            **Solutions:**
            1. **Wait a few minutes** and try again
            2. **Check your Google AI Studio quota** at https://makersuite.google.com/app/apikey
            3. **Upgrade to a paid plan** if you need more requests
            4. **Use a different API key** if you have one
            
            For now, here are some general questions to help plan your trip:
            - What specific areas or neighborhoods interest you most?
            - Are there any cultural experiences you'd like to include?
            - Do you have any dietary restrictions or mobility concerns?
            - What's your preferred travel pace (relaxed, moderate, or fast-paced)?
            """
        else:
            return f"""
            ⚠️ **Error Generating Questions**
            
            An unexpected error occurred: {error_msg}
            
            Please try again in a few moments, or contact support if the issue persists.
            """

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
        str: Generated travel itinerary or error message
    """
    if not API_KEY:
        return """
        ⚠️ **API Key Not Configured**
        
        Please add your Google Gemini API key to the .env file:
        GOOGLE_API_KEY=your_api_key_here
        
        Get your API key from: https://makersuite.google.com/app/apikey
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
    
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(itinerary_prompt)
            return response.text
        except Exception as e:
            error_msg = str(e)
            
            if "quota" in error_msg.lower() or "429" in error_msg or "rate" in error_msg.lower():
                if attempt < max_retries - 1:
                    # Add exponential backoff with jitter
                    wait_time = retry_delay * (2 ** attempt) + random.uniform(0, 1)
                    time.sleep(wait_time)
                    continue
                else:
                    return f"""
                    ⚠️ **API Rate Limit Reached**
                    
                    We've hit the Google Gemini API rate limits after {max_retries} attempts.
                    
                    **Immediate Solutions:**
                    1. **Wait 1-2 minutes** and try again
                    2. **Check your API quota** at https://makersuite.google.com/app/apikey
                    3. **Consider upgrading** to a paid plan for higher limits
                    
                    **Alternative:**
                    You can manually plan your trip using these general guidelines for {location}:
                    
                    **Day 1-{duration} Itinerary Structure:**
                    - **Morning:** Explore local attractions and landmarks
                    - **Afternoon:** Cultural experiences or outdoor activities
                    - **Evening:** Local dining and entertainment
                    
                    **Budget Tips for {budget} travel:**
                    - Research free attractions and walking tours
                    - Look for local markets and street food
                    - Consider public transportation
                    - Book accommodations in advance for better rates
                    
                    **Based on your interests:** {interests}
                    Focus on activities that match these preferences.
                    """
            else:
                return f"""
                ⚠️ **Error Generating Itinerary**
                
                An unexpected error occurred: {error_msg}
                
                Please try again in a few moments, or contact support if the issue persists.
                """
    
    return "Failed to generate itinerary after multiple attempts." 