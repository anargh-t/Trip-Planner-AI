import streamlit as st
from itinerary_generator import refine_inputs, generate_itinerary

def main():
    st.title("🌍 Travel Itinerary Generator ✈️")
    st.write("Let me help you plan the perfect trip! Answer a few questions to get started.")

    # Collect initial user inputs
    with st.form("Travel Planner"):
        location = st.text_input("Where are you planning to travel?", placeholder="E.g., Kochi, Thriuvanathapuram, Chennai")
        duration = st.slider("How many days will your trip last?", min_value=1, max_value=15, value=5)
        budget = st.selectbox("What's your budget?", ["Low", "Moderate", "High"])
        interests = st.text_area("What are your interests? (E.g., culture, adventure, relaxation, food)")
        accommodation = st.selectbox("Preferred accommodation type:", 
                                   ["Luxury", "Budget", "Mid-range", "Unique stays"])
        additional_notes = st.text_area("Any specific requirements or preferences?", 
                                      placeholder="E.g., dietary restrictions, mobility concerns")
        submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        if location and duration and budget and interests and accommodation:
            with st.spinner("Planning your trip..."):
                # Refine Inputs
                user_input_summary = f"""
                Location: {location}
                Duration: {duration} days
                Budget: {budget}
                Interests: {interests}
                Accommodation: {accommodation}
                Additional Notes: {additional_notes}
                """
                clarifications = refine_inputs(user_input_summary)
                st.write("### 🔎 Clarification Questions:")
                st.write(clarifications)

                # Generate Itinerary
                itinerary = generate_itinerary(
                    location, duration, budget, interests, 
                    accommodation, additional_notes
                )
                st.write("### 📝 Your Personalized Itinerary:")
                st.write(itinerary)
        else:
            st.warning("Please fill out all fields to generate your itinerary!")

if __name__ == "__main__":
    main() 