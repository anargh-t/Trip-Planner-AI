# Trip Planner AI 🌍✈️

An intelligent travel planning assistant that helps users create personalized travel itineraries using Google's Gemini AI.

## Features

- Interactive web interface built with Streamlit
- AI-powered itinerary generation
- Personalized travel recommendations
- Detailed day-by-day planning
- Accommodation and dining suggestions
- Budget-aware recommendations

## Prerequisites

- Python 3.8 or higher (3.8.x, 3.9.x, 3.10.x, or 3.11.x recommended)
- Google Gemini API key (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anargh-t/Trip-Planner-AI.git
cd Trip-Planner-AI
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your Google API key:
   - Create a `.env` file in the project root
   - Add your API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   - Or set it as an environment variable:
   ```bash
   # On Windows
   set GOOGLE_API_KEY=your_api_key_here
   
   # On Linux/Mac
   export GOOGLE_API_KEY=your_api_key_here
   ```

## Project Structure

```
Trip-Planner-AI/
├── src/
│   ├── __init__.py
│   ├── app.py              # Main Streamlit application
│   ├── config.py           # Configuration and constants
│   └── itinerary_generator.py  # Itinerary generation logic
├── run_app.py             # Application entry point
├── .env                    # Environment variables (create this file)
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Usage

1. Start the Streamlit application:
```bash
python run_app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Fill in the travel details:
   - Destination
   - Trip duration
   - Budget
   - Interests
   - Accommodation preferences
   - Additional requirements

4. Click "Generate Itinerary" to get your personalized travel plan

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for powering the itinerary generation
- Streamlit for the web interface framework

