from flask import Flask, redirect, url_for, render_template, request, session
from markupsafe import escape
import mysql.connector
from datetime import timedelta

"""
SESSION NO INCLUIDA
"""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="campamento_de_verano"
)

dias_de_la_semana=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
@app.route("/")

def index():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM modulo")
    select_modulo = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM clase")
    select_curso = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM asistentes")
    select_asistentes = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM horario")
    select_horario = cursor.fetchall()

    return render_template("index.html",modulos=select_modulo,cursos=select_curso,asistentes=select_asistentes,horario = select_horario ,semana=dias_de_la_semana,msn="none")


@app.route("/<mensaje>")

def home(mensaje="none"):
    msn=(mensaje)#escape
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM modulo")
    select_modulo = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM clase")
    select_curso = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM asistentes")
    select_asistentes = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM horario")
    select_horario = cursor.fetchall()

    return render_template("index.html",modulos=select_modulo,cursos=select_curso,asistentes=select_asistentes,horario = select_horario ,semana=dias_de_la_semana,msn=msn)
        
@app.route("/login",methods=["POST","GET"])

def login():
    return render_template("login.html")

@app.route("/clase",methods=["GET","POST"])

def clase():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM clase")
    select_clase = cursor.fetchall()
    return render_template("Cursos.html", clases=select_clase)

@app.route("/insert_clase",methods=["POST"])

def insert_clase():
    if (request.method == "POST"):
        insert= "INSERT INTO clase (id, nombre_clase) VALUES (%s, %s)"
        val = ("",request.form["nombre_clase"])
        
        cursor = mydb.cursor()
        cursor.execute(insert, val)
        mydb.commit()
        
        return redirect(url_for("clase"))#el redirect la salida
    else:
        return redirect(url_for("clase"))

@app.route("/delete_clase",methods=["POST"])

def delete_clase():
    if (request.method == "POST"):
        delete= "DELETE FROM clase where id="+request.form["id"]+""
        cursor = mydb.cursor()
        cursor.execute(delete)
        mydb.commit()
        
        return redirect(url_for("clase"))#el redirect la salida
    else:
        return redirect(url_for("clase"))

@app.route("/modificar_clase",methods=["POST"])

def modificar_clase():
    if (request.method == "POST"):
        id=request.form["id"]
        nombre=request.form["nombre"]

        return render_template("modificar_clase.html", nombre=nombre,id=id)
    else:
        return redirect(url_for("clase"))

@app.route("/modificar_clase_c",methods=["POST"])

def modificar_clase_c():
    if(request.method == "POST"):
        update= "UPDATE clase SET nombre_clase=%s where clase.id=%s"
        val = (request.form["nombre_clase"],request.form["id"])
        cursor = mydb.cursor()
        cursor.execute(update,val)
        mydb.commit()
        return redirect(url_for("clase"))
    else:
        return redirect(url_for("clase"))
        
@app.route("/asistentes",methods=["GET","POST"])

def asistentes():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM asistentes")
    select_clase = cursor.fetchall()
    return render_template("Asistentes.html", asistentes=select_clase)

@app.route("/insert_asistente",methods=["POST"])

def insert_asistente():
    if (request.method == "POST"):
        insert= "INSERT INTO asistentes (id, nombre) VALUES (%s, %s)"
        val = ("",request.form["nombre"])
        
        cursor = mydb.cursor()
        cursor.execute(insert, val)
        mydb.commit()
        
        return redirect(url_for("asistentes"))#el redirect la salida
    else:
        return redirect(url_for("asistentes"))

@app.route("/delete_asistente",methods=["POST"])

def delete_asistente():
    if (request.method == "POST"):
        delete= "DELETE FROM asistentes where id="+request.form["id"]+""
        cursor = mydb.cursor()
        cursor.execute(delete)
        mydb.commit()
        
        return redirect(url_for("asistentes"))#el redirect la salida
    else:
        return redirect(url_for("asistentes"))

@app.route("/modificar_asistente",methods=["POST"])

def modificar_asistente():
    if (request.method == "POST"):
        id=request.form["id"]
        nombre=request.form["nombre"]

        return render_template("modificar_asistente.html", nombre=nombre,id=id)
    else:
        return redirect(url_for("asistentes"))

@app.route("/modificar_asistente_c",methods=["POST"])

def modificar_asistente_c():
    if(request.method == "POST"):
        update= "UPDATE asistentes SET nombre=%s where asistentes.id=%s"
        val = (request.form["nombre"],request.form["id"])
        cursor = mydb.cursor()
        cursor.execute(update,val)
        mydb.commit()
        return redirect(url_for("asistentes"))
    else:
        return redirect(url_for("asistentes"))

@app.route("/modulo",methods=["GET"])

def modulo():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM modulo")
    select_clase = cursor.fetchall()
    return render_template("modulo.html", modulos=select_clase)

@app.route("/insert_modulo",methods=["POST"])

def insert_modulo():
    if (request.method == "POST"):
        insert= "INSERT INTO modulo (id,hora_ini,hora_fin ) VALUES (%s, %s,%s)"
        val = ("",request.form["ini"],request.form["fin"])
        
        cursor = mydb.cursor()
        cursor.execute(insert, val)
        mydb.commit()
        
        return redirect(url_for("modulo"))#el redirect la salida
    else:
        return redirect(url_for("modulo"))

@app.route("/delete_modulo",methods=["POST"])

def delete_modulo():
    if (request.method == "POST"):
        delete= "DELETE FROM modulo where id="+request.form["id"]+""
        cursor = mydb.cursor()
        cursor.execute(delete)
        mydb.commit()
        
        return redirect(url_for("modulo"))#el redirect la salida
    else:
        return redirect(url_for("modulo"))

@app.route("/modificar_modulo",methods=["POST"])

def modificar_modulo():
    if (request.method == "POST"):
        id=request.form["id"]
        ini=request.form["ini"]
        fin=request.form["fin"]

        return render_template("modificar_modulo.html", fin=fin,ini=ini,id=id)
    else:
        return redirect(url_for("modulo"))

@app.route("/modificar_modulo_c",methods=["POST"])

def modificar_modulo_c():
    if(request.method == "POST"):
        update= "UPDATE modulo SET hora_ini=%s ,hora_fin=%s where modulo.id=%s"
        val = (request.form["ini"],request.form["fin"] ,request.form["id"])
        cursor = mydb.cursor()
        cursor.execute(update,val)
        mydb.commit()
        return redirect(url_for("modulo"))
    else:
        return redirect(url_for("modulo"))

@app.route("/insert_horario",methods=["POST"])

def insert_horario():
    if(request.method == "POST"):
        if(request.form["asistente"] == "NO") or (request.form["clase"] == "NO") or (request.form["modulo"] == "NO") or(request.form["dia"] == "NO"):
            return redirect(url_for("home",mensaje="Alguno de los datos para su hora no fue seleccionado"))
        else:
            cursor = mydb.cursor()
            select = "SELECT * FROM horario where id_modulo=%s and id_asistente=%s and id_clase=%s and Dia=%s"
            val = (request.form["modulo"],request.form["asistente"],request.form["clase"],request.form["dia"])
            cursor = mydb.cursor()
            cursor.execute(select, val)
            select_hora = cursor.fetchall()
            if(len(select_hora)>0):
                return redirect(url_for("home",mensaje="esta hora esta acupada"))
            else:
                insert= "INSERT INTO horario (id_modulo,id_asistente,id_clase,Dia ) VALUES (%s, %s,%s,%s)"
                cursor2 = mydb.cursor()
                cursor2.execute(insert, val)
                mydb.commit()
                return redirect(url_for("home",mensaje="se guardará!"))
    else:
        return redirect(url_for("home"))

@app.route("/delete_horario",methods=["POST"])

def delete_horario():
    if (request.method == "POST"):
        delete= "DELETE FROM horario where id_modulo=%s and  id_asistente=%s and id_clase=%s and Dia=%s"
        val = (request.form["modulo"],request.form["asistente"],request.form["clase"],request.form["Dia"])
        cursor = mydb.cursor()
        cursor.execute(delete, val)
        mydb.commit()
        
        return redirect(url_for("home",mensaje="esta hora fue eliminada"))#el redirect la salida
    else:
        return redirect(url_for("home",mensaje="esta hora no existe"))

@app.route("/page_login",methods=["GET"])

def page_login():
    return render_template("login.html")

@app.route("/iniciar_sesion", methods=["POST"])

def iniciar_sesion():
    cursor = mydb.cursor()
    select = "SELECT * FROM users where id=%s and password=%s"
    val = (request.form["id"],request.form["pass"])
    cursor = mydb.cursor()
    cursor.execute(select, val)
    select_user = cursor.fetchall()
    if(len(select_user)>0):
        session.permanent = True
        id =request.form["id"]
        session["user"]= id
        return redirect(url_for("home"))
    else:
        return redirect(url_for("page_login"))

@app.route("/cerrar_sesion", methods=["GET"])

def cerrar_sesion():
    session.pop("user", None)
    return redirect(url_for("page_login"))

if __name__ == "__main__":
    app.run(debug=True)
