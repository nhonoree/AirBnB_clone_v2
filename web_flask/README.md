# AirBnB Clone - Web Framework

This project is part of the AirBnB clone project. It involves building a Flask web application with various routes.

## Files

- `0-hello_route.py`: Starts a Flask app and displays "Hello HBNB!" at the root route.
- `1-hbnb_route.py`: Extends the app to display "HBNB" at the `/hbnb` route.
- `2-c_route.py`: Displays "C " followed by the value of the `text` variable at `/c/<text>`.
- `3-python_route.py`: Displays "Python " followed by the value of the `text` variable at `/python/<text>`.
- `4-number_route.py`: Displays "n is a number" at `/number/<n>` if `n` is an integer.
- `5-number_template.py`: Displays an HTML page at `/number_template/<n>` if `n` is an integer.

## How to Run

1. Make the scripts executable:
   ```bash
   chmod +x *.py
   ```

2. Run the Flask app:
   ```bash
   python3 0-hello_route.py
   ```

3. Access the app in your browser or using `curl`:
   ```bash
   curl http://0.0.0.0:5000/
   ```
