from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import BUILD, GPU,CPU,RAM,MB,CASE,DRIVE,PSU,FAN
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)


def build_save(data):
    session = Session()
    
    cpu = session.query(CPU).filter_by(model=data.get("CPU")).first()
    gpu = session.query(GPU).filter_by(model=data.get("GPU")).first()
    ram = session.query(RAM).filter_by(model=data.get("RAM")).first()
    mb = session.query(MB).filter_by(model=data.get("MB")).first()
    case = session.query(CASE).filter_by(model=data.get("CASE")).first()
    drive = session.query(DRIVE).filter_by(model=data.get("DRIVE")).first()
    psu = session.query(PSU).filter_by(model=data.get("PSU")).first()
    fan = session.query(FAN).filter_by(model=data.get("FAN")).first()

   

    new_build = BUILD(
        cpu_id=cpu.id, 
        gpu_id=gpu.id, 
        ram_id=ram.id, 
        mb_id=mb.id,
        case_id=case.id, 
        drive_id=drive.id, 
        psu_id=psu.id, 
        fan_id=fan.id
        )

        
    try:
        session.add(new_build)
        session.commit()
    except Exception as e:
        session.rollback()
        return jsonify({"message": "Error saving build!"}), 500
    finally:
        session.close()
    return jsonify({"message": "Build saved successfully!"}), 200

