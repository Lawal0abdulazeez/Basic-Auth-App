from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing the frontend to communicate with the backend
CORS(app)

# A simple in-memory "database" to store user data.
# In a real-world application, you would use a proper database like PostgreSQL or MySQL.
# The key is the username, and the value is a dictionary with the password.
users = {}

# --- API Endpoints ---

@app.route('/api/signup', methods=['POST'])
def signup():
    """
    Handles user registration.
    Expects a JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if username in users:
        return jsonify({"message": "Username already exists"}), 409  # 409 Conflict

    # In a real app, you MUST hash the password before storing it.
    # For simplicity, we are storing it in plain text.
    users[username] = {'password': password}
    
    print("Registered users:", users) # For debugging purposes on the server console
    
    return jsonify({"message": "User created successfully"}), 201  # 201 Created

@app.route('/api/login', methods=['POST'])
def login():
    """
    Handles user login.
    Expects a JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and user['password'] == password:
        # Successful login
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        # Invalid credentials
        return jsonify({"message": "Invalid username or password"}), 401 # 401 Unauthorized

# --- Main execution ---
if __name__ == '__main__':
    # Runs the Flask app on http://localhost:5000
    # debug=True allows for auto-reloading when code changes.
    app.run(debug=True)