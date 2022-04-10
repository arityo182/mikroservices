from flask import Flask, request, jsonify, make_response
import pymysql

app = Flask(__name__)

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_sekolah"
)


@app.route('/siswa/get_data_siswa', methods=['GET'])
def get_data_siswa():
    query = "SELECT * FROM tb_siswa WHERE 1=1"
    values = ()

    nis = request.args.get("nis")
    nama = request.args.get("nama")
    umur = request.args.get("umur")

    if nis:
        query += " AND nis=%s "
        values += (nis,)
    if nama:
        query += " AND nama LIKE %s "
        values += ("%"+nama+"%", )
    if umur:
        query += " AND umur=%s "
        values += (umur,)

    mycursor = mydb.cursor()
    mycursor.execute(query, values)
    row_headers = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    return make_response(jsonify(json_data), 200)


@app.route('/siswa/insert_data_siswa', methods=['POST'])
def insert_data_siswa():
    hasil = {"status": "gagal insert data siswa"}

    try:
        data = request.json

        query = "INSERT INTO tb_siswa(nis, nama, umur, alamat) VALUES(%s,%s,%s,%s)"
        values = (data["nis"], data["nama"], data["umur"], data["alamat"],)
        mycursor = mydb.cursor()
        mycursor.execute(query, values)
        mydb.commit()
        hasil = {"status": "berhasil insert data siswa"}

    except Exception as e:
        print("Error: " + str(e))

    return jsonify(hasil)


if __name__ == '__main__':
    app.run(debug=True, port=8092)
