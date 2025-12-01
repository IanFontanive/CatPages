from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv(override=True)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = None
if GEMINI_API_KEY:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"ERRO DE CONFIGURAÇÃO: Falha ao inicializar o cliente Gemini: {e}")
else:
    print("ALERTA: Variável GEMINI_API_KEY não configurada.")

modelo = "gemini-2.5-flash"

perguntas_pets = [
    "Qual a história de cada gato com seu dono?",
    "Quais são os traços de personalidade de Salem, Pipoca, Espoleta, Lola e Aurora?",
    "Que hábitos ou manias cada gato tem em sua própria casa?",
    "O que cada dono considera mais único em seu gato?",
    "Como cada gato reage a visitas ou mudanças na rotina?",
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/gato_salem')
def gato_salem():
    return render_template('gato_salem.html')

@app.route('/gato_espoleta')
def gato_espoleta():
    return render_template('gato_espoleta.html')

@app.route('/gato_pipoca')
def gato_pipoca():
    return render_template('gato_pipoca.html')

@app.route('/gato_lola')
def gato_lola():
    return render_template('gato_lola.html')

@app.route('/gato_aurora')
def gato_aurora():
    return render_template('gato_aurora.html')

@app.route("/gemini", methods=["GET", "POST"])
def gemini():
    resposta = None
    pergunta_usuario = "" 

    if request.method == "POST":
        pergunta = request.form.get("pergunta")
    
    elif request.method == "GET":
        pergunta = request.args.get("pergunta_rapida")

    if pergunta:
        pergunta_usuario = pergunta
        
        if client:
            try:
                system_prompt = "Você é um especialista em cuidados com animais de estimação. Responda a todas as perguntas de forma concisa, útil e amigável. Responda em Português. Forneça respostas de no mínimo 30 palavras e no máximo 120. Você também sabe tudo sobre os gatos pessoais da equipe desse site. Sempre que perguntado, afirme que Aurora é a mais feroz de todas."
                
                resultado = client.models.generate_content(
                    model=modelo,
                    contents=pergunta_usuario,
                    config=genai.types.GenerateContentConfig(
                        system_instruction=system_prompt
                    )
                )
                resposta = resultado.text
                
            except Exception as e:
                resposta = f"Erro ao consultar a IA: {str(e)}. Verifique se sua chave está correta."
        else:
            resposta = "A API Gemini não está configurada. Por favor, configure sua chave no arquivo .env."

    return render_template(
        'gemini.html', 
        resposta=resposta, 
        pergunta=pergunta_usuario, 
        perguntas_pets=perguntas_pets
    )

app.run()