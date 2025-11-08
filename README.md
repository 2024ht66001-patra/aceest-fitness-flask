# ACEest Fitness & Gym Tracker

This is a Flask-based application for tracking workouts, including warm-ups, workouts, and cool-downs. Users can log their exercises, view summaries of their sessions, and track their progress over time.

## Features

- Add workout sessions with exercise names and durations.
- View a summary of logged workouts categorized by session type.
- User-friendly interface with input validation.
- Motivational messages based on total workout time.

## Project Structure

```
aceest-fitness-flask
├── app
│   ├── __init__.py         # Initializes the Flask application
│   ├── routes.py           # Defines application routes
│   ├── forms.py            # Contains form classes for user input
│   └── models.py           # Defines data models for workouts
├── templates
│   ├── base.html           # Base HTML template
│   ├── index.html          # Main page for inputting workouts
│   └── summary.html        # Summary page for logged workouts
├── static
│   ├── css
│   │   └── styles.css      # CSS styles for the application
│   └── js
│       └── main.js         # JavaScript for client-side functionality
├── tests
│   └── test_app.py         # Unit tests for the application
├── instance
│   └── config.py           # Instance-specific configuration settings
├── requirements.txt         # Lists project dependencies
├── run.py                   # Entry point to run the Flask application
├── config.py                # Main configuration settings
└── README.md                # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd aceest-fitness-flask
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the interface to log your workouts and view summaries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.