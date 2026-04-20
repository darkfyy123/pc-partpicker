from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CPU(Base):
    __tablename__ = "CPU"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    socket = Column(String, nullable=False)
    usage = Column(Integer, nullable=False)



class GPU(Base):
    __tablename__ = "GPU"
    
    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    slots = Column(Integer, nullable=False)
    usage = Column(Integer, nullable=False)


class MB(Base):
    __tablename__ = "MB"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    socket = Column(String, nullable=False)
    ram = Column(String, nullable=False)
    type = Column(String, nullable=False)
    drive = Column(String, nullable=False)


class RAM(Base):
    __tablename__ = "RAM"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    type = Column(String, nullable=False)
    usage = Column(Integer, nullable=False)


class DRIVE(Base):
    __tablename__ = "DRIVE"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    type = Column(String, nullable=False)
    usage = Column(Integer, nullable=False)


class FAN(Base):
    __tablename__ = "FAN"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    socket = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    usage = Column(Integer, nullable=False)


class PSU(Base):
    __tablename__ = "PSU"

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    wattage = Column(Integer, nullable=False)


class CASE(Base):
    __tablename__ = "CASE"

    id = Column(Integer, primary_key=True)     
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)  
    slots = Column(Integer, nullable=False)
    mb_type = Column(String, nullable=False)
    gpu_length = Column(Integer, nullable=False)
    fan_height = Column(Integer, nullable=False)









class BUILD(Base):
    __tablename__ = "BUILD"

    id = Column(Integer, primary_key=True)
    cpu_id = Column(Integer, ForeignKey("CPU.id"), nullable=False)
    gpu_id = Column(Integer, ForeignKey("GPU.id"), nullable=False)
    mb_id = Column(Integer, ForeignKey("MB.id"), nullable=False)
    ram_id = Column(Integer, ForeignKey("RAM.id"), nullable=False)
    drive_id = Column(Integer, ForeignKey("DRIVE.id"), nullable=False)
    fan_id = Column(Integer, ForeignKey("FAN.id"), nullable=False)
    case_id = Column(Integer, ForeignKey("CASE.id"), nullable=False)
    psu_id = Column(Integer, ForeignKey("PSU.id"), nullable=False)


    cpu = relationship("CPU")
    gpu = relationship("GPU")
    mb = relationship("MB")
    ram = relationship("RAM")
    drive = relationship("DRIVE")
    fan = relationship("FAN")
    case = relationship("CASE")
    psu = relationship("PSU")








