from unicodedata import category
from flask import Flask, jsonify, render_template, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from func.compatibility import compatibility
from func.curent_update import curent_update
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)




def show(data):
    category = data.get("category")


    model_map = {
        "CPU": CPU, "GPU": GPU, "RAM": RAM, "MB": MB,
        "CASE": CASE, "DRIVE": DRIVE, "PSU": PSU, "FAN": FAN
    }

    
    session = Session() 
    
    
    model_cat = model_map.get(category)
        
    if not model_cat:
        return jsonify({"error": "Category not found"}), 400

       
    components_list = session.query(model_cat).all()

    results = []
    for item in components_list:
            component_data = {col.name: getattr(item, col.name) for col in item.__table__.columns}
            results.append(component_data)

    return jsonify({
            "category": category,
            "count": len(results),
            "components": results
    }), 200