from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os

Category = {
    "CPU": CPU,
    "GPU": GPU,
    "RAM": RAM,
    "MB": MB,
    "DRIVE": DRIVE,
    "FAN": FAN,
    "CASE": CASE,
    "PSU": PSU,
}



basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)




def search(CAT):
    cat_class = Category.get(CAT) 
    
    if not cat_class:
        return jsonify([])

    query = request.args.get("q", "").lower()
    if not query:
        return jsonify([])

    s = Session()

    parts = s.query(cat_class).filter(cat_class.model.ilike(f'%{query}%')).all()
    
    results = [
        {
            "model": p.model,
            "brand": p.brand
        } 
        for p in parts
    ]
    
    s.close()
    return jsonify(results)

