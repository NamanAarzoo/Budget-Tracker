from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy data to store transactions
transactions = []


@app.route('/')
def home():
    return render_template('index.html', transactions=transactions)


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    transaction_type = request.form.get('type')

    transaction = {
        'amount': amount,
        'category': category,
        'type': transaction_type
    }

    transactions.append(transaction)
    return redirect('/')

# To run the project
# make sure you install flask 'pip3 insall flask'
# run this python file, and visit http://localhost:5000/
if __name__ == '__main__':
    app.run()
