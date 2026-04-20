from flask import Flask, render_template, blueprints, request
from flask import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from func.build_del import build_del
from models import BUILD, Base, CPU, GPU, MB, RAM, DRIVE, FAN, CASE, PSU

from func.search import search
from func.table_del import del_table
from func.table_add import add_table
from func.table_upd import upd_table 
from func.build_save import build_save
from func.builds_load import builds
from func.compatibility import compatibility
from func.curent_update import curent_update
from func.table_show import show
from func.curent_update import curent_update



function = blueprints.Blueprint("function", __name__)







@function.route("/api/search/CPU")
def searchCPU():
    return search("CPU")



@function.route("/api/search/GPU")
def searchGPU():
    return search("GPU")



@function.route("/api/search/RAM")
def searchRAM():
    return search("RAM")



@function.route("/api/search/MB")
def searchMB():
    return search("MB")



@function.route("/api/search/DRIVE")
def searchDRIVE():
    return search("DRIVE")



@function.route("/api/search/FAN")
def searchFAN():
    return search("FAN")



@function.route("/api/search/PSU")
def searchPSU():
    return search("PSU")



@function.route("/api/search/CASE")
def searchCASE():
    return search("CASE")


@function.route("/api/current_update", methods=["POST"])
def current_update():
    data = request.get_json()
    return curent_update(data)



@function.route("/api/compare", methods=["POST"])
def compare():
    data = request.get_json()
    return compatibility(data)        



@function.route("/api/add", methods=["POST"])
def add():
    data = request.get_json()
    return add_table(data)   
            


@function.route("/api/del", methods=["POST"])
def delete():
    data = request.get_json()
    return del_table(data)



@function.route("/api/upd", methods=["POST"])
def update():
    data = request.get_json()
    return upd_table(data)



@function.route("/api/show_components", methods=["POST"])
def show_components():
    data = request.get_json()
    return show(data)


  
@function.route("/api/builds")
def show_builds():
    return builds()



@function.route("/api/save_build", methods=["POST"])
def save_build():
    data = request.get_json()
    return build_save(data)


@function.route("/api/build_DELETE", methods=["POST", "GET"])
def del_build():
    data = request.get_json()
    return build_del(data)