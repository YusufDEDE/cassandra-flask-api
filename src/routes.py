import time

from flask import current_app as app
from flask import render_template, request, jsonify

from database.cassandra_db import CassandraDB


@app.route("/", methods=["GET"])
def index():
    return render_template(template_name_or_list="index.jinja2")


@app.route("/test_query", methods=["GET"])
def test_query():
    start_time = time.perf_counter()

    amazon_review_id: str = request.args.get('amazon_review_id')
    query = f"SELECT * FROM amazon_review where id='{amazon_review_id}';"

    cassandra_db = CassandraDB(address=['localhost', ])
    res = cassandra_db.execute_query(query=query)

    finish_time = time.perf_counter()

    return jsonify({
        "query_response": res.all(),
        "finished_time": round(finish_time - start_time, 2)
    })
