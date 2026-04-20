from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)


def curent_update(data):
    data = request.get_json()

    model = data.get("model") 
    brand = data.get("brand")
    category = data.get("type")

    s = Session()

    match category:
        case "CPU":
            part = s.query(CPU).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            curent_socket = part.socket
            curent_usage = part.usage

            return jsonify({"curent_socket": curent_socket, "curent_usage": curent_usage, "test": "uspesne nahrano"}), 200

        case "GPU":
            part = s.query(GPU).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            curent_lenght = part.lenght
            curent_slots = part.slots
            curent_usage = part.usage

            return jsonify({"curent_lenght": curent_lenght, "curent_slots": curent_slots, "curent_usage": curent_usage, "test": "uspesne nahrano"}), 200

        case "RAM":
            part = s.query(RAM).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            curent_type = part.type
            curent_usage = part.usage

            return jsonify({"curent_type": curent_type, "curent_usage": curent_usage, "test": "uspesne nahrano"}), 200

        case "MB":
            part = s.query(MB).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            curent_socket = part.socket
            curent_ram = part.ram
            curent_type = part.type
            curent_drive = part.drive
            
            return jsonify({"curent_socket": curent_socket, "curent_ram": curent_ram, "curent_type": curent_type, "curent_drive": curent_drive, "test": "uspesne nahrano"}), 200

        case "DRIVE":
            part = s.query(DRIVE).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            curent_type = part.type
            curent_usage = part.usage

            return jsonify({"curent_type": curent_type, "curent_usage": curent_usage, "test": "uspesne nahrano"}), 200

        case "FAN":
            part = s.query(FAN).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400   

            curent_usage = part.usage
            curent_socket = part.socket
            curent_height = part.height

            return jsonify({"curent_usage": curent_usage, "curent_socket": curent_socket, "curent_height": curent_height, "test": "uspesne nahrano"}), 200

        case "PSU":
            part = s.query(PSU).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400
            
            curent_wattage = part.wattage

            return jsonify({"curent_wattage": curent_wattage, "test": "uspesne nahrano"}), 200

        case "CASE":
            part = s.query(CASE).filter_by(model=model, brand=brand).first()

            if not part:
                return jsonify({"result": "neplatny model nebo znacka"}), 400
            
            curent_slots = part.slots
            curent_mb_type = part.mb_type
            curent_gpu_lenght = part.gpu_lenght
            curent_fan_height = part.fan_height

            return jsonify({"curent_slots": curent_slots, "curent_mb_type": curent_mb_type, "curent_gpu_lenght": curent_gpu_lenght, "curent_fan_height": curent_fan_height, "test": "uspesne nahrano"}), 200


        case _:
            return jsonify({"result": "neplatna kategorie"}), 400
