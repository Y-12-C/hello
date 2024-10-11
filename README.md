
# Expense Tracker Application

This is a simple Expense Tracker web application where users can log their income and expenses, generate reports, and visualize data using charts. The project uses **Flask** (Python web framework), **Bootstrap 5** (for frontend design), and **MySQL** (for storing the data).

## Features

- Users can log their **income** and **expenses**.
- View transaction history with details like amount, category, and type.
- Generate and visualize data (charts) to track **spending patterns** over time.

## Prerequisites

Before running this application, ensure you have the following installed:

1. Python 3.x
2. MySQL Database
3. pip (Python package manager)

## Installation

Follow the steps below to set up the **Expense Tracker** application on your local machine for various platforms.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### Step 2: Set Up a Virtual Environment (Recommended for Isolation)

#### **For Windows:**

1. Open a command prompt or PowerShell in the project directory.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

#### **For macOS/Linux:**

1. Open a terminal in the project directory.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

### Step 3: Install Dependencies

Once the virtual environment is activated, install the necessary Python packages (Flask, MySQL connector, and any other dependencies) using `pip`:

```bash
pip install Flask mysql-connector-python
```

For Windows, ensure Python is added to your system's PATH. You may need to use `pip3` instead of `pip` on macOS/Linux depending on your Python setup.

### Step 4: Set Up MySQL Database

#### **MySQL Installation**:

- **Windows**: Download and install MySQL from the [official website](https://dev.mysql.com/downloads/installer/). During installation, ensure that MySQL Workbench and MySQL Server are selected.
  
- **macOS**: Install MySQL using Homebrew:

  ```bash
  brew install mysql
  ```

  Then, start MySQL:

  ```bash
  brew services start mysql
  ```

- **Linux**: Install MySQL using your package manager:

  ```bash
  sudo apt update
  sudo apt install mysql-server
  ```

  Start the MySQL service:

  ```bash
  sudo systemctl start mysql
  ```

#### **Create Database and Tables**:

1. After MySQL is installed and running, access the MySQL CLI by running:

   ```bash
   mysql -u root -p
   ```

2. Create the **expense_tracker** database:

   ```sql
   CREATE DATABASE expense_tracker;
   ```

3. Create the **transactions** table:

   ```sql
   CREATE TABLE transactions (
       id INT AUTO_INCREMENT PRIMARY KEY,
       description VARCHAR(255) NOT NULL,
       amount DECIMAL(10, 2) NOT NULL,
       date DATE NOT NULL,
       category VARCHAR(50) NOT NULL,
       type ENUM('Income', 'Expense') NOT NULL
   );
   ```

### Step 5: Configure MySQL in Flask

In your `app.py`, update the MySQL connection settings with your username, password, and database:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',      # Replace with your MySQL username
    password='your_password',  # Replace with your MySQL password
    database='expense_tracker'
)
```

### Step 6: Running the Flask Application

Once everything is set up, you can start the Flask server:

```bash
python app.py
```

For **macOS/Linux**, if you're using Python 3, the command may be:

```bash
python3 app.py
```

Once the server is running, the application will be available at `http://127.0.0.1:5000/`.

### Step 7: Access the Application

- Open a web browser and go to `http://127.0.0.1:5000/`.
- You should be able to view and use the Expense Tracker application, log transactions, and visualize data.

## Application Structure

```bash
expense-tracker/
│
├── static/
│   ├── style.css         # Custom CSS file
│   ├── charts.js         # Chart.js logic for generating charts
│
├── templates/
│   ├── index.html        # Main page for viewing transactions and charts
│   ├── add_entry.html    # Form for adding income or expense
│
├── app.py                # Flask application
├── README.md             # Documentation
└── requirements.txt      # List of dependencies (optional)
```

## Technologies Used

- **Flask** - Backend framework to handle requests and manage the application.
- **Bootstrap 5** - Frontend framework for styling and responsive design.
- **Chart.js** - Library used to generate visual charts.
- **MySQL** - Relational database to store the transaction details.
- **Python** - Backend language to handle server-side logic.

## Future Improvements

- Add **user authentication** for multiple users.
- Enhance **reporting features** to allow filtering by date range and categories.
- Implement **export options** (e.g., CSV, PDF) for the transaction data.

## License

This project is licensed under the MIT License.
