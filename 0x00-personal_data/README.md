# 🔒 **0x00. Personal data Project**


---

## 🚀 **Tasks Overview**

### 0. Regex-ing 🧑‍💻
**File:** `filtered_logger.py`

The goal here is to implement a **regex-based data obfuscation** function called `filter_datum` that meets the following requirements:

- **Arguments**:
  - `fields`: List of field names that need obfuscation.
  - `redaction`: The string that replaces sensitive data (e.g., `"***"`).
  - `message`: The log entry to process.
  - `separator`: Character that separates fields in the log (`message`).
- **Functionality**:
  - Use `re.sub` to mask sensitive fields in a single, powerful regex operation.
  - **Pro tip**: Keep this function under **5 lines** for performance and simplicity. 💡

---

### 1. Log Formatter 📝
**File:** `filtered_logger.py`

Build a **custom logging formatter** with the `RedactingFormatter` class that ensures sensitive fields are dynamically redacted in log records.

- **Key Elements**:
  - A predefined redaction string: `"***"`.
  - A clear, structured log format: `"[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"`.
  - Accept a list of fields to redact dynamically during the log formatting process.
  - **Best Practice**: Use the `filter_datum` function to streamline log filtering with minimal code (keep the method under **5 lines**).

**Note:** Avoid manually extrapolating format strings—**automate** filtering with smart regex.

---

### 2. Create a Logger 🔧
**File:** `filtered_logger.py`

Develop a logging system by creating the `get_logger` function that will:

- Return a **custom logger** named `"user_data"`, preconfigured for:
  - Logging up to **INFO level**.
  - Not propagating log messages to parent loggers.
  - A `StreamHandler` configured with the `RedactingFormatter`, which ensures sensitive fields from the `PII_FIELDS` tuple (like `name`, `email`, `phone`, `ssn`, `password`) are always redacted.
- **Note**: This logger is optimized for handling **Personal Identifiable Information (PII)**, making it essential for secure applications.

**PII_FIELDS** = `('name', 'email', 'phone', 'ssn', 'password')` ⚠️

---

### 3. Connect to a Secure Database 🛡️
**File:** `filtered_logger.py`

To securely interact with the database, you'll need to build a `get_db` function that connects using **environment variables** for credentials—no hardcoded secrets!

- **Env Variables**:
  - `PERSONAL_DATA_DB_USERNAME` (default: `"root"`)
  - `PERSONAL_DATA_DB_PASSWORD` (default: `""`)
  - `PERSONAL_DATA_DB_HOST` (default: `"localhost"`)
  - `PERSONAL_DATA_DB_NAME`
- **Implementation**:
  - Leverage **os.environ** to securely access environment variables.
  - Connect to the **MySQL** database using `mysql-connector-python` (`pip install mysql-connector-python`).

**Security Tip**: Never store database credentials in code! Always use environment variables to protect sensitive information. 🔐

---

### 4. Read and Filter Data 📄
**File:** `filtered_logger.py`

Create a `main` function that will:

1. Use `get_db` to establish a secure connection with the database.
2. Retrieve rows from the **users** table and log each row in a filtered, safe format.
3. Each log entry should look like this:
    ```log
    [HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
    ```
4. Fields to filter: `name`, `email`, `phone`, `ssn`, and `password`.

Ensure that this script only runs when executed directly.

---

### 5. Password Encryption 🛡️
**File:** `encrypt_password.py`

Password security is crucial! Implement `hash_password` to securely hash user passwords:

- **Hashing**: Use **bcrypt** to apply strong, salted hashing.
- **Output**: A salted, hashed password as a byte string.
- **Usage**: `bcrypt.hashpw()` ensures passwords are stored securely, preventing plaintext vulnerabilities.

💡 **Reminder**: **Never store passwords in plain text**. Proper hashing is a must for any modern application!

---

### 6. Password Validation 🔍
**File:** `app.py`

Implement `is_valid`, a function that:

- **Verifies** if a provided password matches the stored, hashed password using **bcrypt**.
- **Returns** `True` if the passwords match, otherwise `False`.

This ensures secure, validated authentication in your app. 🔑

---

🔐 **Secure Practices**:
- **Environment variables** for sensitive data.
- **Strong encryption** for passwords.
- **Regex filtering** for log safety.
- **Minimal logging exposure** for personal data.

Embrace security—let's keep personal data safe! 🌐✨
