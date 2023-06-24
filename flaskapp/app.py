from flask import Flask, request, render_template, redirect
from .models import connect
from .__init__ import create_app

app = create_app()

conn = connect()
cursor = conn.cursor()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/word', methods=['GET'])
def get_word():
    query = "SELECT word FROM words"
    cursor.execute(query)
    result = cursor.fetchone()
    word = result[0] if result else None
    return word

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        new_word = request.form['new_Word']
        update_query = "UPDATE words SET word = %s"
        cursor.execute(update_query, (new_word,))
        conn.commit()
        return redirect('/admin')
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)
