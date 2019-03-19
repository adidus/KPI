from flask import Flask, jsonify, request, url_for
import arrow

measurements = [
    {
        "id": 0,
        "date": "2019-03-10 17:50",
        "systolic": 120,
        "diastolic": 80,
    },
    {
        "id": 1,
        "date": "2019-03-15 17:50",
        "systolic": 180,
        "diastolic": 80,
    },
]


def make_public_task(task):
    """
    Make pretty print for
    :param task: for pretty print
    :return: pretty print task
    """
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('/api.api_get_measurements', measurement_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


# @app.route("/api/v0.1/measurements", methods=["GET"])
def get_measurements():
    """
    :return: all measurements
    """
    return jsonify({"measurements": [i for i in map(make_public_task, measurements)]})


# @app.route("/api/v0.1/measurement/<int:id>", methods=["GET"])
def get_measurement(measurement_id):
    """
    get measurement by id
    :param measurement_id: id for getting this node
    :return: measurement
    """
    elem = list(filter(lambda t: t['id'] == measurement_id, measurements))
    if len(elem) == 0:
        return {
                'Success': False,
                "Error": "Not found this node"
               }, 406
    return jsonify(make_public_task(measurements[measurement_id]))


# @app.route("/api/v0.1/measurements", methods=["POST"])
def add_measurement(systolic, diastolic):
    """
    Adding new node in our db
    :param systolic: measurement of systolic
    :param diastolic: measurement of diastolic
    :return: code of success
    """
    if not "diastolic" and not "systolic":
        return {
                   'Success': False,
                   "Error": "Not found this node"
               }, 406

    measurement = {
        "id": measurements[-1]["id"] + 1,
        "systolic": systolic,
        "diastolic": diastolic,
        "date": arrow.now().format("YYYY-MM-DD HH:mm")
    }
    measurements.append(measurement)
    return {
               'Success': True
           }, 202


# @app.route("/api/v0.1/measurement/<int:measurement_id>", methods=["PUT"])
def edit_measurement(measurement_id, systolic, diastolic):
    """
    Method for editing measurement by id
    :param measurement_id: id for editing
    :param systolic: new measurement
    :param diastolic: new measurement
    :return: code of success
    """
    elem = list(filter(lambda t: t['id'] == measurement_id, measurements))
    if len(elem) == 0:
        return {
                   'Success': False,
                   "Error": "Not found this node"
               }, 406

    elem[0]['systolic'] = systolic
    elem[0]['diastolic'] = diastolic
    elem[0]["date"] = elem[0]["date"]

    return {
               'Success': True
           }, 202


# @app.route("/api/v0.1/measurement/<int:measurement_id>", methods=["DELETE"])
def del_measurement(measurement_id):
    """
    delete measurement by id
    :param measurement_id: id for deleting
    :return: code of success
    """
    elem = list(filter(lambda t: t['id'] == measurement_id, measurements))
    if len(elem) == 0:
        return {
                   'Success': False,
                   "Error": "Not found this node"
               }, 406
    measurements.remove(elem[0])
    return {
               'Success': True
           }, 202
