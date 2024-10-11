from flask import Flask, render_template, request, redirect, jsonify
from config import get_db_connection

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        category = request.form['category']
        entry_type = request.form['type']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (description, amount, date, category, type)
            VALUES (%s, %s, %s, %s, %s)
        """, (description, amount, date, category, entry_type))
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('add_entry.html')

@app.route('/get-chart-data', methods=['GET'])
def get_chart_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch data grouped by categories for the pie chart
    cursor.execute("""
        SELECT category, 
        SUM(amount) as total_amount
        FROM transactions
     #    WHERE type = 'Expense'  -- Adjust this to 'Income' or 'Expense' if needed
        GROUP BY category
    """)
    
    chart_data = cursor.fetchall()
    conn.close()

    # Prepare the data for the pie chart
    categories = [row['category'] for row in chart_data]
    amounts = [row['total_amount'] for row in chart_data]

    return jsonify({'categories': categories, 'amounts': amounts})


@app.route('/')
def index():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Basic query for transactions, add date filters if present
    query = "SELECT * FROM transactions WHERE 1=1"
    filters = []

    if start_date:
        query += " AND date >= %s"
        filters.append(start_date)
    if end_date:
        query += " AND date <= %s"
        filters.append(end_date)

    cursor.execute(query, filters)
    transactions = cursor.fetchall()

    # Calculate total income, expense, and profit/loss
    cursor.execute("""
        SELECT 
        SUM(CASE WHEN type = 'Income' THEN amount ELSE 0 END) AS total_income,
        SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END) AS total_expense
        FROM transactions WHERE 1=1
    """ + (" AND date >= %s AND date <= %s" if start_date and end_date else ""),
    filters)

    totals = cursor.fetchone()
    total_income = totals['total_income'] or 0
    total_expense = totals['total_expense'] or 0
    profit_loss = total_income - total_expense

    conn.close()

    return render_template('index.html', transactions=transactions, total_income=total_income,
                           total_expense=total_expense, profit_loss=profit_loss)


if __name__ == "__main__":
    app.run(debug=True)
