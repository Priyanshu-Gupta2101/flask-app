from flask import Blueprint, request, render_template, redirect
import mysql.connector
from .models import connect

conn = connect()[0]
cursor = connect()[1]

main = Blueprint("main", __name__)

@main.route('/')
def main():
    return render_template('index.html')

@main.route('/api/word', methods=['GET'])
def get_word():
    query = "SELECT word FROM words"
    cursor.execute(query)
    result = cursor.fetchone()
    word = result[0] if result else None
    return word

@main.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        new_word = request.form['new_Word']
        update_query = "UPDATE words SET word = %s"
        cursor.execute(update_query, (new_word,))
        conn.commit()
        return redirect('/admin')
    return render_template('admin.html')
