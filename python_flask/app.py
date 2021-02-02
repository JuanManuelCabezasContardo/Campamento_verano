from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="campamento_de_verano"
)

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM modulo")
    select_modulo = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM clase")
    select_curso = cursor.fetchall()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM asistentes")
    select_asistentes = cursor.fetchall()


    return render_template("index.html",modulos=select_modulo,cursos=select_curso,asistentes=select_asistentes)

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

if __name__ == "__main__":
    app.run(debug=True)
