from flask import jsonify
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from models import BUILD
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)


def build_del(data):

    s = Session()

    builds_id = data.get("id_build")
    build = s.query(BUILD).filter(BUILD.id == builds_id).first()
    if build:
        s.delete(build)
        s.commit()
        s.close()
        return jsonify({"message": "Sestava smazána"}), 200
    else:
        s.close()
        return jsonify({"message": "Sestava nenalezena"}), 404



   
    
    
