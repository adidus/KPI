import unittest
import arrow
import requests


class PythonApi(unittest.TestCase):

    def test_get_measurements(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5050/api/measurements')

        if res.status_code == 200:
            print("Test 'get_measurements()' PASS at " + str(utc))
        else:
            print("Test 'get_measurements()' FAIL at " + str(utc))

    def test_get_measurement(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5050/api/measurement?measurement_id=0')

        if res.status_code == 200:
            print("Test 'get_measurement()' PASS at " + str(utc))
        else:
            print("Test 'get_measurement()' FAIL at " + str(utc))

    def test_add_measurements(self):
        utc = arrow.utcnow()

        res = requests.post('http://localhost:5050/api/add_measurement?systolic=200&diastolic=400')

        if res.status_code == 202:
            print("Test 'add_measurements()' PASS at " + str(utc))
        else:
            print("Test 'add_measurements()' FAIL at " + str(utc))
