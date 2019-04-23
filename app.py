from jdatetime import datetime, date, time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models import MeterInfo, MeterInfoSchema, app, metersinfo_schema
from models import Customer, customers_schema


# Get All MeterInfo
@app.route('/api/meterinfo/', methods=['GET'])
def get_meterinfo():

    id_status = str('')
    end_time_status = ''
    start_time_status = ''

    _id = request.args.get('id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    id_status = '' if ((_id.isnumeric()) and (
        len(_id) <= 64)) else "Validation Error !!!"

    try:
        datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        start_time = start_time.replace(' ', '-')
        start_time = start_time.replace(':', '-')
        start_time = ''.join(start_time.split('-'))
    except:
        start_time_status = "Validation Error !!!"

    try:
        datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        end_time = end_time.replace(' ', '-')
        end_time = end_time.replace(':', '-')
        end_time = ''.join(end_time.split('-'))
    except:
        end_time_status = "Validation Error !!!"

    if(not id_status.strip() and not start_time_status.strip() and not end_time_status.strip()):

        all_meterinfo = MeterInfo.query.filter(MeterInfo.ID == _id).filter(
            MeterInfo.TimeTag >= start_time, MeterInfo.TimeTag <= end_time)

        response = metersinfo_schema.jsonify(all_meterinfo)

        if not response:
            response.status_code = 204
        else:
            response.status_code = 200

    else:
        response = jsonify({
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

# Get Customer
@app.route('/api/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):

    customer_id_status = str('')
    # customer_id = request.args.get(id)

    customer_id_status = '' if (
        customer_id.isnumeric()) else "Validation Error !!!"

    if(not customer_id_status.strip()):

        customer_info = Customer.query.filter(
            Customer.xSubscriptionId_Pk == customer_id)

        response = jsonify(customers_schema.dump(customer_info).data)
        # response = customer_info
        # if not response:
        #     response.status_code = 204
        # else:
        #     response.status_code = 200

    else:
        response = jsonify({
            'message': customer_id_status
        })
        response.status_code = 400
    return response


# run server
if __name__ == '__main__':
    app.run(debug=True)
