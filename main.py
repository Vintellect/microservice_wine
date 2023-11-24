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
    return f"SELECT w.years, w.code_barre, w.percent, a.advice, app.appellation, r.region, t.type, wa.warning, c.cuve, p.productor FROM wine w LEFT JOIN advice a ON w.id_advice = a.id LEFT JOIN appellation app ON w.id_appellation = app.id LEFT JOIN region r ON w.id_region = r.id LEFT JOIN type t ON w.id_type = t.id LEFT JOIN warning wa ON w.id_warning = wa.id LEFT JOIN cuve c ON w.id_cuve = c.id LEFT JOIN productor p ON w.id_productor = p.id {where};"



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

# [END app]