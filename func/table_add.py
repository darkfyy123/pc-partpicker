from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)






def add_table(data):

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

            new_item = CPU(model=model, socket=socket_cpu, brand=brand, usage=cpu_usage)


        case "GPU":

            gpu_length = data.get('gpu_length')
            gpu_slots = data.get('gpu_slots')
            gpu_usage = data.get('gpu_usage')


            new_item = GPU(model=model, brand=brand, length=gpu_length, slots=gpu_slots, usage=gpu_usage)


  

        case "RAM":

            ram_type = data.get('ram_type')
            ram_usage = data.get('ram_usage')

            new_item = RAM(model=model, type=ram_type, usage=ram_usage, brand=brand)
     

 
        case "MB":

            mb_socket = data.get('mb_socket')
            mb_ram = data.get('mb_ram')
            mb_type = data.get('mb_type')
            mb_drive = data.get('mb_drive')


            new_item = MB(model=model, socket=mb_socket, ram=mb_ram, type=mb_type, drive=mb_drive, brand=brand)


        case "FAN":

            fan_usage = data.get('fan_usage')
            fan_socket = data.get('fan_socket')
            fan_height = data.get('fan_height')
            fan_usage = data.get('fan_usage')


            new_item = FAN(model=model, usage=fan_usage, socket=fan_socket, height=fan_height, brand=brand)

 
        case "CASE":

            case_slots = data.get('case_slots')
            case_mb_type = data.get('case_mb_type')
            case_gpu_length = data.get('case_gpu_length')
            case_fan_height = data.get('case_fan_height')


            new_item = CASE(model=model, slots=case_slots, mb_type=case_mb_type, gpu_length=case_gpu_length, fan_height=case_fan_height, brand=brand)

 
        case "DRIVE":

            drive_type = data.get('drive_type')
            drive_usage = data.get('drive_usage')


            new_item = DRIVE(model=model, type=drive_type, usage=drive_usage, brand=brand)



        case "PSU":

            psu_wattage = data.get('psu_wattage')


            new_item = PSU(model=model, wattage=psu_wattage)


        case _:

            return jsonify({"result": "Neplatný typ komponentu!"})


    if new_item:
        s.add(new_item)
        s.commit()
        s.close()
        return jsonify({"result": "Komponenta úspěšně přidána!"}), 200
    else:
        return jsonify({"result": "Komponenta nebyla přidána!"}), 400




