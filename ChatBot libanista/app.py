from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Configurar la clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Diccionario con preguntas y respuestas
faq = {
    "¿Dónde está ubicada la institución?": "La IED Líbano sede principal se encuentra ubicada en la carrera 34 #44A- 26, Urb. Libano y la Sede santa cruz se encuentra en la calle 48 #27-04, Barrio Santa Cruz.",
    "¿Cuáles son los requisitos de admisión?": "Descargar y llenar un formulario de inscripción con los documentos requeridos, llevarlo a la secretaria de la escuela, presentar y pasar un examen y una entrevista de admisión.",
    "¿Hay opciones de becas disponibles?": "No.",
    "¿Cuáles son los métodos de evaluación en la institución?": "En la práctica se desarrolla la autoevaluación, la coevaluación y la heteroevaluación. Dentro de esta se tiene en cuenta los componentes: SABER, SABER HACER Y SER.",
    "¿Hay actividades extracurriculares?": "Sí, múltiples actividades como danza, tambora, recreación y deporte.",
    "¿Cómo se pueden consultar las calificaciones?": "Mediante la plataforma SIAN365.",
    "¿Qué servicios de apoyo se ofrecen a los estudiantes?": "Psicoorientación.",
    "¿Cómo puedo contactar a un profesor o administrador?": "Todos los profesores tienen un horario de atención estipulado.",
    "¿Hay un servicio de biblioteca?": "Aún no.",
    "¿Cuáles son sus horarios?": "No hay.",
    "¿Qué instalaciones deportivas están disponibles?": "Cancha de microfutbol que se adapta a baloncesto y voleibol.",
    "¿Cuál es el proceso de inscripción?": "a. descargar formulario, b. diligenciar formulario, c. acercarse a la secretaria con todos los documentos requeridos, d. presentar examen de admisión, e. Entrevista.",
    "¿Hay fechas límite para la inscripción?": "Sí.",
    "¿Cuáles son los próximos eventos o actividades en la institución?": "Semana cultural, Clausura.",
    "¿Cómo puedo participar en los eventos de la institución?": "De forma activa con el docente encargado.",
    "¿Hay acceso a recursos tecnológicos, como computadoras o Wi-Fi?": "Sí, dos salas de informática dotadas con computadores portátiles.",
    "¿Qué actividades se organizan para los estudiantes?": "Actividades lúdicas como conmemoraciones, izadas de banderas, semana cultural.",
    "¿Cuáles son las reglas y políticas de la institución?": "Las puedes consultar en el manual de convivencia el cual se encuentra en la plataforma, pronto lo integraremos para brindarlo acá.",
    "¿Qué hacer si tengo un problema con un compañero de clase?": "Informarlo al tutor."
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Verificar si la pregunta está en el diccionario
    response = faq.get(user_message)
    
    # Si no se encuentra una respuesta, se consulta a OpenAI
    if response is None:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        response = response['choices'][0]['message']['content']
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
