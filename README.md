# 🔐 Simple Full-Stack User Authentication App

This is a basic, full-stack web application that demonstrates a fundamental **user authentication system**. It illustrates how a frontend client communicates with a backend server to manage user registration, login, and access to protected pages.

---

## 🌐 Overview

This application includes three primary pages:

- **Sign Up Page**: Allows new users to create an account.
- **Sign In Page**: Allows existing users to log in.
- **Welcome Page**: A *protected* page accessible only to logged-in users.

The core purpose is to show how the frontend interacts with the backend via a RESTful API and how login state is managed on the client using `localStorage`.

---

## 🛠️ Technology Stack

### Frontend (Client)
- **HTML5**: Structure of the web pages.
- **CSS3**: Styling and layout.
- **Vanilla JavaScript**:
  - Captures form input.
  - Handles UI events.
  - Makes API calls via `fetch()`.
  - Stores user login state with `localStorage`.

### Backend (Server)
- **Python**: Language used for backend logic.
- **Flask**: Lightweight web framework for building the RESTful API.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing between frontend and backend.

---

## 🔁 Application Flow

### 1. User Sign Up

- **User Action**: Fills out the sign-up form and clicks "Sign Up".
- **Frontend**: 
  - Prevents default form submission.
  - Captures input values.
  - Sends a `POST` request to `http://127.0.0.1:5000/api/signup`.
- **Backend**:
  - Parses JSON input.
  - Checks if the username exists.
  - Responds accordingly:
    - `201 Created` – User created successfully.
    - `409 Conflict` – Username already exists.
- **Frontend Response**:
  - Displays success or error message to the user.

### 2. User Sign In

- **User Action**: Fills in the form and clicks "Sign In".
- **Frontend**:
  - Sends a `POST` request to `/api/login` with credentials.
- **Backend**:
  - Validates credentials.
  - Responds with:
    - `200 OK` – Login successful (`{ "message": "Login successful", "username": "user123" }`).
    - `401 Unauthorized` – Invalid credentials.
- **Frontend**:
  - Stores username in `localStorage`.
  - Redirects to `welcome.html`.

### 3. Accessing the Protected Welcome Page

- **On Page Load (welcome.html)**:
  - JavaScript checks `localStorage` for a username.
  - If found:
    - Displays welcome message (e.g., "Welcome, user123!").
  - If not:
    - Redirects user to `signin.html`.

### 4. Logging Out

- **User Action**: Clicks "Logout".
- **Frontend**:
  - Removes username from `localStorage`.
  - Redirects to `signin.html`.

