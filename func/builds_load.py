from unicodedata import category
from flask import Flask, jsonify, render_template, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from func.compatibility import compatibility
from func.curent_update import Session, curent_update
from models import GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN, BUILD;
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)





def builds():
    s = Session() 
    try:
        all_builds = s.query(BUILD).all()
        
        if not all_builds:
            return jsonify({"message": "Nenalezena žádná sestava"}), 404
        
        results = []
        for item in all_builds:
           
            build_data = {
                "id": item.id,
                "cpu": item.cpu.model if item.cpu else "N/A",
                "gpu": item.gpu.model if item.gpu else "N/A",
                "mb": item.mb.model if item.mb else "N/A",
                "ram": item.ram.model if item.ram else "N/A",
                "drive": item.drive.model if item.drive else "N/A",
                "fan": item.fan.model if item.fan else "N/A",
                "case": item.case.model if item.case else "N/A",
                "psu": item.psu.model if item.psu else "N/A"
            }
            results.append(build_data)

        return jsonify({"builds": results}), 200

    except Exception as e:
        print(f"Chyba: {e}")
        return jsonify({"message": "Chyba při načítání dat"}), 500
    finally:
        s.close() 
    