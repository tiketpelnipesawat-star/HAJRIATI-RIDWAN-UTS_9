from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data sementara (Database simulasi)
users = [
    {"username": "budi", "role": "dosen"},
    {"username": "andi", "role": "mahasiswa"},
    {"username": "rian", "role": "dosen"},
    {"username": "admin", "role": "admin"},
    {"username": "ani", "role": "mahasiswa"},
]

@app.route('/')
def home():
    return render_template('home.html', users=users)

@app.route('/tambah', methods=['POST'])
def tambah_user():
    username = request.form.get('username')
    role = request.form.get('role')
    if username:
        users.append({"username": username, "role": role.lower()})
    return redirect(url_for('home'))

@app.route('/hapus/<int:index>')
def hapus_user(index):
    # index - 1 karena di tampilan kita mulai dari angka 1
    if 0 <= index - 1 < len(users):
        users.pop(index - 1)
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulasi login langsung ke dashboard ani
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/mahasiswa/dashboard')
def dashboard():
    return render_template('dashboard.html', username="ani")

if __name__ == '__main__':
    app.run(debug=True)