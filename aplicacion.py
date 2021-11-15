from flask import Flask, json, jsonify, request

from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()



app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ado123'
app.config['MYSQL_DATABASE_DB'] = 'Empresa_automoviles'
mysql.init_app(app)

@app.route('/')
def index_router():
    return "Sistema para controlar el ingreso de vendededor"


@app.route('/vendedor', methods=['GET', 'POST'])
def index_vendedor():
    if(request.method == 'POST'):
        nuevo_vendedor =request.get_json();
        id = nuevo_vendedor['id']
        vend_CIU = nuevo_vendedor['vend_CIU']
        vend_PrimerNombre = nuevo_vendedor['vend_PrimerNombre']
        vend_PrimerApellido = nuevo_vendedor['vend_PrimerApellido']
        vend_FechaNacimiento = nuevo_vendedor['vend_FechaNacimiento']
        vend_Tipo = nuevo_vendedor['vend_Tipo']
        vend_Salario = nuevo_vendedor['vend_Salario']
        vend_DireccionResidencia = nuevo_vendedor['vend_DireccionResidencia']
        vend_NumeroTelefono = nuevo_vendedor['vend_NumeroTelefono']
        vend_PorcentajeComision = nuevo_vendedor['vend_PorcentajeComision']
        vend_MOntoCOmision = nuevo_vendedor['vend_MOntoCOmision']

        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO vendedor(id, vend_CIU, vend_PrimerNombre, vend_PrimerApellido, vend_FechaNacimiento, vend_Tipo,vend_Salario, vend_DireccionResidencia, vend_NumeroTelefono, vend_PorcentajeComision, vend_MOntoCOmision) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (id, vend_CIU, vend_PrimerNombre, vend_PrimerApellido, vend_FechaNacimiento, vend_Tipo,vend_Salario, vend_DireccionResidencia, vend_NumeroTelefono, vend_PorcentajeComision, vend_MOntoCOmision))
        conn.commit()
        cur.close
        return jsonify({"response": "Vendedor creado con exito"}), 201
    else: 
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Estudiantes")
 # arreglo de arreglos con la informacion de la DB
        data_vendedor = cur.fetchall()
        responseData = []
        for vendedor in data_vendedor:
            responseData.append(
            {
            "id": estudiante[0],
            "id_estudiante": estudiante[1],
            "nombre": estudiante[2],
            "carrera": estudiante[3]
            }
        )
        cur.close()
    return jsonify({"response": responseData}), 200
@app.route('/clientes', methods=['GET', 'POST'])
def index_cliente():
    if(request.method == 'POST'):
        nuevo_cliente =request.get_json();
        id = nuevo_cliente['id']
        clien_CedulaIdentidad = nuevo_cliente['clien_CedulaIdentidad']
        clien_TipoCedulaIdentidad = nuevo_cliente['clien_TipoCedulaIdentidad']
        clien_PrimerNombre = nuevo_cliente['clien_PrimerNombre']
        clien_PrimerApellido = nuevo_cliente['clien_PrimerApellido']
        clien_CalificacionCrdito = nuevo_cliente['clien_CalificacionCrdito']
        clien_DireccionResidencia = nuevo_cliente['clien_DireccionResidencia']
        clien_NumeroTelefono = nuevo_cliente['clien_NumeroTelefono']
        clien_FechaNacimiento = nuevo_cliente['clien_FechaNacimiento']
        

        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO vendedor(id, clien_CedulaIdentidad, clien_TipoCedulaIdentidad, clien_PrimerNombre, clien_PrimerApellido, clien_CalificacionCrdito,clien_DireccionResidencia, clien_NumeroTelefono, clien_FechaNacimiento) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (id, clien_CedulaIdentidad, clien_TipoCedulaIdentidad, clien_PrimerNombre, clien_PrimerApellido, clien_CalificacionCrdito,clien_DireccionResidencia, clien_NumeroTelefono, clien_FechaNacimiento))
        conn.commit()
        cur.close
        return jsonify({"response": "Vendedor creado con exito"}), 201
    else: 
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Estudiantes")
 # arreglo de arreglos con la informacion de la DB
        data_vendedor = cur.fetchall()
        responseData = []
        for vendedor in data_vendedor:
            responseData.append(
            {
            "id": estudiante[0],
            "id_estudiante": estudiante[1],
            "nombre": estudiante[2],
            "carrera": estudiante[3]
            }
        )
        cur.close()
    return jsonify({"response": responseData}), 200
@app.route('/vendedor/<int:vendedor_CIU>', methods=['GET', 'PUT', 'DELETE'])
def vendedor_CIU(vendedor_CIU):
    if request.method == 'PUT':
        conn = mysql.connect()
        cur = conn.cursor()
        info_actualizar_vendedor = request.get_json()
        vend_PrimerNombre = None
        vend_PrimerApellido = None
        vend_FechaNacimiento = None
        vend_Tipo = None
        vend_Salario = None
        vend_DireccionResidencia = None
        vend_NumeroTelefono = None
        vend_PorcentajeComision = None

    if info_actualizar_vendedor != None:
        if "vend_PrimerNombre" in info_actualizar_vendedor:
            vend_PrimerNombre = info_actualizar_vendedor['vend_PrimerNombre']

    elif "vend_PrimerApellido" in info_actualizar_vendedor:
        vend_PrimerApellido = info_actualizar_vendedor['vend_PrimerApellido']

    elif "vend_FechaNacimiento" in info_actualizar_vendedor:
        vend_FechaNacimiento = info_actualizar_vendedor['vend_FechaNacimiento']

    elif "vend_Tipo" in info_actualizar_vendedor:
        vend_Tipo = info_actualizar_vendedor['vend_Tipo']

    elif "vend_Salario" in info_actualizar_vendedor:
        vend_Salario = info_actualizar_vendedor['vend_Salario']

    elif "vend_DireccionResidencia" in info_actualizar_vendedor:
        vend_DireccionResidencia = info_actualizar_vendedor['vend_DireccionResidencia']

    elif "vend_NumeroTelefono" in info_actualizar_vendedor:
        vend_NumeroTelefono = info_actualizar_vendedor['vend_NumeroTelefono']

    elif "vend_PorcentajeComision" in info_actualizar_vendedor:
        vend_PorcentajeComision = info_actualizar_vendedor['vend_PorcentajeComision']

    elif "vend_MOntoComision" in info_actualizar_vendedor:
        vend_MOntoComision = info_actualizar_vendedor['vend_MOntoComision']
    
    else:
        return jsonify({"response": "La informacion para actualizar no fue provista"}), 400

    if vend_PrimerNombre != None and vend_PrimerApellido != None and vend_FechaNacimiento != None and vend_Tipo != None and vend_Tipo != None and vend_Salario != None and vend_DireccionResidencia != None and vend_NumeroTelefono != None and vend_PorcentajeComision != None and vend_MOntoComision:
        respuesta = cur.execute("UPDATE vendedor SET vend_vend_PrimerNOmbre = %s, vend_PrimerApellido = %s, vend_FechaNacimiento = %s, vend_tipo = %s, vend_Salario = %s, vend_DireccionResidencia = %s, vend_NumeroTelefono = %s, vend_PorcentajeComision = %s, vend_MOntoComision WHERE vend_CIU = %s", 
    (vend_PrimerNombre, vend_PrimerApellido, vend_FechaNacimiento, vend_Tipo,vend_Salario, vend_DireccionResidencia, vend_NumeroTelefono, vend_PorcentajeComision, vend_MOntoComision))
    
    elif vend_PrimerNombre != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PrimerNombre = %s WHERE vend_CIU = %s", (vend_PrimerNombre, vendedor_CIU))

    elif vend_PrimerApellido != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PrimerApellido = %s WHERE vend_CIU = %s", (vend_PrimerApellido, vendedor_CIU))

    elif vend_FechaNacimiento != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_FechaNacimiento = %s WHERE vend_CIU = %s", (vend_FechaNacimiento, vendedor_CIU))

    elif vend_Tipo != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_Tipo= %s WHERE vend_CIU = %s", (vend_Tipo, vendedor_CIU))

    elif vend_Salario != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_Salario = %s WHERE vend_CIU = %s", (vend_Salario, vendedor_CIU))

    elif vend_DireccionResidencia != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_DireccionResidencia = %s WHERE vend_CIU = %s", (vend_DireccionResidencia, vendedor_CIU))

    elif vend_NumeroTelefono != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_NumeroTelefono = %s WHERE vend_CIU = %s", (vend_NumeroTelefono, vendedor_CIU))

    elif vend_PorcentajeComision != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PorcentajeComision = %s WHERE vend_CIU = %s", (vend_PorcentajeComision, vendedor_CIU))

    elif vend_MOntoComision != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_MOntoComision = %s WHERE vend_CIU = %s", (vend_MOntoComision, vendedor_CIU))

    else:
        return jsonify({"response": "La informacion para actualizar no fue provista"}), 400
    conn.commit()
    cur.close()
    return jsonify({"response": "vendedor " + str(vendedor_CIU) + " actualizado con exito!"}), 200
    
    elif request.method == 'DELETE':
        conn = mysql.connect()
        cur = conn.cursor()

        response = cur.execute('DELETE FROM vendedor WHERE vend_CIU = %s', (vendedor_CIU))
        print(response)
        conn.momit()
        cur.close()
        # data_vendedor =cur.fetchone()

        # response = cur.execute('SELECT * FROM vendedor WHERE vend_CIU = %s', (vendedor_CIU))
        return jsonify({"response": "vendedor: " + str(vendedor_CIU) + ". Borrado con exito!" })
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        

        data_vendedor = cur.fetchone()

        if data_vendedor == None:
            return jsonify({"response": "No se encontraron estudiantes con ID de estudiante: " + str(vendedor_CIU)}), 200
        else:
            return jsonify({"response": {
            "id": data_vendedor[0],
            "vend_CIU": data_vendedor[1],
            "vend_PrimerNombre": data_vendedor[2],
            "vend_PrimerApellido": data_vendedor[3],
            "vend_FechaNacimiento": data_vendedor[3],
            "vend_Tipo": data_vendedor[3],
            "vend_Salario": data_vendedor[3],
            "vend_DireccionResidencia": data_vendedor[3],
            "vend_NumeroTelefono": data_vendedor[3],
            "vend_PorcentajeComision": data_vendedor[3],
            "vend_MOntoComision": data_vendedor[3],


@app.route('/vendedor/<int:vendedor_CIU>', methods=['GET', 'PUT', 'DELETE'])
def vendedor_CIU(vendedor_CIU):
    if request.method == 'PUT':
        conn = mysql.connect()
        cur = conn.cursor()
        info_actualizar_vendedor = request.get_json()
        vend_PrimerNombre = None
        vend_PrimerApellido = None
        vend_FechaNacimiento = None
        vend_Tipo = None
        vend_Salario = None
        vend_DireccionResidencia = None
        vend_NumeroTelefono = None
        vend_PorcentajeComision = None

    if info_actualizar_vendedor != None:
        if "vend_PrimerNombre" in info_actualizar_vendedor:
            vend_PrimerNombre = info_actualizar_vendedor['vend_PrimerNombre']

    elif "vend_PrimerApellido" in info_actualizar_vendedor:
        vend_PrimerApellido = info_actualizar_vendedor['vend_PrimerApellido']

    elif "vend_FechaNacimiento" in info_actualizar_vendedor:
        vend_FechaNacimiento = info_actualizar_vendedor['vend_FechaNacimiento']

    elif "vend_Tipo" in info_actualizar_vendedor:
        vend_Tipo = info_actualizar_vendedor['vend_Tipo']

    elif "vend_Salario" in info_actualizar_vendedor:
        vend_Salario = info_actualizar_vendedor['vend_Salario']

    elif "vend_DireccionResidencia" in info_actualizar_vendedor:
        vend_DireccionResidencia = info_actualizar_vendedor['vend_DireccionResidencia']

    elif "vend_NumeroTelefono" in info_actualizar_vendedor:
        vend_NumeroTelefono = info_actualizar_vendedor['vend_NumeroTelefono']

    elif "vend_PorcentajeComision" in info_actualizar_vendedor:
        vend_PorcentajeComision = info_actualizar_vendedor['vend_PorcentajeComision']

    elif "vend_MOntoComision" in info_actualizar_vendedor:
        vend_MOntoComision = info_actualizar_vendedor['vend_MOntoComision']
    
    else:
        return jsonify({"response": "La informacion para actualizar no fue provista"}), 400

    if vend_PrimerNombre != None and vend_PrimerApellido != None and vend_FechaNacimiento != None and vend_Tipo != None and vend_Tipo != None and vend_Salario != None and vend_DireccionResidencia != None and vend_NumeroTelefono != None and vend_PorcentajeComision != None and vend_MOntoComision:
        respuesta = cur.execute("UPDATE vendedor SET vend_vend_PrimerNOmbre = %s, vend_PrimerApellido = %s, vend_FechaNacimiento = %s, vend_tipo = %s, vend_Salario = %s, vend_DireccionResidencia = %s, vend_NumeroTelefono = %s, vend_PorcentajeComision = %s, vend_MOntoComision WHERE vend_CIU = %s", 
    (vend_PrimerNombre, vend_PrimerApellido, vend_FechaNacimiento, vend_Tipo,vend_Salario, vend_DireccionResidencia, vend_NumeroTelefono, vend_PorcentajeComision, vend_MOntoComision))
    
    elif vend_PrimerNombre != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PrimerNombre = %s WHERE vend_CIU = %s", (vend_PrimerNombre, vendedor_CIU))

    elif vend_PrimerApellido != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PrimerApellido = %s WHERE vend_CIU = %s", (vend_PrimerApellido, vendedor_CIU))

    elif vend_FechaNacimiento != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_FechaNacimiento = %s WHERE vend_CIU = %s", (vend_FechaNacimiento, vendedor_CIU))

    elif vend_Tipo != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_Tipo= %s WHERE vend_CIU = %s", (vend_Tipo, vendedor_CIU))

    elif vend_Salario != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_Salario = %s WHERE vend_CIU = %s", (vend_Salario, vendedor_CIU))

    elif vend_DireccionResidencia != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_DireccionResidencia = %s WHERE vend_CIU = %s", (vend_DireccionResidencia, vendedor_CIU))

    elif vend_NumeroTelefono != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_NumeroTelefono = %s WHERE vend_CIU = %s", (vend_NumeroTelefono, vendedor_CIU))

    elif vend_PorcentajeComision != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_PorcentajeComision = %s WHERE vend_CIU = %s", (vend_PorcentajeComision, vendedor_CIU))

    elif vend_MOntoComision != None:
        respuesta = cur.execute("UPDATE vendedor SET vend_MOntoComision = %s WHERE vend_CIU = %s", (vend_MOntoComision, vendedor_CIU))

    else:
        return jsonify({"response": "La informacion para actualizar no fue provista"}), 400
    conn.commit()
    cur.close()
    return jsonify({"response": "vendedor " + str(vendedor_CIU) + " actualizado con exito!"}), 200
    
    elif request.method == 'DELETE':
        conn = mysql.connect()
        cur = conn.cursor()

        response = cur.execute('DELETE FROM vendedor WHERE vend_CIU = %s', (vendedor_CIU))
        print(response)
        conn.momit()
        cur.close()
        # data_vendedor =cur.fetchone()

        # response = cur.execute('SELECT * FROM vendedor WHERE vend_CIU = %s', (vendedor_CIU))
        return jsonify({"response": "vendedor: " + str(vendedor_CIU) + ". Borrado con exito!" })
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        

        data_vendedor = cur.fetchone()

        if data_vendedor == None:
            return jsonify({"response": "No se encontraron estudiantes con ID de estudiante: " + str(vendedor_CIU)}), 200
        else:
            return jsonify({"response": {
            "id": data_vendedor[0],
            "vend_CIU": data_vendedor[1],
            "vend_PrimerNombre": data_vendedor[2],
            "vend_PrimerApellido": data_vendedor[3],
            "vend_FechaNacimiento": data_vendedor[3],
            "vend_Tipo": data_vendedor[3],
            "vend_Salario": data_vendedor[3],
            "vend_DireccionResidencia": data_vendedor[3],
            "vend_NumeroTelefono": data_vendedor[3],
            "vend_PorcentajeComision": data_vendedor[3],
            "vend_MOntoComision": data_vendedor[3],
        }}), 302
        }}), 302

