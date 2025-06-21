import streamlit as st
from itinerary_generator import refine_inputs, generate_itinerary

def generate_basic_itinerary(location, duration, budget, interests, accommodation, additional_notes):
    """
    Generate a basic itinerary without using the API as a fallback.
    """
    budget_tips = {
        "Low": "Focus on free attractions, public transport, and budget accommodations like hostels or guesthouses.",
        "Moderate": "Mix of paid and free activities, mid-range hotels, and local restaurants.",
        "High": "Premium experiences, luxury accommodations, and fine dining options."
    }
    
    accommodation_tips = {
        "Luxury": "Consider 5-star hotels, boutique resorts, or luxury vacation rentals.",
        "Budget": "Look for hostels, budget hotels, or affordable guesthouses.",
        "Mid-range": "Choose 3-4 star hotels or comfortable vacation rentals.",
        "Unique stays": "Consider boutique hotels, eco-lodges, or themed accommodations."
    }
    
    return f"""
    ## 📝 Basic Travel Itinerary for {location}
    
    ### 🗓️ {duration}-Day Trip Overview
    
    **Destination:** {location}
    **Budget Level:** {budget}
    **Interests:** {interests}
    **Accommodation:** {accommodation}
    
    ### 📋 Daily Structure
    
    **Day 1: Arrival & Orientation**
    - **Morning:** Arrive and check into your accommodation
    - **Afternoon:** Explore the city center and get oriented
    - **Evening:** Enjoy a local dinner and rest
    
    **Day 2-{duration-1}: Main Activities**
    - **Morning:** Visit main attractions and landmarks
    - **Afternoon:** Cultural experiences or outdoor activities
    - **Evening:** Local dining and entertainment
    
    **Day {duration}: Departure**
    - **Morning:** Final exploration or souvenir shopping
    - **Afternoon:** Check out and depart
    
    ### 💡 Recommendations
    
    **Budget Tips:**
    {budget_tips.get(budget, "Plan according to your budget preferences.")}
    
    **Accommodation:**
    {accommodation_tips.get(accommodation, "Choose based on your comfort preferences.")}
    
    **Based on Your Interests ({interests}):**
    - Research specific attractions related to your interests
    - Look for local experiences that match your preferences
    - Consider guided tours or workshops
    
    **Additional Notes:**
    {additional_notes if additional_notes else "No specific requirements noted."}
    
    ### 🔍 Next Steps
    1. Research specific attractions in {location}
    2. Book accommodations in advance
    3. Check local weather and pack accordingly
    4. Research local customs and etiquette
    5. Plan transportation within the city
    
    *This is a basic itinerary template. For more detailed AI-generated recommendations, please try again when the API is available.*
    """

def main():
    st.set_page_config(
        page_title="Trip Planner AI",
        page_icon="🌍",
        layout="wide"
    )
    
    st.title("🌍 Trip Planner AI ✈️")
    st.write("Let me help you plan the perfect trip! Answer a few questions to get started.")

    # Add a toggle for fallback mode
    use_fallback = st.checkbox(
        "Use basic mode (no AI required)", 
        help="Enable this if you're experiencing API issues"
    )

    # Collect initial user inputs
    with st.form("Travel Planner"):
        col1, col2 = st.columns(2)
        
        with col1:
            location = st.text_input(
                "Where are you planning to travel?", 
                placeholder="E.g., Kochi, Thriuvanathapuram, Chennai"
            )
            duration = st.slider(
                "How many days will your trip last?", 
                min_value=1, max_value=15, value=5
            )
            budget = st.selectbox(
                "What's your budget?", 
                ["Low", "Moderate", "High"]
            )
        
        with col2:
            accommodation = st.selectbox(
                "Preferred accommodation type:", 
                ["Luxury", "Budget", "Mid-range", "Unique stays"]
            )
            interests = st.text_area(
                "What are your interests?", 
                placeholder="E.g., culture, adventure, relaxation, food"
            )
            additional_notes = st.text_area(
                "Any specific requirements or preferences?", 
                placeholder="E.g., dietary restrictions, mobility concerns"
            )
        
        submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        if location and duration and budget and interests and accommodation:
            with st.spinner("Planning your trip..."):
                if use_fallback:
                    # Use basic itinerary generation
                    itinerary = generate_basic_itinerary(
                        location, duration, budget, interests, 
                        accommodation, additional_notes
                    )
                    st.write("### 📝 Your Basic Travel Itinerary:")
                    st.markdown(itinerary)
                else:
                    # Use AI-powered generation
                    user_input_summary = f"""
                    Location: {location}
                    Duration: {duration} days
                    Budget: {budget}
                    Interests: {interests}
                    Accommodation: {accommodation}
                    Additional Notes: {additional_notes}
                    """
                    
                    # Generate clarifications
                    clarifications = refine_inputs(user_input_summary)
                    st.write("### 🔎 Clarification Questions:")
                    st.markdown(clarifications)

                    # Generate Itinerary
                    itinerary = generate_itinerary(
                        location, duration, budget, interests, 
                        accommodation, additional_notes
                    )
                    st.write("### 📝 Your Personalized Itinerary:")
                    st.markdown(itinerary)
                    
                    # Add helpful tips if API errors occurred
                    if "API Rate Limit" in itinerary or "Error" in itinerary or "API Key Not Configured" in itinerary:
                        st.info("💡 **Tip:** You can enable 'basic mode' above for a template itinerary that doesn't require the API.")
        else:
            st.warning("Please fill out all fields to generate your itinerary!")

if __name__ == "__main__":
    main() 