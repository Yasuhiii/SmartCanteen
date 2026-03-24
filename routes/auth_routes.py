from flask import Blueprint, render_template, request, redirect, session
from models.utilizador import autenticar, criar_utilizador

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        numero = request.form["numero"]
        password = request.form["password"]

        user = autenticar(numero, password)

        if user:
            session["user_id"] = user["id"]
            session["tipo"] = user["tipo"]
            session["nome"] = user["nome"]
            session["saldo"] = user["saldo"]
            session["numero"] = user["numero"]
            return redirect("/dashboard")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        tipo = request.form["tipo"]
        nome = request.form["nome"]
        numero = request.form["numero"]
        curso_dep = request.form["curso_dep"]
        email = request.form["email"]
        password = request.form["password"]

        criar_utilizador(tipo, nome, numero, curso_dep, email, password)

        return redirect("/")

    return render_template("register.html")


@auth_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    return render_template("dashboard.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")