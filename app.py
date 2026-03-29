from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)
database.connect_db()

@app.route('/')
def index():
    query = request.args.get('search')
    books = database.get_books(query)
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    t = request.form.get('title')
    a = request.form.get('author')
    if t and a:
        database.add_book(t, a)
    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete(book_id):
    database.delete_book(book_id)
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    database.reset_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)