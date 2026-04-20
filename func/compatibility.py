from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine 
from sqlalchemy.orm import Session, sessionmaker
from models import CPU, GPU, RAM, MB, CASE, DRIVE, PSU, FAN
import json
import os 


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(os.path.dirname(basedir), "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)


def compatibility(data):

    
    test = []
    categories = ["CPU", "MB", "RAM", "DRIVE", "GPU", "PSU", "CASE", "FAN"]
    Missing = "Chybějící komponenty"
    s = Session()

        
    cpu_socket = cpu_usage = mb_socket = mb_ram_type = mb_disk_type = mb_type = case_mb_size = case_slots = case_gpu_length = case_fan_height = ram_type = ram_speed = ram_usage = disk_type = drive_usage = gpu_length = gpu_slots = gpu_usage = psu_wattage = fan_usage = fan_socket = fan_height = None


    for key in data.keys():
        match key:

            case "CPU":
                
                cpu = s.query(CPU).filter_by(model=data.get("CPU")).first()
                if cpu: 
                    cpu_socket = cpu.socket
                    cpu_usage = cpu.usage

                    test.append("CPU")
            
            case "MB":
                
                mb = s.query(MB).filter_by(model=data.get("MB")).first()
                if mb:
                    mb_socket = mb.socket
                    mb_ram_type = mb.ram
                    mb_disk_type = mb.drive
                    mb_type = mb.type

                    test.append("MB")

            case "RAM":
               
                ram = s.query(RAM).filter_by(model=data.get("RAM")).first()
                if ram:
                    ram_type = ram.type
                    ram_usage = ram.usage

                test.append("RAM")

            case "DRIVE":
                
                drive = s.query(DRIVE).filter_by(model=data.get("DRIVE")).first()
                if drive:
                    disk_type = drive.type
                    drive_usage = drive.usage

                    test.append("DRIVE")

            case "GPU":
               
                gpu = s.query(GPU).filter_by(model=data.get("GPU")).first()
                if gpu:
                    gpu_length = gpu.length
                    gpu_slots = gpu.slots
                    gpu_usage = gpu.usage

                    test.append("GPU")

            case "PSU":
               
                psu = s.query(PSU).filter_by(model=data.get("PSU")).first()
                if psu:
                    psu_wattage = psu.wattage

                    test.append("PSU")

            case "CASE":
                
                case = s.query(CASE).filter_by(model=data.get("CASE")).first()
                if case:
                    case_mb_size = case.mb_type
                    case_slots = case.slots
                    case_gpu_length = case.gpu_length
                    case_fan_height = case.fan_height

                    test.append("CASE")

            case "FAN":
                
                fan = s.query(FAN).filter_by(model=data.get("FAN")).first()
                if fan:
                    fan_usage = fan.usage
                    fan_socket = fan.socket
                    fan_height = fan.height

                    test.append("FAN")

            case _:
                pass
        
    s.close()
    
    for p in categories:
        if p not in test:
            Missing += f" {p}"

    if Missing != "Chybějící komponenty":
        return jsonify({"missing": Missing})        




    if cpu_socket and mb_socket:
        if cpu_socket == mb_socket:
            socket_compatibility = True
        else:
            socket_compatibility = False

    if mb_ram_type and ram_type:
        if mb_ram_type == ram_type:
            ram_compatibility = True
        else:
            ram_compatibility = False
    
    if mb_disk_type and disk_type:
        if mb_disk_type == disk_type:
            disk_compatibility = True
        else:
            disk_compatibility = False

    if mb_type and case_mb_size:
        if mb_type == case_mb_size:
            mb_case_compatibility = True
        else:
            mb_case_compatibility = False

    if gpu_length and case_gpu_length:
        if gpu_length <= case_gpu_length:
            gpu_case_compatibility = True
        else:
            gpu_case_compatibility = False
    
    if fan_height and case_fan_height:
        if fan_height <= case_fan_height:
            fan_case_compatibility = True
        else:
            fan_case_compatibility = False

    if gpu_slots and case_slots:
        if gpu_slots <= case_slots:
            gpu_case_slots_compatibility = True
        else:
            gpu_case_slots_compatibility = False
    
    if fan_socket and cpu_socket:
        if fan_socket == cpu_socket:
            fan_cpu_compatibility = True
        else:
            fan_cpu_compatibility = False

    if cpu_usage and ram_usage and drive_usage and gpu_usage and fan_usage and psu_wattage:

        total_usage = int(cpu_usage) + int(ram_usage) + int(drive_usage) + int(gpu_usage) + int(fan_usage)
        total_usage = total_usage * 1.2 

        if psu_wattage:
            if psu_wattage >= total_usage:
                wattage_compatibility = True
            else:
                wattage_compatibility = False 


    compatibility_result = {
        "socket_compatibility": socket_compatibility,
        "ram_compatibility": ram_compatibility,
        "disk_compatibility": disk_compatibility,
        "mb_case_compatibility": mb_case_compatibility,
        "gpu_case_compatibility": gpu_case_compatibility,
        "fan_case_compatibility": fan_case_compatibility,
        "gpu_case_slots_compatibility": gpu_case_slots_compatibility, 
        "wattage_compatibility": wattage_compatibility, 
        "fan_cpu_compatibility": fan_cpu_compatibility 
    }       


    return jsonify(compatibility_result), 200
            