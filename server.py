from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

#Crea una ruta raíz ("/") que responda con "¡Hola Mundo!"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return '¡Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

#Crea una ruta que responda con "¡Dojo!"

@app.route('/dojo')
def success():
    return "¡Dojo!"

#Crea una ruta que responda con "Hola" y el nombre que esté en la URL después de /say/

@app.route('/say/<string:nombre>')
def say_name(nombre):
    return f"¡Hola, {nombre}!"

#Crea una ruta que responda con la palabra dada repetida tantas veces como se especifique en la URL

@app.route('/repeat/<int:numero>/<string:palabra>')
def repetir_palabra(numero,palabra):
    return numero*(palabra + " ")

#BONUS SENSEI: Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
#este lo googleamos en clase, se usco como editar el estado 404 no estaba en la plataforma. 

@app.errorhandler(404)
def page_not_found(e): #esta 'e' es el evento de flask
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404
    #return render_template('404.html'), 404

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración