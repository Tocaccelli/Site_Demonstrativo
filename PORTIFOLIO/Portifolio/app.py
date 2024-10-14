from flask import Flask, render_template

# Inicializar a aplicação Flask
app = Flask(__name__)


# Rota para a página inicial (index)
@app.route("/")
def index():
    return render_template("index.html")




# Rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
