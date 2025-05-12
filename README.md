🌤️ Weather App – PyQt5 GUI with Live Weather Data
This is a modern and interactive Weather Application built using Python and PyQt5, designed to fetch and display real-time weather information from the OpenWeatherMap API. With a sleek GUI, the app allows users to input any city name and receive detailed weather data including:

Temperature in Celsius, Fahrenheit, and Kelvin

Current weather condition description

Humidity level

A visual emoji representation of the weather condition (e.g., ☀️ for sunny, ☔ for rain)

The application uses HTTP requests to pull weather data in JSON format and updates the user interface dynamically based on the response. It features a polished design with custom fonts (Lato-black.ttf), hover effects, and proper error handling for invalid inputs.

✨ Key Features
🧭 City Search: Enter any city name to get current weather details.

🌡️ Multi-Unit Temperature Display: Shows temperatures in Celsius, Fahrenheit, and Kelvin.

🌥️ Weather Emoji Indicator: Visual emoji to represent the current weather state (like rain, snow, fog, etc.).

💧 Humidity Level: Displays current humidity percentage.

🎨 Modern PyQt UI: Clean layout with responsive design and custom styling.

❌ Error Handling: Graceful response when an invalid city is entered.

🔤 Custom Font Support: Uses a modern Lato font for UI consistency.

🌐 API Integration: Uses OpenWeatherMap API for up-to-date weather data.

🖼️ GUI Preview
Here's a quick look at the user interface of the weather app:

![image](https://github.com/user-attachments/assets/e43f640c-f93a-45e9-baea-f3c20607fcd9)

🛠️ Technologies Used
Python 3

PyQt5

OpenWeatherMap API

QGridLayout, QLabel, QPushButton, QLineEdit for layout and UI components

QFont, QIcon for custom design and branding

How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/weather-app.git
cd weather-app
Install dependencies:

bash
Copy
Edit
pip install PyQt5 requests
Get your API key from OpenWeatherMap and paste it in the api_key variable in the script.

Run the app:

bash
Copy
Edit
python weather_app.py
