from jdatetime import datetime, date, time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models import MeterInfo, MeterInfoSchema, app, meterinfo_schema, meterinfos_schema

# Get All Products
@app.route('/meterinfo', methods=['GET'])
def get_products():

    id_status = ''
    end_time_status = ''
    start_time_status = ''

    _id = request.headers.get('id')
    start_time = request.headers.get('start_time')
    end_time = request.headers.get('end_time')

    id_status = '' if ((_id.isnumeric()) and (len(_id) <= 64)) else "Validation Error !!!"

    try:
        datetime.strptime(start_time, "%Y-%m-%d-%H-%M-%S")
        start_time = ''.join(start_time.split('-'))
    except:
        start_time_status = "Validation Error !!!"

    try:
        datetime.strptime(end_time, "%Y-%m-%d-%H-%M-%S")
        end_time = ''.join(end_time.split('-'))
    except:
        end_time_status = "Validation Error !!!"

    if(not id_status.strip() and not start_time_status.strip() and not end_time_status.strip()):

        all_meterinfo = MeterInfo.query.filter(MeterInfo.ID == _id).filter(
            MeterInfo.TimeTag >= start_time, MeterInfo.TimeTag <= end_time)

        result = meterinfos_schema.dump(all_meterinfo)

        status = {'status': 'Successful'}
        result.data.append(status)
        response = jsonify(result.data)
        response.status_code = 200

    else:
        response =  jsonify({
            "status": "Unsuccessful",
            "id": [
                {
                    'message': id_status,
                }
            ],
            "start_time": [
                {
                    'message': start_time_status,
                }
            ],
            "end_time": [
                {
                    'message': end_time_status,

                }
            ]

        })
        response.status_code = 400
    return response


# run server
if __name__ == '__main__':
    app.run(debug=True)
