from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Konfigurasi ke database
app.secret_key = 'hawq'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hawq'
mysql = MySQL(app)

@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('Landingpage.html')
    flash('Harap Login Terlebih Dahulu','danger')
    return redirect(url_for('login'))

@app.route('/login', methods=('GET','POST')) #Buat Login
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # validasi data
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE email=%s',(email, ))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal Username Tidak ditemukan','error')
        elif not check_password_hash(akun[3], password):
            flash('Login Gagal check password anda','error')
        else:
            session['loggedin'] = True
            session['username'] = akun[1]
            return redirect(url_for('index'))
    return render_template('Login.html')


@app.route('/register', methods=('GET','POST')) #Buat Register
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        no_handphone = request.form['no_handphone']
        
        # validasi username dan email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username=%s OR email=%s', (username, email))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s )', (username, email, generate_password_hash (password), no_handphone))
            mysql.connection.commit()
            flash('Berhasil Registrasi', 'success')
        else:
            flash('username atau email sudah ada', 'warning')
            
    return render_template('Registrasi.html')

# logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)