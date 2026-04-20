from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
from func.search import search
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)









def del_table(data):
    

    brand = data.get('Brand')
    model = data.get('Model')
    item_type = data.get('Type')
    
    
    database = {
        "CPU":CPU,
        "GPU":GPU,
        "MB":MB,
        "RAM":RAM,
        "FAN":FAN,
        "DRIVE":DRIVE,
        "CASE":CASE,
        "PSU":PSU,
    }

    s = Session()

    data_type = database.get(item_type)

    for klic, hodnota in data.items():
        if (hodnota == ""):
            return jsonify({"result": f"Pole {klic} je prázdné!"})




    if (data_type):
        item_to_delete = s.query(data_type).filter(data_type.model == model, data_type.brand == brand).first()
        
        if (item_to_delete):
            s.delete(item_to_delete)
            s.commit()
            s.close()
  
            return jsonify({"result":"Komponenta odstraněna!"}), 200
            
        else:
            
            return jsonify({"result":"Komponenta nenalezena!"}), 404

   
