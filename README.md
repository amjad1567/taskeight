Here's the updated **README** file with `register.py` changed to `app.py`:

---

# Task Eight - HTML and Python Registration Form

## Project Overview

This project contains two tasks:

1. **HTML Registration Form**: A user-friendly form for collecting registration details such as full name, email, password, gender, and date of birth.
2. **Python Script**: A Python script that handles user input directly via the terminal, validates input data using regular expressions for email validation and checks for matching passwords.

### Contents

- `index.html`: The registration form implemented using HTML and styled with CSS.
- `app.py`: The Python script to process user input. It validates input provided directly from the terminal and displays a success message upon successful registration.
- `styles.css`: The CSS file used to style the registration form.

## Prerequisites

- Python 3.x

### Installing VSCodium

To edit and work with these files, VSCodium was used for syntax highlighting and editing. You can install VSCodium on **Kali Linux** by running:

```bash
sudo apt install -y codium
```

For more details, visit: [VSCodium Official Site](https://vscodium.com/).

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/taskeight.git
cd taskeight
```

### Step 2: Run the Python Script

The registration process is handled entirely within the terminal. To run the script:

```bash
python app.py
```

### Step 3: Validate the HTML File

Open the `index.html` file in **VSCodium**. Use the Emmet extension to improve the structure and validation of the HTML code.

### Running the Python Script Without `python` Command

After adding the shebang line (`#!/usr/bin/env python3`) to the script, make the Python script executable with the following command (if running on a Linux-based OS):

```bash
chmod +x app.py
```

Now, you can run the script directly using:
```bash
./app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--
