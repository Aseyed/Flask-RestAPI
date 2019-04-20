# coding: utf-8
from flask import Flask
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import __name__ as app_name

# init app
app = Flask(app_name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3113@localhost/myELEC'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)


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


# init ma
ma = Marshmallow(app)


# MeterInfo Schema
class MeterInfoSchema(ma.Schema):
    class Meta:
        fields = ("TimeTag", "ID", "PowerActive", "PowerReactive", "Frequency", "ActiveEnergy",
                  "ReactiveEnergy", "VoltageL1", "VoltageL2", "VoltageL3", "CurrentL1", "CurrentL2",
                  "CurrentL3", "demand", "PowerFactor", "ActiveEnergyExport", "ReActiveEnergyExport",
                  "ProfileStatusEnergy", "ProfileStatusPower")

# init Schema
meterinfo_schema = MeterInfoSchema(strict=True)
meterinfos_schema = MeterInfoSchema(many=True, strict=True)
