#!/usr/bin/env python
"""
usage: $ HD.py <input_filename>
"""
import sys
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import math
import matplotlib.patches as mpatches
import scipy
from operator import contains
import itertools

comp_out_walls = []
ext_walls_against_tech=[]
ext_walls_shops_tech=[]
wall_against_shelter=[]
ext_wall5=[]
ext_wall6=[]
ext_wall7=[]
ext_wall8=[]
floor_against_shelter=[]
floor_against_exterior=[]
comp_out_floor_against_tech=[]
floor4=[]
floor5=[]
comp_out_roof=[]
roof2=[]
roof3=[]
components_in_wall = []
components_in_wall_emb=[]
components_in_ceiling=[]
components_in_ceiling_emb=[]
components_in_floor=[]
components_in_floor2=[]
components_in_floor3=[]
components_in_floor_emb=[]
components_in_floor_emb2=[]
components_in_floor_emb3=[]
windows_out_vertical=[]
windows_out_horizontal=[]
ext_wall_finish=[]
int_wall_finish=[]
roof_cover=[]
roof_finish=[]
floor_cover=[]
partition=[]
windows_emb=[]
electr_equip=[]
heat_gen=[]
heat_distr=[]
vent_system=[]
water_system=[]
operation_impact=[]
insulation=[]
insulation_roof=[]
insulation_floor=[]
external_render_plaster=[]
New_components=[]
New_components_roof=[]
New_components_floor=[]
New_components_against_unheated=[]
Heating_system=[]
Maintenance_LCC=[]

filename = sys.argv[-1] # Read filename from CLI, assume only one
#
with open(filename, "r") as f:
    Building_category=float(f.readline())
    room_temperature=float(f.readline())
    number_people=int(f.readline())
    occupation_time=float(f.readline())
    city=int(f.readline())
    build_case=int(f.readline())
    constr_method=int(f.readline())
    thermal_bridge=float(f.readline())
    room_regulation=int(f.readline())
    EBF=float(f.readline())
    vent_type=int(f.readline())
    Air_flow_therm_eff1=float(f.readline())
    preheat_air=int(f.readline())
    heat_rec=int(f.readline())
    heat_rec_eff=float(f.readline())
    room_number=int(f.readline())
    inflation_rate=float(f.readline())
    electricity_cost=float(f.readline())
    heating_cost=float(f.readline())
    price_growth_el=float(f.readline())
    price_growth_heating=float(f.readline())
    interest_rate=float(f.readline())
    timeperiod=float(f.readline())
    perf_loss_ext_walls=float(f.readline())
    perf_loss_roofs=float(f.readline())
    perf_loss_floor=float(f.readline())
    perf_loss_comp_in=float(f.readline())
    perf_loss_wind_vert=float(f.readline())
    perf_loss_wind_hor=float(f.readline())
    perf_loss_heat_rec=float(f.readline())
    perf_loss_ext_walls_new=float(f.readline())
    perf_loss_roofs_new=float(f.readline())
    perf_loss_floor_new=float(f.readline())
    perf_loss_wind_vert_new=float(f.readline())
    perf_loss_heat_rec_new=float(f.readline())
    final_energy_losses=float(f.readline())
    final_energy_losses_new= float(f.readline())
    Air_flow_therm_eff_new=float(f.readline())
    heat_rec_eff_new=float(f.readline())
    preheat_air_new=int(f.readline())
    heat_rec_new=int(f.readline())
    thermal_bridge_new=float(f.readline())
    heating_cost_new=float(f.readline())
    heating_type = float(f.readline())
    heating_type_new = float(f.readline())
    vent_type_new=float(f.readline())
    f.readline()
    line = f.readline()
    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        comp_out_walls.append(data)
        line = f.readline()
    line = f.readline()   
    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_walls_against_tech.append(data)
        line = f.readline()
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_walls_shops_tech.append(data)
        line = f.readline()
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        wall_against_shelter.append(data)
        line = f.readline()
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_wall5.append(data)
        line = f.readline()
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_wall6.append(data)
        line = f.readline()
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_wall7.append(data)
        line = f.readline()        
    line = f.readline()  

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_walls": float(values[2]),
            "thickness_walls": float(values[3])
        }
        ext_wall8.append(data)
        line = f.readline()

    line = f.readline()
    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_roof": float(values[2]),
            "thickness_roof": float(values[3])
        }
        comp_out_roof.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_roof": float(values[2]),
            "thickness_roof": float(values[3])
        }
        roof2.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_roof": float(values[2]),
            "thickness_roof": float(values[3])
        }
        roof3.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_floor": float(values[2]),
            "thickness_floor": float(values[3])
        }
        comp_out_floor_against_tech.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_floor": float(values[2]),
            "thickness_floor": float(values[3])
        }
        floor4.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_floor": float(values[2]),
            "thickness_floor": float(values[3])
        }
        floor5.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_floor": float(values[2]),
            "thickness_floor": float(values[3])
        }
        floor_against_shelter.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type": values[0],
            "Area": float(values[1]),
            "lambda_floor": float(values[2]),
            "thickness_floor": float(values[3])
        }
        floor_against_exterior.append(data)
        line = f.readline()
    line = f.readline()
    while not line.startswith("="):
        values = line.split()
        data = {
            "Type_in": values[0],
            "Area_in": float(values[1]),
            "lambda_in": float(values[2]),
            "thickness_in": float(values[3]),
            "b-value": float(values[4])
        }
        components_in_wall.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type_in": values[0],
            "Area_in": float(values[1]),
            "lambda_in": float(values[2]),
            "thickness_in": float(values[3]),
            "b-value": float(values[4])
        }
        components_in_ceiling.append(data)
        line = f.readline()
    line = f.readline()
        
    while not line.startswith("="):
        values = line.split()
        data = {
            "Type_in": values[0],
            "Area_in": float(values[1]),
            "lambda_in": float(values[2]),
            "thickness_in": float(values[3]),
            "b-value": float(values[4])
        }
        components_in_floor.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type_in": values[0],
            "Area_in": float(values[1]),
            "lambda_in": float(values[2]),
            "thickness_in": float(values[3]),
            "b-value": float(values[4])
        }
        components_in_floor2.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Type_in": values[0],
            "Area_in": float(values[1]),
            "lambda_in": float(values[2]),
            "thickness_in": float(values[3]),
            "b-value": float(values[4])
        }
        components_in_floor3.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Orientation": values[0],
            "Area_wind": float(values[1]),
            "UValue_wind": float(values[2]),
            "gvalue_wind": float(values[3]),
            "glass_perc": float(values[4]),
            "hor": int(values[5]),
            "over": int(values[6]),
            "side1": int(values[7]),
            "side2": int(values[8]),
            "coef1": float(values[9]),
            "coef2": float(values[10]),
            "coef3": float(values[11]),
            "coef4": float(values[12]),
            "UValue_wind_new": float(values[13]),
            "gvalue_wind_new": float(values[14]),
            "glass_perc_new": float(values[15]),
            "type": float(values[16]),
            "RSL": float(values[17]),
            "Uncertainty_GWP": float(values[18]),
            "Uncertainty_cost": float(values[19]),
            "Uncertainty_U-value": float(values[20])
        }
        windows_out_vertical.append(data)
        line = f.readline()
    line = f.readline()

    while not line.startswith("="):
        values = line.split()
        data = {
            "Area_wind_h": float(values[0]),
            "U-Value_wind_h": float(values[1]),
            "g-value_wind_h": float(values[2]),
            "glass_perc_h": float(values[3]),
            "HorizonS": int(values[4]),
            "HorizonW": int(values[5]),
            "HorizonO": int(values[6]),
            "HorizonN": int(values[7]),
            "U-Value_wind_h_new": float(values[8]),
            "g-value_wind_h_new": float(values[9]),
            "glass_perc_h_new": float(values[10]),            
        }
        windows_out_horizontal.append(data)
        line = f.readline()
    line = f.readline()

#New component types exterior walls

    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Type": float(values[1]),
            "Insulation thickness": float(values[2]),
            "RSL": float(values[3]),
            "Uncertainty_GWP": float(values[4]),
            "Uncertainty_cost": float(values[5]),
            "Uncertainty_conductivity": float(values[6])
        }
        New_components.append(data)
        line = f.readline()
    line = f.readline()

#New component types roofs
    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Type": float(values[1]),
            "Insulation thickness": float(values[2]),
            "RSL": float(values[3]),
            "Uncertainty_GWP": float(values[4]),
            "Uncertainty_cost": float(values[5]),
            "Uncertainty conductivity roof":float(values[6])
        }
        New_components_roof.append(data)
        line = f.readline()
    line = f.readline()

#New component types ground floor
    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Type": float(values[1]),
            "Insulation thickness": float(values[2]),
            "RSL": float(values[3]),
            "Uncertainty_GWP": float(values[4]),
            "Uncertainty_cost": float(values[5]),
            "Uncertainty conductivity": float(values[6])
        }
        New_components_floor.append(data)
        line = f.readline()
    line = f.readline()

#Components against unheated
    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Type": float(values[1]),
            "Insulation thickness": float(values[2]),
            "RSL": float(values[3]),
            "Uncertainty_GWP": float(values[4]),
            "Uncertainty_cost": float(values[5])
        }
        New_components_against_unheated.append(data)
        line = f.readline()
    line = f.readline()

#Heat generation
    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Type": float(values[1]),
            "Embodied_GWP_heat_generation": float(values[2]),
            "GWP production": float(values[3]),
            "Initial_cost_heat_generation": float(values[4]),
            "Cost production": float(values[5]),
            "RSL": float(values[6]),
            "Price growth rate heating": float(values[7])
        }
        Heating_system.append(data)
        line = f.readline()
    line = f.readline()
#Maintenance LCC
    while not line.startswith("="):
        values = line.split()
        data = {
            "Description": str(values[0]),
            "Maintenance_LCC": float(values[1]),
        }
        Maintenance_LCC.append(data)
        line = f.readline()
    line = f.readline()

#Internal wall finish (G3)
    while not line.startswith("="):
        values = line.split()
        data = {
            "int_wall_finish_type": int(values[0]),
            "int_wall_finish_Pr_GWP": float(values[1]),
            "int_wall_finish_EoL_GWP": float(values[2]),
            "int_wall_finish_Pr_PE": float(values[3]),
            "int_wall_finish_EoL_PE": float(values[4]),
            "int_wall_finish_Pr_UBP": float(values[5]),
            "int_wall_finish_EoL_UBP": float(values[6]),
            "int_wall_finish_RSL": float(values[7]),
            "int_wall_finish_cost": float(values[8]),
            "int_wall_finish_cost_change": float(values[9]),
            "description": str(values[10])
        }
        int_wall_finish.append(data)
        line = f.readline()
    line = f.readline()
#Roof cover (F1)
    while not line.startswith("="):
        values = line.split()
        data = {
            "roof_cover_type": int(values[0]),
            "roof_cover_Pr_GWP": float(values[1]),
            "roof_cover_EoL_GWP": float(values[2]),
            "roof_cover_Pr_PE": float(values[3]),
            "roof_cover_EoL_PE": float(values[4]),
            "roof_cover_Pr_UBP": float(values[5]),
            "roof_cover_EoL_UBP": float(values[6]),
            "roof_cover_RSL": int(values[7]),
            "roof_cover_cost": float(values[8]),
            "roof_cover_cost_change": float(values[9]),
            "roof_cover_RSL_new": int(values[10]),
            "description": str(values[11])
        }
        roof_cover.append(data)
        line = f.readline()
    line = f.readline()
#Roof finish (inside) G4
    while not line.startswith("="):
        values = line.split()
        data = {
            "roof_finish_type": int(values[0]),
            "roof_finish_Pr_GWP": float(values[1]),
            "roof_finish_EoL_GWP": float(values[2]),
            "roof_finish_Pr_PE": float(values[3]),
            "roof_finish_EoL_PE": float(values[4]),
            "roof_finish_Pr_UBP": float(values[5]),
            "roof_finish_EoL_UBP": float(values[6]),
            "roof_finish_RSL": float(values[7]),
            "roof_finish_cost": float(values[8]),
            "roof_finish_cost_change": float(values[9]),
            "description": str(values[10])
        }
        roof_finish.append(data)
        line = f.readline()
    line = f.readline()
#Floor cover (G2)
    while not line.startswith("="):
        values = line.split()
        data = {
            "floor_cover_type": int(values[0]),
            "floor_cover_Pr_GWP": float(values[1]),
            "floor_cover_EoL_GWP": float(values[2]),
            "floor_cover_Pr_PE": float(values[3]),
            "floor_cover_EoL_PE": float(values[4]),
            "floor_cover_Pr_UBP": float(values[5]),
            "floor_cover_EoL_UBP": float(values[6]),
            "floor_cover_RSL": float(values[7]),
            "floor_cover_cost": float(values[8]),
            "floor_cover_cost_change": float(values[9]),
            "floor_cover_RSL_new": float(values[10]),
            "description": str(values[11])
        }
        floor_cover.append(data)
        line = f.readline()
    line = f.readline()
#Partition wall (G1)
    while not line.startswith("="):
        values = line.split()
        data = {
            "partition_type": int(values[0]),
            "partition_Pr_GWP": float(values[1]),
            "partition_EoL_GWP": float(values[2]),
            "partition_Pr_PE": float(values[3]),
            "partition_EoL_PE": float(values[4]),
            "partition_Pr_UBP": float(values[5]),
            "partition_EoL_UBP": float(values[6]),
            "partition_RSL": float(values[7]),
            "partition_cost": float(values[8]),
            "partition_cost_change": float(values[9]),
            "description": str(values[10])
        }
        partition.append(data)
        line = f.readline()
    line = f.readline()

#walls against unheated 
    while not line.startswith("="):
        values = line.split()
        data = {
            "comp_in_wall_type": int(values[0]),
            "comp_in_wall_Pr_GWP": float(values[1]),
            "comp_in_wall_EoL_GWP": float(values[2]),
            "comp_in_wall_Pr_PE": float(values[3]),
            "comp_in_wall_EoL_PE": float(values[4]),
            "comp_in_wall_Pr_UBP": float(values[5]),
            "comp_in_wall_EoL_UBP": float(values[6]),
            "comp_in_wall_RSL": float(values[7]),
            "comp_in_wall_cost": float(values[8]),
            "comp_in_wall_cost_change": float(values[9]),
            "description": str(values[10])
        }
        components_in_wall_emb.append(data)
        line = f.readline()
    line = f.readline()

#ceiling against unheated 
    while not line.startswith("="):
        values = line.split()
        data = {
            "comp_in_ceiling_type": int(values[0]),
            "comp_in_ceiling_Pr_GWP": float(values[1]),
            "comp_in_ceiling_EoL_GWP": float(values[2]),
            "comp_in_ceiling_Pr_PE": float(values[3]),
            "comp_in_ceiling_EoL_PE": float(values[4]),
            "comp_in_ceiling_Pr_UBP": float(values[5]),
            "comp_in_ceiling_EoL_UBP": float(values[6]),
            "comp_in_ceiling_RSL": float(values[7]),
            "comp_in_ceiling_cost": float(values[8]),
            "comp_in_ceiling_cost_change": float(values[9]),
            "description": str(values[10])
        }
        components_in_ceiling_emb.append(data)
        line = f.readline()
    line = f.readline()

#floor against unheated 
    while not line.startswith("="):
        values = line.split()
        data = {
            "comp_in_floor_type": int(values[0]),
            "comp_in_floor_Pr_GWP": float(values[1]),
            "comp_in_floor_EoL_GWP": float(values[2]),
            "comp_in_floor_Pr_PE": float(values[3]),
            "comp_in_floor_EoL_PE": float(values[4]),
            "comp_in_floor_Pr_UBP": float(values[5]),
            "comp_in_floor_EoL_UBP": float(values[6]),
            "comp_in_floor_RSL": float(values[7]),
            "comp_in_floor_cost": float(values[8]),
            "comp_in_floor_cost_change": float(values[9]),
            "description": str(values[10])
        }
        components_in_floor_emb.append(data)
        line = f.readline()
    line = f.readline()

#floor agains unheated 2
    while not line.startswith("="):
        values = line.split()
        data = {
            "comp_in_floor_type": int(values[0]),
            "comp_in_floor_Pr_GWP": float(values[1]),
            "comp_in_floor_EoL_GWP": float(values[2]),
            "comp_in_floor_Pr_PE": float(values[3]),
            "comp_in_floor_EoL_PE": float(values[4]),
            "comp_in_floor_Pr_UBP": float(values[5]),
            "comp_in_floor_EoL_UBP": float(values[6]),
            "comp_in_floor_RSL": float(values[7]),
            "comp_in_floor_cost": float(values[8]),
            "comp_in_floor_cost_change": float(values[9]),
            "description": str(values[10])
        }
        components_in_floor_emb2.append(data)
        line = f.readline()
    line = f.readline()

#floor against unheated3
    while not line.startswith("="):
        values = line.split()
        data = {
            "comp_in_floor_type": int(values[0]),
            "comp_in_floor_Pr_GWP": float(values[1]),
            "comp_in_floor_EoL_GWP": float(values[2]),
            "comp_in_floor_Pr_PE": float(values[3]),
            "comp_in_floor_EoL_PE": float(values[4]),
            "comp_in_floor_Pr_UBP": float(values[5]),
            "comp_in_floor_EoL_UBP": float(values[6]),
            "comp_in_floor_RSL": float(values[7]),
            "comp_in_floor_cost": float(values[8]),
            "comp_in_floor_cost_change": float(values[9]),
            "description": str(values[10])
        }
        components_in_floor_emb3.append(data)
        line = f.readline()
    line = f.readline()

#Electric_equipment(D1)
    while not line.startswith("="):
        values = line.split()
        data = {
            "el_equip_type": int(values[0]),
            "el_equip_Pr_GWP": float(values[1]),
            "el_equip_EoL_GWP": float(values[2]),
            "el_equip_Pr_PE": float(values[3]),
            "el_equip_EoL_PE": float(values[4]),
            "el_equip_Pr_UBP": float(values[5]),
            "el_equip_EoL_UBP": float(values[6]),
            "el_equip_RSL": float(values[7]),
            "el_equip_cost": float(values[8]),
            "el_equip_cost_change": float(values[9]),
            "description": str(values[10])
        }
        electr_equip.append(data)
        line = f.readline()
    line = f.readline()
#Heat generation (D5.2)
    while not line.startswith("="):
        values = line.split()
        data = {
            "heat_gen_type": int(values[0]),
            "heat_gen_Pr_GWP": float(values[1]),
            "heat_gen_EoL_GWP": float(values[2]),
            "heat_gen_Pr_PE": float(values[3]),
            "heat_gen_EoL_PE": float(values[4]),
            "heat_gen_Pr_UBP": float(values[5]),
            "heat_gen_EoL_UBP": float(values[6]),
            "heat_gen_RSL": float(values[7]),
            "heat_gen_cost": float(values[8]),
            "heat_gen_cost_change": float(values[9]),
            "description": str(values[10])
        }
        heat_gen.append(data)
        line = f.readline()
    line = f.readline()
#Heat distribution and delivery (D5.3/D5.4)
    while not line.startswith("="):
        values = line.split()
        data = {
            "heat_distr_type": int(values[0]),
            "heat_distr_Pr_GWP": float(values[1]),
            "heat_distr_EoL_GWP": float(values[2]),
            "heat_distr_Pr_PE": float(values[3]),
            "heat_distr_EoL_PE": float(values[4]),
            "heat_distr_Pr_UBP": float(values[5]),
            "heat_distr_EoL_UBP": float(values[6]),
            "heat_distr_RSL": float(values[7]),
            "heat_distr_cost": float(values[8]),
            "heat_distr_cost_change": float(values[9]),
            "description": str(values[10])
        }
        heat_distr.append(data)
        line = f.readline()
    line = f.readline()
#Ventilation system (D7)
    while not line.startswith("="):
        values = line.split()
        data = {
            "vent_system_type": int(values[0]),
            "vent_system_Pr_GWP": float(values[1]),
            "vent_system_EoL_GWP": float(values[2]),
            "vent_system_Pr_PE": float(values[3]),
            "vent_system_EoL_PE": float(values[4]),
            "vent_system_Pr_UBP": float(values[5]),
            "vent_system_EoL_UBP": float(values[6]),
            "vent_system_RSL": float(values[7]),
            "vent_system_cost": float(values[8]),
            "vent_system_cost_change": float(values[9]),
            "description": str(values[10])
        }
        vent_system.append(data)
        line = f.readline()
    line = f.readline()
#Water system (D8)
    while not line.startswith("="):
        values = line.split()
        data = {
            "water_system_type": int(values[0]),
            "water_system_Pr_GWP": float(values[1]),
            "water_system_EoL_GWP": float(values[2]),
            "water_system_Pr_PE": float(values[3]),
            "water_system_EoL_PE": float(values[4]),
            "water_system_Pr_UBP": float(values[5]),
            "water_system_EoL_UBP": float(values[6]),
            "water_system_RSL": float(values[7]),
            "water_system_cost": float(values[8]),
            "water_system_cost_change": float(values[9]),
            "description": str(values[10])
        }
        water_system.append(data)
        line = f.readline()
    line = f.readline()
    while not line.startswith("="):
        values = line.split()
        data = {
            "heating_type": int(values[0]),
            "UBP_op": float(values[1]),
            "Primary_en_op_nonren": float(values[2]),
            "Primary_en_op_ren": float(values[3]),
            "CO2_op":float(values[4]),
            "description": str(values[5])
        }
        operation_impact.append(data)
        line=f.readline()
    line=f.readline()

file='Components_catalog_data.xlsx'
xl=pd.ExcelFile(file)
df1 = xl.parse('Wand')
size=len(df1)
#size1=df1
exterior_wall_ren=np.zeros((size,30))
exterior_wall_ren=exterior_wall_ren.tolist()
for i in range (size):
    for j in range (30):
        exterior_wall_ren[i][j]=df1.iloc[i] [j]

df2 = xl.parse('Dach')
size=len(df2)
roof_ren=np.zeros((size,30))
roof_ren=roof_ren.tolist()
for i in range (size):
    for j in range (30):
        roof_ren[i][j]=df2.iloc[i][j]

df1 = xl.parse("Boden")
size=len(df1)
floor_ren = np.zeros((size, 30))
floor_ren = floor_ren.tolist()
for i in range(size):
    for j in range(30):
        floor_ren[i][j]=df1.iloc[i][j]

df1 = xl.parse("Heating system")
size = len(df1)
heating_system_ren = np.zeros((size, 4))
heating_system_ren = heating_system_ren.tolist()
for i in range(size):
    for j in range(4):
        heating_system_ren[i][j]=df1.iloc[i][j]

df1 = xl.parse("Fenster")
size = len(df1)
windows_ren = np.zeros((size, 12))
windows_ren = windows_ren.tolist()
for i in range(size):
    for j in range(12):
        windows_ren[i][j] = df1.iloc[i][j]

df1 = xl.parse("Unheated")
size = len(df1)
unheated_ren = np.zeros((size, 29))
unheated_ren = unheated_ren.tolist()
for i in range(size):
    for j in range(29):
        unheated_ren[i][j] = df1.iloc[i][j]


#def heating_demand(x):
check=0 
while check==0:
    if Building_category<1 or Building_category>2:
        Building_category= int(input("Choose 1 or 2 "))
    else: 
        check=1

if Building_category==1:
    #room_temperature=int(input("Enter the room temperature (recommended value from SIA - 20 C): "))
    #number_people=int(input("Enter the number of people living in the house: "))
    Heat_gain_people=70 #W/P
    #occupation_time=int(input("Enter average time staying in the house (hours): "))
    check=0
    while check==0:
        if occupation_time<0 or occupation_time>24:
            occupation_time=int(input("Enter average time staying in the house (hours):" ))
        else:
            check=1
    Reference_time_constant=15 #hours
    Electricity_demand_year=28 #kWh/m2
    Electricity_reductionfactor=0.7
    Air_flow_therm_eff=0.7 #m3/m2h
    Base_Qh=13 #kWh/m2
    Delta_Qh=15 #kWh/m2
    Util_parameter=1
    heat_input_std_usage=3.1
    Phli=20
    Area_per_person=40
else:
    #room_temperature=int(input("Enter the room temperature (recommended value from SIA - 20 C): "))
    #number_people=int(input("Enter the number of people living in the house: "))
    Heat_gain_people=70 #W/P
    #occupation_time=int(input("Enter average time staying in the house (hours): "))
    check=0
    while check==0:
        if occupation_time<0 or occupation_time>24:
            occupation_time=int(input("Enter average time staying in the house (hours):" ))
        else:
            check=1
    Reference_time_constant=15 #hours
    Electricity_demand_year=22 #kWh/m2
    Electricity_reductionfactor=0.7
    Air_flow_therm_eff=0.7 #m3/m2h
    Base_Qh=16 #kWh/m2
    Delta_Qh=15 #kWh/m2
    Util_parameter=1
    heat_input_std_usage=2.4
    Phli=25
    Area_per_person=60

#climate data

climate=[(1,"Adelboden",1320,-1.2,297,96,134,75,150,-0.9,331,143,169,102,213,1.7,431,271,257,171,364,4.1,293,233,181,101,443,9.2,268,295,198,129,530,11.8,236,311,187,140,537,14.2,265,327,198,139,560,14.4,300,279,187,112,493,10.5,314,197,156,83,371,7.3,359,179,190,123,254,2.0,262,96,122,75,150,0.0,244,78,104,62,121,6.1,-10),(2,"Aigle",381,1.1,238,94,75,48,139,2.5,273,128,109,60,201,6.2,354,212,185,94,362,9.3,308,249,210,114,456,14.1,295,303,244,147,570,16.9,270,321,259,163,599,19.1,305,332,279,158,632,18.9,340,308,249,131,549,14.6,340,228,194,98,394,10.5,316,161,131,70,262,5.1,220,91,70,44,145,2.3,196,72,54,37,112,10.1,-6),(3,"Altdorf",449,1.2,134,51,48,40,104,2.1,220,99,94,63,174,5.9,303,174,142,88,324,9.1,290,231,184,106,435,14.1,281,289,220,137,549,16.5,244,290,207,143,547,18.6,268,297,212,142,554,18.6,295,268,193,118,485,14.6,280,187,137,86,345,10.6,241,115,94,59,225,5.2,140,52,49,36,117,2.5,96,37,32,29,80,9.9,-6),(4,"Basel-Binningen",316,1.7,190,72,80,43,110,2.9,232,109,119,60,167,6.8,303,182,193,94,305,9.6,283,231,236,119,410,14.2,281,295,292,161,528,17.2,275,321,327,189,583,19.5,303,332,346,185,605,19.4,337,303,313,147,530,14.9,314,202,223,101,358,10.9,279,131,150,67,225,5.4,187,73,80,41,119,3.0,150,54,59,32,86,10.5,-7),(5,"Bern-Liebefeld",565,-0.1,201,75,88,48,118,1.3,252,116,126,65,181,5.3,337,204,204,99,335,8.1,285,244,228,119,420,13.2,284,305,281,161,546,16.1,270,329,306,181,594,18.4,305,348,332,182,624,18.4,343,316,297,145,544,13.9,324,213,220,98,373,9.6,271,126,145,67,230,3.9,179,67,80,41,122,1.2,153,54,64,35,91,9.1,-7),(6,"Buchs-Aarau",387,0.6,115,48,59,37,86,1.7,181,87,97,58,148,5.8,268,161,166,88,284,8.8,270,213,207,114,391,14.0,279,276,273,153,522,16.8,264,293,290,171,560,18.9,292,311,311,174,581,18.7,316,271,273,139,501,14.2,283,176,197,96,334,10.0,201,91,121,62,187,4.4,109,47,60,34,91,2.0,88,35,40,27,67,9.7,-7),(7,"Chur",555,0.5,260,80,104,54,142,1.7,307,121,148,77,208,5.8,362,179,204,102,359,8.9,311,220,215,114,459,14.1,295,287,249,142,570,16.5,264,288,241,148,578,18.5,292,303,252,147,597,18.4,324,260,238,123,520,14.2,316,179,184,91,373,10.4,308,118,145,64,257,4.7,228,67,91,44,148,1.7,204,56,75,40,112,9.6,-7),(8,"Davos",1590,-4.7,402,147,166,94,182,-4.2,450,218,225,131,256,-1.1,536,348,329,196,429,1.8,435,373,329,202,524,7.2,324,340,276,161,603,9.9,272,327,259,158,604,12.3,297,335,265,150,619,12.3,340,303,244,123,544,8.4,360,241,205,96,407,5.1,394,179,171,78,297,-0.7,342,130,135,73,184,-3.4,327,107,129,72,145,3.6,-13),(9,"Disentis",1190,-1.1,321,107,142,83,161,-0.8,392,174,198,123,235,2.2,474,289,279,166,404,4.9,345,298,241,143,469,10.2,281,313,228,134,552,12.9,259,327,233,143,588,15.3,292,348,241,142,611,15.3,329,321,217,118,533,11.3,340,226,176,83,391,8.0,324,131,139,62,265,2.3,264,86,106,57,158,-0.1,260,80,110,62,129,6.7,-10),(10,"Engelberg",1035,-2.0,177,64,72,51,121,-1.1,302,145,128,82,203,2.2,380,228,206,121,354,5.1,308,231,220,119,435,10.2,273,249,238,123,538,12.7,233,267,215,127,537,14.9,254,262,214,123,536,14.9,287,236,198,104,471,11.0,285,181,148,78,345,7.5,279,131,110,56,241,1.8,176,65,62,39,132,-0.7,104,37,48,32,86,6.4,-11),(11,"Genève-Cointrin",420,1.7,163,64,78,40,107,2.9,244,106,126,60,181,6.5,362,206,222,96,362,9.4,319,259,251,119,461,14.4,308,319,305,163,592,17.6,293,350,329,189,643,20.2,327,364,354,185,670,20.0,362,327,313,147,573,15.4,355,226,238,101,404,11.2,292,134,161,70,246,5.6,174,67,83,41,122,3.1,150,54,62,32,91,10.7,-4),(12,"Glarus",515,-0.6,182,75,51,43,118,0.6,218,104,77,60,172,4.7,271,161,110,86,295,8.3,267,197,166,101,412,13.3,268,244,225,129,530,15.7,236,244,218,135,531,17.7,260,252,222,131,541,17.6,284,228,196,112,471,13.5,246,156,104,80,314,9.6,217,107,67,56,212,3.9,161,65,41,36,122,0.9,137,51,35,29,91,8.8,-8),(13,"Grand-St-Bernhard",2472,-7.1,246,104,166,96,147,-7.2,472,215,281,162,266,-5.6,670,445,453,279,471,-3.8,588,485,508,324,557,1.3,477,493,469,319,629,4.9,363,430,384,251,643,7.9,324,383,332,187,645,8.4,340,329,289,134,562,4.3,347,233,231,101,397,1.0,383,182,214,110,281,-4.0,285,111,181,101,163,-5.8,126,78,94,72,104,-0.5,-15),(14,"Güttingen",440,0.3,134,59,62,40,96,1.3,201,99,104,58,157,5.1,305,187,185,96,311,8.2,298,251,228,122,428,13.4,297,313,289,163,557,16.2,277,327,303,181,588,18.4,303,343,319,179,603,18.3,337,297,289,142,522,13.9,301,192,207,98,345,9.6,225,107,126,64,201,4.2,130,57,62,39,101,1.8,102,43,43,29,72,9.2,-7),(15,"Interlaken",580,-0.6,198,62,80,46,123,0.8,240,92,114,65,181,4.8,319,158,185,94,329,7.9,288,210,218,109,433,13.0,276,284,252,142,549,15.7,249,301,251,158,568,18.0,281,316,271,155,592,17.8,313,262,249,126,512,13.5,303,168,189,91,363,9.3,252,96,121,62,230,3.7,176,52,73,39,127,0.9,142,40,56,32,94,8.7,-7),(16,"La Chaux-de-Fonds",1019,-1.4,300,121,121,67,142,-0.7,329,167,167,94,203,2.1,386,254,238,134,343,4.8,308,280,241,137,425,9.8,262,313,252,155,506,12.6,257,340,277,181,560,15.0,292,359,311,179,597,15.1,327,329,276,142,525,11.0,316,226,205,96,363,7.8,308,153,147,67,244,2.3,259,104,101,52,145,0.1,233,88,88,48,110,6.5,-10),(17,"La Frétaz",1202,-1.2,273,104,86,40,145,-0.8,298,140,121,53,203,1.6,348,222,196,88,346,3.8,285,264,205,114,420,8.8,271,308,249,147,520,11.7,257,342,267,174,562,14.2,289,359,292,171,597,14.5,324,332,257,137,520,10.4,308,228,197,93,358,7.1,292,158,139,64,236,2.0,233,101,78,41,140,0.1,225,80,67,35,112,6.0,-10),(18,"Locarno-Monti",366,3.3,319,102,110,46,158,4.9,341,152,140,60,227,9.0,404,236,222,86,391,11.5,306,246,241,101,443,15.8,276,281,268,131,536,19.1,277,319,298,156,614,21.7,316,340,321,161,648,21.5,356,313,295,131,570,17.0,342,223,220,88,391,12.6,319,155,142,59,252,7.3,264,93,91,39,153,4.4,271,78,86,35,129,12.3,-1),(19,"Lugano",273,3.3,287,86,112,46,153,4.8,314,131,148,65,218,8.6,370,212,214,94,370,11.3,285,223,223,106,420,15.8,271,252,265,142,525,19.3,275,285,306,163,601,22.0,313,311,332,166,643,21.7,364,297,316,137,581,17.3,345,218,231,96,397,12.9,308,137,153,64,249,7.8,251,78,101,41,150,4.5,246,64,94,37,123,12.4,-1),(20,"Luzern",456,0.5,153,67,62,43,102,1.8,208,104,104,60,162,5.7,295,185,174,94,305,8.8,262,228,200,114,394,13.9,257,284,244,153,496,16.7,244,301,257,171,529,19.0,273,321,276,171,557,18.8,305,287,254,137,493,14.4,280,192,184,96,334,10.2,233,118,121,64,206,4.5,143,62,62,39,109,2.0,118,51,46,32,80,9.7,-6),(21,"Magadino",197,1.2,287,99,110,48,150,3.5,307,135,143,65,215,8.2,364,214,214,91,370,11.4,280,231,228,104,420,16.0,252,265,254,137,506,19.4,262,303,293,163,591,21.8,300,329,321,166,629,21.3,340,303,295,134,554,16.8,321,213,220,91,378,11.9,295,139,145,62,241,6.1,238,86,96,39,148,2.3,222,75,78,35,118,11.7,-3),(22,"Montana",1508,-1.7,431,171,171,91,185,-1.4,448,225,225,126,252,1.3,528,354,329,185,426,3.7,373,327,290,143,513,9.0,324,364,305,155,632,11.9,293,371,301,168,658,14.5,329,399,321,169,691,14.6,372,362,297,134,597,10.5,404,272,249,96,446,7.1,415,201,190,70,308,1.7,340,127,124,49,181,-0.4,364,129,129,62,150,5.9,-10),(23,"Neuchâtel",485,1.4,131,56,59,35,91,2.5,213,102,104,53,160,6.2,316,193,182,88,319,9.2,293,244,213,111,420,14.1,292,300,265,150,544,17.1,275,324,277,168,583,19.7,308,346,305,169,613,19.7,343,311,273,137,533,15.1,319,207,202,93,365,10.8,246,115,131,62,212,5.2,145,60,62,34,104,2.7,118,46,48,27,75,10.3,-5),(24,"Payerne",490,0.3,166,70,75,46,107,1.6,230,109,119,63,174,5.5,340,201,214,96,340,8.3,298,251,244,122,435,13.4,297,308,303,163,562,16.4,283,342,321,187,614,18.7,313,359,346,182,640,18.6,351,321,308,147,552,14.1,329,213,231,101,376,9.9,257,123,145,70,222,4.2,161,67,73,41,114,1.7,137,54,56,35,86,9.4,-7),(25,"Piotta",1007,-1.3,99,62,54,48,88,0.1,314,194,131,109,198,3.9,418,268,230,139,375,6.6,295,236,220,106,435,11.4,233,241,217,110,490,14.7,238,275,241,127,560,17.2,273,297,254,131,595,16.8,308,273,233,110,517,12.6,301,202,171,75,363,8.3,257,142,91,51,228,2.9,119,70,41,34,106,0.0,40,35,32,29,62,7.8,-7),(26,"Pully",461,2.3,198,72,80,40,118,3.3,259,109,123,56,186,6.8,364,209,217,91,356,9.5,319,254,251,114,459,14.5,311,313,313,158,592,17.5,290,337,329,176,638,20.1,324,356,356,174,667,20.1,362,308,319,139,570,15.7,355,220,241,96,399,11.6,308,139,161,67,252,6.2,210,78,88,39,132,3.6,174,59,64,32,99,10.9,-4),(27,"Robbia",1078,-2.1,305,104,118,75,161,-0.8,360,155,162,102,232,3.3,410,196,217,115,388,6.4,311,200,197,101,451,10.8,265,236,206,118,530,13.7,249,249,215,124,560,16.0,284,271,230,126,592,15.7,311,225,196,107,506,11.6,301,150,153,78,360,7.6,289,107,112,56,249,2.6,246,73,78,44,158,-0.5,241,67,78,48,129,7.0,-8),(28,"Rünenberg",610,0.4,193,78,67,37,115,1.5,235,109,104,53,174,5.2,305,190,177,88,311,7.8,283,244,228,117,412,12.7,279,303,284,158,530,15.6,270,324,308,184,581,17.9,297,343,324,182,600,18.1,332,313,292,145,525,13.7,311,215,205,98,358,9.8,268,137,131,67,225,4.2,176,75,67,39,119,1.8,147,59,48,32,88,9.1,-8),(29,"Samedan",1705,-9.3,442,177,204,121,196,-7.6,486,237,266,165,269,-2.8,581,348,386,225,450,1.1,441,337,347,200,537,6.6,321,319,297,155,621,9.5,277,319,285,158,630,11.9,313,340,287,153,656,11.6,351,284,260,126,562,7.5,365,194,218,96,420,3.5,383,150,177,75,300,-3.1,342,124,145,78,189,-7.4,370,137,155,91,158,1.8,-18),(30,"San Bernardino",1639,-3.6,367,171,126,94,174,-3.4,431,227,189,131,252,-0.7,533,340,311,196,423,1.5,402,327,290,189,472,6.4,284,287,236,147,517,10.1,251,293,215,137,560,12.7,281,300,220,137,581,12.7,313,268,201,115,506,8.6,314,202,161,83,368,4.8,308,147,112,64,249,-0.2,288,124,93,65,163,-2.6,308,134,96,70,139,3.9,-11),(31,"St. Gallen",779,-0.3,193,75,86,51,112,0.7,244,119,133,73,169,4.1,319,198,206,112,308,6.9,283,241,236,127,407,12.0,271,292,284,161,522,14.7,251,293,295,176,550,16.9,281,311,319,174,576,17.1,313,279,292,139,504,12.8,285,187,205,96,334,9.0,241,115,137,64,209,3.5,171,70,78,44,117,1.1,145,56,59,37,86,8.2,-9),(32,"Schaffhausen",437,0.1,139,59,59,40,96,1.3,210,102,99,58,162,5.4,297,187,161,91,305,8.7,290,246,202,117,417,13.8,295,316,268,158,554,16.5,280,334,288,179,594,18.7,308,354,300,174,611,18.6,343,313,260,139,530,14.1,314,207,184,96,358,9.6,236,110,121,64,206,4.1,130,57,57,36,101,1.5,110,46,43,29,75,9.4,-8),(33,"Scuol",1298,-4.3,364,129,153,91,174,-2.8,419,181,215,119,247,1.4,490,279,297,147,426,4.8,365,308,264,135,516,10.1,303,348,262,150,605,12.7,267,347,257,161,609,15.0,305,370,281,161,643,14.8,337,316,246,123,549,10.7,358,223,218,91,412,6.6,367,145,174,67,292,0.2,293,91,114,54,174,-3.2,271,88,99,64,134,5.5,-12),(34,"Sion",482,-0.1,236,62,102,46,145,2.0,324,123,152,68,225,6.7,402,222,220,94,402,10.0,350,283,257,122,516,15.0,324,346,303,161,640,17.8,295,365,311,174,677,19.9,327,378,327,171,694,19.4,367,337,292,137,595,15.0,381,241,236,98,435,10.3,354,153,166,72,289,4.3,236,65,104,44,156,0.8,174,43,75,37,110,10.1,-6),(35,"Ulrichen",1345,-7.5,289,96,161,88,147,-5.6,394,177,223,133,230,-0.7,565,362,370,233,421,2.8,500,407,410,280,498,8.3,289,297,265,137,584,11.6,270,324,267,153,614,14.1,303,335,281,150,637,13.8,340,289,252,121,552,9.6,347,202,210,88,402,5.3,327,131,153,62,268,-1.4,215,52,101,39,148,-5.6,225,72,129,67,110,3.7,-16),(36,"Vaduz",460,0.8,209,64,86,46,126,2.1,266,106,128,68,189,6.3,316,161,179,88,327,9.4,293,200,215,109,428,14.4,287,246,271,139,549,16.7,254,244,264,148,552,18.7,281,257,276,145,568,18.7,313,228,249,121,498,14.6,303,168,181,88,353,10.8,279,112,129,64,238,4.9,187,60,75,39,127,2.0,153,43,59,32,94,10.0,-8),(37,"Wynau",422,0.0,131,54,67,40,94,1.0,213,97,116,63,162,4.9,308,177,198,96,313,8.0,285,228,231,117,417,13.2,287,289,292,158,544,16.2,275,319,308,179,588,18.4,305,337,329,179,616,18.1,337,295,292,139,530,13.7,308,187,218,98,358,9.5,225,99,137,64,204,3.9,122,49,65,36,98,1.4,104,40,48,29,72,9.0,-7),(38,"Zermatt",1638,-4.0,354,137,169,112,171,-3.3,421,208,225,157,247,-0.1,541,332,319,212,429,2.8,394,301,249,161,505,8.0,308,297,212,131,597,10.8,270,301,205,127,609,13.3,303,311,214,126,632,13.1,343,279,196,110,552,9.0,363,205,168,86,420,5.3,359,142,137,67,295,-0.3,288,91,114,65,174,-2.8,297,99,129,80,139,4.3,-11),(39,"Zürich-Kloten",425,0.2,163,67,78,43,102,1.3,235,109,123,65,167,5.4,316,190,196,96,313,8.5,298,244,236,119,425,13.6,295,303,297,163,546,16.5,277,321,311,184,583,18.7,303,335,332,182,603,18.5,337,297,297,142,525,14.0,311,194,218,98,355,9.7,244,107,142,67,209,4.1,148,60,73,39,106,1.7,123,48,56,32,80,9.4,-8),(40,"Zürich-Meteo-Schweiz",556,0.4,177,67,80,43,104,1.6,235,109,123,63,165,5.5,313,185,198,94,311,8.4,290,233,231,111,417,13.4,284,281,287,150,536,16.2,270,295,303,166,570,18.4,297,311,327,166,595,18.4,332,287,295,134,522,14.0,311,192,218,91,355,9.9,254,112,142,62,214,4.2,158,62,75,39,109,1.8,137,51,59,32,80,9.4,-8)]


length=len(climate)
#for i in range(length) :
    #print(climate [i][1], "=" , i+1)

#city=int(input("Insert city number for climate data: "))
check=0 

while check==0:
    if city<1 or city>40:
        city= int(input("Insert city number for climate data: "))
    else: 
        check=1

city=city-1 #index number in climate  
mean_temp=np.zeros(12)
j=3
for i in range(12):
    mean_temp[i]=climate[city] [j]
    j=j+6

days = [31,28,31,30,31,30,31,31,30,31,30,31]
sea_height=float(climate[city][2])
annual_mean_temp=climate[city][75]
irradiance=np.zeros((17,12))

j=8
for i in range (12):
    irradiance[0][i]=(climate[city][j])/3.6
    j=j+6

k=4
for i in range (12):
    #main orientation
    irradiance[3][i]=(climate[city][k])/3.6 #S
    irradiance[7][i]=(climate[city][k+2])/3.6 #W
    irradiance[11][i]=(climate[city][k+3])/3.6 #N
    irradiance[15][i]=(climate[city][k+1])/3.6 #O
    #middle orientations
    irradiance[1][i]=(irradiance[3][i]*irradiance[15][i])**(1.0/2) #SO
    irradiance[5][i]=(irradiance[3][i]*irradiance[7][i])**(1.0/2) #SW
    irradiance[9][i]= (irradiance[11][i]*irradiance[7][i])**(1.0/2)#NW
    irradiance[13][i]=(irradiance[11][i]*irradiance[15][i])**(1.0/2) #NO
    #second middle orientations
    irradiance[2][i]=(irradiance[3][i]*irradiance[1][i])**(1.0/2) #SSO
    irradiance[4][i]=(irradiance[3][i]*irradiance[5][i])**(1.0/2) #SSW
    irradiance[6][i]=(irradiance[7][i]*irradiance[5][i])**(1.0/2) #WSW
    irradiance[8][i]=(irradiance[7][i]*irradiance[9][i])**(1.0/2) #WNW
    irradiance[10][i]=(irradiance[11][i]*irradiance[9][i])**(1.0/2) #NNW
    irradiance[12][i]=(irradiance[11][i]*irradiance[13][i])**(1.0/2) #NNO
    irradiance[14]=(irradiance[15][i]*irradiance[13][i])**(1.0/2) #ONO
    irradiance[16][i]=(irradiance[15][i]*irradiance[1][i])**(1.0/2) #OSO
    
    k=k+6

#BASE CASE
#new or renovation
#build_case= int(input("Enter the building case (1- New building, 2- Renovation): "))
check=0 
while check==0:
    if build_case<1 or build_case>2:
        build_case= int(input("Insert building case number: "))
    else: 
        check=1

#construction method
#constr_method=int(input("Enter the Construction method (1 - very light, 2 - light, 3- medium, 4 - heavy): "))
while check==0:
    if constr_method<1 or constr_method>4:
        constr_method= int(input("Enter the Construction method (1 - very light, 2 - light, 3- medium, 4 - heavy): "))
    else: 
        check=1
if constr_method==1:
    constr_factor=0.01
elif constr_method==2:
    constr_factor=0.03
elif constr_method==3:
    constr_factor=0.08
elif constr_method==4:
    constr_factor=0.15

#room temperature regulations
#room_regulation=int(input("Enter a regulation type (1 - one room temperature regulation, 2 - reference room temperature regulation, 3 - Rest): "))
check=0 
while check==0:
    if room_regulation<1 or room_regulation>3:
        room_regulation= int(input("Enter a regulation type (1 - one room temperature regulation, 2 - reference room temperature regulation, 3 - Rest): "))
    else: 
        check=1

#EBF=int(input("Enter energy reference area: "))
#Input finish
#Transmission losses calculation
Components_outside=["Roof","Walls","Vertical Windows","horizontal Windows","Floors","Doors"]
Components_thermalbridges=["Linear","Points"]
Components_earth_unheated=["Roof","Walls","Windows","Floors","Doors"]

num_components=len(comp_out_walls)+len(comp_out_roof)+len(comp_out_floor_against_tech)+len(components_in_wall)+len(components_in_ceiling)+len(components_in_ceiling)+len(components_in_floor)+len(windows_out_vertical)+len(windows_out_horizontal)+len(ext_walls_against_tech)+len(ext_walls_shops_tech)+len(floor_against_exterior)+len(floor_against_shelter)

Inner_temp=20
Q_t_monthly_ext_walls=np.zeros((num_components,12))
Q_t_monthly_roof=np.zeros((num_components,12))
Q_t_monthly_floor_ag_tech=np.zeros((num_components,12))
Q_t_monthly_comp_in=np.zeros((num_components,12))
Q_t_monthly_comp_in1=np.zeros((num_components,12))
Q_t_monthly_wind_vert=np.zeros((num_components,12))
Q_t_monthly_wind_vert1=np.zeros((num_components,12))
Q_t_monthly_wind_hor=np.zeros((num_components,12))

#old materials

el_equipment_type=2
el_equipment_type==electr_equip[0]

heat_gen_type=2
heat_gen_type==heat_gen[0]

heat_distr_type=2
heat_distr_type==heat_distr[0]

vent_system_type=2
vent_system_type==vent_system[0]

water_system_type=2
water_system_type==water_system[0]


#exterior walls
i=0
R_ext_wall=np.zeros((num_components,1))
for j in range(len(comp_out_walls)):
    if comp_out_walls[j]["thickness_walls"]==0 or comp_out_walls[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall[i]=comp_out_walls[j]["thickness_walls"]/comp_out_walls[j]["lambda_walls"]
        i=i+1
R_ext_wall_all=R_ext_wall.sum(axis=0)

Q_t_m_ext_wall=np.zeros((num_components,12))
Q_t_y_ext_wall1=[]
for k in range(12):
    Q_t_m_ext_wall[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_walls[0]["Area"] * (1/(R_ext_wall_all+0.17))* 24/(EBF*1000)
Q_m_ext_wall=Q_t_m_ext_wall.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall1.append(Q_m_ext_wall)



"""
Q_t_y_ext_wall1=[]
def ext_wall_finish_calc(perf_loss_ext_walls1):
    l=0
    perf_loss_ext_walls1=0
    for year in range(math.ceil(ext_wall_finish[ext_wall_finish_type-1]["ext_wall_finish_RSL"])):
        for b in range(12):
            Q_t_monthly_ext_walls[l][b]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[b])*days[b]*comp_out_walls[0]["Area"] * ((perf_loss_ext_walls1+1)/(R_ext_wall_all+0.17))* 24/(EBF*1000)
            perf_loss_ext_walls1 += perf_loss_ext_walls
            Q_t=Q_t_monthly_ext_walls.sum(axis=0)
        Q_t_y_ext_wall.append(Q_t)
    l=l+1
for i in range(counter_ext_walls):
    ext_wall_finish_calc(perf_loss_ext_walls)
for x in Q_t_y_ext_wall[0:60]:
    Q_t_y_ext_wall1.append(x)
"""
#Ext_walls_against_tech_rooms
i=0
R_ext_wall_ag_tech=np.zeros((num_components,1))
Q_t_y_ext_wall_ag_tech=[]
for j in range(len(ext_walls_against_tech)):
    if ext_walls_against_tech[j]["thickness_walls"]==0 or ext_walls_against_tech[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall_ag_tech[i]=ext_walls_against_tech[j]["thickness_walls"]/ext_walls_against_tech[j]["lambda_walls"]
        i=i+1
R_ext_wall_ag_tech_all=R_ext_wall_ag_tech.sum(axis=0)
Q_t_m_ext_wall_ag_tech=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_ext_wall_ag_tech[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_against_tech[0]["Area"] * (1/(R_ext_wall_ag_tech_all+0.17))* 24/(EBF*1000)  
Q_m_ext_wall_ag_tech=Q_t_m_ext_wall_ag_tech.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall_ag_tech.append(Q_m_ext_wall_ag_tech)

#ext_walls_shops_tech
i=0
R_ext_wall_shops=np.zeros((num_components,1))
Q_t_y_ext_wall_shops=[]
for j in range(len(ext_walls_shops_tech)):
    if ext_walls_shops_tech[j]["thickness_walls"]==0 or ext_walls_shops_tech[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall_shops[i]=ext_walls_shops_tech[j]["thickness_walls"]/ext_walls_shops_tech[j]["lambda_walls"]
        i=i+1
R_ext_wall_shops_all=R_ext_wall_shops.sum(axis=0)
Q_t_m_ext_wall_shops=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_ext_wall_shops[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_shops_tech[0]["Area"] * (1/(R_ext_wall_shops_all+0.17))* 24/(EBF*1000)
Q_m_ext_wall_shops=Q_t_m_ext_wall_shops.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall_shops.append(Q_m_ext_wall_shops)

#wall_against_shelter
i=0
R_wall_ag_shelt=np.zeros((num_components,1))
Q_t_y_wall_ag_shelt=[]
for j in range(len(wall_against_shelter)):
    if wall_against_shelter[j]["thickness_walls"]==0 or wall_against_shelter[j]["lambda_walls"]==0:
        pass
    else:
        R_wall_ag_shelt[i]=wall_against_shelter[j]["thickness_walls"]/wall_against_shelter[j]["lambda_walls"]
        i=i+1
R_wall_ag_shelt_all=R_wall_ag_shelt.sum(axis=0)

Q_t_m_wall_ag_shelt=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_wall_ag_shelt[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*wall_against_shelter[0]["Area"] * (1/(R_wall_ag_shelt_all+0.17))* 24/(EBF*1000)
Q_m_wall_ag_shelt=Q_t_m_wall_ag_shelt.sum(axis=0)
for i in range(60):
    Q_t_y_wall_ag_shelt.append(Q_m_wall_ag_shelt)

#ext wall5
i=0
R_ext_wall5=np.zeros((num_components,1))
Q_t_y_ext_wall5=[]
for j in range(len(ext_wall5)):
    if ext_wall5[j]["thickness_walls"]==0 or ext_wall5[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall5[i]=ext_wall5[j]["thickness_walls"]/ext_wall5[j]["lambda_walls"]
        i=i+1
R_ext_wall5=R_ext_wall5.sum(axis=0)

Q_t_m_ext_wall5=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_ext_wall5[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall5[0]["Area"] * (1/(R_ext_wall5+0.17))* 24/(EBF*1000)
Q_m_ext_wall5=Q_t_m_ext_wall5.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall5.append(Q_m_ext_wall5)

#ext wall6
i=0
R_ext_wall6=np.zeros((num_components,1))
Q_t_y_ext_wall6=[]
for j in range(len(ext_wall6)):
    if ext_wall6[j]["thickness_walls"]==0 or ext_wall6[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall6[i]=ext_wall6[j]["thickness_walls"]/ext_wall6[j]["lambda_walls"]
        i=i+1
R_ext_wall6=R_ext_wall6.sum(axis=0)

Q_t_m_ext_wall6=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_ext_wall6[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall6[0]["Area"] * (1/(R_ext_wall6+0.17))* 24/(EBF*1000)
Q_m_ext_wall6=Q_t_m_ext_wall6.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall6.append(Q_m_ext_wall6)

#ext wall7
i=0
R_ext_wall7=np.zeros((num_components,1))
Q_t_y_ext_wall7=[]
for j in range(len(ext_wall7)):
    if ext_wall7[j]["thickness_walls"]==0 or ext_wall7[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall7[i]=ext_wall7[j]["thickness_walls"]/ext_wall7[j]["lambda_walls"]
        i=i+1
R_ext_wall7=R_ext_wall7.sum(axis=0)

Q_t_m_ext_wall7=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_ext_wall7[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall7[0]["Area"] * (1/(R_ext_wall7+0.17))* 24/(EBF*1000)
Q_m_ext_wall7=Q_t_m_ext_wall7.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall7.append(Q_m_ext_wall7)

#ext wall8
i=0
R_ext_wall8=np.zeros((num_components,1))
Q_t_y_ext_wall8=[]
for j in range(len(ext_wall8)):
    if ext_wall8[j]["thickness_walls"]==0 or ext_wall8[j]["lambda_walls"]==0:
        pass
    else:
        R_ext_wall8[i]=ext_wall8[j]["thickness_walls"]/ext_wall8[j]["lambda_walls"]
        i=i+1
R_ext_wall8all=R_ext_wall8.sum(axis=0)
Q_t_m_ext_wall8=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_ext_wall8[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall8[0]["Area"] * (1/(R_ext_wall8all+0.17))* 24/(EBF*1000)
Q_m_ext_wall8=Q_t_m_ext_wall8.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall8.append(Q_m_ext_wall8)

Q_t_ext_walls = []
for a, b, c, d, e, f, g, h in zip(Q_t_y_ext_wall1 , Q_t_y_ext_wall_ag_tech, Q_t_y_ext_wall_shops, Q_t_y_wall_ag_shelt, Q_t_y_ext_wall5, Q_t_y_ext_wall6, Q_t_y_ext_wall7, Q_t_y_ext_wall8):
    Q_t_ext_walls.append(a+ b+ c+ d+ e+ f+ g+ h)
Q_transm_loss_walls=np.concatenate(Q_t_ext_walls, axis=0)

#roof
i=0
R_roof=np.zeros((num_components,1))
Q_t_y_roof=[]
for j in range(len(comp_out_roof)):
    if comp_out_roof[j]["thickness_roof"]==0 or comp_out_roof[j]["lambda_roof"]==0:
        pass
    else:
        R_roof[i]=comp_out_roof[j]["thickness_roof"]/comp_out_roof[j]["lambda_roof"]
        i=i+1
R_roof_all=R_roof.sum(axis=0)
R_roof_perf_loss=R_roof_all*(1-perf_loss_roofs)
i=0
Q_t_m_roof=np.zeros((num_components,12))
Q_t_y_roof1=[]

for k in range(12):
    Q_t_m_roof[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_roof[0]["Area"] * (1/(R_roof_all+0.17))* 24/(EBF*1000)
Q_m_roof=Q_t_m_roof.sum(axis=0)  
for i in range(60):
    Q_t_y_roof1.append(Q_m_roof)

"""
Q_t_y_roof1=[]
def roof(perf_loss_roofs):
    l=0
    perf_loss_roofs1=0
    for year in range(roof_cover[roof_cover_type-1]["roof_cover_RSL"]):
        for b in range(12):
            Q_t_monthly_roof[l][b]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[b])*days[b]*comp_out_roof[0]["Area"] * ((perf_loss_roofs1+1)/(R_roof_all+0.26))* 24/(EBF*1000)
            perf_loss_roofs1 += perf_loss_roofs
            Q_t=Q_t_monthly_roof.sum(axis=0)
        Q_t_y_roof.append(Q_t)
    l=l+1
for i in range(counter_roof):
    roof(perf_loss_roofs)
for x in Q_t_y_roof[0:60]:
    Q_t_y_roof1.append(x)
"""
#roof2
i=0
R_roof2=np.zeros((num_components,1))
Q_t_y_roof2=[]
for j in range(len(roof2)):
    if roof2[j]["thickness_roof"]==0 or roof2[j]["lambda_roof"]==0:
        pass
    else:
        R_roof2[i]=roof2[j]["thickness_roof"]/roof2[j]["lambda_roof"]
        i=i+1
R_roof_all2=R_roof2.sum(axis=0)

Q_t_m_roof2=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_roof2[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof2[0]["Area"] * (1/(R_roof_all2+0.17))* 24/(EBF*1000)
Q_m_roof2=Q_t_m_roof2.sum(axis=0)
for i in range(60):
    Q_t_y_roof2.append(Q_m_roof2)

#roof3
i=0
R_roof3=np.zeros((num_components,1))
for j in range(len(roof3)):
    if roof3[j]["thickness_roof"]==0 or roof3[j]["lambda_roof"]==0:
        pass
    else:
        R_roof3[i]=roof3[j]["thickness_roof"]/roof3[j]["lambda_roof"]
        i=i+1
R_roof_all3=R_roof3.sum(axis=0)

i=0
Q_t_m_roof3=np.zeros((num_components,12))
Q_t_y_roof3=[]

for k in range(12):
    Q_t_m_roof3[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof3[0]["Area"] * (1/(R_roof_all3+0.17))* 24/(EBF*1000)
Q_m_roof3=Q_t_m_roof3.sum(axis=0) 
for i in range(60):
    Q_t_y_roof3.append(Q_m_roof3)

Q_t_roof = []
for a, b, c in zip(Q_t_y_roof1 , Q_t_y_roof2, Q_t_y_roof3):
    Q_t_roof.append(a+ b+ c)
Q_transm_loss_roof=np.concatenate(Q_t_roof, axis=0)




#components in ceiling
i=0
R_comp_in_ceiling=np.zeros((num_components,1))
Q_t_y_comp_in_ceiling=[]
for j in range(len(components_in_ceiling)):
    R_comp_in_ceiling[i]=components_in_ceiling[j]["thickness_in"]/components_in_ceiling[j]["lambda_in"]
    i=i+1
R_comp_in_ceiling_all=R_comp_in_ceiling.sum(axis=0)
Q_t_m_comp_in_ceiling=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_comp_in_ceiling[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_ceiling[0]["Area_in"] * (1/(R_comp_in_ceiling_all+0.26))* components_in_ceiling[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_ceiling=Q_t_m_comp_in_ceiling.sum(axis=0)  
for i in range(60):
    Q_t_y_comp_in_ceiling.append(Q_m_comp_in_ceiling)

#components in wall
i=0
R_comp_in_wall=np.zeros((num_components,1))
Q_t_comp_in_year=[]
for j in range(len(components_in_wall)):
    R_comp_in_wall[i]=components_in_wall[j]["thickness_in"]/components_in_wall[j]["lambda_in"]
    i=i+1
R_comp_in_wall_all=R_comp_in_wall.sum(axis=0)
Q_t_m_comp_in_wall=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_comp_in_wall[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_wall[0]["Area_in"] * (1/(R_comp_in_wall_all+0.13))* components_in_wall[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_wall=Q_t_m_comp_in_wall.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_year.append(Q_m_comp_in_wall)

#components in floor
i=0
R_comp_in_floor=np.zeros((num_components,1))
Q_t_comp_in_floor_year=[]
for j in range(len(components_in_floor)):
    R_comp_in_floor[i]=components_in_floor[j]["thickness_in"]/components_in_floor[j]["lambda_in"]
    i=i+1
R_comp_in_floor_all=R_comp_in_floor.sum(axis=0)
Q_t_m_comp_in_floor=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_comp_in_floor[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor[0]["Area_in"] * (1/(R_comp_in_floor_all+0.26))* components_in_floor[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor=Q_t_m_comp_in_floor.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_floor_year.append(Q_m_comp_in_floor)

#components in floor2
i=0
R_comp_in_floor2=np.zeros((num_components,1))
Q_t_comp_in_floor_year2=[]
for j in range(len(components_in_floor2)):
    R_comp_in_floor2[i]=components_in_floor2[j]["thickness_in"]/components_in_floor2[j]["lambda_in"]
    i=i+1
R_comp_in_floor_all2=R_comp_in_floor2.sum(axis=0)
Q_t_m_comp_in_floor2=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_comp_in_floor2[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor2[0]["Area_in"] * (1/(R_comp_in_floor_all2+0.26))* components_in_floor2[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor2=Q_t_m_comp_in_floor2.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_floor_year2.append(Q_m_comp_in_floor2)

#components in floor3
i=0
R_comp_in_floor3=np.zeros((num_components,1))
Q_t_comp_in_floor_year3=[]
for j in range(len(components_in_floor3)):
    R_comp_in_floor3[i]=components_in_floor3[j]["thickness_in"]/components_in_floor3[j]["lambda_in"]
    i=i+1
R_comp_in_floor_all3=R_comp_in_floor3.sum(axis=0)
Q_t_m_comp_in_floor3=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_comp_in_floor3[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor3[0]["Area_in"] * (1/(R_comp_in_floor_all3+0.26))* components_in_floor3[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor3=Q_t_m_comp_in_floor3.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_floor_year3.append(Q_m_comp_in_floor3)

Q_t_comp_in_floor = []
for a, b, c in zip(Q_t_comp_in_floor_year3 , Q_t_comp_in_floor_year2, Q_t_comp_in_floor_year):
    Q_t_comp_in_floor.append(a+ b+ c )

#floor1
i=0
R_floor_ag_ext=np.zeros((num_components,1))
Q_t_y_floor_ag_ext=[]
for j in range(len(floor_against_exterior)):
    if floor_against_exterior[j]["thickness_floor"]==0 or floor_against_exterior[j]["lambda_floor"]==0:
        pass
    else:
        R_floor_ag_ext[i]=floor_against_exterior[j]["thickness_floor"]/floor_against_exterior[j]["lambda_floor"]
        i=i+1

R_floor_ag_ext_all=R_floor_ag_ext.sum(axis=0)

Q_t_m_floor_ag_ext=np.zeros((num_components,12))

for k in range(12):
    Q_t_m_floor_ag_ext[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_exterior[0]["Area"] * (1/(R_floor_ag_ext_all+0.17))* 24/(EBF*1000)
Q_m_floor_ag_ext=Q_t_m_floor_ag_ext.sum(axis=0)  
for i in range(60):
    Q_t_y_floor_ag_ext.append(Q_m_floor_ag_ext)

#floor2
i=0
R_floor_ag_shelt=np.zeros((num_components,1))
Q_t_y_floor_ag_shelt=[]
for j in range(len(floor_against_shelter)):
    if floor_against_shelter[j]["thickness_floor"]==0 or floor_against_shelter[j]["lambda_floor"]==0:
        pass
    else:
        R_floor_ag_shelt[i]=floor_against_shelter[j]["thickness_floor"]/floor_against_shelter[j]["lambda_floor"]
        i=i+1
R_floor_ag_shelt_all=R_floor_ag_shelt.sum(axis=0)

Q_t_m_floor_ag_shelt=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_floor_ag_shelt[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_shelter[0]["Area"] * (1/(R_floor_ag_shelt_all+0.17))* 24/(EBF*1000)
Q_m_floor_ag_shelt=Q_t_m_floor_ag_shelt.sum(axis=0)  
for i in range(60):
    Q_t_y_floor_ag_shelt.append(Q_m_floor_ag_shelt)

#comp_out_floor_against_tech
i=0
R_floor_ag_tech=np.zeros((num_components,1))
Q_t_y_floor_ag_tech1=[]
for j in range(len(comp_out_floor_against_tech)):
    if comp_out_floor_against_tech[j]["thickness_floor"] ==0 or comp_out_floor_against_tech[j]["lambda_floor"]==0:
        pass
    else:
        R_floor_ag_tech[i]=comp_out_floor_against_tech[j]["thickness_floor"]/comp_out_floor_against_tech[j]["lambda_floor"]
        i=i+1
R_floor_ag_tech_all=R_floor_ag_tech.sum(axis=0)
i=0
Q_t_m_floor_ag_tech=np.zeros((num_components,12))
Q_t_y_floor_ag_tech=[]
for k in range(12):
    Q_t_m_floor_ag_tech[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_floor_against_tech[0]["Area"] * (1/(R_floor_ag_tech_all+0.17))* 24/(EBF*1000)
Q_m_floor_ag_tech=Q_t_m_floor_ag_tech.sum(axis=0)  
for i in range(60):
    Q_t_y_floor_ag_tech1.append(Q_m_floor_ag_tech)

"""
# comp_out_floor_against_tech
i=0
R_floor_ag_tech=np.zeros((num_components,1))
Q_t_y_floor_ag_tech=[]
for j in range(len(comp_out_floor_against_tech)):
    R_floor_ag_tech[i]=comp_out_floor_against_tech[j]["thickness_floor"]/comp_out_floor_against_tech[j]["lambda_floor"]
    i=i+1
R_floor_ag_tech_all=R_floor_ag_tech.sum(axis=0)

i=0
Q_t_m_floor_ag_tech=np.zeros((num_components,12))
Q_t_y_floor_ag_tech=[]
for j in range(len(comp_out_floor_against_tech)):
    for k in range(12):
        Q_t_m_floor_ag_tech[i][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_floor_against_tech[j]["Area"] * (1/(R_floor_ag_tech_all+0.26))* 24/(EBF*1000)
    Q_m_floor_ag_tech=Q_t_m_floor_ag_tech.sum(axis=0)  
for i in range(10):
    Q_t_y_floor_ag_tech.append(Q_m_floor_ag_tech)

Q_t_y_floor_ag_tech1=[]
def floor_ag_tech(perf_loss_floor):
    l=0
    perf_loss_floor1=0
    for year in range(math.ceil(floor_cover[floor_cover_type-1]["floor_cover_RSL"])):
        for b in range(12):
            Q_t_monthly_floor_ag_tech[l][b]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[b])*days[b]*comp_out_floor_against_tech[0]["Area"] * ((perf_loss_floor1+1)/(R_floor_ag_tech_all+0.26))* 24/(EBF*1000)
            perf_loss_floor1 += perf_loss_floor
            Q_t=Q_t_monthly_floor_ag_tech.sum(axis=0)
        Q_t_y_floor_ag_tech.append(Q_t)
    l=l+1
for i in range(counter_floor):
    floor_ag_tech(perf_loss_floor)
for x in Q_t_y_floor_ag_tech[0:60]:
    Q_t_y_floor_ag_tech1.append(x)
"""
#floor4
i=0
R_floor4=np.zeros((num_components,1))
Q_t_y_floor4=[]
for j in range(len(floor4)):
    if floor4[j]["thickness_floor"]==0 or floor4[j]["lambda_floor"]==0:
        pass
    else:
        R_floor4[i]=floor4[j]["thickness_floor"]/floor4[j]["lambda_floor"]
        i=i+1
R_floor4_all=R_floor4.sum(axis=0)

Q_t_m_floor4=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_floor4[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor4[0]["Area"] * (1/(R_floor4_all+0.26))* 24/(EBF*1000)
Q_m_floor4=Q_t_m_floor4.sum(axis=0)  
for i in range(60):
    Q_t_y_floor4.append(Q_m_floor4)

#floor5
i=0
R_floor5=np.zeros((num_components,1))
Q_t_y_floor5=[]
for j in range(len(floor5)):
    if floor5[j]["thickness_floor"]==0 or floor5[j]["lambda_floor"]==0:
        pass
    else:
        R_floor5[i]=floor5[j]["thickness_floor"]/floor5[j]["lambda_floor"]
        i=i+1
R_floor5_all=R_floor5.sum(axis=0)
Q_t_m_floor5=np.zeros((num_components,12))
for k in range(12):
    Q_t_m_floor5[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor5[0]["Area"] * (1/(R_floor5_all+0.26))* 24/(EBF*1000)
Q_m_floor5=Q_t_m_floor5.sum(axis=0)  
for i in range(60):
    Q_t_y_floor5.append(Q_m_floor5)

Q_t_ext_floor = []
for a, b, c, d, e in zip(Q_t_y_floor5 , Q_t_y_floor4, Q_t_y_floor_ag_tech1, Q_t_y_floor_ag_shelt, Q_t_y_floor_ag_ext):
    Q_t_ext_floor.append(a+ b+ c +d +e)
Q_transm_loss_ext_floor=np.concatenate(Q_t_ext_floor, axis=0)

#Windows vertical
i=0
Q_t_wind_vert_year=[]
Q_t_wind_vert_year1=[]
performance_loss_wind_vert = []
for f in range(len(windows_out_vertical)):
    for g in range(12):                       
        Q_t_monthly_wind_vert1[f][g]=(((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/2)-mean_temp[g])*days[g]*windows_out_vertical[f]["Area_wind"]*windows_out_vertical[f]["UValue_wind"]*24)/(EBF*1000)   
    Q_t_each_month_wind_vert=Q_t_monthly_wind_vert1.sum(axis=0)
for i in range(60):
    Q_t_wind_vert_year1.append(Q_t_each_month_wind_vert)     

"""
def windows_vert_calc(perf_loss_wind_vert):
    i=0 
    Q_t_wind_vert = []
    for year in range(math.ceil(windows_emb[windows_type-1]["windows_RSL"])):
        for month in range(12):
            perf_loss_wind_vert += 0.0005
            performance_loss_wind_vert.append(perf_loss_wind_vert)
    for x in range(math.ceil(windows_emb[windows_type-1]["windows_RSL"])):
        Q_t_wind_vert.append(Q_t_each_month_wind_vert)
    for x, y in zip(Q_t_wind_vert, performance_loss_wind_vert):
        Q_t_wind_vert_year.append(x * y)    
for i in range(counter_windows):
    windows_vert_calc(perf_loss_wind_vert)
for i in Q_t_wind_vert_year[0:60]:
    Q_t_wind_vert_year1.append(i)
"""

i=0
#Windows horizontal
Q_t_wind_hor_year=[]
for h in range(len(windows_out_horizontal)):
    for l in range(12):
        Q_t_monthly_wind_hor[h][l]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/2)-mean_temp[l])*days[l]*windows_out_horizontal[h]["Area_wind_h"]*windows_out_horizontal[h]["U-Value_wind_h"]*24/(EBF*1000)        
    i=i+1
#performance loss windows horizontal
Q_t_each_month_wind_hor=sum(Q_t_monthly_wind_hor)
for i in range(10):
    Q_t_wind_hor_year.append(Q_t_each_month_wind_hor)
performance_loss_wind_hor = []
for year in range(60):
    for month in range(12):
        perf_loss_wind_hor += 0.005
        performance_loss_wind_hor.append(perf_loss_wind_hor)
Q_t_wind_hor=[]
for x in range(60):
    Q_t_wind_hor.append(Q_t_each_month_wind_hor)
for x, y in zip(Q_t_wind_hor, performance_loss_wind_hor):
    Q_t_wind_hor_year.append(x * y)
Q_t_wind_hor_year1=[]
for i in Q_t_wind_hor_year[0:60]:
    Q_t_wind_hor_year1.append(i)

Q_t_perf_loss = []
for a, b, c, d, e, f, g, h in zip(Q_t_ext_walls, Q_t_wind_vert_year1, Q_t_wind_hor_year1, Q_t_roof, Q_t_ext_floor,Q_t_y_comp_in_ceiling, Q_t_comp_in_floor, Q_t_comp_in_year):
    Q_t_perf_loss.append(a+ b+ c+ d+ e+ f+ g+ h)
Q_transm_loss=np.concatenate(Q_t_perf_loss, axis=0)

#plt.plot(Q_transm_loss)
#plt.ylabel("kwh/m2")
#plt.xlabel("Months")
#plt.title("Transmission losses")
#plt.show()
#Ph and Phli calculation (Specific heating load and limit)

#vent_type=int(input("Enter a ventilation type (Natural - 1, Mechanical - 2): "))

#heat transfer coefficients to calculate Htotal

H_transfer_coef=0
if R_ext_wall_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+comp_out_walls[0]["Area"]*(1/R_ext_wall_all)
if R_ext_wall_ag_tech_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_walls_against_tech[0]["Area"]*(1/R_ext_wall_ag_tech_all)
if R_ext_wall_shops_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_walls_shops_tech[0]["Area"]*(1/R_ext_wall_shops_all)
if R_wall_ag_shelt_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+wall_against_shelter[0]["Area"]*(1/R_wall_ag_shelt_all)

if R_ext_wall5==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_wall5[0]["Area"]*(1/R_ext_wall5)
if R_ext_wall6==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_wall6[0]["Area"]*(1/R_ext_wall6)
if R_ext_wall7==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_wall7[0]["Area"]*(1/R_ext_wall7)
if R_ext_wall8all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+ext_wall8[0]["Area"]*(1/R_ext_wall8all)    
if R_roof_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+comp_out_roof[0]["Area"]*(1/R_roof_all)    
if R_roof_all2==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+roof2[0]["Area"]*(1/R_roof_all2)    
if R_roof_all3==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+roof3[0]["Area"]*(1/R_roof_all3)  
if R_comp_in_ceiling_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+components_in_ceiling[0]["Area_in"]*(1/R_comp_in_ceiling_all)  
if R_comp_in_wall_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+components_in_wall[0]["Area_in"]*(1/R_comp_in_wall_all) 
if R_comp_in_floor_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+components_in_floor[0]["Area_in"]*(1/R_comp_in_floor_all) 
if R_comp_in_floor_all2==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+components_in_floor2[0]["Area_in"]*(1/R_comp_in_floor_all2) 
if R_comp_in_floor_all3==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+components_in_floor3[0]["Area_in"]*(1/R_comp_in_floor_all3) 
if R_floor_ag_ext_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+floor_against_exterior[0]["Area"]*(1/R_floor_ag_ext_all) 
if R_floor_ag_shelt_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+floor_against_shelter[0]["Area"]*(1/R_floor_ag_shelt_all) 
if R_floor_ag_tech_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+comp_out_floor_against_tech[0]["Area"]*(1/R_floor_ag_tech_all) 
if R_floor4_all==0:
    H_transfer_coef=H_transfer_coef+0
else:
    H_transfer_coef=H_transfer_coef+floor4[0]["Area"]*(1/R_floor4_all) 
if R_floor5_all==0:
    H_transfer_coef=H_transfer_coef+0
for i in range(len(windows_out_vertical)):
    H_transfer_coef=H_transfer_coef + windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["UValue_wind"]
for i in range(len(windows_out_horizontal)):
    H_transfer_coef=H_transfer_coef+windows_out_horizontal[i]["Area_wind_h"]+windows_out_horizontal[i]["U-Value_wind_h"]

design_temp=climate[city][76]


#ventilation loss
check=0
Air_flow_new=Air_flow_therm_eff
while check==0:
    if vent_type<1 or vent_type>2:
        vent_type=int(input("Enter a ventilation type (Natural - 1, Mechanical - 2): "))
    else:
        check=1

#natural ventilation
Qvent_nat=np.zeros(12)
if vent_type ==1:
    heat_storage_capacity=(1220-(0.14*sea_height))/3600
    for i in range(12):
        Qvent_nat[i]=((room_temperature+room_regulation-1)-mean_temp[i])*Air_flow_therm_eff*days[i]*heat_storage_capacity*24/1000
        if Qvent_nat[i]<0:
            Qvent_nat[i]=0
Qvent_nat_year=[]
for i in range(60):
    Qvent_nat_year.append(Qvent_nat)
Q_vent_loss_nat=np.concatenate(Qvent_nat_year, axis=0)

#comfort mechanical ventilation
if vent_type==2:
    Air_flow=Air_flow_therm_eff
    H_vent=Air_flow*heat_storage_capacity*EBF
    design_temp=climate[city][76]
    Htotal=H_vent+H_transfer_coef
    Ph=(Htotal*(room_temperature-design_temp)/EBF)-heat_input_std_usage
    if design_temp<8:
        Ph_corrected=Phli*(room_temperature-design_temp)/(room_temperature-(-8))
    else:
        Ph_corrected=Phli

check=0
while check==0:
    if preheat_air<0 or preheat_air>2:
        print("Enter 1 or 2")
    else:
        check=1

Oper_hours_step1=84
Oper_hours_step2=70
Oper_hours_step3=14

Basic_air_exchange_rate=0.15
if preheat_air==1:
    thermal_eff_airrate_step1=(1-heat_rec_eff)*(room_number*20/EBF)*heat_rec_eff+Basic_air_exchange_rate
    thermal_eff_airrate_step2=(1-heat_rec_eff)*(room_number*30/EBF)*heat_rec_eff+Basic_air_exchange_rate
    thermal_eff_airrate_step3=(1-heat_rec_eff)*(room_number*45/EBF)*heat_rec_eff+Basic_air_exchange_rate
else:
    thermal_eff_airrate_step1=(1-heat_rec_eff)*(room_number*20/EBF)+Basic_air_exchange_rate
    thermal_eff_airrate_step2=(1-heat_rec_eff)*(room_number*30/EBF)+Basic_air_exchange_rate
    thermal_eff_airrate_step3=(1-heat_rec_eff)*(room_number*45/EBF)+Basic_air_exchange_rate

thermal_eff_outer_volume=(Oper_hours_step1*thermal_eff_airrate_step1+Oper_hours_step2*thermal_eff_airrate_step2+Oper_hours_step3*thermal_eff_airrate_step3)/(Oper_hours_step1+Oper_hours_step2+Oper_hours_step3)
Qvent_with_heatrec=np.zeros(12)
if heat_rec==1:
    for i in range(12):
        Qvent_with_heatrec[i]=(room_temperature+room_regulation-1-mean_temp[i])*thermal_eff_outer_volume*days[i]*EBF*heat_storage_capacity*24/(EBF*1000)
        if Qvent_with_heatrec[i]<0:
            Qvent_with_heatrec[i]=0
Q_vent_loss_mech = []
for i in range(60):
    Q_vent_loss_mech.append(Qvent_with_heatrec)
Q_vent_loss_mech_year=np.concatenate(Q_vent_loss_mech, axis=0)

if heat_rec==1:
    difference=0
else:
    difference=Qvent_nat-Qvent_with_heatrec

Qvent_without_heat_rec1 = []
for x in range(60):
    for y in Qvent_nat:
        Qvent_without_heat_rec1.append(y)


#Electricity consumption

air_electricity_step1=0.3
air_electricity_step2=0.35
air_electricity_step3=0.5

el_consumption_step1=room_number*Oper_hours_step1*20*air_electricity_step1/1000
el_consumption_step2=room_number*Oper_hours_step2*30*air_electricity_step2/1000
el_consumption_step3=room_number*Oper_hours_step3*45*air_electricity_step3/1000

el_consumption_total=((el_consumption_step1+el_consumption_step2+el_consumption_step3)*52)/EBF 

#gains
#heat gains electricity
duration=365
Qiel=Electricity_demand_year*Electricity_reductionfactor*duration/365
Qiel_monthly=np.zeros(12)
for i in range(12):
    Qiel_monthly[i]=Qiel/12
Qiel1=[]
for x in range(60):
    for y in Qiel_monthly:
        Qiel1.append(y)
#heat gains occupancy

Qiocc=Heat_gain_people*occupation_time*duration/(Area_per_person*1000)

Qiocc_monthly=np.zeros(12)
for i in range(12):
    Qiocc_monthly[i]=Qiocc/12
Qiocc1=[]
for x in range(60):
    for y in Qiocc_monthly:
        Qiocc1.append(y)

#solar gains
#daten SIA excel
horizon=[("-","SW","SE","SSE","S","SSW","WSW","W","E","WNW","NW","NE","NNW","N","NNE","ENE","ESE"),(0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,0.99,0.99,1,1,1,1,1,1,1,1),(2,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,1,1,1,1,1,1,1,0.99),(3,0.99,0.99,0.99,0.99,0.99,0.99,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.99),(4,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.98),(5,0.98,0.98,0.98,0.98,0.98,0.98,0.97,0.97,0.98,0.99,0.99,1,1,1,0.98,0.98),(6,0.97,0.97,0.98,0.98,0.98,0.97,0.96,0.96,0.97,0.98,0.98,0.99,1,0.99,0.97,0.97),(7,0.97,0.97,0.97,0.97,0.97,0.97,0.96,0.96,0.97,0.98,0.98,0.99,1,0.99,0.97,0.97),(8,0.96,0.96,0.97,0.97,0.97,0.96,0.95,0.95,0.97,0.98,0.98,0.99,1,0.99,0.97,0.96),(9,0.96,0.96,0.96,0.96,0.96,0.96,0.95,0.95,0.97,0.98,0.98,0.99,1,0.99,0.97,0.96),(10,0.95,0.95,0.96,0.96,0.96,0.95,0.94,0.94,0.96,0.97,0.97,0.99,1,0.99,0.96,0.95),(11,0.94,0.94,0.95,0.95,0.95,0.93,0.92,0.92,0.94,0.96,0.96,0.98,1,0.98,0.94,0.93),(12,0.92,0.92,0.93,0.93,0.93,0.92,0.91,0.91,0.93,0.95,0.95,0.97,0.99,0.97,0.93,0.92),(13,0.91,0.91,0.92,0.92,0.92,0.9,0.89,0.89,0.92,0.94,0.94,0.97,0.99,0.97,0.92,0.9),(14,0.89,0.89,0.9,0.9,0.9,0.89,0.88,0.88,0.91,0.94,0.94,0.97,0.99,0.97,0.91,0.89),(15,0.88,0.88,0.89,0.89,0.89,0.88,0.87,0.87,0.9,0.93,0.93,0.96,0.99,0.96,0.9,0.88),(16,0.87,0.87,0.88,0.88,0.88,0.87,0.86,0.86,0.89,0.92,0.92,0.95,0.98,0.95,0.89,0.87),(17,0.86,0.86,0.86,0.86,0.86,0.86,0.85,0.85,0.89,0.92,0.92,0.95,0.98,0.95,0.89,0.86),(18,0.84,0.84,0.85,0.85,0.85,0.84,0.83,0.83,0.87,0.91,0.91,0.95,0.98,0.95,0.87,0.84),(19,0.83,0.83,0.83,0.83,0.83,0.83,0.82,0.82,0.86,0.9,0.9,0.94,0.97,0.94,0.86,0.83),(20,0.82,0.82,0.82,0.82,0.82,0.82,0.81,0.81,0.85,0.89,0.89,0.93,0.97,0.93,0.85,0.82),(21,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.85,0.89,0.89,0.93,0.97,0.93,0.85,0.8),(22,0.78,0.78,0.78,0.77,0.78,0.78,0.78,0.78,0.83,0.87,0.87,0.92,0.96,0.92,0.83,0.78),(23,0.76,0.76,0.76,0.75,0.76,0.77,0.77,0.77,0.82,0.87,0.87,0.92,0.96,0.92,0.82,0.77),(24,0.75,0.75,0.74,0.73,0.74,0.76,0.76,0.76,0.81,0.86,0.86,0.91,0.96,0.91,0.81,0.76),(25,0.73,0.73,0.72,0.71,0.72,0.74,0.75,0.75,0.81,0.86,0.86,0.91,0.96,0.91,0.81,0.74),(26,0.71,0.71,0.7,0.68,0.7,0.72,0.73,0.73,0.79,0.84,0.84,0.9,0.95,0.9,0.79,0.72),(27,0.69,0.69,0.68,0.66,0.68,0.71,0.72,0.72,0.78,0.84,0.84,0.9,0.95,0.9,0.78,0.71),(28,0.68,0.68,0.66,0.64,0.66,0.7,0.71,0.71,0.77,0.83,0.83,0.89,0.95,0.89,0.77,0.7),(29,0.65,0.65,0.63,0.61,0.63,0.67,0.69,0.69,0.76,0.82,0.82,0.88,0.94,0.88,0.76,0.67),(30,0.64,0.64,0.62,0.59,0.62,0.66,0.68,0.68,0.75,0.81,0.81,0.88,0.94,0.88,0.75,0.66),(31,0.63,0.63,0.61,0.58,0.61,0.65,0.67,0.67,0.74,0.81,0.81,0.88,0.94,0.88,0.74,0.65),(32,0.61,0.61,0.59,0.56,0.59,0.64,0.66,0.66,0.73,0.8,0.8,0.87,0.93,0.87,0.73,0.64),(33,0.61,0.61,0.58,0.55,0.58,0.64,0.66,0.66,0.73,0.8,0.8,0.87,0.93,0.87,0.73,0.64),(34,0.59,0.59,0.56,0.53,0.56,0.62,0.65,0.65,0.72,0.79,0.79,0.86,0.92,0.86,0.72,0.62),(35,0.58,0.58,0.55,0.52,0.55,0.61,0.64,0.64,0.71,0.78,0.78,0.85,0.92,0.85,0.71,0.61),(36,0.57,0.57,0.54,0.51,0.54,0.6,0.63,0.63,0.71,0.78,0.78,0.85,0.92,0.85,0.71,0.6),(37,0.56,0.56,0.53,0.49,0.53,0.59,0.62,0.62,0.7,0.77,0.77,0.84,0.91,0.84,0.7,0.59),(38,0.55,0.55,0.52,0.48,0.52,0.59,0.62,0.62,0.7,0.77,0.77,0.84,0.91,0.84,0.7,0.59),(39,0.54,0.54,0.5,0.46,0.5,0.58,0.61,0.61,0.69,0.76,0.76,0.83,0.9,0.83,0.69,0.58),(40,0.53,0.53,0.49,0.45,0.49,0.57,0.6,0.6,0.68,0.75,0.75,0.83,0.9,0.83,0.68,0.57),(41,0.52,0.52,0.48,0.44,0.48,0.56,0.59,0.59,0.67,0.75,0.75,0.83,0.9,0.83,0.67,0.56),(42,0.51,0.51,0.47,0.43,0.47,0.55,0.58,0.58,0.66,0.74,0.74,0.82,0.89,0.82,0.66,0.55),(43,0.5,0.5,0.46,0.42,0.46,0.54,0.57,0.57,0.65,0.73,0.73,0.81,0.89,0.81,0.65,0.54),(44,0.49,0.49,0.45,0.41,0.45,0.53,0.56,0.56,0.64,0.72,0.72,0.8,0.88,0.8,0.64,0.53),(45,0.48,0.48,0.45,0.41,0.45,0.52,0.55,0.55,0.64,0.72,0.72,0.8,0.88,0.8,0.64,0.52),(46,0.47,0.47,0.44,0.4,0.44,0.51,0.54,0.54,0.63,0.71,0.71,0.8,0.88,0.8,0.63,0.51),(47,0.46,0.46,0.43,0.39,0.43,0.5,0.53,0.53,0.62,0.7,0.7,0.79,0.87,0.79,0.62,0.5),(48,0.45,0.45,0.42,0.38,0.42,0.49,0.52,0.52,0.61,0.7,0.7,0.79,0.87,0.79,0.61,0.49),(49,0.44,0.44,0.41,0.37,0.41,0.48,0.51,0.51,0.6,0.69,0.69,0.78,0.86,0.78,0.6,0.48),(50,0.43,0.43,0.4,0.36,0.4,0.47,0.5,0.5,0.59,0.68,0.68,0.77,0.86,0.77,0.59,0.47),(51,0.42,0.42,0.39,0.35,0.39,0.46,0.49,0.49,0.59,0.68,0.68,0.77,0.86,0.77,0.59,0.46),(52,0.41,0.41,0.38,0.34,0.38,0.45,0.48,0.48,0.58,0.67,0.67,0.76,0.85,0.76,0.58,0.45),(53,0.4,0.4,0.37,0.33,0.37,0.44,0.47,0.47,0.57,0.66,0.66,0.76,0.85,0.76,0.57,0.44),(54,0.39,0.39,0.36,0.32,0.36,0.43,0.46,0.46,0.56,0.65,0.65,0.75,0.84,0.75,0.56,0.43),(55,0.39,0.39,0.36,0.32,0.36,0.42,0.45,0.45,0.55,0.65,0.65,0.75,0.84,0.75,0.55,0.42),(56,0.38,0.38,0.35,0.31,0.35,0.41,0.44,0.44,0.54,0.64,0.64,0.74,0.84,0.74,0.54,0.41),(57,0.37,0.37,0.34,0.3,0.34,0.4,0.43,0.43,0.53,0.63,0.63,0.73,0.83,0.73,0.53,0.4),(58,0.36,0.36,0.33,0.29,0.33,0.39,0.42,0.42,0.53,0.63,0.63,0.73,0.83,0.73,0.53,0.39),(59,0.35,0.35,0.32,0.28,0.32,0.38,0.41,0.41,0.52,0.62,0.62,0.72,0.82,0.72,0.52,0.38),(60,0.34,0.34,0.31,0.27,0.31,0.37,0.4,0.4,0.51,0.61,0.61,0.72,0.82,0.72,0.51,0.37),(61,0.33,0.33,0.3,0.26,0.3,0.36,0.39,0.39,0.5,0.61,0.61,0.72,0.82,0.72,0.5,0.36),(62,0.32,0.32,0.29,0.25,0.29,0.35,0.38,0.38,0.49,0.6,0.6,0.71,0.81,0.71,0.49,0.35),(63,0.31,0.31,0.28,0.25,0.28,0.34,0.37,0.37,0.48,0.59,0.59,0.7,0.81,0.7,0.48,0.34),(64,0.3,0.3,0.27,0.24,0.27,0.33,0.36,0.36,0.47,0.58,0.58,0.69,0.8,0.69,0.47,0.33),(65,0.29,0.29,0.26,0.23,0.26,0.32,0.35,0.35,0.47,0.58,0.58,0.69,0.8,0.69,0.47,0.32),(66,0.28,0.28,0.25,0.22,0.25,0.31,0.34,0.34,0.46,0.57,0.57,0.69,0.8,0.69,0.46,0.31),(67,0.27,0.27,0.24,0.21,0.24,0.3,0.33,0.33,0.45,0.56,0.56,0.68,0.79,0.68,0.45,0.3),(68,0.27,0.27,0.24,0.21,0.24,0.3,0.32,0.32,0.44,0.56,0.56,0.68,0.79,0.68,0.44,0.3),(69,0.26,0.26,0.23,0.2,0.23,0.29,0.31,0.31,0.43,0.55,0.55,0.67,0.78,0.67,0.43,0.29),(70,0.25,0.25,0.22,0.19,0.22,0.28,0.3,0.3,0.42,0.54,0.54,0.66,0.78,0.66,0.42,0.28)]
overhang=[("-","SW","SE","SSE","S","SSW","WSW","W","E","WNW","NW","NE","NNW","N","NNE","ENE","ESE"),(0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(2,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99),(3,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99),(4,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99),(5,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.98),(6,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98),(7,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98),(8,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.97),(9,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.97),(10,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97),(11,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.96),(12,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.96),(13,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.96),(14,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.95),(15,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.95),(16,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.96,0.96,0.96,0.96,0.96,0.96,0.96,0.95),(17,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.94),(18,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.95,0.95,0.95,0.95,0.95,0.95,0.95,0.94),(19,0.94,0.94,0.94,0.94,0.94,0.94,0.93,0.93,0.94,0.94,0.94,0.95,0.95,0.95,0.94,0.94),(20,0.94,0.94,0.94,0.94,0.94,0.94,0.93,0.93,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.94),(21,0.93,0.93,0.93,0.93,0.93,0.93,0.93,0.93,0.94,0.94,0.94,0.94,0.94,0.94,0.94,0.93),(22,0.93,0.93,0.93,0.93,0.93,0.93,0.92,0.92,0.93,0.93,0.93,0.94,0.94,0.94,0.93,0.93),(23,0.93,0.93,0.93,0.93,0.93,0.93,0.92,0.92,0.93,0.93,0.93,0.93,0.93,0.93,0.93,0.93),(24,0.92,0.92,0.93,0.93,0.93,0.92,0.91,0.91,0.92,0.92,0.92,0.93,0.93,0.93,0.92,0.92),(25,0.92,0.92,0.92,0.92,0.92,0.92,0.91,0.91,0.92,0.92,0.92,0.93,0.93,0.93,0.92,0.92),(26,0.92,0.92,0.92,0.92,0.92,0.92,0.91,0.91,0.92,0.92,0.92,0.92,0.92,0.92,0.92,0.92),(27,0.91,0.91,0.92,0.92,0.92,0.91,0.9,0.9,0.91,0.91,0.91,0.92,0.92,0.92,0.91,0.91),(28,0.91,0.91,0.92,0.92,0.92,0.91,0.9,0.9,0.91,0.91,0.91,0.92,0.92,0.92,0.91,0.91),(29,0.9,0.9,0.91,0.91,0.91,0.9,0.89,0.89,0.9,0.9,0.9,0.91,0.91,0.91,0.9,0.9),(30,0.9,0.9,0.91,0.91,0.91,0.9,0.89,0.89,0.9,0.9,0.9,0.91,0.91,0.91,0.9,0.9),(31,0.89,0.89,0.9,0.9,0.9,0.89,0.88,0.88,0.89,0.89,0.89,0.9,0.9,0.9,0.89,0.89),(32,0.88,0.88,0.89,0.89,0.89,0.88,0.87,0.87,0.88,0.89,0.89,0.9,0.9,0.9,0.88,0.88),(33,0.88,0.88,0.88,0.88,0.88,0.88,0.87,0.87,0.88,0.88,0.88,0.89,0.89,0.89,0.88,0.88),(34,0.87,0.87,0.87,0.87,0.87,0.87,0.86,0.86,0.87,0.87,0.87,0.88,0.88,0.88,0.87,0.87),(35,0.86,0.86,0.86,0.86,0.86,0.86,0.85,0.85,0.86,0.86,0.86,0.87,0.87,0.87,0.86,0.86),(36,0.85,0.85,0.85,0.85,0.85,0.85,0.84,0.84,0.85,0.86,0.86,0.87,0.87,0.87,0.85,0.85),(37,0.84,0.84,0.84,0.84,0.84,0.84,0.83,0.83,0.84,0.85,0.85,0.86,0.86,0.86,0.84,0.84),(38,0.83,0.83,0.83,0.82,0.83,0.83,0.83,0.83,0.84,0.84,0.84,0.85,0.85,0.85,0.84,0.83),(39,0.82,0.82,0.82,0.81,0.82,0.82,0.82,0.82,0.83,0.83,0.83,0.84,0.84,0.84,0.83,0.82),(40,0.81,0.81,0.81,0.8,0.81,0.81,0.81,0.81,0.82,0.83,0.83,0.84,0.84,0.84,0.82,0.81),(41,0.8,0.8,0.8,0.79,0.8,0.8,0.8,0.8,0.81,0.82,0.82,0.83,0.83,0.83,0.81,0.8),(42,0.79,0.79,0.79,0.78,0.79,0.79,0.79,0.79,0.8,0.81,0.81,0.82,0.82,0.82,0.8,0.79),(43,0.78,0.78,0.78,0.77,0.78,0.79,0.79,0.79,0.8,0.8,0.8,0.81,0.81,0.81,0.8,0.79),(44,0.77,0.77,0.77,0.76,0.77,0.78,0.78,0.78,0.79,0.8,0.8,0.81,0.81,0.81,0.79,0.78),(45,0.76,0.76,0.76,0.75,0.76,0.77,0.77,0.77,0.78,0.79,0.79,0.8,0.8,0.8,0.78,0.77),(46,0.75,0.75,0.74,0.73,0.74,0.76,0.76,0.76,0.77,0.78,0.78,0.79,0.79,0.79,0.77,0.76),(47,0.74,0.74,0.73,0.72,0.73,0.75,0.75,0.75,0.76,0.77,0.77,0.78,0.78,0.78,0.76,0.75),(48,0.72,0.72,0.71,0.7,0.71,0.73,0.73,0.73,0.74,0.75,0.75,0.76,0.77,0.76,0.74,0.73),(49,0.71,0.71,0.7,0.69,0.7,0.72,0.72,0.72,0.73,0.74,0.74,0.75,0.76,0.75,0.73,0.72),(50,0.69,0.69,0.68,0.67,0.68,0.7,0.71,0.71,0.72,0.73,0.73,0.74,0.75,0.74,0.72,0.7),(51,0.68,0.68,0.67,0.66,0.67,0.69,0.7,0.7,0.71,0.72,0.72,0.73,0.74,0.73,0.71,0.69),(52,0.67,0.67,0.66,0.64,0.66,0.68,0.69,0.69,0.7,0.71,0.71,0.72,0.73,0.72,0.7,0.68),(53,0.65,0.65,0.64,0.63,0.64,0.66,0.67,0.67,0.69,0.7,0.7,0.72,0.73,0.72,0.69,0.66),(54,0.64,0.64,0.63,0.61,0.63,0.65,0.66,0.66,0.68,0.69,0.69,0.71,0.72,0.71,0.68,0.65),(55,0.63,0.63,0.62,0.6,0.62,0.64,0.65,0.65,0.67,0.68,0.68,0.7,0.71,0.7,0.67,0.64),(56,0.61,0.61,0.6,0.58,0.6,0.63,0.64,0.64,0.66,0.67,0.67,0.69,0.7,0.69,0.66,0.63),(57,0.6,0.6,0.59,0.57,0.59,0.62,0.63,0.63,0.65,0.66,0.66,0.68,0.69,0.68,0.65,0.62),(58,0.58,0.58,0.57,0.55,0.57,0.6,0.61,0.61,0.63,0.65,0.65,0.67,0.68,0.67,0.63,0.6),(59,0.57,0.57,0.56,0.54,0.56,0.59,0.6,0.6,0.62,0.64,0.64,0.66,0.67,0.66,0.62,0.59),(60,0.56,0.56,0.54,0.52,0.54,0.58,0.59,0.59,0.61,0.63,0.63,0.65,0.66,0.65,0.61,0.58),(61,0.54,0.54,0.52,0.5,0.52,0.56,0.57,0.57,0.59,0.61,0.61,0.63,0.65,0.63,0.59,0.56),(62,0.53,0.53,0.51,0.49,0.51,0.55,0.56,0.56,0.58,0.6,0.6,0.62,0.64,0.62,0.58,0.55),(63,0.51,0.51,0.49,0.47,0.49,0.53,0.54,0.54,0.56,0.58,0.58,0.6,0.62,0.6,0.56,0.53),(64,0.49,0.49,0.47,0.45,0.47,0.51,0.52,0.52,0.55,0.57,0.57,0.59,0.61,0.59,0.55,0.51),(65,0.47,0.47,0.45,0.43,0.45,0.49,0.51,0.51,0.54,0.56,0.56,0.58,0.6,0.58,0.54,0.49),(66,0.46,0.46,0.44,0.42,0.44,0.48,0.49,0.49,0.52,0.54,0.54,0.57,0.59,0.57,0.52,0.48),(67,0.44,0.44,0.42,0.4,0.42,0.46,0.47,0.47,0.5,0.53,0.53,0.56,0.58,0.56,0.5,0.46),(68,0.42,0.42,0.4,0.38,0.4,0.44,0.46,0.46,0.49,0.51,0.51,0.54,0.56,0.54,0.49,0.44),(69,0.4,0.4,0.38,0.36,0.38,0.42,0.44,0.44,0.47,0.5,0.5,0.53,0.55,0.53,0.47,0.42),(70,0.39,0.39,0.37,0.35,0.37,0.41,0.42,0.42,0.45,0.48,0.48,0.51,0.54,0.51,0.45,0.41),(71,0.37,0.37,0.35,0.33,0.35,0.39,0.41,0.41,0.44,0.47,0.47,0.5,0.53,0.5,0.44,0.39),(72,0.35,0.35,0.33,0.31,0.33,0.37,0.39,0.39,0.43,0.46,0.46,0.49,0.52,0.49,0.43,0.37),(73,0.33,0.33,0.31,0.29,0.31,0.35,0.37,0.37,0.41,0.44,0.44,0.47,0.5,0.47,0.41,0.35),(74,0.32,0.32,0.3,0.28,0.3,0.34,0.36,0.36,0.4,0.43,0.43,0.46,0.49,0.46,0.4,0.34),(75,0.3,0.3,0.28,0.26,0.28,0.32,0.34,0.34,0.38,0.41,0.41,0.45,0.48,0.45,0.38,0.32)]
sideblind=[("-","SW","SE","SSE","S","SSW","WSW","W","E","WNW","NW","NE","NNW","N","NNE","ENE","ESE"),(0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(2,1,1,1,1,1,1,0.99,0.99,1,1,1,1,1,1,1,1),(3,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,1,1,1,1,1,1,1,0.99),(4,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,1,1,1,1,1,1,1,0.99),(5,0.99,0.99,0.99,0.99,0.99,0.99,0.99,0.99,1,1,1,1,1,1,1,0.99),(6,0.99,0.99,0.99,0.99,0.99,0.99,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.99),(7,0.99,0.99,0.99,0.99,0.99,0.99,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.99),(8,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.98),(9,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.98,0.99,0.99,0.99,1,1,1,0.99,0.98),(10,0.98,0.98,0.98,0.98,0.98,0.98,0.97,0.97,0.98,0.99,0.99,1,1,1,0.98,0.98),(11,0.98,0.98,0.98,0.98,0.98,0.98,0.97,0.97,0.98,0.99,0.99,1,1,1,0.98,0.98),(12,0.98,0.98,0.98,0.98,0.98,0.98,0.97,0.97,0.98,0.99,0.99,1,1,1,0.98,0.98),(13,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.97,0.98,0.99,0.99,1,1,1,0.98,0.97),(14,0.97,0.97,0.97,0.97,0.97,0.97,0.96,0.96,0.97,0.98,0.98,1,1,1,0.97,0.97),(15,0.97,0.97,0.97,0.97,0.97,0.97,0.96,0.96,0.97,0.98,0.98,1,1,1,0.97,0.97),(16,0.97,0.97,0.97,0.97,0.97,0.97,0.96,0.96,0.97,0.98,0.98,1,1,1,0.97,0.97),(17,0.96,0.96,0.97,0.97,0.97,0.96,0.95,0.95,0.97,0.98,0.98,1,1,1,0.97,0.96),(18,0.96,0.96,0.96,0.96,0.96,0.96,0.95,0.95,0.97,0.98,0.98,1,1,1,0.97,0.96),(19,0.96,0.96,0.96,0.96,0.96,0.96,0.95,0.95,0.97,0.98,0.98,1,1,1,0.97,0.96),(20,0.96,0.96,0.96,0.96,0.96,0.96,0.95,0.95,0.97,0.98,0.98,1,1,1,0.97,0.96),(21,0.95,0.95,0.96,0.96,0.96,0.95,0.94,0.94,0.96,0.97,0.97,1,1,1,0.96,0.95),(22,0.95,0.95,0.96,0.96,0.96,0.95,0.94,0.94,0.96,0.97,0.97,1,1,1,0.96,0.95),(23,0.95,0.95,0.95,0.95,0.95,0.95,0.94,0.94,0.96,0.97,0.97,1,1,1,0.96,0.95),(24,0.95,0.95,0.95,0.95,0.95,0.95,0.94,0.94,0.96,0.97,0.97,1,1,1,0.96,0.95),(25,0.94,0.94,0.95,0.95,0.95,0.94,0.93,0.93,0.95,0.97,0.97,1,1,1,0.95,0.94),(26,0.94,0.94,0.95,0.95,0.95,0.94,0.93,0.93,0.95,0.97,0.97,1,1,1,0.95,0.94),(27,0.94,0.94,0.95,0.95,0.95,0.94,0.93,0.93,0.95,0.97,0.97,1,1,1,0.95,0.94),(28,0.94,0.94,0.94,0.94,0.94,0.94,0.93,0.93,0.95,0.97,0.97,1,1,1,0.95,0.94),(29,0.93,0.93,0.94,0.94,0.94,0.93,0.92,0.92,0.94,0.96,0.96,1,1,1,0.94,0.93),(30,0.93,0.93,0.94,0.94,0.94,0.93,0.92,0.92,0.94,0.96,0.96,1,1,1,0.94,0.93),(31,0.92,0.92,0.93,0.93,0.93,0.92,0.91,0.91,0.94,0.96,0.96,1,1,1,0.94,0.92),(32,0.92,0.92,0.93,0.93,0.93,0.92,0.91,0.91,0.94,0.96,0.96,1,1,1,0.94,0.92),(33,0.91,0.91,0.92,0.92,0.92,0.91,0.9,0.9,0.93,0.95,0.95,1,1,1,0.93,0.91),(34,0.91,0.91,0.91,0.91,0.91,0.91,0.9,0.9,0.93,0.95,0.95,1,1,1,0.93,0.91),(35,0.9,0.9,0.91,0.91,0.91,0.9,0.89,0.89,0.92,0.95,0.95,1,1,1,0.92,0.9),(36,0.9,0.9,0.9,0.9,0.9,0.9,0.89,0.89,0.92,0.95,0.95,1,1,1,0.92,0.9),(37,0.89,0.89,0.89,0.89,0.89,0.89,0.88,0.88,0.91,0.94,0.94,1,1,1,0.91,0.89),(38,0.89,0.89,0.89,0.89,0.89,0.89,0.88,0.88,0.91,0.94,0.94,1,1,1,0.91,0.89),(39,0.88,0.88,0.88,0.88,0.88,0.88,0.87,0.87,0.91,0.94,0.94,1,1,1,0.91,0.88),(40,0.87,0.87,0.87,0.87,0.87,0.87,0.87,0.87,0.91,0.94,0.94,1,1,1,0.91,0.87),(41,0.87,0.87,0.87,0.87,0.87,0.87,0.86,0.86,0.9,0.93,0.93,1,1,1,0.9,0.87),(42,0.86,0.86,0.86,0.86,0.86,0.86,0.86,0.86,0.9,0.93,0.93,1,1,1,0.9,0.86),(43,0.85,0.85,0.85,0.85,0.85,0.85,0.85,0.85,0.89,0.93,0.93,1,1,1,0.89,0.85),(44,0.85,0.85,0.85,0.85,0.85,0.85,0.85,0.85,0.89,0.93,0.93,1,1,1,0.89,0.85),(45,0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.88,0.92,0.92,1,1,1,0.88,0.84),(46,0.83,0.83,0.83,0.83,0.83,0.83,0.83,0.83,0.88,0.92,0.92,1,1,1,0.88,0.83),(47,0.83,0.83,0.83,0.82,0.83,0.83,0.83,0.83,0.88,0.92,0.92,1,1,1,0.88,0.83),(48,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.87,0.91,0.91,1,1,1,0.87,0.82),(49,0.82,0.82,0.82,0.81,0.82,0.82,0.82,0.82,0.87,0.91,0.91,1,1,1,0.87,0.82),(50,0.81,0.81,0.81,0.8,0.81,0.81,0.81,0.81,0.86,0.91,0.91,1,1,1,0.86,0.81),(51,0.8,0.8,0.8,0.79,0.8,0.8,0.8,0.8,0.85,0.9,0.9,1,1,1,0.85,0.8),(52,0.79,0.79,0.79,0.78,0.79,0.8,0.8,0.8,0.85,0.9,0.9,1,1,1,0.85,0.8),(53,0.79,0.79,0.79,0.78,0.79,0.79,0.79,0.79,0.85,0.9,0.9,1,1,1,0.85,0.79),(54,0.78,0.78,0.78,0.77,0.78,0.79,0.79,0.79,0.85,0.9,0.9,1,1,1,0.85,0.79),(55,0.77,0.77,0.77,0.76,0.77,0.78,0.78,0.78,0.84,0.89,0.89,1,1,1,0.84,0.78),(56,0.76,0.76,0.76,0.75,0.76,0.77,0.77,0.77,0.83,0.89,0.89,1,1,1,0.83,0.77),(57,0.76,0.76,0.75,0.74,0.75,0.77,0.77,0.77,0.83,0.89,0.89,1,1,1,0.83,0.77),(58,0.75,0.75,0.75,0.74,0.75,0.76,0.76,0.76,0.82,0.88,0.88,1,1,1,0.82,0.76),(59,0.75,0.75,0.74,0.73,0.74,0.76,0.76,0.76,0.82,0.88,0.88,1,1,1,0.82,0.76),(60,0.74,0.74,0.73,0.72,0.73,0.75,0.75,0.75,0.82,0.88,0.88,1,1,1,0.82,0.75),(61,0.73,0.73,0.72,0.71,0.72,0.74,0.74,0.74,0.81,0.87,0.87,1,1,1,0.81,0.74),(62,0.72,0.72,0.71,0.7,0.71,0.73,0.74,0.74,0.81,0.87,0.87,1,1,1,0.81,0.73),(63,0.71,0.71,0.7,0.69,0.7,0.72,0.73,0.73,0.8,0.87,0.87,1,1,1,0.8,0.72),(64,0.7,0.7,0.69,0.68,0.69,0.71,0.72,0.72,0.79,0.86,0.86,1,1,1,0.79,0.71),(65,0.7,0.7,0.69,0.67,0.69,0.71,0.72,0.72,0.79,0.86,0.86,1,1,1,0.79,0.71),(66,0.69,0.69,0.68,0.66,0.68,0.7,0.71,0.71,0.79,0.86,0.86,1,1,1,0.79,0.7),(67,0.68,0.68,0.67,0.65,0.67,0.69,0.7,0.7,0.78,0.85,0.85,1,1,1,0.78,0.69),(68,0.67,0.67,0.66,0.64,0.66,0.69,0.7,0.7,0.78,0.85,0.85,1,1,1,0.78,0.69),(69,0.66,0.66,0.65,0.63,0.65,0.68,0.69,0.69,0.77,0.85,0.85,1,1,1,0.77,0.68),(70,0.65,0.65,0.64,0.62,0.64,0.67,0.68,0.68,0.76,0.84,0.84,1,1,1,0.76,0.67),(71,0.65,0.65,0.63,0.61,0.63,0.67,0.68,0.68,0.76,0.84,0.84,1,1,1,0.76,0.67),(72,0.64,0.64,0.62,0.6,0.62,0.66,0.67,0.67,0.76,0.84,0.84,1,1,1,0.76,0.66),(73,0.63,0.63,0.61,0.59,0.61,0.65,0.66,0.66,0.75,0.83,0.83,1,1,1,0.75,0.65),(74,0.62,0.62,0.6,0.58,0.6,0.64,0.66,0.66,0.75,0.83,0.83,1,1,1,0.75,0.64),(75,0.61,0.61,0.59,0.57,0.59,0.63,0.65,0.65,0.74,0.83,0.83,1,1,1,0.74,0.63)]

windows=len(windows_out_vertical)+len(windows_out_horizontal)
Qisol_month=np.zeros((windows,12))
for i in range(len(windows_out_vertical)):
    orientation=windows_out_vertical[i]["Orientation"]
    index_h=horizon[0].index(orientation)
    index_o=overhang[0].index(orientation)
    index_s=sideblind[0].index(orientation)
    hor=windows_out_vertical[i]["hor"]
    over=windows_out_vertical[i]["over"]
    side1=windows_out_vertical[i]["side1"]
    side2=windows_out_vertical[i]["side2"]

    #fs1 - factor for horizon
    #fs2 - factor for overhang
    #fs3,1 - sideblinds
    #fs3,2 - sideblinds

    if hor==0:
        fs1=1
    elif hor<1:
        fs1=hor
    else:
        fs1=horizon[hor+1][index_h]  #plus 1?

    fs2=overhang[over+1][index_o]
    fs3_1=sideblind[side1+1][index_s]

    # if orientation in ["SW", "SE", "S", "SSW", "SSE"]:
    if orientation=="SW" or orientation=="SE" or orientation=="S" or orientation=="SSW" or orientation=="SSE":
        fs3_2=sideblind[side2+1][index_s]
    else:
        fs3_2=1
    irradiance_orient=[("H","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N","NNE","NE","ENE","E","ESE")]
    index_ir=irradiance_orient[0].index(orientation)

    for j in range(12):
        Qisol_month[i][j]=(irradiance[index_ir][j])*0.9*windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["gvalue_wind"]*windows_out_vertical[i]["glass_perc"]*windows_out_vertical[i]["coef1"]*windows_out_vertical[i]["coef2"]*windows_out_vertical[i]["coef3"]*windows_out_vertical[i]["coef4"]/EBF
        k=i+1
    Q_solar_gains=Qisol_month.sum(axis=0)


for n in range(len(windows_out_horizontal)):
    horS=windows_out_horizontal[n]["HorizonS"]
    horW=windows_out_horizontal[n]["HorizonW"]
    horO=windows_out_horizontal[n]["HorizonO"]
    horN=windows_out_horizontal[n]["HorizonN"]
    fs1=horizon[horS+1] [4]
    fs2=horizon[horW+1] [7]
    fs3_1=horizon[horO+1][8]
    fs3_2=horizon[horN+1][13]
    for j in range(12):
        m=k+n
        Qisol_month[m][j]=(irradiance[0][j])*windows_out_horizontal[n]["Area_wind_h"]*windows_out_horizontal[n]["glass_perc_h"]*windows_out_horizontal[n]["g-value_wind_h"]*0.9*fs1*fs2*fs3_1*fs3_2/EBF

Qisol_m=sum(Qisol_month)

Qisol=[]
for x in range(60):
    for y in Qisol_m:
        Qisol.append(y)

#Qisol_annual=sum(Qisol_m)
#transmission losses
Qtr_losses=np.zeros(720)
#total losses
Qtotal_losses=np.zeros(720)
#heat gains
Qheat_gains=np.zeros(720)
#heat gains/losses coefficient
Qcoef=np.zeros(720)
#time constant
Time_constant=np.zeros(720)
#Heat loss coefficient
Heat_loss_coef=np.zeros(720)
#utilization factor
Utiliz_factor=np.zeros(720)
#Util_degree_for heat gains
Utiliz_degree_case1=np.zeros(720)
Utiliz_degree_case2=np.zeros(720)
Utiliz_degree_decision=np.zeros(720)
#Utilized heat gains
Utilized_heatgain=np.zeros(720)
#Heating demand
Heating_demand=np.zeros(720)

H_comp=0.0 # heat transfer coeff. for components

if R_ext_wall_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+comp_out_walls[0]["Area"]*(1/R_ext_wall_all)
if R_ext_wall_ag_tech_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_walls_against_tech[0]["Area"]*(1/R_ext_wall_ag_tech_all)
if R_ext_wall_shops_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_walls_shops_tech[0]["Area"]*(1/R_ext_wall_shops_all)
if R_wall_ag_shelt_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+wall_against_shelter[0]["Area"]*(1/R_wall_ag_shelt_all)
if R_ext_wall5==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_wall5[0]["Area"]*(1/R_ext_wall5)
if R_ext_wall6==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_wall6[0]["Area"]*(1/R_ext_wall6)
if R_ext_wall7==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_wall7[0]["Area"]*(1/R_ext_wall7)
if R_ext_wall8all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+ext_wall8[0]["Area"]*(1/R_ext_wall8all)    
if R_roof_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+comp_out_roof[0]["Area"]*(1/R_roof_all)    
if R_roof_all2==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+roof2[0]["Area"]*(1/R_roof_all2)    
if R_roof_all3==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+roof3[0]["Area"]*(1/R_roof_all3)  
if R_comp_in_ceiling_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+components_in_ceiling[0]["Area_in"]*(1/R_comp_in_ceiling_all)  
if R_comp_in_wall_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+components_in_wall[0]["Area_in"]*(1/R_comp_in_wall_all) 
if R_comp_in_floor_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+components_in_floor[0]["Area_in"]*(1/R_comp_in_floor_all) 
if R_comp_in_floor_all2==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+components_in_floor2[0]["Area_in"]*(1/R_comp_in_floor_all2) 
if R_comp_in_floor_all3==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+components_in_floor3[0]["Area_in"]*(1/R_comp_in_floor_all3) 
if R_floor_ag_ext_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+floor_against_exterior[0]["Area"]*(1/R_floor_ag_ext_all) 
if R_floor_ag_shelt_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+floor_against_shelter[0]["Area"]*(1/R_floor_ag_shelt_all) 
if R_floor_ag_tech_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+comp_out_floor_against_tech[0]["Area"]*(1/R_floor_ag_tech_all) 
if R_floor4_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+floor4[0]["Area"]*(1/R_floor4_all) 
if R_floor5_all==0:
    H_comp=H_comp+0
else:
    H_comp=H_comp+floor5[0]["Area"]*(1/R_floor5_all) 
for i in range(len(windows_out_vertical)):
    H_comp=H_comp+windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["UValue_wind"]    
for i in range(len(windows_out_horizontal)):
    H_comp=H_comp+windows_out_horizontal[i]["Area_wind_h"]*windows_out_horizontal[i]["U-Value_wind_h"]

"""
H_transfer_coef=0
for i in range(len(comp_out_walls)):
    H_transfer_coef=H_transfer_coef+comp_out_walls[i]["Area"]*(1/R_ext_wall_all)
for i in range(len(comp_out_roof)):
    H_transfer_coef=H_transfer_coef+comp_out_roof[i]["Area"]*(1/R_roof_all)
for i in range(len(comp_out_floor_against_tech)):
    H_transfer_coef=H_transfer_coef+comp_out_floor_against_tech[i]["Area"]*(1/R_floor_ag_tech_all)
for i in range(len(windows_out_vertical)):
    H_transfer_coef=H_transfer_coef+windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["UValue_wind"]
for i in range(len(windows_out_horizontal)):
    H_transfer_coef=H_transfer_coef+windows_out_horizontal[i]["Area_wind_h"]*windows_out_horizontal[i]["U-Value_wind_h"]
"""

for i in range(720):
    Qtr_losses[i]=Q_transm_loss[i]+Q_transm_loss[i]*thermal_bridge

    #total losses

    if vent_type == 1:
        Qtotal_losses[i]=Qtr_losses[i] +Q_vent_loss_nat[i]
    else:
        if heat_rec==1:
            Qtotal_losses[i]=Qtr_losses[i] +Q_vent_loss_mech_year[i]
        else:
            Qtotal_losses[i]=Qtr_losses[i]+Qvent_without_heat_rec1[i]

    #heat gains
    Qheat_gains[i]=Qiel1[i]+Qiocc1[i]+Qisol[i]

    #Heat gains to loss ratio
    Qcoef[i]=Qheat_gains[i]/Qtotal_losses[i]

    #time constant
    Time_constant[i]=constr_factor*EBF*1000/(H_comp+Air_flow_therm_eff*EBF*heat_storage_capacity)

    #Heat loss coefficient
    Heat_loss_coef[i]=(H_transfer_coef+Air_flow_therm_eff*heat_storage_capacity*EBF/3600)*(1+thermal_bridge)

    #Utilization factor
    Utiliz_factor[i]=Util_parameter+Time_constant[i]/Reference_time_constant
    
    #Utiliz_factor
    if Qtotal_losses[i]<0:
        Utiliz_degree_case1[i]=0
    else:
        Utiliz_degree_case1[i]=1
    
    if Qcoef[i]==1:
        Utiliz_degree_case2[i]=Util_parameter/(Util_parameter+1)
    else:
        Utiliz_degree_case2[i]=(1-(Qcoef[i]**Utiliz_factor[i]))/(1-(Qcoef[i]**(Utiliz_factor[i]+1)))
    
    if Utiliz_degree_case1[i]==0:
        Utiliz_degree_decision[i]==0
    else:
        Utiliz_degree_decision[i]=Utiliz_degree_case2[i]

    #Utilized heat gains
    Utilized_heatgain[i]=Qheat_gains[i]*Utiliz_degree_decision[i]

    #Heating demand
    Heating_demand[i]=(Qtotal_losses[i]-Utilized_heatgain[i])


Heating_demand_annual=[]
k=np.array_split(Heating_demand,60)  # k -> np.array
#Heating_demand_annual.append(k)      # Heating_demand_annual -> [ np.array ]
Heating_demand_annual = k

#print(Heating_demand_annual)
Qhd=[ sum(elem) for elem in Heating_demand_annual ]

#final energy
Qheating_demand=[]
for i in Qhd:
    Q_final=i*(1+final_energy_losses)
    Qheating_demand.append(Q_final)
Corr_factor_mean_temp=(1-1*(0.06*(9.4-annual_mean_temp)))


#Area of the components

Ath=0
for i in range(len(comp_out_walls)):
    Ath=Ath+comp_out_walls[0]["Area"]
for i in range(len(comp_out_roof)):
    Ath=Ath+comp_out_roof[0]["Area"]
for i in range(len(comp_out_floor_against_tech)):
    Ath=Ath+comp_out_floor_against_tech[0]["Area"]
for i in range(len(components_in_wall)):
    Ath=Ath+components_in_wall[0]["Area_in"]
for i in range(len(windows_out_vertical)):
    Ath=Ath+windows_out_vertical[0]["Area_wind"]
for i in range(len(windows_out_horizontal)):
    Ath=Ath+windows_out_horizontal[0]["Area_wind_h"]


if build_case==1:
    Qhli=Corr_factor_mean_temp*(Base_Qh+Delta_Qh*(Ath/EBF))
    Qhta=Qhli*0.6
else:
    Qhli=Corr_factor_mean_temp*(Base_Qh+Delta_Qh*(Ath/EBF))
    Qhta=Qhli/1.5

#LCA part
#LCA heating
Heating_renovation_operation_GWP_old = np.zeros(1)
Heating_renovation_operation_cost_old = np.zeros(1)
Price_growth_heating_old = np.zeros(1)
RSL_heat_generation_old = np.zeros(1)
Embodied_heat_generation_old=np.zeros(1)
Initial_cost_heat_generation_old=np.zeros(1)
for i in Heating_system:
    if round(heating_type) == i["Type"]:
        Heating_renovation_operation_GWP_old = i["GWP production"]
        Heating_renovation_operation_cost_old = i["Cost production"]
        Price_growth_heating_old = i["Price growth rate heating"]
        Embodied_heat_generation_old = i["Embodied_GWP_heat_generation"]
        RSL_heat_generation_old = i["RSL"]
        Initial_cost_heat_generation_old = i["Initial_cost_heat_generation"]
LCA_old_operation=[]
for year in Qheating_demand:
    oper=year*Heating_renovation_operation_GWP_old*EBF
    LCA_old_operation.append(oper)
    units="kg CO2-eq."
LCA_oper=sum(LCA_old_operation)

#heat generation
def frange(start, stop, step):
    x=start
    while x < stop:
        yield x
        x += step
rn_heat_gen_old=math.ceil(timeperiod/RSL_heat_generation_old) - 1
LCA_replace_heat_gen_old=round((Embodied_heat_generation_old*EBF*rn_heat_gen_old),1)

initial_heat_gen_old=Initial_cost_heat_generation_old*EBF
RSL_heat_gen_old=[]
for x in frange(RSL_heat_generation_old,timeperiod,RSL_heat_generation_old):
    RSL_heat_gen_old.append(x)

repl_cost_heat_gen_old=[]
for k in RSL_heat_gen_old:
    repl_cost=round(initial_heat_gen_old*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    repl_cost_heat_gen_old.append(repl_cost)

Total_LCA_old = LCA_oper + LCA_replace_heat_gen_old 

#LCC
LCC_old=[]
for year, period in zip(Qheating_demand, range(1,61)):
    #LCC_tot=i*EBF*heating_cost*(1+price_growth_heating)
    #LCC_operation=year*EBF*heating_cost_new*(1+Price_growth_heating)
    LCC_operation_old=year*EBF*Heating_renovation_operation_cost_old*((1+inflation_rate+Price_growth_heating_old)**period)/((1+interest_rate+inflation_rate)**period)
    LCC_old.append(LCC_operation_old)

Maintenance_heating_system_old = []
for t in range(round(timeperiod)):
    Maintenance_heating_system_old.append((initial_heat_gen_old*Maintenance_LCC[0]["Maintenance_LCC"]/100)*(1+inflation_rate)**t/((1+interest_rate)**t))

LCC_total_old = sum(LCC_old) + sum(repl_cost_heat_gen_old) + sum(Maintenance_heating_system_old)

#Renovation
#electrical equipment
electr_eq_type1 = 1
electr_eq_type1 == electr_equip[0]

electr_eq_type2 =2
electr_eq_type2 == electr_equip[0]

#heat generation
heat_gen_type1 = 1
heat_gen_type1 == heat_gen[0]

heat_gen_type2 = 2
heat_gen_type2 == heat_gen[0]

#heat distribution
heat_distr_type1 = 1
heat_distr_type1 == heat_distr[0]

heat_distr_type2 = 2
heat_distr_type2 == heat_distr[0]

#ventilation system
vent_type1 = 1
vent_type1 == vent_system[0]

vent_type2=2
vent_type2 == vent_system[0]

#water system
water_system_type1 = 1
water_system_type1 == water_system[0]

water_system_type2 = 2
water_system_type2 == water_system[0]

#Heating demand of a renovated building
Q_t_monthly_ext_walls_new=np.zeros((num_components,12))
Q_t_monthly_ext_walls_new=np.zeros((num_components,12))
Q_t_monthly_floor_ag_tech_new=np.zeros((num_components,12))
Q_t_monthly_roof_new=np.zeros((num_components,12))

#exterior walls new
conductivity_uncertainty=[]
for i in New_components:
    conductivity_uncertainty.append(i["Uncertainty_conductivity"])
#exterior walls 1
Q_t_y_ext_wall_new=[]
R_wall1=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[0]["Type"]): 
        if round(New_components[0]["Type"])==0:
            R1=0        
        elif math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R1_ins= New_components[0]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[0]))
            R_wall1.append(R1_ins)
        else:
            R1= i[3]/(i[4]*(1+conductivity_uncertainty[0]))      
            R_wall1.append(R1)  
R_ext_wall_new=sum(R_wall1)
Q_t_m_ext_wall_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[0]["Type"])==0:
        Q_t_m_ext_wall_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_walls[0]["Area"] * (1/(R_ext_wall_all+0.17))* 24/(EBF*1000)
    elif R_ext_wall_new==0 and R_ext_wall_all==0:
        Q_t_m_ext_wall_new[j][k]=0
    else:    
        Q_t_m_ext_wall_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_walls[0]["Area"] * (1/(R_ext_wall_new + R_ext_wall_all+0.17))* 24/(EBF*1000)
Q_m_ext_wall_new=Q_t_m_ext_wall_new.sum(axis=0)
for i in range(60):
    Q_t_y_ext_wall_new.append(Q_m_ext_wall_new)


#Ext_walls_2
R_wall2=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[1]["Type"]): 
        if round(New_components[1]["Type"])==0:
            R2=0        
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R2_ins= New_components[1]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[1]))
            R_wall2.append(R2_ins)
        else:
            R2= i[3]/(i[4]*(1+conductivity_uncertainty[1]))
            R_wall2.append(R2)
R_ext_wall_ag_tech_new=sum(R_wall2)
Q_t_y_ext_wall_ag_tech_new=[]
Q_t_m_ext_wall_ag_tech_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[1]["Type"])==0:
        Q_t_m_ext_wall_ag_tech_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_against_tech[0]["Area"] * (1/(R_ext_wall_ag_tech_all+0.17))* 24/(EBF*1000)
    else:     
        Q_t_m_ext_wall_ag_tech_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_against_tech[0]["Area"] * (1/(R_ext_wall_ag_tech_new+R_ext_wall_ag_tech_all+0.17))* 24/(EBF*1000)
Q_m_ext_wall_ag_tech_new=Q_t_m_ext_wall_ag_tech_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall_ag_tech_new.append(Q_m_ext_wall_ag_tech_new)
#ext_walls_3
R_wall3=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[2]["Type"]): 
        if round(New_components[2]["Type"])==0:
            R3=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R3_ins= New_components[2]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[2]))
            R_wall3.append(R3_ins)
        else:
            R3= i[3]/(i[4]*(1+conductivity_uncertainty[2]))
            R_wall3.append(R3)
R_ext_wall_shops_new=sum(R_wall3)
Q_t_y_ext_wall_shops_new=[]
Q_t_m_ext_wall_shops_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[2]["Type"])==0:
        Q_t_m_ext_wall_shops_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_shops_tech[0]["Area"] * (1/(R_ext_wall_shops_all+0.17))* 24/(EBF*1000)
    else:
        Q_t_m_ext_wall_shops_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_walls_shops_tech[0]["Area"] * (1/(R_ext_wall_shops_new+R_ext_wall_shops_all+0.17))* 24/(EBF*1000)
Q_m_ext_wall_shops_new=Q_t_m_ext_wall_shops_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall_shops_new.append(Q_m_ext_wall_shops_new)

#wall_4
R_wall4=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[3]["Type"]): 
        if round(New_components[3]["Type"])==0:
            R4=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R1_ins= New_components[3]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[3]))
            R_wall1.append(R1_ins)
        else:
            R4= i[3]/(i[4]*(1+conductivity_uncertainty[3]))
            R_wall4.append(R4)
R_wall_ag_shelt_new=sum(R_wall4)
Q_t_y_wall_ag_shelt_new=[]
Q_t_m_wall_ag_shelt_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[3]["Type"])==0:
        Q_t_m_wall_ag_shelt_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*wall_against_shelter[0]["Area"] * (1/(0.17+R_wall_ag_shelt_all))* 24/(EBF*1000)
    else:
        Q_t_m_wall_ag_shelt_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*wall_against_shelter[0]["Area"] * (1/(R_wall_ag_shelt_new+0.17+R_wall_ag_shelt_all))* 24/(EBF*1000)
Q_m_wall_ag_shelt_new=Q_t_m_wall_ag_shelt_new.sum(axis=0)
for i in range(60):
    Q_t_y_wall_ag_shelt_new.append(Q_m_wall_ag_shelt_new)

#ext wall5 new
R_wall5=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[4]["Type"]): 
        if New_components[4]["Type"]==0:
            R5=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R5_ins= New_components[4]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[4]))
            R_wall5.append(R5_ins)
        else:
            R5= i[3]/(i[4]*(1+conductivity_uncertainty[4]))
            R_wall5.append(R5)
R_ext_wall5_new=sum(R_wall5)
Q_t_y_ext_wall5_new=[]
Q_t_m_ext_wall5_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[4]["Type"])==0:
        Q_t_m_ext_wall5_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall5[0]["Area"] * (1/(0.17+R_ext_wall5))* 24/(EBF*1000)
    else:
        Q_t_m_ext_wall5_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall5[0]["Area"] * (1/(R_ext_wall5_new+0.17+R_ext_wall5))* 24/(EBF*1000)
Q_m_ext_wall5_new=Q_t_m_ext_wall5_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall5_new.append(Q_m_ext_wall5_new)

#ext wall6 new
R_wall6=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[5]["Type"]): 
        if round(New_components[5]["Type"])==0:
            R6=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R6_ins= New_components[5]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[5]))
            R_wall6.append(R6_ins)  
        else:              
            R6= i[3]/(i[4]*(1+conductivity_uncertainty[5]))
            R_wall6.append(R6)
R_ext_wall6_new=sum(R_wall6)
Q_t_y_ext_wall6_new=[]
Q_t_m_ext_wall6_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[5]["Type"])==0:
        Q_t_m_ext_wall6_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall6[0]["Area"] * (1/(0.17+R_ext_wall6))* 24/(EBF*1000)
    else:
        Q_t_m_ext_wall6_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall6[0]["Area"] * (1/(R_ext_wall6_new+0.17+R_ext_wall6))* 24/(EBF*1000)
Q_m_ext_wall6_new=Q_t_m_ext_wall6_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall6_new.append(Q_m_ext_wall6_new)

#ext wall7 new
R_wall7=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[6]["Type"]): 
        if round(New_components[6]["Type"])==0:
            R6=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R7_ins= New_components[6]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[6]))
            R_wall7.append(R7_ins)  
        else:         
            R7= i[3]/(i[4]*(1+conductivity_uncertainty[6]))
            R_wall7.append(R7)
R_ext_wall7_new=sum(R_wall7)
Q_t_y_ext_wall7_new=[]
Q_t_m_ext_wall7_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[6]["Type"])==0:
        Q_t_m_ext_wall7_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall7[0]["Area"] * (1/(0.17+R_ext_wall7))* 24/(EBF*1000)
    else:
        Q_t_m_ext_wall7_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall7[0]["Area"] * (1/(R_ext_wall7_new+0.17+R_ext_wall7))* 24/(EBF*1000)
Q_m_ext_wall7_new=Q_t_m_ext_wall7_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall7_new.append(Q_m_ext_wall7_new)

#ext wall8 new
R_wall8=[]
for i in exterior_wall_ren: 
    if i[0] == round(New_components[7]["Type"]): 
        if round(New_components[7]["Type"])==0:
            R8=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R8_ins= New_components[7]["Insulation thickness"]/(i[4]*(1+conductivity_uncertainty[7]))
            R_wall8.append(R8_ins)  
        else:                 
            R8= i[3]/(i[4]*(1+conductivity_uncertainty[7]))
            R_wall8.append(R8)
R_ext_wall8_new=sum(R_wall8)
Q_t_y_ext_wall8_new=[]
Q_t_m_ext_wall8_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components[7]["Type"])==0:
        Q_t_m_ext_wall8_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall8[0]["Area"] * (1/(0.17+R_ext_wall8all))* 24/(EBF*1000)
    else:
        Q_t_m_ext_wall8_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*ext_wall8[0]["Area"] * (1/(R_ext_wall8_new+0.17+R_ext_wall8all))* 24/(EBF*1000)
Q_m_ext_wall8_new=Q_t_m_ext_wall8_new.sum(axis=0)  
for i in range(60):
    Q_t_y_ext_wall8_new.append(Q_m_ext_wall8_new)

Q_t_ext_walls_new = []
for a, b, c, d, e, f, g, h in zip(Q_t_y_ext_wall_new, Q_t_y_ext_wall_ag_tech_new, Q_t_y_ext_wall_shops_new, Q_t_y_wall_ag_shelt_new, Q_t_y_ext_wall5_new, Q_t_y_ext_wall6_new, Q_t_y_ext_wall7_new, Q_t_y_ext_wall8_new):
    Q_t_ext_walls_new.append(a+ b+ c+ d+ e+ f+ g+ h)
Q_transm_loss_walls_new=np.concatenate(Q_t_ext_walls_new, axis=0)

#components in ceiling new
R_ceil_unheated1=[]
for i in unheated_ren: 
    if i[0] == round(New_components_against_unheated[4]["Type"]) and i[1] == "Dach": 
        if round(New_components_against_unheated[4]["Type"])==0:
            R_ceil1=0
        if math.isnan(i[4]) or math.isnan(i[5]):
            continue
        if i[3]=="Insulation" or i[3]=="insulation":
            R_ceil_ins= New_components_against_unheated[4]["Insulation thickness"]/i[5]
            R_ceil_unheated1.append(R_ceil_ins)  
        else:                 
            R_ceil1= i[4]/i[5]
            R_ceil_unheated1.append(R_ceil1)
R_ceil1_unheated_all=sum(R_ceil_unheated1)
Q_t_y_comp_in_ceiling_new=[]
Q_t_m_comp_in_ceiling_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components_against_unheated[4]["Type"])==0:
        Q_t_m_comp_in_ceiling_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_ceiling[0]["Area_in"] * (1/(0.26 + R_comp_in_ceiling_all))* components_in_ceiling[0]["b-value"]*24/(EBF*1000)
    else:
        Q_t_m_comp_in_ceiling_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_ceiling[0]["Area_in"] * (1/(R_ceil1_unheated_all + 0.26 + R_comp_in_ceiling_all))* components_in_ceiling[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_ceiling_new=Q_t_m_comp_in_ceiling_new.sum(axis=0)  
for i in range(60):
    Q_t_y_comp_in_ceiling_new.append(Q_m_comp_in_ceiling_new)

#components in wall new
R_wall_unheated1=[]
for i in unheated_ren: 
    if i[0] == round(New_components_against_unheated[0]["Type"]) and i[1] == "Wand": 
        if round(New_components_against_unheated[0]["Type"])==0:
            R_wall1=0
        if math.isnan(i[4]) or math.isnan(i[5]):
            continue
        if i[3]=="Insulation" or i[3]=="insulation":
            R_wall_ins= New_components_against_unheated[0]["Insulation thickness"]/i[5]
            R_wall_unheated1.append(R_wall_ins)  
        else:                 
            R_wall1= i[4]/i[5]
            R_wall_unheated1.append(R_wall1)
R_wall1_unheated_all=sum(R_wall_unheated1)
Q_t_comp_in_year_new=[]
Q_t_m_comp_in_wall_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components_against_unheated[0]["Type"])==0:
        Q_t_m_comp_in_wall_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_wall[0]["Area_in"] * (1/(0.13 + R_comp_in_wall_all))* components_in_wall[0]["b-value"]*24/(EBF*1000)
    else:
        Q_t_m_comp_in_wall_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_wall[0]["Area_in"] * (1/(R_wall1_unheated_all+0.13 + R_comp_in_wall_all))* components_in_wall[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_wall_new=Q_t_m_comp_in_wall_new.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_year_new.append(Q_m_comp_in_wall_new)

#components in slab1 
R_slab_unheated1=[]
for i in unheated_ren: 
    if i[0] == round(New_components_against_unheated[1]["Type"]) and i[1] == "Boden": 
        if round(New_components_against_unheated[1]["Type"])==0:
            R_slab1=0
        if math.isnan(i[4]) or math.isnan(i[5]):
            continue
        if i[3]=="Insulation" or i[3]=="insulation":
            R_slab_ins= New_components_against_unheated[1]["Insulation thickness"]/i[5]
            R_slab_unheated1.append(R_slab_ins)  
        else:                 
            R_slab1= i[4]/i[5]
            R_slab_unheated1.append(R_slab1)
R_slab1_unheated_all=sum(R_slab_unheated1)
Q_t_m_comp_in_floor_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components_against_unheated[1]["Type"])==0:
        Q_t_m_comp_in_floor_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor[0]["Area_in"] * (1/(0.26 + R_comp_in_floor_all))* components_in_floor[0]["b-value"]*24/(EBF*1000)
    else:
        Q_t_m_comp_in_floor_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor[0]["Area_in"] * (1/(R_slab1_unheated_all + 0.26 + R_comp_in_floor_all))* components_in_floor[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor_new=Q_t_m_comp_in_floor_new.sum(axis=0)  
Q_t_comp_in_floor_year_new = []
for i in range(60):
    Q_t_comp_in_floor_year_new.append(Q_m_comp_in_floor_new)

#components in slab2 new
R_slab_unheated2=[]
for i in unheated_ren: 
    if i[0] == round(New_components_against_unheated[2]["Type"]) and i[1] == "Boden": 
        if round(New_components_against_unheated[2]["Type"])==0:
            R_slab2=0
        if math.isnan(i[4]) or math.isnan(i[5]):
            continue
        if i[3]=="Insulation" or i[3]=="insulation":
            R_slab_ins= New_components_against_unheated[2]["Insulation thickness"]/i[5]
            R_slab_unheated2.append(R_slab_ins)  
        else:                 
            R_slab2= i[4]/i[5]
            R_slab_unheated2.append(R_slab2)
R_slab2_unheated_all=sum(R_slab_unheated2)
Q_t_comp_in_floor_year2_new=[]
Q_t_m_comp_in_floor2_new=np.zeros((num_components,12))
for k in range(12):
    if New_components_against_unheated[2]["Type"]==0:
        Q_t_m_comp_in_floor2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor2[0]["Area_in"] * (1/(R_comp_in_floor_all2+0.26))* components_in_floor2[0]["b-value"]*24/(EBF*1000)
    else:
        Q_t_m_comp_in_floor2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor2[0]["Area_in"] * (1/(R_slab2_unheated_all + R_comp_in_floor_all2+0.26))* components_in_floor2[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor2_new=Q_t_m_comp_in_floor2_new.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_floor_year2_new.append(Q_m_comp_in_floor2_new)

#components in slab3 new
R_slab_unheated3=[]
for i in unheated_ren: 
    if i[0] == round(New_components_against_unheated[3]["Type"]) and i[1] == "Boden": 
        if round(New_components_against_unheated[3]["Type"])==0:
            R_slab3=0
        if math.isnan(i[4]) or math.isnan(i[5]):
            continue
        if i[3]=="Insulation" or i[3]=="insulation":
            R_slab_ins= New_components_against_unheated[3]["Insulation thickness"]/i[5]
            R_slab_unheated3.append(R_slab_ins)  
        else:                 
            R_slab3= i[4]/i[5]
            R_slab_unheated3.append(R_slab3)
R_slab3_unheated_all=sum(R_slab_unheated3)
Q_t_comp_in_floor_year3_new=[]
Q_t_m_comp_in_floor3_new=np.zeros((num_components,12))
for k in range(12):
    if round(New_components_against_unheated[3]["Type"])==0:
        Q_t_m_comp_in_floor3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor3[0]["Area_in"] * (1/(0.26+R_comp_in_floor_all3))* components_in_floor3[0]["b-value"]*24/(EBF*1000)
    else:
        Q_t_m_comp_in_floor3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*components_in_floor3[0]["Area_in"] * (1/(R_slab3_unheated_all+0.26+R_comp_in_floor_all3))* components_in_floor3[0]["b-value"]*24/(EBF*1000)
Q_m_comp_in_floor3_new=Q_t_m_comp_in_floor3_new.sum(axis=0)  
for i in range(60):
    Q_t_comp_in_floor_year3_new.append(Q_m_comp_in_floor3_new)

Q_t_comp_in_floor_new=[]
for a,b,c in zip(Q_t_comp_in_floor_year3_new, Q_t_comp_in_floor_year2_new, Q_t_comp_in_floor_year_new):
    Q_t_comp_in_floor_new.append(a+b+c)

#roof
Uncertainty_conductivity_roof=[]
for i in New_components_roof:
    Uncertainty_conductivity_roof.append(i["Uncertainty conductivity roof"])

#roof new
Roof1=[]
for i in roof_ren: 
    if i[0] == round(New_components_roof[0]["Type"]): 
        if round(New_components_roof[0]["Type"])==0:
            R_roof1=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R1_r_ins = New_components_roof[0]["Insulation thickness"]/((1+Uncertainty_conductivity_roof[0])*i[4])
            Roof1.append(R1_r_ins)    
        else:        
            R_roof1= i[3]/((1+Uncertainty_conductivity_roof[0])*i[4])    
            Roof1.append(R_roof1)
R_roof_all_new=sum(Roof1)
Q_t_y_roof1_new=[]
Q_t_m_roof_new=np.zeros((num_components,12))
Q_t_y_roof_new=[]
for k in range(12):
    if round(New_components_roof[0]["Type"])==0:
        Q_t_m_roof_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_roof[0]["Area"] * (1/(R_roof_all+0.17))* 24/(EBF*1000)
    elif R_roof_all_new==0 and R_roof_all==0:
        Q_t_m_roof_new[j][k]=0
    else:
        Q_t_m_roof_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_roof[0]["Area"] * (1/(R_roof_all_new+R_roof_all+0.17))* 24/(EBF*1000)
Q_t_y_roof_new=Q_t_m_roof_new.sum(axis=0) 
for i in range(60):
    Q_t_y_roof1_new.append(Q_t_y_roof_new)

#roof2 new
Roof2=[]
for i in roof_ren: 
    if i[0] == round(New_components_roof[1]["Type"]): 
        if round(New_components_roof[1]["Type"])==0:
            R_roof2=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R2_r_ins = New_components_roof[1]["Insulation thickness"]/((Uncertainty_conductivity_roof[1]+1)*i[4])
            Roof2.append(R2_r_ins)    
        else:          
            R_roof2= i[3]/((Uncertainty_conductivity_roof[1]+1)*i[4])
            Roof2.append(R_roof2)
R_roof_all2_new=sum(Roof2)
Q_t_m_roof2_new=np.zeros((num_components,12))
Q_t_y_roof2_new=[]
for k in range(12):
    if round(New_components_roof[1]["Type"])==0:
        Q_t_m_roof2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof2[0]["Area"] * (1/(0.17+R_roof_all2))* 24/(EBF*1000)
    elif R_roof_all2==0 and R_roof_all2_new==0:
        Q_t_m_roof2_new[j][k]=0
    else:
        Q_t_m_roof2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof2[0]["Area"] * (1/(R_roof_all2_new + R_roof_all2+0.17))* 24/(EBF*1000)
Q_m_roof2_new=Q_t_m_roof2_new.sum(axis=0)  
for i in range(60):
    Q_t_y_roof2_new.append(Q_m_roof2_new)

#roof3 new
Roof3=[]
for i in roof_ren: 
    if i[0] == round(New_components_roof[2]["Type"]): 
        if round(New_components_roof[2]["Type"])==0:
            R_roof3=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R3_r_ins = New_components_roof[2]["Insulation thickness"]/((1+Uncertainty_conductivity_roof[2])*i[4])
            Roof3.append(R3_r_ins)    
        else:                  
            R_roof3= i[3]/((1+Uncertainty_conductivity_roof[2])*i[4])
            Roof3.append(R_roof3)
R_roof_all3_new=sum(Roof3)
Q_t_m_roof3_new=np.zeros((num_components,12))
Q_t_y_roof3_new=[]
for k in range(12):
    if round(New_components_roof[2]["Type"])==0:
        Q_t_m_roof3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof3[0]["Area"] * (1/(R_roof_all3+0.17))* 24/(EBF*1000)
    elif R_roof_all3==0 and R_roof_all3_new==0:
        Q_t_m_roof3_new[j][k]=0
    else:
        Q_t_m_roof3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*roof3[0]["Area"] * (1/(R_roof_all3_new+R_roof_all3+0.17))* 24/(EBF*1000)
Q_m_roof3_new=Q_t_m_roof3_new.sum(axis=0)  
for i in range(60):
    Q_t_y_roof3_new.append(Q_m_roof3_new)

Q_t_roof_new=[]
for a,b,c in zip(Q_t_y_roof1_new, Q_t_y_roof2_new, Q_t_y_roof3_new):
    Q_t_roof_new.append(a+b+c)


Uncertainty_conductivity_slab=[]
for i in New_components_floor:
    Uncertainty_conductivity_slab.append(i["Uncertainty conductivity"])
#floor1 new
Floor1 = []
for i in floor_ren:
    if i[0]==round(New_components_floor[0]["Type"]):
        if round(New_components_floor[0]["Type"])==0:
            R_floor1_new=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R1_f_ins = New_components_floor[0]["Insulation thickness"]/(i[4]*(1+Uncertainty_conductivity_slab[0]))
            Floor1.append(R1_f_ins)    
        else:                          
            R_floor1_new = i[3]/(i[4]*(1+Uncertainty_conductivity_slab[0]))
            Floor1.append(R_floor1_new)
R_floor1_all_new = sum(Floor1)
Q_t_m_floor1_new=np.zeros((num_components,12))
Q_t_y_floor1_new=[]
for k in range(12):
    if round(New_components_floor[0]["Type"]) ==0:
        Q_t_m_floor1_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_exterior[0]["Area"] * (1/(R_floor_ag_ext_all+0.17))* 24/(EBF*1000)
    elif R_floor_ag_ext_all ==0 and R_floor1_all_new ==0:
        Q_t_m_floor1_new[j][k]=0
    else:
        Q_t_m_floor1_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_exterior[0]["Area"] * (1/(R_floor1_all_new+R_floor_ag_ext_all+0.17))* 24/(EBF*1000)
Q_m_floor1_new=Q_t_m_floor1_new.sum(axis=0)  
for i in range(60):
    Q_t_y_floor1_new.append(Q_m_floor1_new)

#floor2 new
Floor2 = []
for i in floor_ren:
    if i[0]==round(New_components_floor[1]["Type"]):
        if round(New_components_floor[1]["Type"])==0:
            R_floor2_new=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R2_f_ins = New_components_floor[1]["Insulation thickness"]/(i[4]*(1+Uncertainty_conductivity_slab[1]))
            Floor2.append(R2_f_ins)    
        else:                                  
            R_floor2_new = i[3]/(i[4]*(1+Uncertainty_conductivity_slab[1]))
            Floor2.append(R_floor2_new)
R_floor2_all_new = sum(Floor2)
Q_t_m_floor2_new=np.zeros((num_components,12))
Q_t_y_floor2_new=[]
for k in range(12):
    if round(New_components_floor[1]["Type"]) ==0:
        Q_t_m_floor2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_exterior[0]["Area"] * (1/(R_floor_ag_shelt_all+0.17))* 24/(EBF*1000)
    elif R_floor_ag_shelt_all ==0 and R_floor2_all_new ==0:
        Q_t_m_floor2_new[j][k]=0
    else:
        Q_t_m_floor2_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor_against_exterior[0]["Area"] * (1/(R_floor2_all_new+R_floor_ag_shelt_all+0.17))* 24/(EBF*1000)
Q_m_floor2_new=Q_t_m_floor2_new.sum(axis = 0)
for i in range(60):
    Q_t_y_floor2_new.append(Q_m_floor2_new)

# floor3
Floor3=[]
for i in floor_ren:
    if i[0]==round(New_components_floor[2]["Type"]):
        if round(New_components_floor[2]["Type"])==0:
            R_floor3_new=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R3_f_ins = New_components_floor[2]["Insulation thickness"]/(i[4]*(1+Uncertainty_conductivity_slab[2]))
            Floor3.append(R3_f_ins)    
        else:                                  
            R_floor3_new = i[3]/(i[4]*(1+Uncertainty_conductivity_slab[2]))
            Floor3.append(R_floor3_new)
R_floor3_all_new = sum(Floor3)
Q_t_m_floor3_new=np.zeros((num_components,12))
Q_t_y_floor3_new=[]
for k in range(12):
    if round(New_components_floor[2]["Type"]) ==0:
        Q_t_m_floor3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_floor_against_tech[0]["Area"] * (1/(R_floor_ag_tech_all+0.17))* 24/(EBF*1000)
    elif R_floor_ag_tech_all ==0 and R_floor3_all_new ==0:
        Q_t_m_floor3_new[j][k]=0
    else:
        Q_t_m_floor3_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*comp_out_floor_against_tech[0]["Area"] * (1/(R_floor_ag_tech_all+R_floor3_all_new+0.17))* 24/(EBF*1000)
Q_m_floor3=Q_t_m_floor3_new.sum(axis=0)  
for i in range(60):
    Q_t_y_floor3_new.append(Q_m_floor3)

#floor4 new
Floor4=[]
for i in floor_ren:
    if i[0]==round(New_components_floor[3]["Type"]):
        if round(New_components_floor[3]["Type"])==0:
            R_floor4_new=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R4_f_ins = New_components_floor[3]["Insulation thickness"]/(i[4]*(1+Uncertainty_conductivity_slab[3]))
            Floor4.append(R4_f_ins)    
        else:                                  
            R_floor4_new = i[3]/(i[4]*(1+Uncertainty_conductivity_slab[3]))
            Floor4.append(R_floor4_new)
R_floor4_all_new = sum(Floor4)
Q_t_m_floor4_new=np.zeros((num_components,12))
Q_t_y_floor4_new=[]
for k in range(12):
    if round(New_components_floor[3]["Type"]) ==0:
        Q_t_m_floor4_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor4[0]["Area"] * (1/(0.17+R_floor4_all))* 24/(EBF*1000)
    elif R_floor4_all ==0 and R_floor4_all_new ==0:
        Q_t_m_floor4_new[j][k]=0
    else:
        Q_t_m_floor4_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor4[0]["Area"] * (1/(R_floor4_all_new+R_floor4_all+0.17))* 24/(EBF*1000)
Q_m_floor4_new=Q_t_m_floor4_new.sum(axis=0)  
for i in range(60):
    Q_t_y_floor4_new.append(Q_m_floor4_new)

#floor5 new
Floor5=[]
for i in floor_ren:
    if i[0]==round(New_components_floor[4]["Type"]):
        if round(New_components_floor[4]["Type"])==0:
            R_floor5_new=0
        if math.isnan(i[3]) or math.isnan(i[4]):
            continue
        if i[2]=="Insulation" or i[2]=="insulation":
            R5_f_ins = New_components_floor[4]["Insulation thickness"]/(i[4]*(1+Uncertainty_conductivity_slab[4]))
            Floor5.append(R5_f_ins)    
        else:                                  
            R_floor5_new = i[3]/(i[4]*(1+Uncertainty_conductivity_slab[4]))
            Floor5.append(R_floor5_new)
R_floor5_all_new = sum(Floor5)
Q_t_m_floor5_new=np.zeros((num_components,12))
Q_t_y_floor5_new=[]
for k in range(12):
    if round(New_components_floor[4]["Type"]) ==0:
        Q_t_m_floor5_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor5[0]["Area"] * (1/(0.17+R_floor5_all))* 24/(EBF*1000)
    elif R_floor5_all ==0 and R_floor5_all_new ==0:
        Q_t_m_floor5_new[j][k]=0
    else:
        Q_t_m_floor5_new[j][k]=((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/4)-mean_temp[k])*days[k]*floor5[0]["Area"] * (1/(R_floor5_all_new+R_floor5_all+0.17))* 24/(EBF*1000)
Q_m_floor5_new=Q_t_m_floor5_new.sum(axis=0)  
for i in range(60):
    Q_t_y_floor5_new.append(Q_m_floor5_new)

Q_t_ext_floor_new=[]
for a,b,c,d,e in zip(Q_t_y_floor1_new, Q_t_y_floor2_new, Q_t_y_floor3_new, Q_t_y_floor4_new, Q_t_y_floor5_new):
    Q_t_ext_floor_new.append(a+b+c+d+e)

#Windows vertical new
i=0
Q_t_wind_vert_year_new=[]
Q_t_wind_vert_year1_new=[]
U_windows = []

Uncertainty_Uvalue=[]
for i in windows_out_vertical:
    Uncertainty_Uvalue.append(i["Uncertainty_U-value"])
for i in windows_ren:
    if windows_out_vertical[0]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[0]["type"] == 0:
    U_windows.append(windows_out_vertical[0]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[1]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[1]["type"] == 0:
    U_windows.append(windows_out_vertical[1]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[2]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[2]["type"] == 0:
    U_windows.append(windows_out_vertical[2]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[3]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[3]["type"] == 0:
    U_windows.append(windows_out_vertical[3]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[4]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[4]["type"] == 0:
    U_windows.append(windows_out_vertical[4]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[5]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[5]["type"] == 0:
    U_windows.append(windows_out_vertical[5]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[6]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[6]["type"] == 0:
    U_windows.append(windows_out_vertical[6]["UValue_wind"])

for i in windows_ren:
    if windows_out_vertical[7]["type"] == i[0]:
        U_windows.append(i[3])
if windows_out_vertical[7]["type"] == 0:
    U_windows.append(windows_out_vertical[7]["UValue_wind"])        

Q_t_monthly_wind_vert1_new=np.zeros((num_components,12))
for i, n, x in zip(range(len(windows_out_vertical)), U_windows, Uncertainty_Uvalue):
    for k in range(12):
        Q_t_monthly_wind_vert1_new[i][k]=(((room_temperature+room_regulation-1)+((Inner_temp-room_temperature)/2)-mean_temp[k])*days[k]*windows_out_vertical[i]["Area_wind"]*n*(1+x)*24)/(EBF*1000)   
Q_t_wind_vert_year_new=Q_t_monthly_wind_vert1_new.sum(axis=0)

performance_loss_wind_vert_new = []
for i in range(60):
    Q_t_wind_vert_year1_new.append(Q_t_wind_vert_year_new)

"""
def windows_vert_calc_new(perf_loss_wind_vert_new):
    i=0 
    Q_t_wind_vert = []
    for year in range(windows_emb_RSL_new):
        for month in range(12):
            perf_loss_wind_vert_new += 0.0
            performance_loss_wind_vert_new.append(perf_loss_wind_vert_new)
    for x in range(windows_emb_RSL_new):
        Q_t_wind_vert.append(Q_t_each_month_wind_vert)
    for x, y in zip(Q_t_wind_vert, performance_loss_wind_vert_new):
        Q_t_wind_vert_year_new.append(x * y)    
for i in range(counter_windows_new):
    windows_vert_calc_new(perf_loss_wind_vert_new)
for i in Q_t_wind_vert_year_new[0:60]:
    Q_t_wind_vert_year1_new.append(i)
"""
Q_t_perf_loss_new = []
for a, b, c, d, e, f, g, h in zip(Q_t_roof_new, Q_t_wind_vert_year1_new, Q_t_wind_hor_year1, Q_t_ext_floor_new, Q_t_ext_walls_new, Q_t_comp_in_floor_new, Q_t_comp_in_year_new, Q_t_y_comp_in_ceiling_new):
    Q_t_perf_loss_new.append(a+ b+ c+ d+ e+ f+ g+ h)
Q_transm_loss_new=np.concatenate(Q_t_perf_loss_new, axis=0)

#heat transfer coefficients to calculate Htotal
H_transfer_coef_new=0
if R_ext_wall_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+comp_out_walls[0]["Area"]*(1/R_ext_wall_new)
if R_ext_wall_ag_tech_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_walls_against_tech[0]["Area"]*(1/R_ext_wall_ag_tech_new)
if R_ext_wall_shops_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_walls_shops_tech[0]["Area"]*(1/R_ext_wall_shops_new)
if R_wall_ag_shelt_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+wall_against_shelter[0]["Area"]*(1/R_wall_ag_shelt_new)

if R_ext_wall5_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_wall5[0]["Area"]*(1/R_ext_wall5_new)
if R_ext_wall6_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_wall6[0]["Area"]*(1/R_ext_wall6_new)
if R_ext_wall7_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_wall7[0]["Area"]*(1/R_ext_wall7_new)
if R_ext_wall8_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+ext_wall8[0]["Area"]*(1/R_ext_wall8_new)    
if R_roof_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+comp_out_roof[0]["Area"]*(1/R_roof_all_new)    
if R_roof_all2_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+roof2[0]["Area"]*(1/R_roof_all2_new)    
if R_roof_all3_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+roof3[0]["Area"]*(1/R_roof_all3_new)  
if R_ceil1_unheated_all==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+components_in_ceiling[0]["Area_in"]*(1/R_ceil1_unheated_all)  
if R_wall1_unheated_all==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+components_in_wall[0]["Area_in"]*(1/R_wall1_unheated_all) 
if R_slab1_unheated_all==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+components_in_floor[0]["Area_in"]*(1/R_slab1_unheated_all) 
if R_slab2_unheated_all==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+components_in_floor2[0]["Area_in"]*(1/R_slab2_unheated_all) 
if R_slab3_unheated_all==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+components_in_floor3[0]["Area_in"]*(1/R_slab3_unheated_all) 
if R_floor1_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+floor_against_exterior[0]["Area"]*(1/R_floor1_all_new) 
if R_floor2_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+floor_against_shelter[0]["Area"]*(1/R_floor2_all_new) 
if R_floor3_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+comp_out_floor_against_tech[0]["Area"]*(1/R_floor3_all_new) 
if R_floor4_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
else:
    H_transfer_coef_new=H_transfer_coef_new+floor4[0]["Area"]*(1/R_floor4_all_new) 
if R_floor5_all_new==0:
    H_transfer_coef_new=H_transfer_coef_new+0
for i in range(len(windows_out_vertical)):
    H_transfer_coef_new=H_transfer_coef_new + windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["UValue_wind_new"]
for i in range(len(windows_out_horizontal)):
    H_transfer_coef_new=H_transfer_coef_new+windows_out_horizontal[i]["Area_wind_h"]+windows_out_horizontal[i]["U-Value_wind_h_new"]


#new ventilation loss
check=0
Air_flow_new=Air_flow_therm_eff
while check==0:
    if vent_type<1 or vent_type>2:
        vent_type=int(input("Enter a ventilation type (Natural - 1, Mechanical - 2): "))
    else:
        check=1

#natural ventilation
Qvent_nat_new=np.zeros(12)
if vent_type_new ==1:
    heat_storage_capacity=(1220-(0.14*sea_height))/3600
    for i in range(12):
        Qvent_nat_new[i]=((room_temperature+room_regulation-1)-mean_temp[i])*Air_flow_therm_eff*days[i]*heat_storage_capacity*24/1000
        if Qvent_nat_new[i]<0:
            Qvent_nat_new[i]=0
Qvent_nat_new_year=[]
for i in range(60):
    Qvent_nat_new_year.append(Qvent_nat_new)
Q_vent_loss_new_nat=np.concatenate(Qvent_nat_new_year, axis=0)

#comfort mechanical ventilation
if vent_type_new==2:
    Air_flow_new=Air_flow_therm_eff_new
    H_vent_new=Air_flow_new*heat_storage_capacity*EBF
    design_temp=climate[city][76]
    Htotal_new=H_vent_new+H_transfer_coef_new
    Ph=(Htotal_new*(room_temperature-design_temp)/EBF)-heat_input_std_usage
    if design_temp<8:
        Ph_corrected=Phli*(room_temperature-design_temp)/(room_temperature-(-8))
    else:
        Ph_corrected=Phli

check=0
while check==0:
    if preheat_air<0 or preheat_air>2:
        print("Enter 1 or 2")
    else:
        check=1

Oper_hours_step1=84
Oper_hours_step2=70
Oper_hours_step3=14

Basic_air_exchange_rate=0.15
if preheat_air_new==1:
    thermal_eff_airrate_step1_new=(1-heat_rec_eff_new)*(room_number*20/EBF)*heat_rec_eff_new+Basic_air_exchange_rate
    thermal_eff_airrate_step2_new=(1-heat_rec_eff_new)*(room_number*30/EBF)*heat_rec_eff_new+Basic_air_exchange_rate
    thermal_eff_airrate_step3_new=(1-heat_rec_eff_new)*(room_number*45/EBF)*heat_rec_eff_new+Basic_air_exchange_rate
else:
    thermal_eff_airrate_step1_new=(1-heat_rec_eff_new)*(room_number*20/EBF)+Basic_air_exchange_rate
    thermal_eff_airrate_step2_new=(1-heat_rec_eff_new)*(room_number*30/EBF)+Basic_air_exchange_rate
    thermal_eff_airrate_step3_new=(1-heat_rec_eff_new)*(room_number*45/EBF)+Basic_air_exchange_rate

thermal_eff_outer_volume_new=(Oper_hours_step1*thermal_eff_airrate_step1_new+Oper_hours_step2*thermal_eff_airrate_step2_new+Oper_hours_step3*thermal_eff_airrate_step3_new)/(Oper_hours_step1+Oper_hours_step2+Oper_hours_step3)
Qvent_with_heatrec_new=np.zeros(12)
if heat_rec_new==1:
    for i in range(12):
        Qvent_with_heatrec_new[i]=(room_temperature+room_regulation-1-mean_temp[i])*thermal_eff_outer_volume_new*days[i]*EBF*heat_storage_capacity*24/(EBF*1000)
        if Qvent_with_heatrec_new[i]<0:
            Qvent_with_heatrec_new[i]=0
Q_vent_loss_new_mech = []
for i in range(60):
    Q_vent_loss_new_mech.append(Qvent_with_heatrec_new)
Q_vent_loss_new_mech_year=np.concatenate(Q_vent_loss_new_mech, axis=0)


if heat_rec_new==1:
    difference=0
else:
    difference=Qvent_nat_new-Qvent_with_heatrec_new

Qvent_without_heat_rec_new1 = []
for x in range(60):
    for y in Qvent_nat_new:
        Qvent_without_heat_rec_new1.append(y)


#new solar gains
windows=len(windows_out_vertical)+len(windows_out_horizontal)
Qisol_month_new=np.zeros((windows,12))
for i in range(len(windows_out_vertical)):
    orientation=windows_out_vertical[i]["Orientation"]
    index_h=horizon[0].index(orientation)
    index_o=overhang[0].index(orientation)
    index_s=sideblind[0].index(orientation)
    hor=windows_out_vertical[i]["hor"]
    over=windows_out_vertical[i]["over"]
    side1=windows_out_vertical[i]["side1"]
    side2=windows_out_vertical[i]["side2"]

    #fs1 - factor for horizon
    #fs2 - factor for overhang
    #fs3,1 - sideblinds
    #fs3,2 - sideblinds

    if hor==0:
        fs1=1
    elif hor<1:
        fs1=hor
    else:
        fs1=horizon[hor+1][index_h]  #plus 1?

    fs2=overhang[over+1][index_o]
    fs3_1=sideblind[side1+1][index_s]

    if orientation=="SW" or orientation=="SE" or orientation=="S" or orientation=="SSW" or orientation=="SSE":
        fs3_2=sideblind[side2+1][index_s]
    else:
        fs3_2=1
    irradiance_orient=[("H","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N","NNE","NE","ENE","E","ESE")]
    index_ir=irradiance_orient[0].index(orientation)

    for j in range(12):
        Qisol_month_new[i][j]=(irradiance[index_ir][j])*windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["gvalue_wind_new"]*windows_out_vertical[i]["glass_perc_new"]*0.9*windows_out_vertical[i]["coef1"]*windows_out_vertical[i]["coef2"]*windows_out_vertical[i]["coef3"]*windows_out_vertical[i]["coef4"]/EBF
        k=i+1

for n in range(len(windows_out_horizontal)):
    horS=windows_out_horizontal[n]["HorizonS"]
    horW=windows_out_horizontal[n]["HorizonW"]
    horO=windows_out_horizontal[n]["HorizonO"]
    horN=windows_out_horizontal[n]["HorizonN"]
    fs1=horizon[horS+1] [4]
    fs2=horizon[horW+1] [7]
    fs3_1=horizon[horO+1][8]
    fs3_2=horizon[horN+1][13]
    for j in range(12):
        m=k+n
        Qisol_month_new[m][j]=(irradiance[0][j])*windows_out_horizontal[n]["Area_wind_h"]*windows_out_horizontal[n]["glass_perc_h_new"]*windows_out_horizontal[n]["g-value_wind_h_new"]*0.9*fs1*fs2*fs3_1*fs3_2/EBF

Qisol_m_new=Qisol_month_new.sum(axis=0)

Qisol_new=[]
for x in range(60):
    for y in Qisol_m_new:
        Qisol_new.append(y)

#transmission losses renovation
Qtr_losses_new=np.zeros(720)
#total losses renovation
Qtotal_losses_new=np.zeros(720)
Qvent_with_heatrec_new=np.zeros(720)
#heat gains renovation
Qheat_gains_new=np.zeros(720)
#heat gains/losses coefficient
Qcoef_new=np.zeros(720)
#time constant
Time_constant_new=np.zeros(720)
#Heat loss coefficient
Heat_loss_coef_new=np.zeros(720)
#utilization factor
Utiliz_factor_new=np.zeros(720)
#Util_degree_for heat gains
Utiliz_degree_case1_new=np.zeros(720)
Utiliz_degree_case2_new=np.zeros(720)
Utiliz_degree_decision_new=np.zeros(720)
#Utilized heat gains
Utilized_heatgain_new=np.zeros(720)
#Heating demand renovation
Heating_demand_new=np.zeros(720)
Qtotal_losses_new1=np.zeros(720)
#heat transfer coefficient
H_comp_new=0.0 # heat transfer coeff. for components

if R_ext_wall_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+comp_out_walls[0]["Area"]*(1/R_ext_wall_new)
if R_ext_wall_ag_tech_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_walls_against_tech[0]["Area"]*(1/R_ext_wall_ag_tech_new)
if R_ext_wall_shops_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_walls_shops_tech[0]["Area"]*(1/R_ext_wall_shops_new)
if R_wall_ag_shelt_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+wall_against_shelter[0]["Area"]*(1/R_wall_ag_shelt_new)
if R_ext_wall5_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_wall5[0]["Area"]*(1/R_ext_wall5_new)
if R_ext_wall6_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_wall6[0]["Area"]*(1/R_ext_wall6_new)
if R_ext_wall7_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_wall7[0]["Area"]*(1/R_ext_wall7_new)
if R_ext_wall8_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+ext_wall8[0]["Area"]*(1/R_ext_wall8_new)    
if R_roof_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+comp_out_roof[0]["Area"]*(1/R_roof_all_new)    
if R_roof_all2_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+roof2[0]["Area"]*(1/R_roof_all2_new)    
if R_roof_all3_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+roof3[0]["Area"]*(1/R_roof_all3_new)  
if R_ceil1_unheated_all==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+components_in_ceiling[0]["Area_in"]*(1/R_ceil1_unheated_all)  
if R_comp_in_wall_all==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+components_in_wall[0]["Area_in"]*(1/R_comp_in_wall_all) 
if R_slab1_unheated_all==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+components_in_floor[0]["Area_in"]*(1/R_slab1_unheated_all) 
if R_slab2_unheated_all==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+components_in_floor2[0]["Area_in"]*(1/R_slab2_unheated_all) 
if R_slab3_unheated_all==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+components_in_floor3[0]["Area_in"]*(1/R_slab3_unheated_all) 
if R_floor1_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+floor_against_exterior[0]["Area"]*(1/R_floor1_all_new) 
if R_floor2_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+floor_against_shelter[0]["Area"]*(1/R_floor2_all_new) 
if R_floor3_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+comp_out_floor_against_tech[0]["Area"]*(1/R_floor3_all_new) 
if R_floor4_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+floor4[0]["Area"]*(1/R_floor4_all_new) 
if R_floor5_all_new==0:
    H_comp_new=H_comp_new+0
else:
    H_comp_new=H_comp_new+floor5[0]["Area"]*(1/R_floor5_all_new) 
for i in range(len(windows_out_vertical)):
    H_comp_new=H_comp_new+windows_out_vertical[i]["Area_wind"]*windows_out_vertical[i]["UValue_wind_new"]    
for i in range(len(windows_out_horizontal)):
    H_comp_new=H_comp_new+windows_out_horizontal[i]["Area_wind_h"]*windows_out_horizontal[i]["U-Value_wind_h_new"]


for i in range(720):
    Qtr_losses_new[i]=Q_transm_loss_new[i]+Q_transm_loss_new[i]*thermal_bridge_new

    #total losses

    if vent_type_new == 1:
        Qtotal_losses_new1[i]=Qtr_losses_new[i] +Q_vent_loss_new_nat[i]
    else:
        if heat_rec_new==1:
            Qtotal_losses_new1[i]=Qtr_losses_new[i] +Q_vent_loss_new_mech_year[i]
        else:
            Qtotal_losses_new1[i]=Qtr_losses_new[i]+Qvent_without_heat_rec_new1[i]

    #heat gains
    Qheat_gains_new[i]=Qiel1[i]+Qiocc1[i]+Qisol_new[i]
    #Heat gains to loss ratio
    Qcoef_new[i]=Qheat_gains_new[i]/Qtotal_losses_new1[i]
    #time constant
    Time_constant_new[i]=constr_factor*EBF*1000/(H_comp_new+Air_flow_therm_eff_new*EBF*heat_storage_capacity)
    #Heat loss coefficient
    Heat_loss_coef_new[i]=(H_transfer_coef_new+Air_flow_therm_eff_new*heat_storage_capacity*EBF/3600)*(1+thermal_bridge_new)
    #Utilization factor
    Utiliz_factor_new[i]=Util_parameter+Time_constant_new[i]/Reference_time_constant   
    #Utiliz_factor
    if Qtotal_losses_new1[i]<0:
        Utiliz_degree_case1_new[i]=0
    else:
        Utiliz_degree_case1_new[i]=1
    
    if Qcoef_new[i]==1:
        Utiliz_degree_case2_new[i]=Util_parameter/(Util_parameter+1)
    else:
        Utiliz_degree_case2_new[i]=(1-(Qcoef_new[i]**Utiliz_factor_new[i]))/(1-(Qcoef_new[i]**(Utiliz_factor_new[i]+1)))
    
    if Utiliz_degree_case1_new[i]==0:
        Utiliz_degree_decision_new[i]==0
    else:
        Utiliz_degree_decision_new[i]=Utiliz_degree_case2_new[i]
    #Utilized heat gains
    Utilized_heatgain_new[i]=Qheat_gains_new[i]*Utiliz_degree_decision_new[i]
    #Heating demand
    Heating_demand_new[i]=(Qtotal_losses_new1[i]-Utilized_heatgain_new[i])

Heating_demand_annual_new=[]
p=np.array_split(Heating_demand_new,60)  # k -> np.array
#Heating_demand_annual.append(k)      # Heating_demand_annual -> [ np.array ]
Heating_demand_annual_new = p


#print(Heating_demand_annual)
Qhd_new=[ sum(elem) for elem in Heating_demand_annual_new ]

Qheating_demand_new=[]
for i in Qhd_new:
    Q_final_new=i*(1+final_energy_losses_new)
    Qheating_demand_new.append(Q_final_new)


#LCA renovation

#exterior walls
Area_walls=[]
Area_walls.append(comp_out_walls[0]["Area"])
Area_walls.append(ext_walls_against_tech[0]["Area"])
Area_walls.append(ext_walls_shops_tech[0]["Area"])
Area_walls.append(wall_against_shelter[0]["Area"])
Area_walls.append(ext_wall5[0]["Area"])
Area_walls.append(ext_wall6[0]["Area"])
Area_walls.append(ext_wall7[0]["Area"])
Area_walls.append(ext_wall8[0]["Area"])

#exterior walls
Types=[]
Insulation_thickness_ext_walls=[]
RSL_ext_walls = []
Uncertainty_GWP=[]
Uncertainty_cost = []
for i in New_components:
    Types.append(round(i["Type"]))
    Insulation_thickness_ext_walls.append(i["Insulation thickness"])
    RSL_ext_walls.append(i["RSL"])
    Uncertainty_GWP.append(i["Uncertainty_GWP"])
    Uncertainty_cost.append(i["Uncertainty_cost"])
exterior_wall_emb=[]
repl_ext_wall = []
initial_cost_ext_walls=[]
for j, k, l, n, p, h in zip(Types, Insulation_thickness_ext_walls, RSL_ext_walls, Area_walls, Uncertainty_GWP, Uncertainty_cost):
    temp=[]
    for i in exterior_wall_ren:
        if i[0] == j:            
            if i[2] == "Insulation" or i[2] =="insulation":
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue
                emb_ext_wall_ins = n*(k*(i[9]+i[12])*(1+p)/i[3])
                repl_number_ins = math.ceil((timeperiod/l)-1)
                exterior_wall_emb.append(emb_ext_wall_ins)
                repl_ext_wall.append(repl_number_ins*emb_ext_wall_ins)
                ext_wall_initial_cost_ins = n*(k*(i[23]+i[26])*(1+h)/i[3])
                temp.append(ext_wall_initial_cost_ins)                
            else:
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue                
                emb_ext_wall = n*(i[9]+i[12])*(1+p)
                repl_number = math.ceil((timeperiod/l)-1)               
                exterior_wall_emb.append(emb_ext_wall)
                repl_ext_wall.append(repl_number*emb_ext_wall)
                ext_wall_initial_cost = n*(i[23]+i[26])*(1+h)
                temp.append(ext_wall_initial_cost)               
    initial_cost_ext_walls.append(temp)



#replacement LCC ext wall

RSLEW1=[]
RSLEW2=[]
RSLEW3=[]
RSLEW4=[]
RSLEW5=[]
RSLEW6=[]
RSLEW7=[]
RSLEW8=[]

for x in frange(round(New_components[0]["RSL"]),timeperiod,round(New_components[0]["RSL"])):
    RSLEW1.append(x)
for x in frange(round(New_components[1]["RSL"]),timeperiod,round(New_components[1]["RSL"])):
    RSLEW2.append(x)
for x in frange(round(New_components[2]["RSL"]),timeperiod,round(New_components[2]["RSL"])):
    RSLEW3.append(x)
for x in frange(round(New_components[3]["RSL"]),timeperiod,round(New_components[3]["RSL"])):
    RSLEW4.append(x)
for x in frange(round(New_components[4]["RSL"]),timeperiod,round(New_components[4]["RSL"])):
    RSLEW5.append(x)
for x in frange(round(New_components[5]["RSL"]),timeperiod,round(New_components[5]["RSL"])):
    RSLEW6.append(x)
for x in frange(round(New_components[6]["RSL"]),timeperiod,round(New_components[6]["RSL"])):
    RSLEW7.append(x)
for x in frange(round(New_components[7]["RSL"]),timeperiod,round(New_components[7]["RSL"])):
    RSLEW8.append(x)

replacement_ext_walls=[]
for k in RSLEW1:
    repl_cost_ext_wall=round((sum(initial_cost_ext_walls[0])*((1+inflation_rate)**k)/((1+interest_rate)**k)),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW2:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[1])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW3:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[2])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW4:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[3])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW5:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[4])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW6:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[5])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW7:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[6])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)
for k in RSLEW8:
    repl_cost_ext_wall=round(sum(initial_cost_ext_walls[7])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_ext_walls.append(repl_cost_ext_wall)



# interior walls
int_wall_types=[]
for i in range(len(int_wall_finish)):
    int_wall_type=int_wall_finish[i]["int_wall_finish_type"]
    int_wall_types.append(int_wall_type)

int_wall_repl_numbers=[]
for i in range(len(int_wall_types)):
    if int_wall_finish[i]["int_wall_finish_RSL"]==0:
        repl_number=0
    else:
        repl_number=math.ceil((timeperiod/(int_wall_finish[i]["int_wall_finish_RSL"]))-1)
    int_wall_repl_numbers.append(repl_number)
indicator=1
emb_int_walls=[]
for k,i in zip(int_wall_types, Area_walls):
    if indicator==1:
        emb_int_wall= round(((int_wall_finish[k-1]["int_wall_finish_Pr_GWP"]+int_wall_finish[k-1]["int_wall_finish_EoL_GWP"])*i),1)
        units="kg CO2eq."
    if indicator==2:
        emb_int_wall= round(((int_wall_finish[k-1]["int_wall_finish_Pr_PE"]+int_wall_finish[k-1]["int_wall_finish_EoL_PE"])*i),1)
        units = "kWh oil-eq."
    if indicator==3:
        emb_int_wall= round(((int_wall_finish[k-1]["int_wall_finish_Pr_UBP"]+int_wall_finish[k-1]["int_wall_finish_EoL_UBP"])*i),1)
        units = "UBP points"
    emb_int_walls.append(emb_int_wall)

#Interior walls
initial_int_walls=[]
for k,i in zip(int_wall_types, Area_walls):
    initial_int_w=int_wall_finish[k-1]["int_wall_finish_cost"]*i
    initial_int_walls.append(initial_int_w)
#lcc replacement int wall
RSLIW1=[]
RSLIW2=[]
RSLIW3=[]
RSLIW4=[]
RSLIW5=[]
RSLIW6=[]
RSLIW7=[]
RSLIW8=[]
if int_wall_finish[0]["int_wall_finish_RSL"]==0: RSLIW1.append(0) 
else: 
    for x in frange(int_wall_finish[0]["int_wall_finish_RSL"],timeperiod,int_wall_finish[0]["int_wall_finish_RSL"]):
        RSLIW1.append(x)
if int_wall_finish[1]["int_wall_finish_RSL"]==0: RSLIW2.append(0) 
else: 
    for x in frange(int_wall_finish[1]["int_wall_finish_RSL"],timeperiod,int_wall_finish[1]["int_wall_finish_RSL"]):
        RSLIW2.append(x)
if int_wall_finish[2]["int_wall_finish_RSL"]==0: RSLIW3.append(0) 
else: 
    for x in frange(int_wall_finish[2]["int_wall_finish_RSL"],timeperiod,int_wall_finish[2]["int_wall_finish_RSL"]):
        RSLIW3.append(x)
if int_wall_finish[3]["int_wall_finish_RSL"]==0: RSLIW4.append(0) 
else: 
    for x in frange(int_wall_finish[3]["int_wall_finish_RSL"],timeperiod,int_wall_finish[3]["int_wall_finish_RSL"]):
        RSLIW4.append(x)
if int_wall_finish[4]["int_wall_finish_RSL"]==0: RSLIW5.append(0) 
else: 
    for x in frange(int_wall_finish[4]["int_wall_finish_RSL"],timeperiod,int_wall_finish[4]["int_wall_finish_RSL"]):
        RSLIW5.append(x)
if int_wall_finish[5]["int_wall_finish_RSL"]==0: RSLIW6.append(0) 
else: 
    for x in frange(int_wall_finish[5]["int_wall_finish_RSL"],timeperiod,int_wall_finish[5]["int_wall_finish_RSL"]):
        RSLIW6.append(x)
if int_wall_finish[6]["int_wall_finish_RSL"]==0: RSLIW7.append(0) 
else: 
    for x in frange(int_wall_finish[6]["int_wall_finish_RSL"],timeperiod,int_wall_finish[6]["int_wall_finish_RSL"]):
        RSLIW7.append(x)
if int_wall_finish[7]["int_wall_finish_RSL"]==0: RSLIW8.append(0) 
else: 
    for x in frange(int_wall_finish[7]["int_wall_finish_RSL"],timeperiod,int_wall_finish[7]["int_wall_finish_RSL"]):
        RSLIW8.append(x)
replacement_int_walls=[]
for k in RSLIW1:
    repl_cost_int_wall=round(initial_int_walls[0]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW2:
    repl_cost_int_wall=round(initial_int_walls[1]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW3:
    repl_cost_int_wall=round(initial_int_walls[2]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW4:
    repl_cost_int_wall=round(initial_int_walls[3]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW5:
    repl_cost_int_wall=round(initial_int_walls[4]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW6:
    repl_cost_int_wall=round(initial_int_walls[5]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW7:
    repl_cost_int_wall=round(initial_int_walls[6]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)
for k in RSLIW8:
    repl_cost_int_wall=round(initial_int_walls[7]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_int_walls.append(repl_cost_int_wall)

#lca replacement int wall
wall_int_replacement=[]
for k,i in zip(emb_int_walls,int_wall_repl_numbers):
    wall_int_repl=k*i
    wall_int_replacement.append(wall_int_repl)

#roof
Area_roofs=[]
Area_roofs.append(comp_out_roof[0]["Area"])
Area_roofs.append(roof2[0]["Area"])
Area_roofs.append(roof3[0]["Area"])
Types_roof=[]
Insulation_thickness_roof=[]
RSL_roof = []
Uncertainty_GWP_roof = []
Uncertainty_cost_roof=[]
for i in New_components_roof:
    Types_roof.append(round(i["Type"]))
    Insulation_thickness_roof.append(i["Insulation thickness"])
    RSL_roof.append(i["RSL"])
    Uncertainty_GWP_roof.append(i["Uncertainty_GWP"])
    Uncertainty_cost_roof.append(i["Uncertainty_cost"])

roof_emb=[]
repl_roof = []
initial_cost_roof=[]
for j, k, l, n, p, h in zip(Types_roof, Insulation_thickness_roof, RSL_roof, Area_roofs, Uncertainty_GWP_roof, Uncertainty_cost_roof):
    temp=[]
    for i in roof_ren:
        if i[0] == j:            
            if i[2] == "Insulation" or i[2] =="insulation":
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue
                emb_roof_ins = n*(k*(i[9]+i[12])*(1+p)/i[3])
                repl_number_ins = math.ceil((timeperiod/l)-1)
                roof_emb.append(emb_roof_ins)
                repl_roof.append(repl_number_ins*emb_roof_ins)
                roof_initial_cost_ins = n*(k*(i[23]+i[26])*(1+h)/i[3])
                temp.append(roof_initial_cost_ins)
            else:
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue                
                emb_roof = n*(i[9]+i[12])*(1+p)
                repl_number = math.ceil((timeperiod/l)-1)               
                roof_emb.append(emb_roof)
                repl_roof.append(repl_number*emb_roof)
                roof_initial_cost = n*(i[23]+i[26])*(1+h)
                temp.append(roof_initial_cost)
    initial_cost_roof.append(temp)

#replacement LCC roof
RSLR1=[]
RSLR2=[]
RSLR3=[]

for x in frange(round(New_components_roof[0]["RSL"]),timeperiod,round(New_components_roof[0]["RSL"])):
    RSLR1.append(x)
for x in frange(round(New_components_roof[1]["RSL"]),timeperiod,round(New_components_roof[1]["RSL"])):
    RSLR2.append(x)
for x in frange(round(New_components_roof[2]["RSL"]),timeperiod,round(New_components_roof[2]["RSL"])):
    RSLR3.append(x)
replacement_roof_cover=[]
for k in RSLR1:
    repl_cost_roof=round((sum(initial_cost_roof[0])*((1+inflation_rate)**k)/((1+interest_rate)**k)),1)
    replacement_roof_cover.append(repl_cost_roof)
for k in RSLR2:
    repl_cost_roof=round(sum(initial_cost_roof[1])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_roof_cover.append(repl_cost_roof)
for k in RSLR3:
    repl_cost_roof=round(sum(initial_cost_roof[2])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_roof_cover.append(repl_cost_roof)

#roof finish
roof_types=[]
for i in range(len(roof_cover)):
    roof_type=roof_cover[i]["roof_cover_type"]
    roof_types.append(roof_type)

emb_roof_finishes=[]
for k, i in zip(roof_types, Area_roofs):
    if indicator==1:
        emb_roof_finish= round(((roof_finish[k-1]["roof_finish_Pr_GWP"]+roof_finish[k-1]["roof_finish_EoL_GWP"])*i),1)
        units="kg CO2eq."
    if indicator==2:
        emb_roof_finish= round(((roof_finish[k-1]["roof_finish_Pr_PE"]+roof_finish[k-1]["roof_finish_EoL_PE"])*i),1)
        units="KWh oil-eq."
    if indicator==3:
        emb_roof_finish= round(((roof_finish[k-1]["roof_finish_Pr_UBP"]+roof_finish[k-1]["roof_finish_EoL_UBP"])*i),1)
        units="UBP points"
    emb_roof_finishes.append(emb_roof_finish)

initial_roof_finish=[]
for k, i in zip(roof_types, Area_roofs):
    initial_roof_f=roof_finish[k-1]["roof_finish_cost"]*i
    initial_roof_finish.append(initial_roof_f)
#replacement lcc roof finish
RSLRF1=[]
RSLRF2=[]
RSLRF3=[]
for x in frange(New_components_roof[0]["RSL"],timeperiod,New_components_roof[0]["RSL"]):
    RSLRF1.append(x)
for x in frange(New_components_roof[1]["RSL"],timeperiod,New_components_roof[1]["RSL"]):
    RSLRF2.append(x)
for x in frange(New_components_roof[2]["RSL"],timeperiod,New_components_roof[2]["RSL"]):
    RSLRF3.append(x)

replacement_roof_finish=[]
for k in RSLRF1:
    repl_cost_roof_finish=round(initial_roof_finish[0]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_roof_finish.append(repl_cost_roof_finish)
for k in RSLRF2:
    repl_cost_roof_finish=round(initial_roof_finish[1]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_roof_finish.append(repl_cost_roof_finish)
for k in RSLRF3:
    repl_cost_roof_finish=round(initial_roof_finish[2]*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_roof_finish.append(repl_cost_roof_finish)

#lca replacement roof finish
roof_finish_replacement=[]
for i,k in zip(emb_roof_finishes, replacement_roof_finish):
    roof_finish_repl=k*i
    roof_finish_replacement.append(roof_finish_repl)

#Slab
Area_floors=[]
Area_floors.append(comp_out_floor_against_tech[0]["Area"])
Area_floors.append(floor4[0]["Area"])
Area_floors.append(floor5[0]["Area"])
Area_floors.append(floor_against_shelter[0]["Area"])
Area_floors.append(floor_against_exterior[0]["Area"])
Types_floor=[]
Insulation_thickness_floor=[]
RSL_floor = []
Uncertainty_GWP_slabs=[]
Uncertabity_cost_slabs=[]

for i in New_components_floor:
    Types_floor.append(round(i["Type"]))
    Insulation_thickness_floor.append(i["Insulation thickness"])
    RSL_floor.append(i["RSL"])
    Uncertainty_GWP_slabs.append(i["Uncertainty_GWP"])
    Uncertabity_cost_slabs.append(i["Uncertainty_cost"])
floor_emb=[]
repl_floor = []
initial_cost_floor=[]
for j, k, l, n, p, h in zip(Types_floor, Insulation_thickness_floor, RSL_floor, Area_floors, Uncertainty_GWP_slabs, Uncertabity_cost_slabs):
    temp=[]
    for i in floor_ren:
        if i[0] == j:            
            if i[2] == "Insulation" or i[2] =="insulation":
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue
                emb_floor_ins = n*(k*(i[9]+i[12])*(1+p)/i[3])
                repl_number_ins = math.ceil((timeperiod/l)-1)
                floor_emb.append(emb_floor_ins)
                repl_floor.append(repl_number_ins*emb_floor_ins)
                floor_initial_cost_ins = n*(k*(i[23]+i[26])*(1+h)/i[3])
                temp.append(floor_initial_cost_ins)
            else:
                if math.isnan(i[9]) or math.isnan(i[12]):
                    continue                
                emb_floor = n*(i[9]+i[12])*(1+p)
                repl_number = math.ceil((timeperiod/l)-1)               
                floor_emb.append(emb_floor)
                repl_floor.append(repl_number*emb_floor)
                floor_initial_cost = n*(i[23]+i[26])*(1+h)
                temp.append(floor_initial_cost)
    initial_cost_floor.append(temp)

#replacement lcc floor cover
RSLF1=[]
for x in frange(New_components_floor[0]["RSL"],60,New_components_floor[0]["RSL"]):
        RSLF1.append(x)
RSLF2=[]
for x in frange(New_components_floor[1]["RSL"],60,New_components_floor[1]["RSL"]):
    RSLF2.append(x)
RSLF3=[]
for x in frange(New_components_floor[2]["RSL"],60,New_components_floor[2]["RSL"]):
    RSLF3.append(x)
RSLF4=[]
for x in frange(New_components_floor[3]["RSL"],60,New_components_floor[3]["RSL"]):
    RSLF4.append(x)
RSLF5=[]
for x in frange(New_components_floor[4]["RSL"],60,New_components_floor[4]["RSL"]):
    RSLF5.append(x)

replacement_floor=[]
for k in RSLF1:
    repl_cost_floor=round(sum(initial_cost_floor[0])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_floor.append(repl_cost_floor)
for k in RSLF2:
    repl_cost_floor=round(sum(initial_cost_floor[1])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_floor.append(repl_cost_floor)
for k in RSLF3:
    repl_cost_floor=round(sum(initial_cost_floor[2])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_floor.append(repl_cost_floor)
for k in RSLF4:
    repl_cost_floor=round(sum(initial_cost_floor[3])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_floor.append(repl_cost_floor)
for k in RSLF5:
    repl_cost_floor=round(sum(initial_cost_floor[4])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    replacement_floor.append(repl_cost_floor)


#windows
Area_windows=[]
Types_windows=[]
RSL_windows = []
Uncertainty_GWP_windows=[]
Uncertainty_cost_windows=[]
for i in windows_out_vertical:
    Area_windows.append(i["Area_wind"])
    Types_windows.append(round(i["type"]))
    RSL_windows.append(i["RSL"])
    Uncertainty_GWP_windows.append(i["Uncertainty_GWP"])
    Uncertainty_cost_windows.append(i["Uncertainty_cost"])

windows_emb=[]
repl_windows = []
initial_cost_windows=[]

for j, k, l, h, n in zip(Types_windows, RSL_windows, Area_windows, Uncertainty_GWP_windows, Uncertainty_cost_windows):
    temp=[]
    for i in windows_ren:
        if i[0] == j:                           
            emb_windows = l*(i[5]+i[6])*(1+h)
            repl_number = math.ceil((timeperiod/k)-1)               
            windows_emb.append(emb_windows)
            repl_windows.append(repl_number*emb_windows)
            windows_initial_cost = l*(i[11])*(1+n)
            temp.append(windows_initial_cost)
    initial_cost_windows.append(temp)

#replacement lcc windows
RSLW1=[]
RSLW2=[]
RSLW3=[]
RSLW4=[]
RSLW5=[]
RSLW6=[]
RSLW7=[]
RSLW8=[]

for x in frange(windows_out_vertical[0]["RSL"],60,windows_out_vertical[0]["RSL"]):
    RSLW1.append(x)
for x in frange(windows_out_vertical[1]["RSL"],60,windows_out_vertical[1]["RSL"]):
    RSLW2.append(x)
for x in frange(windows_out_vertical[2]["RSL"],60,windows_out_vertical[2]["RSL"]):
    RSLW3.append(x)
for x in frange(windows_out_vertical[3]["RSL"],60,windows_out_vertical[3]["RSL"]):
    RSLW4.append(x)
for x in frange(windows_out_vertical[4]["RSL"],60,windows_out_vertical[4]["RSL"]):
    RSLW5.append(x)
for x in frange(windows_out_vertical[5]["RSL"],60,windows_out_vertical[5]["RSL"]):
    RSLW6.append(x)
for x in frange(windows_out_vertical[6]["RSL"],60,windows_out_vertical[6]["RSL"]):
    RSLW7.append(x)
for x in frange(windows_out_vertical[7]["RSL"],60,windows_out_vertical[7]["RSL"]):
    RSLW8.append(x)

windows_replacement=[]
for k in RSLW1:
    repl_cost_windows=round(sum(initial_cost_windows[0])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW2:
    repl_cost_windows=round(sum(initial_cost_windows[1])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW3:
    repl_cost_windows=round(sum(initial_cost_windows[2])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW4:
    repl_cost_windows=round(sum(initial_cost_windows[3])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW5:
    repl_cost_windows=round(sum(initial_cost_windows[4])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW6:
    repl_cost_windows=round(sum(initial_cost_windows[5])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW7:
    repl_cost_windows=round(sum(initial_cost_windows[6])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)
for k in RSLW8:
    repl_cost_windows=round(sum(initial_cost_windows[7])*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    windows_replacement.append(repl_cost_windows)

#components_wall_agains unheated
wall_ag_unheated_emb=[]
repl_wall_ag_unheated=[]
wall_ag_unheated_initial=[]
for i in unheated_ren:
    if i[0] == New_components_against_unheated[0]["Type"] and i[1] == "Wand":            
        if i[3] == "Insulation" or i[3] =="insulation":
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_wall_unheated_ins = New_components_against_unheated[0]["Insulation thickness"]*components_in_wall[0]["Area_in"]*(i[10]+i[13])*(1+New_components_against_unheated[0]["Uncertainty_GWP"])/i[4]
            repl_number_ins = math.ceil((timeperiod/New_components_against_unheated[0]["RSL"])-1)
            wall_ag_unheated_emb.append(emb_wall_unheated_ins)
            repl_wall_ag_unheated.append(repl_number_ins*emb_wall_unheated_ins)
            wall_ag_unheated_initial_cost_ins = New_components_against_unheated[0]["Insulation thickness"]*components_in_wall[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[0]["Uncertainty_cost"])/i[4]
            wall_ag_unheated_initial.append(wall_ag_unheated_initial_cost_ins)
        else:
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue                
            emb_wall_unheated = components_in_wall[0]["Area_in"]*(i[10]+i[13])*(1+New_components_against_unheated[0]["Uncertainty_GWP"])
            repl_number = math.ceil((timeperiod/New_components_against_unheated[0]["RSL"])-1)               
            wall_ag_unheated_emb.append(emb_wall_unheated)
            repl_wall_ag_unheated.append(repl_number*emb_wall_unheated)
            wall_ag_unheated_initial_cost = components_in_wall[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[0]["Uncertainty_cost"])
            wall_ag_unheated_initial.append(wall_ag_unheated_initial_cost)

RSLUW1=[]
for x in frange(New_components_against_unheated[0]["RSL"],60,New_components_against_unheated[0]["RSL"]):
    RSLUW1.append(x)
wall_ag_unheated_repl=[]
for k in RSLUW1:
    repl_cost_unheated_walls=round(sum(wall_ag_unheated_initial)*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    wall_ag_unheated_repl.append(repl_cost_unheated_walls)

#components slab1 against unheated
slab1_ag_unheated_emb=[]
repl_slab1_ag_unheated=[]
slab1_ag_unheated_initial=[]
for i in unheated_ren:
    if i[0] == New_components_against_unheated[1]["Type"] and i[1] == "Boden":
        if i[3] == "Insulation" or i[3] =="insulation":
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab1_unheated_ins = New_components_against_unheated[1]["Insulation thickness"]*(components_in_floor[0]["Area_in"]*(1+New_components_against_unheated[1]["Uncertainty_GWP"])*(i[10]+i[13])/i[4])
            repl_number_ins = math.ceil((timeperiod/New_components_against_unheated[1]["RSL"])-1)
            slab1_ag_unheated_emb.append(emb_slab1_unheated_ins)
            repl_slab1_ag_unheated.append(repl_number_ins*emb_slab1_unheated_ins)
            slab1_ag_unheated_initial_cost_ins = New_components_against_unheated[1]["Insulation thickness"]*(components_in_floor[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[1]["Uncertainty_cost"])/i[4])
            slab1_ag_unheated_initial.append(slab1_ag_unheated_initial_cost_ins)
        else:
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab1_unheated = components_in_floor[0]["Area_in"]*(1+New_components_against_unheated[1]["Uncertainty_GWP"])*(i[10]+i[13])
            repl_number = math.ceil((timeperiod/New_components_against_unheated[1]["RSL"])-1)
            slab1_ag_unheated_emb.append(emb_slab1_unheated)
            repl_slab1_ag_unheated.append(repl_number*emb_slab1_unheated)
            slab1_ag_unheated_initial_cost = components_in_floor[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[1]["Uncertainty_cost"])
            slab1_ag_unheated_initial.append(slab1_ag_unheated_initial_cost)
RSLUS1=[]
for x in frange(New_components_against_unheated[1]["RSL"],60,New_components_against_unheated[1]["RSL"]):
    RSLUS1.append(x)          
slab1_ag_unheated_repl = []
for k in RSLUS1:
    repl_cost_unheated_slab1=round(sum(slab1_ag_unheated_initial)*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    slab1_ag_unheated_repl.append(repl_cost_unheated_slab1)

#components slab2 against unheated
slab2_ag_unheated_emb=[]
repl_slab2_ag_unheated=[]
slab2_ag_unheated_initial=[]
for i in unheated_ren:
    if i[0] == New_components_against_unheated[2]["Type"] and i[1] == "Boden":
        if i[3] == "Insulation" or i[3] =="insulation":
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab2_unheated_ins = components_in_floor2[0]["Area_in"] *(New_components_against_unheated[2]["Insulation thickness"]*(i[10]+i[13])*(1+New_components_against_unheated[2]["Uncertainty_GWP"])/i[4])
            repl_number_ins = math.ceil((timeperiod/New_components_against_unheated[2]["RSL"])-1)
            slab2_ag_unheated_emb.append(emb_slab2_unheated_ins)
            repl_slab2_ag_unheated.append(repl_number_ins*emb_slab2_unheated_ins)
            slab2_ag_unheated_initial_cost_ins = New_components_against_unheated[2]["Insulation thickness"]*(components_in_floor2[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[2]["Uncertainty_cost"])/i[4])
            slab2_ag_unheated_initial.append(slab2_ag_unheated_initial_cost_ins)
        else:
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab2_unheated = components_in_floor2[0]["Area_in"]*(1+New_components_against_unheated[2]["Uncertainty_GWP"])*(i[10]+i[13])
            repl_number = math.ceil((timeperiod/New_components_against_unheated[2]["RSL"])-1)
            slab2_ag_unheated_emb.append(emb_slab2_unheated)
            repl_slab2_ag_unheated.append(repl_number*emb_slab2_unheated)
            slab2_ag_unheated_initial_cost = components_in_floor2[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[2]["Uncertainty_cost"])
            slab2_ag_unheated_initial.append(slab2_ag_unheated_initial_cost)

RSLUS2 = []
for x in frange(New_components_against_unheated[2]["RSL"],60,New_components_against_unheated[2]["RSL"]):
    RSLUS2.append(x)          
slab2_ag_unheated_repl = []
for k in RSLUS2:
    repl_cost_unheated_slab2=round(sum(slab2_ag_unheated_initial)*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    slab2_ag_unheated_repl.append(repl_cost_unheated_slab2)

#components slab3 against unheated
slab3_ag_unheated_emb=[]
repl_slab3_ag_unheated=[]
slab3_ag_unheated_initial=[]
for i in unheated_ren:
    if i[0] == New_components_against_unheated[3]["Type"] and i[1] == "Boden":
        if i[3] == "Insulation" or i[3] =="insulation":
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab3_unheated_ins = components_in_floor3[0]["Area_in"] *(New_components_against_unheated[3]["Insulation thickness"]*(i[10]+i[13])*(1+New_components_against_unheated[3]["Uncertainty_GWP"])/i[4])
            repl_number_ins = math.ceil((timeperiod/New_components_against_unheated[3]["RSL"])-1)
            slab3_ag_unheated_emb.append(emb_slab3_unheated_ins)
            repl_slab3_ag_unheated.append(repl_number_ins*emb_slab3_unheated_ins)
            slab3_ag_unheated_initial_cost_ins = New_components_against_unheated[3]["Insulation thickness"]*(components_in_floor3[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[3]["Uncertainty_cost"])/i[4])
            slab3_ag_unheated_initial.append(slab3_ag_unheated_initial_cost_ins)
        else:
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_slab3_unheated = components_in_floor3[0]["Area_in"]*(i[10]+i[13])*(1+New_components_against_unheated[3]["Uncertainty_GWP"])
            repl_number = math.ceil((timeperiod/New_components_against_unheated[3]["RSL"])-1)
            slab3_ag_unheated_emb.append(emb_slab3_unheated)
            repl_slab3_ag_unheated.append(repl_number*emb_slab3_unheated)
            slab3_ag_unheated_initial_cost = components_in_floor3[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[3]["Uncertainty_cost"])
            slab3_ag_unheated_initial.append(slab3_ag_unheated_initial_cost)
RSLUS3 = []
for x in frange(New_components_against_unheated[3]["RSL"],60,New_components_against_unheated[3]["RSL"]):
    RSLUS3.append(x)          
slab3_ag_unheated_repl = []
for k in RSLUS3:
    repl_cost_unheated_slab3=round(sum(slab3_ag_unheated_initial)*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    slab3_ag_unheated_repl.append(repl_cost_unheated_slab3)

#components roof against unheated cellar
roof_ag_unheated_emb = []
repl_roof_ag_unheated = []
roof_ag_unheated_initial =[]
for i in unheated_ren:
    if i[0] == New_components_against_unheated[4]["Type"] and i[1] == "Dach":
        if i[3] == "Insulation" or i[3] =="insulation":
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_roof_unheated_ins = components_in_ceiling[0]["Area_in"] *(New_components_against_unheated[4]["Insulation thickness"]*(1+New_components_against_unheated[4]["Uncertainty_GWP"])*(i[10]+i[13])/i[4])
            repl_number_ins = math.ceil((timeperiod/New_components_against_unheated[4]["RSL"])-1)
            roof_ag_unheated_emb.append(emb_roof_unheated_ins)
            repl_roof_ag_unheated.append(repl_number_ins*emb_roof_unheated_ins)
            roof_ag_unheated_initial_cost_ins = New_components_against_unheated[4]["Insulation thickness"]*(components_in_ceiling[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[4]["Uncertainty_cost"])/i[4])
            roof_ag_unheated_initial.append(roof_ag_unheated_initial_cost_ins)
        else:
            if math.isnan(i[10]) or math.isnan(i[13]):
                continue
            emb_roof_unheated = components_in_ceiling[0]["Area_in"]*(1+New_components_against_unheated[4]["Uncertainty_GWP"])*(i[10]+i[13])
            repl_number = math.ceil((timeperiod/New_components_against_unheated[4]["RSL"])-1)
            roof_ag_unheated_emb.append(emb_roof_unheated)
            repl_roof_ag_unheated.append(repl_number*emb_roof_unheated)
            roof_ag_unheated_initial_cost = components_in_ceiling[0]["Area_in"]*(i[24]+i[27])*(1+New_components_against_unheated[4]["Uncertainty_cost"])
            roof_ag_unheated_initial.append(roof_ag_unheated_initial_cost)
RSLUR = []
for x in frange(New_components_against_unheated[4]["RSL"],60,New_components_against_unheated[4]["RSL"]):
    RSLUR.append(x)
roof_ag_unheated_repl = []
for k in RSLUR:
    repl_cost_unheated_roof=round(sum(roof_ag_unheated_initial)*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    roof_ag_unheated_repl.append(repl_cost_unheated_roof)

#heating system
#heat distribution
heat_distr_type=1
heat_distr_type==heat_distr[0]
rn_heat_distr=timeperiod/(heat_distr[heat_distr_type-1]["heat_distr_RSL"])
if indicator==1:
    emb_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_GWP"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_GWP"])*EBF),1)
    LCA_replace_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_GWP"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_GWP"])*EBF*rn_heat_distr),1)
if indicator==2:
    emb_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_PE"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_PE"])*EBF),1)
    LCA_replace_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_PE"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_PE"])*EBF*rn_heat_distr),1)
if indicator==3:
    emb_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_UBP"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_UBP"])*EBF),1)
    LCA_replace_heat_distr=round(((heat_distr[heat_distr_type-1]["heat_distr_Pr_UBP"]+heat_distr[heat_distr_type-1]["heat_distr_EoL_UBP"])*EBF*rn_heat_distr),1)

initial_heat_distr=heat_distr[heat_distr_type-1]["heat_distr_cost"]*EBF
RSL_heat_distr=[]
if heat_distr[0]["heat_distr_RSL"]==0: RSL_heat_distr.append(0)
else:
    for x in frange(heat_distr[0]["heat_distr_RSL"],60,heat_distr[0]["heat_distr_RSL"]):
        RSL_heat_distr.append(x)
repl_cost_heat_distr=[]
for k in RSL_heat_distr:
    repl_cost=round(initial_heat_distr*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    repl_cost_heat_distr.append(repl_cost)

#operation LCA heating
Heating_renovation_operation_GWP = np.zeros(1)
Heating_renovation_operation_cost = np.zeros(1)
Price_growth_heating = np.zeros(1)
RSL_heat_generation = np.zeros(1)
Embodied_heat_generation=np.zeros(1)
Initial_cost_heat_generation=np.zeros(1)
for i in Heating_system:
    if round(heating_type_new) ==0:
        Heating_renovation_operation_GWP = Heating_renovation_operation_GWP_old
        Heating_renovation_operation_cost = Heating_renovation_operation_cost_old
        Price_growth_heating = Price_growth_heating_old
        Embodied_heat_generation = Embodied_heat_generation_old
        RSL_heat_generation = RSL_heat_generation_old
        Initial_cost_heat_generation = Initial_cost_heat_generation_old

    if round(heating_type_new) == i["Type"]:
        Heating_renovation_operation_GWP = i["GWP production"]
        Heating_renovation_operation_cost = i["Cost production"]
        Price_growth_heating = i["Price growth rate heating"]
        Embodied_heat_generation = i["Embodied_GWP_heat_generation"]
        RSL_heat_generation = i["RSL"]
        Initial_cost_heat_generation = i["Initial_cost_heat_generation"]
LCA_new_operation=[]
for year in Qheating_demand_new:
    if indicator==1:
        oper_new=year*Heating_renovation_operation_GWP*EBF
        LCA_new_operation.append(oper_new)
        units="kg CO2-eq."
LCA_oper_new=sum(LCA_new_operation)

#heat generation

if heating_type_new==0:
    rn_heat_gen=math.ceil( timeperiod /RSL_heat_generation_old) - 1
    emb_heat_gen=Embodied_heat_generation_old*EBF
    LCA_replace_heat_gen=round((Embodied_heat_generation_old*EBF*rn_heat_gen),1)
else:
    rn_heat_gen=math.ceil( timeperiod /RSL_heat_generation) - 1
    emb_heat_gen=round((Embodied_heat_generation*EBF),1)
    LCA_replace_heat_gen=round((Embodied_heat_generation*EBF*rn_heat_gen),1)

if heating_type_new==0:
    initial_heat_gen=Initial_cost_heat_generation_old*EBF
else:
    initial_heat_gen=Initial_cost_heat_generation*EBF
RSL_heat_gen=[]
if heating_type_new == 0:
    for x in frange(RSL_heat_generation_old,timeperiod,RSL_heat_generation_old):
        RSL_heat_gen.append(x)
else:
    for x in frange(RSL_heat_generation,timeperiod,RSL_heat_generation):
        RSL_heat_gen.append(x)
repl_cost_heat_gen=[]
for k in RSL_heat_gen:
    repl_cost=round(initial_heat_gen*((1+inflation_rate)**k)/((1+interest_rate)**k),1)
    repl_cost_heat_gen.append(repl_cost)
#electricity
el_equipment_type=1
el_equipment_type==electr_equip[0]
rn_el_equip=timeperiod/(electr_equip[el_equipment_type-1]["el_equip_RSL"])
if indicator==1:
    emb_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_GWP"]+electr_equip[el_equipment_type-1]["el_equip_EoL_GWP"])*EBF),1)
    LCA_replace_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_GWP"]+electr_equip[el_equipment_type-1]["el_equip_EoL_GWP"])*EBF*rn_el_equip),1)
if indicator==2:
    emb_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_PE"]+electr_equip[el_equipment_type-1]["el_equip_EoL_PE"])*EBF),1)
    LCA_replace_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_PE"]+electr_equip[el_equipment_type-1]["el_equip_EoL_PE"])*EBF*rn_el_equip),1)
if indicator==3:
    emb_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_UBP"]+electr_equip[el_equipment_type-1]["el_equip_EoL_UBP"])*EBF),1)
    LCA_replace_el_equip=round(((electr_equip[el_equipment_type-1]["el_equip_Pr_UBP"]+electr_equip[el_equipment_type-1]["el_equip_EoL_UBP"])*EBF*rn_el_equip),1)

initial_electr_equip=electr_equip[el_equipment_type-1]["el_equip_cost"]*EBF
repl_cost_electr_equip=round(electr_equip[el_equipment_type-1]["el_equip_cost"]*EBF*((1+inflation_rate)**electr_equip[el_equipment_type-1]["el_equip_RSL"])/((1+interest_rate)**(electr_equip[el_equipment_type-1]["el_equip_RSL"])),1)


Embodied_LCA_new=emb_heat_gen+emb_heat_distr+emb_el_equip+sum(windows_emb)+sum(floor_emb)+sum(roof_emb)+sum(emb_roof_finishes)+sum(exterior_wall_emb)+sum(emb_int_walls)+sum(slab3_ag_unheated_emb) + sum(slab2_ag_unheated_emb) + sum(slab1_ag_unheated_emb) + sum(roof_ag_unheated_emb) + sum(wall_ag_unheated_emb)
LCA_replace_new=round((LCA_replace_heat_gen+LCA_replace_heat_distr+LCA_replace_el_equip+sum(repl_windows)+sum(repl_floor)+sum(repl_roof)+sum(roof_finish_replacement)+sum(repl_ext_wall)+sum(wall_int_replacement)+sum(repl_slab1_ag_unheated)+sum(repl_slab2_ag_unheated)+sum(repl_slab3_ag_unheated)+sum(repl_roof_ag_unheated)+sum(repl_wall_ag_unheated)),1)
Total_LCA_new=Embodied_LCA_new+LCA_replace_new+LCA_oper_new

#initial_wind=windows_emb[windows_type-1]["windows_cost"]*Area_windows
#initial_patitions=partition[partition_type-1]["partition_cost"]*Area_partitions
#initial_floor=floor_cover[floor_cover_type-1]["floor_cover_cost"]*Area_floor
#initial_vent_system=vent_system[vent_system_type-1]["vent_system_cost"]*EBF
#initial_water_system=water_system[water_system_type-1]["water_system_cost"]*EBF
initial_total_exterior_walls = sum(initial_cost_ext_walls[0])+ sum(initial_cost_ext_walls[1])+sum(initial_cost_ext_walls[2])+sum(initial_cost_ext_walls[3])+sum(initial_cost_ext_walls[4])+sum(initial_cost_ext_walls[5])+sum(initial_cost_ext_walls[6])+sum(initial_cost_ext_walls[7])
initial_total_cost_windows = sum(initial_cost_windows[0] + initial_cost_windows[1] + initial_cost_windows[2] + initial_cost_windows[3] + initial_cost_windows[4] + initial_cost_windows[5] + initial_cost_windows[6] + initial_cost_windows[7] ) + initial_total_exterior_walls
initial_total_roof = sum(initial_cost_roof[0])+sum(initial_cost_roof[1])+sum(initial_cost_roof[2])
initial_total_slab = sum(initial_cost_floor[0])+sum(initial_cost_floor[1])+sum(initial_cost_floor[2])+sum(initial_cost_floor[3])+sum(initial_cost_floor[4])
initial_sum=initial_total_slab+initial_total_cost_windows+initial_heat_distr+initial_electr_equip+initial_heat_gen+sum(initial_int_walls)+sum(initial_roof_finish)+sum(wall_ag_unheated_initial)+sum(roof_ag_unheated_initial)+sum(slab1_ag_unheated_initial)+sum(slab2_ag_unheated_initial)+sum(slab3_ag_unheated_initial)
#print("initial cost = {} Fr".format(initial_sum))
#NPV_replacement_cost
#external wall

#repl_cost_windows=round(windows_emb[windows_type-1]["windows_cost"]*Area_windows*((1-windows_emb[windows_type-1]["windows_cost_change"])**windows_emb[windows_type-1]["windows_RSL"])*(1+interest_rate)**(-windows_emb[windows_type-1]["windows_RSL"]),1)

repl_cost=sum(repl_cost_heat_gen)+sum(repl_cost_heat_distr)+repl_cost_electr_equip+sum(windows_replacement)+sum(replacement_ext_walls)+sum(replacement_int_walls)+sum(replacement_roof_cover)+sum(replacement_roof_finish)+sum(replacement_floor)+sum(roof_ag_unheated_repl)+sum(slab1_ag_unheated_repl)+sum(slab2_ag_unheated_repl)+sum(slab3_ag_unheated_repl)+sum(wall_ag_unheated_repl)

LCC=[]
for year, period in zip(Qheating_demand_new, range(1,61)):
    #LCC_tot=i*EBF*heating_cost*(1+price_growth_heating)
    #LCC_operation=year*EBF*heating_cost_new*(1+Price_growth_heating)
    LCC_operation=year*EBF*Heating_renovation_operation_cost*((1+inflation_rate)**period)/((1+interest_rate)**period)
    LCC.append(LCC_operation)
#LCC_operation_year1=Qheating_demand_new[0]*EBF*Heating_renovation_operation_cost*(1+Price_growth_heating)
#LCC_operation = LCC_operation_year1*(1-((1+inflation_rate+Price_growth_heating)**timeperiod)*(1+interest_rate)**(-timeperiod))/(interest_rate-(inflation_rate+Price_growth_heating))
#LCC.append(LCC_operation)


#Maintenance LCC according to CRB values
Maintenance_ext_wall=[]
Maintenance_windows=[]
Maintenace_roof =[]
Maintenance_slab =[]
Maintenance_heating_system = []
Maintenance_ventilation =[]
Maintenace_electrical_equipment = []
Maintenance_water_system = []

for j in range(round(timeperiod)):
    Maintenance_ext_wall.append((initial_total_exterior_walls*Maintenance_LCC[4]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
    Maintenance_windows.append((initial_total_cost_windows*Maintenance_LCC[4]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
    Maintenace_roof.append((initial_total_roof*Maintenance_LCC[5]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
    Maintenance_slab.append((initial_total_slab*Maintenance_LCC[6]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
    Maintenace_electrical_equipment.append((initial_electr_equip*Maintenance_LCC[0]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
    Maintenance_heating_system.append((initial_heat_gen*Maintenance_LCC[0]["Maintenance_LCC"]/100)*(1+inflation_rate)**j/((1+interest_rate)**j))
Maintenance = []
for a, b, c, d, e, f in zip(Maintenance_ext_wall, Maintenance_windows, Maintenace_roof, Maintenance_slab, Maintenance_heating_system, Maintenace_electrical_equipment):
    Maintenance.append(a+ b+ c+ d+ e+ f)

LCC_tot=sum(LCC)+initial_sum+repl_cost+sum(Maintenance)


#labor cost
"""
repl_cost_ext_wall_finish=round(ext_wall_finish[ext_wall_finish_type-1]["ext_wall_finish_cost"]*Area_walls*((1-ext_wall_finish[ext_wall_finish_type-1]["ext_wall_finish_cost_change"])**ext_wall_finish[ext_wall_finish_type-1]["ext_wall_finish_RSL"])*(1+interest_rate)**(-ext_wall_finish[ext_wall_finish_type-1]["ext_wall_finish_RSL"]),1)
repl_cost_int_wall_finish=round(int_wall_finish[int_wall_finish_type-1]["int_wall_finish_cost"]*Area_walls*((1-int_wall_finish[int_wall_finish_type-1]["int_wall_finish_cost_change"])**int_wall_finish[int_wall_finish_type-1]["int_wall_finish_RSL"])*(1+interest_rate)**(-int_wall_finish[int_wall_finish_type-1]["int_wall_finish_RSL"]),1)

repl_cost_roof_finish=round(roof_finish[roof_finish_type-1]["roof_finish_cost"]*Area_roof*((1-roof_finish[roof_finish_type-1]["roof_finish_cost_change"])**roof_finish[roof_finish_type-1]["roof_finish_RSL"])*(1+interest_rate)**(-roof_finish[roof_finish_type-1]["roof_finish_RSL"]),1)
repl_cost_roof_cover=round(roof_cover[roof_cover_type-1]["roof_cover_cost"]*Area_roof*((1-roof_cover[roof_cover_type-1]["roof_cover_cost_change"])**roof_cover[roof_cover_type-1]["roof_cover_RSL"])*(1+interest_rate)**(-roof_cover[roof_cover_type-1]["roof_cover_RSL"]),1)
repl_cost_floor=round(floor_cover[floor_cover_type-1]["floor_cover_cost"]*Area_floor*((1-floor_cover[floor_cover_type-1]["floor_cover_cost_change"])**floor_cover[floor_cover_type-1]["floor_cover_RSL"])*(1+interest_rate)**(-roof_cover[roof_cover_type-1]["roof_cover_RSL"]),1)
repl_cost_partitions=round(partition[partition_type-1]["partition_cost"]*Area_partitions*((1-partition[partition_type-1]["partition_cost_change"])**partition[partition_type-1]["partition_RSL"])*(1+interest_rate)**(-partition[partition_type-1]["partition_RSL"]),1)
repl_cost_vent_system=round(vent_system[vent_system_type-1]["vent_system_cost"]*EBF*((1-vent_system[vent_system_type-1]["vent_system_cost_change"])**vent_system[vent_system_type-1]["vent_system_RSL"])*(1+interest_rate)**(-vent_system[vent_system_type-1]["vent_system_RSL"]),1)

repl_cost_water_system=round(water_system[water_system_type-1]["water_system_cost"]*EBF*((1-water_system[water_system_type-1]["water_system_cost_change"])**water_system[water_system_type-1]["water_system_RSL"])*(1+interest_rate)**(-water_system[water_system_type-1]["water_system_RSL"]),1)
replacement_cost=repl_cost_ext_wall_finish+repl_cost_int_wall_finish+repl_cost_floor+repl_cost_roof_cover+repl_cost_roof_finish+repl_cost_windows+repl_cost_partitions+repl_cost_electr_equip+repl_cost_heat_gen+repl_cost_heat_distr+repl_cost_vent_system+repl_cost_water_system
"""
#print(replacement_cost)

#Heating demand
plt.plot(Qheating_demand, "-")
plt.ylabel("Heating demand base case, kWh/m2,a")
plt.xlabel("Years")
plt.title("Heating demand")
#plt.show()

#Heating demand renovation
plt.plot(Qheating_demand_new, "-")
plt.ylabel("Heating demand renovation, kWh/m2,a")
plt.xlabel("Years")
plt.title("Heating demand")
#plt.show()

#LCA renovation
x=np.arange(1)
bar1=Embodied_LCA_new
plt.bar(x, bar1, color="gray")
plt.bar(x, LCA_replace_new, color="yellow", bottom= Embodied_LCA_new)
plt.bar(x, LCA_oper_new, color="blue", bottom = Embodied_LCA_new+LCA_replace_new)

plt.xticks(x, ["building"])
plt.title("LCA renovation")
plt.ylabel("kg CO2 eq.")
embodied_patch=mpatches.Patch(color="gray", label="Embodied")
replacement_patch=mpatches.Patch(color="yellow", label="Replacement")
operation_patch=mpatches.Patch(color="blue", label="Operation")
plt.legend(handles=[embodied_patch, replacement_patch, operation_patch], loc ="upper left")
#plt.show()

f=open("Results.txt", "w")
f.write("{}\n".format(Qhd_new[-1]))
f.write("{}\n".format(LCC_tot))
f.write("{}\n".format(Total_LCA_new))
f.close()
#print(Q_transm_loss) #transmission loss
#print(Q_transm_loss_new)
#print(Q_vent_perf_loss)
#print(Q_vent_perf_loss_new) #ventilation loss

#print(Qisol)
#print(Qisol_new)
print(Qhd_new[-1])

print(LCC_tot/EBF/timeperiod)
print(Total_LCA_new/EBF/timeperiod)
#print(Qheating_demand_new[-1])
#print(LCA_oper)