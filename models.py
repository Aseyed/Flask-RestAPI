# coding: utf-8
from flask import Flask
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import __name__ as app_name

# init app
app = Flask(app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DB_CONNECTION_STRING'
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)

# MeterInfo Class/Model


class MeterInfo(db.Model):
    __tablename__ = 'MeterInfo'

    TimeTag = db.Column(db.BigInteger, primary_key=True, nullable=False)
    ID = db.Column(db.String(64), primary_key=True, nullable=False)
    GUID = db.Column(db.String(128))
    MeterID = db.Column(db.String(64))
    MeterType = db.Column(db.String(32))
    MeterSerialNumber = db.Column(db.String(64))
    Date = db.Column(db.DateTime)
    ShmasiDate = db.Column(db.String(32))
    SourceID = db.Column(db.String(64))
    SourceName = db.Column(db.String(64))
    PowerActive = db.Column(db.Float(53))
    PowerReactive = db.Column(db.Float(53))
    VoltagePhaseA = db.Column(db.Float(53))
    VoltagePhaseB = db.Column(db.Float(53))
    VoltagePhaseC = db.Column(db.Float(53))
    VoltagePhaseN = db.Column(db.Float(53))
    CurrentPhaseA = db.Column(db.Float(53))
    CurrentPhaseB = db.Column(db.Float(53))
    CurrentPhaseC = db.Column(db.Float(53))
    CurrentPhaseN = db.Column(db.Float(53))
    PhaseAAngle = db.Column(db.Float(53))
    PhaseBAngle = db.Column(db.Float(53))
    PhaseCAngle = db.Column(db.Float(53))
    PhaseNAngle = db.Column(db.Float(53))
    Frequency = db.Column(db.Float(53))
    ActiveEnergy = db.Column(db.Float(53))
    ReactiveEnergy = db.Column(db.Float(53))
    VoltageL1 = db.Column(db.Float(53))
    VoltageL2 = db.Column(db.Float(53))
    VoltageL3 = db.Column(db.Float(53))
    CurrentL1 = db.Column(db.Float(53))
    CurrentL2 = db.Column(db.Float(53))
    CurrentL3 = db.Column(db.Float(53))
    demand = db.Column(db.Float(53))
    PowerFactor = db.Column(db.Float(53))
    ActiveEnergyExport = db.Column(db.Float(53))
    ReActiveEnergyExport = db.Column(db.Float(53))
    ProfileStatusEnergy = db.Column(db.Integer)
    ProfileStatusPower = db.Column(db.Integer)


# MeterInfo Schema
class MeterInfoSchema(ma.Schema):
    class Meta:
        fields = ("TimeTag", "ID", "PowerActive", "PowerReactive", "Frequency", "ActiveEnergy",
                  "ReactiveEnergy", "VoltageL1", "VoltageL2", "VoltageL3", "CurrentL1", "CurrentL2",
                  "CurrentL3", "demand", "PowerFactor", "ActiveEnergyExport", "ReActiveEnergyExport",
                  "ProfileStatusEnergy", "ProfileStatusPower")


# init Schema
# meterinfo_schema = MeterInfoSchema(strict=True)
metersinfo_schema = MeterInfoSchema(many=True, strict=True)


# Customer Class/Model
class Customer(db.Model):
    __tablename__ = 'Customer'

    xSubscriptionId_Pk = db.Column(db.BigInteger,primary_key=True, nullable=False)
    xSubscriberLastUpdateDate = db.Column(db.Integer)
    xSubscriberId_pk = db.Column(db.Integer)
    xSubscriptionLogId_fk = db.Column(db.BigInteger)
    xSubscriberFirstName = db.Column(db.String(50))
    xSubscriberLastName = db.Column(db.String(50))
    xSubscriberMobile = db.Column(db.String(11))
    xSubscriptionPostCode = db.Column(db.String(10))
    xSubscriberTelNo = db.Column(db.String(20))
    xSubscriptionAddress = db.Column(db.String(250))
    xSubscriberIsActive = db.Column(db.Boolean)
    xSubscriptionUsageAvg = db.Column(db.Float(53))
    xGISCode = db.Column(db.String(30))
    xSubscriberAddress = db.Column(db.String(250))
    xComunicateAddress = db.Column(db.String(250))
    xDepartmentName = db.Column(db.String(50))
    xFatherName = db.Column(db.String(50))
    xSubscriptionDebit = db.Column(db.BigInteger)
    xCasteName = db.Column(db.String(50))
    xServiceLineName = db.Column(db.String(60))
    xContractPower = db.Column(db.Integer)
    xFaze = db.Column(db.String(1))
    xAmper = db.Column(db.SmallInteger)
    xCounterBuldingNo = db.Column(db.String(20))
    xCounterMultiple = db.Column(db.Float(53))
    xDigitNum = db.Column(db.SmallInteger)
    xDimandmeterDomain = db.Column(db.Integer)
    xCounterTypeName = db.Column(db.String(30))
    xRegionName = db.Column(db.String(50))
    xBranchStateName = db.Column(db.String(25))
    xLongitude = db.Column(db.Float(53))
    xLatitude = db.Column(db.Float(53))
    xSubscriptionLevelName = db.Column(db.String(50))
    xPayDelayCount = db.Column(db.SmallInteger)
    xBakhshName = db.Column(db.String(30))
    xOmorName = db.Column(db.String(60))
    xActiveCounterId_fk = db.Column(db.Integer)
    xUsageTypeName = db.Column(db.String(250))
    xUsageGroupName = db.Column(db.String(100))
    xUsageSubGroupName = db.Column(db.String(50))
    xISIC_Code = db.Column(db.String(10))
    xISIC_Name = db.Column(db.String(100))
    xPrevOutPowerCount = db.Column(db.Integer)
    xPrev3TariffDayNums = db.Column(db.Integer)
    xPrevSureBillCount = db.Column(db.Integer)
    xTariffName = db.Column(db.String(50))


# Customer Schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("xSubscriptionId_Pk", "xSubscriberLastUpdateDate",
                  "xSubscriberId_pk", "xSubscriptionLogId_fk", "xSubscriberFirstName",
                  "xSubscriberLastName", "xSubscriberMobile", "xSubscriptionPostCode",
                  "xSubscriberTelNo", "xSubscriptionAddress", "xSubscriberIsActive",
                  "xSubscriptionUsageAvg", "xGISCode", "xSubscriberAddress", "xComunicateAddress",
                  "xDepartmentName", "xFatherName", "xSubscriptionDebit", "xCasteName", "xServiceLineName",
                  "xContractPower", "xFaze", "xAmper", "xCounterBuldingNo", "xCounterMultiple", "xDigitNum",
                  "xDimandmeterDomain", "xCounterTypeName", "xRegionName", "xBranchStateName", "xLongitude",
                  "xLatitude", "xSubscriptionLevelName", "xPayDelayCount", "xBakhshName", "xOmorName",
                  "xActiveCounterId_fk", "xUsageTypeName", "xUsageGroupName", "xUsageSubGroupName",
                  "xISIC_Code", "xISIC_Name", "xPrevOutPowerCount", "xPrev3TariffDayNums", "xPrevSureBillCount",
                  "xTariffName")


# init Schema
# customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)
