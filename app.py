from flask import Flask,render_template, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Ruta de inicio de sesión
def login():
    if request.method == 'POST':
        if request.form['usuario'] == '123' and request.form['password'] == '123':
            return redirect(url_for('home'))
        else:
            # Si las credenciales son incorrectas, vuelve a mostrar 'login.html'
            # con un mensaje de error.
            return render_template('login.html', error='Usuario o contraseña incorrectos.')
    # Si es una petición GET, simplemente renderiza 'login.html'
    return render_template('login.html')

@app.route('/home')
def home():
    # Esta función maneja la visualización de 'home.html'
    return render_template('home.html')

@app.route('/workspace')
def workspace():
    return render_template('workspace.html')


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/trabajo')
def workspace():
    # Creas un DataFrame de pandas con tus tareas aquí
    df = pd.DataFrame({
        'Tarea': ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4'],
        'Fecha de entrega': ['2024-04-11', '2024-04-12', '2024-04-13', '2024-04-14'],
        'Completada': [False, False, True, False]
    })

    # Filtras las tareas que no están completadas
    tareas_no_completadas = df[df['Completada'] == False]

    # Pasas las tareas no completadas al template
    return render_template('trabajo.html', tareas_no_completadas=tareas_no_completadas)

if __name__ == '__main__':
    app.run(debug=True)
