# 🔐 User Authentication Service

This project is focused on building a user authentication service using Python, SQLAlchemy, and Flask. 🚀

## 📋 Requirements

- SQLAlchemy 1.3.x
- pycodestyle 2.5
- bcrypt
- python3 3.7

## 📂 Tasks Overview

### ✅ 1. **User Model**  
Create a SQLAlchemy model `User` with essential attributes:  
`id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

### ✅ 2. **Create User**  
Develop the `add_user` method to add new users to the database securely.

### ✅ 3. **Find User**  
Implement a method to find users based on arbitrary keyword arguments.

### ✅ 4. **Update User**  
Enable updating user details and raise appropriate exceptions if invalid attributes are provided.

### ✅ 5. **Hash Passwords**  
Use `bcrypt` to securely hash user passwords before storing them in the database.

### ✅ 6. **Register User via Flask**  
Create an endpoint to register users, returning a JSON response upon success or failure.

### ✅ 7. **Login System**  
Validate login credentials and manage user sessions using UUIDs. Set session cookies for logged-in users. 🍪

### ✅ 8. **Logout & Session Management**  
Develop methods to manage sessions, allowing users to log out and destroy their sessions.

### ✅ 9. **Profile Management**  
Provide user profile functionality, retrieving the user’s email based on the session ID.

### ✅ 10. **Password Reset**  
Allow users to request password reset tokens and update their password using the generated token.

---

🔗 Ready to explore? Let’s dive into the code and start authenticating! ✨
