# [START app]
import logging

# [START imports]
from flask import Flask, request
from flask import jsonify
from google.cloud import spanner
import os
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

# [START create_spanner]
spanner_client = spanner.Client()
instance_id = os.getenv("USER_MICROSERVICES")
instance_id = os.getenv("SPANNER_INSTANCE")
database_id = os.getenv("SPANNER_DATABASE")
# [END create_spanner]

def SQL_SELECT_WINE():
    return SQL_SELECT_WINE_WHERE("")

def SQL_SELECT_WINE_WHERE(where):
    return f"SELECT w.years, w.code_barre, w.percent, a.advice, app.appellation, r.region, t.type, wa.warning, c.cuve, p.productor, w.img_url, STRING_AGG(cep.cepage, ', ') AS cepage FROM wine w LEFT JOIN advice a ON w.id_advice = a.id LEFT JOIN appellation app ON w.id_appellation = app.id LEFT JOIN region r ON w.id_region = r.id LEFT JOIN type t ON w.id_type = t.id LEFT JOIN warning wa ON w.id_warning = wa.id LEFT JOIN cuve c ON w.id_cuve = c.id LEFT JOIN productor p ON w.id_productor = p.id LEFT JOIN cepage_join cj ON w.id = cj.id_wine LEFT JOIN cepage cep ON cj.id_cepage = cep.id {where} GROUP BY w.id, w.years, w.code_barre, w.percent, a.advice, app.appellation, r.region, t.type, wa.warning, c.cuve, p.productor, w.img_url;"



@app.route("/getAllWine", methods=['POST'])
def getAllWine():
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE())
    return jsonify(list(cursor))

@app.route("/getWine/id", methods=['POST'])
def getWineById():
    wine_id = request.args.get('id')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE_WHERE(f"WHERE w.id = {int(wine_id)}"))
    return jsonify(list(cursor))

# [START by years]
@app.route("/getWine/year/before", methods=['POST'])
def getWineBefore():
    year = request.args.get('year')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE_WHERE(f"WHERE w.years < {int(year)}"))
    return jsonify(list(cursor))

@app.route("/getWine/year/after", methods=['POST'])
def getWineAfter():
    year = request.args.get('year')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE_WHERE(f"WHERE w.years > {int(year)}"))
    return jsonify(list(cursor))

@app.route("/getWine/year", methods=['POST'])
def getWineByYear():
    year = request.args.get('year')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE_WHERE(f"WHERE w.years = {int(year)}"))
    return jsonify(list(cursor))
# [END by years]


@app.route("/getWine/codebare", methods=['POST'])
def getWineByCodeBar():
    codebare = request.args.get('codebarre')
    database = spanner_client.instance(instance_id).database(database_id)
    with database.snapshot() as snapshot:
        cursor = snapshot.execute_sql(SQL_SELECT_WINE_WHERE(f"WHERE w.code_barre = '{str(codebare)}'"))
    return jsonify(list(cursor))

# [END app]