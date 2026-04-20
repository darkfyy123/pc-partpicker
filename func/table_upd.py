from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)






def upd_table(data):

    for klic, hodnota in data.items():
        if hodnota == "":
            return jsonify({"result": f"Pole {klic} je prázdné!"})
    

    
    type_comp = data.get('type')

    brand = data.get('brand')
    model = data.get('model')

    s = Session()
    
    match type_comp:

        case "CPU":
           
  
            socket_cpu = data.get('cpu_socket')
            cpu_usage = data.get('cpu_usage')

            item_to_update = s.query(CPU).filter(CPU.model == model, CPU.brand == brand).first()
            if item_to_update:
                item_to_update.socket = socket_cpu
                item_to_update.usage = cpu_usage
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200

        case "GPU":

            gpu_lenght = data.get('gpu_lenght')
            gpu_slots = data.get('gpu_slots')
            gpu_usage = data.get('gpu_usage')


            item_to_update = s.query(GPU).filter(GPU.model == model, GPU.brand == brand).first()
            if item_to_update:
                item_to_update.lenght = gpu_lenght
                item_to_update.slots = gpu_slots
                item_to_update.usage = gpu_usage
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        

        case "RAM":

            ram_type = data.get('ram_type')
            ram_usage = data.get('ram_usage')

            item_to_update = s.query(RAM).filter(RAM.model == model, RAM.brand == brand).first()
            if item_to_update:
                item_to_update.type = ram_type
                item_to_update.usage = ram_usage
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        
        case "MB":

            mb_socket = data.get('mb_socket')
            mb_ram = data.get('mb_ram')
            mb_type = data.get('mb_type')
            mb_drive = data.get('mb_drive')


            item_to_update = s.query(MB).filter(MB.model == model, MB.brand == brand).first()
            if item_to_update:
                item_to_update.socket = mb_socket
                item_to_update.ram = mb_ram
                item_to_update.type = mb_type
                item_to_update.drive = mb_drive
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()   
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        
        case "FAN":

            fan_usage = data.get('fan_usage')
            fan_socket = data.get('fan_socket')
            fan_height = data.get('fan_height')
            fan_usage = data.get('fan_usage')


            item_to_update = s.query(FAN).filter(FAN.model == model, FAN.brand == brand).first()
            if item_to_update:
                item_to_update.usage = fan_usage
                item_to_update.socket = fan_socket
                item_to_update.height = fan_height
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        
        case "CASE":

            case_slots = data.get('case_slots')
            case_mb_type = data.get('case_mb_type')
            case_gpu_lenght = data.get('case_gpu_lenght')
            case_fan_height = data.get('case_fan_height')


            item_to_update = s.query(CASE).filter(CASE.model == model, CASE.brand == brand).first()
            if item_to_update:
                item_to_update.slots = case_slots
                item_to_update.mb_type = case_mb_type
                item_to_update.gpu_lenght = case_gpu_lenght
                item_to_update.fan_height = case_fan_height
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
            
        case "DRIVE":

            drive_type = data.get('drive_type')
            drive_usage = data.get('drive_usage')


            item_to_update = s.query(DRIVE).filter(DRIVE.model == model, DRIVE.brand == brand).first()
            if item_to_update:
                item_to_update.type = drive_type
                item_to_update.usage = drive_usage
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()
            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        
        case "PSU":

            psu_wattage = data.get('psu_wattage')


            item_to_update = s.query(PSU).filter(PSU.model == model, PSU.brand == brand).first()
            if item_to_update:
                item_to_update.wattage = psu_wattage
            else:
                return jsonify({"result": "neplatny model nebo znacka"}), 400

            s.commit()
            s.close()

            

            result = "uspesne nahrano"
            return jsonify({"result": result}), 200
        
        case _:

            
            result = "spatne zadany typ"
            return jsonify({"result": result}), 400
        
   



