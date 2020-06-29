# LCC-LCA-simulation

The current code describes the analysis of Life cycle cost (LCC) and Life cycle assessment (LCA) for building renovation process. The analyses include the following stages - A1-A3 (production), B4 (replacement), B6 (operational energy use) and C1-C4 (end of life). In case of LCC, the repair is also taken into account. The data is taken from the .txt file where the input parameters are listed as well as the excel file (Components_catalog_data.xlsx) where the possible renovation measures for the envelope are listed. 

The code is divided into two parts - The assessed building before renovation and after renovation. The building before renovation includes only the operational energy consumption(heating and electricity) as well as replacement and end of life.

The operational energy consumption is calculated according to the Swiss standard SIA 380/1. 
The monthly heating demand is calculated as following:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_H,_m=&space;(Q_T,_m&space;&plus;&space;Q_V,_m-(Q_s,_m&space;&plus;&space;Q_{int,m})*\eta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_H,_m=&space;(Q_T,_m&space;&plus;&space;Q_V,_m-(Q_s,_m&space;&plus;&space;Q_{int,m})*\eta)" title="Q_H,_m= (Q_T,_m + Q_V,_m-(Q_s,_m + Q_{int,m})*\eta)" /></a>, where

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_T,_m,&space;[kWh/(m^2,month)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_T,_m,&space;[kWh/(m^2,month)]" title="Q_T,_m, [kWh/(m^2,month)]" /></a> – monthly transmission loss, 
<a href="https://www.codecogs.com/eqnedit.php?latex=Q_V,_m,&space;[kWh/(m^2,month)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_V,_m,&space;[kWh/(m^2,month)]" title="Q_V,_m, [kWh/(m^2,month)]" /></a> – ventilation loss, 
<a href="https://www.codecogs.com/eqnedit.php?latex=Q_s,_m,&space;[kWh/(m^2,month)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_s,_m,&space;[kWh/(m^2,month)]" title="Q_s,_m, [kWh/(m^2,month)]" /></a> – solar heat gain, 
<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{int,m},&space;[kWh/(m^2,month)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{int,m},&space;[kWh/(m^2,month)]" title="Q_{int,m}, [kWh/(m^2,month)]" /></a> – internal heat gains, 
<a href="https://www.codecogs.com/eqnedit.php?latex=\eta,&space;[-]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\eta,&space;[-]" title="\eta, [-]" /></a> – coefficient of utilization of the heat gains.

The monthly transmission loss <a href="https://www.codecogs.com/eqnedit.php?latex=Q_T,_m,&space;[kWh/(m^2,month)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_T,_m,&space;[kWh/(m^2,month)]" title="Q_T,_m, [kWh/(m^2,month)]" /></a> – heat transmission through the building envelope (roof, ground, windows). 
It is calculated as: 

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{T,m}&space;=&space;\sum_{i}^{}Q_{T,m,i}*\varphi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{T,m}&space;=&space;\sum_{i}^{}Q_{T,m,i}*\varphi" title="Q_{T,m} = \sum_{i}^{}Q_{T,m,i}*\varphi" /></a>, 

where <a href="https://www.codecogs.com/eqnedit.php?latex=\varphi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi" title="\varphi" /></a> represents the thermal bridge i.e., an area of the building envelope where the heat flow is increased in comparison with adjacent areas (if there is a difference in temperature between the inside and the outside). The thermal bridge can be calculated or can be assumed to have a certain percentage depending on the type/age/construction of the building as it is defined by SIA 380. <a href="https://www.codecogs.com/eqnedit.php?latex=Q_{T,m,i},[kWh/m^2,month]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{T,m,i},[kWh/m^2,month]" title="Q_{T,m,i},[kWh/m^2,month]" /></a> is the monthly transmission loss for the i-th component and is calculated as:

where T_in  [°C] is the operating temperature inside, T_out  [°C] is the mean outside dry-bulb temperature during a month, U_i  [W/m^2 K] is the heat transfer coefficient of the component i, k_i  [m^2]  is a surface area of the component i,  z [days] is the number of days in the current  month and ERA [m^2] is the energy reference area that represents the heated floor area of a building.

After the transmission losses are calculated, the final transmission loss is ![](https://latex.codecogs.com/gif.latex?Q_%7BT%7D%20%3D%20%5Csum%20Q_%7BT%2Cm%7D%20*%20%5Cpsi)
Thermal bridge ![](https://latex.codecogs.com/gif.latex?%5Cpsi) -  an area of the building envelope where the heat flow is increased in comparison with adjacent areas (if there is a difference in temperature between the inside and the outside).
Thermal bridge can be calculated or can be assumed to have a certain percentage depending on the type/age/construction of the building as it is defined by SIA 380/1.

Ventilation loss ![](https://latex.codecogs.com/gif.latex?Q_%7BV%7D)  – heat loss due to ventilation system. 
It is calculated as: ![](https://latex.codecogs.com/gif.latex?Q_%7BV%7D%20%3D%20c_%7Bp%2Cair%7D%20*%20q_%7Bvent%7D*%28T_%7Bin%7D%20-%20T_%7Bout%7D%29), where
![](https://latex.codecogs.com/gif.latex?c_%7Bp%2Cair%7D) [J/kg*k] – air specific heat capacity
![](https://latex.codecogs.com/gif.latex?q_%7Bvent%7D) [m3/s] – outside air volume flow
![](https://latex.codecogs.com/gif.latex?T_%7Bin%7D) [![](https://latex.codecogs.com/gif.latex?%7B%5Ccirc%7D_%7BC%7D)]- comfort temerature inside,
![](https://latex.codecogs.com/gif.latex?T_%7Bout%7D) [![](https://latex.codecogs.com/gif.latex?%7B%5Ccirc%7D_%7BC%7D)] - monthly mean temperature outside.	
 
▪ For the calculation of the outside air volume flow in buildings with mechanical ventilation during the operating time of the ventilation, the larger value between the outside air and exhaust air volume flow of the ventilation system is used. To do this, the outside air volume flow due to the air permeability of the building envelope with running ventilation system is added. In buildings whose air permeability meets the requirements of SIA 180, it can be neglected.
▪ A possible heat recovery with a temperature recovery efficiency can be taken into account.

Heat gains (internal gains) – heat which is released by the occupants, equipment, lighting. It is defined by static values of SIA 380/1.
Solar heat gains ![](https://latex.codecogs.com/gif.latex?Q_%7Bs%7D) - heat gains coming from solar to the building through the transparent surfaces (windows). It is calculated as:

![](https://latex.codecogs.com/gif.latex?Q_%7Bs%7D%20%3D%20I_%7Bsol%7D%20*%20A_%7Bwindow%7D*g*f*f_%7Bs1%7D*f_%7Bs2%7D*f_%7Bs3%28I%29%29%7D*f_%7Bs3%28II%29%29%7D), where

g - solar heat gain coefficient 

![](https://latex.codecogs.com/gif.latex?A_%7Bwindow%7D) [m2] - Window area

f [%] - glazing percentage
 
![](https://latex.codecogs.com/gif.latex?I_%7Bsol%7D) [kWh/m2] - solar irradiation

![](https://latex.codecogs.com/gif.latex?f_%7Bs1%7D) - shading factor for horizon

![](https://latex.codecogs.com/gif.latex?f_%7Bs2%7D) - shading factor for overhang

![](https://latex.codecogs.com/gif.latex?f_%7Bs3%28I%29%29%7D), ![](https://latex.codecogs.com/gif.latex?f_%7Bs3%28II%29%29%7D) - shading factors for side blinds

Heating demand is calculated for each month of the year.

After it is defined, the heating source is selected (heatpump, electricity, gas, oil, wood). For example, geothermal (ground source heat pump GSHP) can have a coefficient of performance (COP) as 3.5 which would mean that for 1 kWh of electricity we get 3.5 kWh of heating. For electricity COP is usually 1. For gas heating systems, there is another factor which is called AFUE – annual fuel utilization efficiency which can be between 70-97%. Once the source is selected, the final energy demand is calculated. 

Life cycle cost analysis

Life cycle cost (LCC) – the sum of all costs over the whole life span of the building. One of the most used methods to calculate LCC is Net present approach (NPV), which is a sum of all costs and revenues discounted to the time of the initial investment.

According to the Swiss Center for buildings’ rationalization, NPV is calculated using the following equation:

![](https://latex.codecogs.com/gif.latex?NPV%20%3D%20C_%7BInvestments%7D%20&plus;%20C_%7BOperation%7D%20&plus;%20C_%7BMaintenance%7D%20&plus;%20C_%7BReplacement%7D%20&plus;%20C_%7BEnd%20of%20life%7D%20%3D%20C_%7BInvestment%7D%20&plus;%20%5Csum_%7BN%7D%5E%7Bn%20%3D%201%7D%20%28%5Cfrac%7BC_%7BMaintenance%7D*%281&plus;k%29%5E%7Bn%7D%7D%7B%281&plus;i_%7Bn%7D%29%5E%7Bn%7D%7D%29%20&plus;%20%5Csum_%7BN%7D%5E%7Bn%20%3D%201%7D%20%28%5Cfrac%7BC_%7BReplacement%7D*%281&plus;k%29%5E%7Bk%7D%7D%7B%281&plus;i_%7Bn%7D%29%5E%7Bk%7D%7D%29%20&plus;%20%5Csum_%7BN%7D%5E%7Bn%20%3D%201%7D%20%28%5Cfrac%7BC_%7BOperation%7D*%281&plus;k%29%5E%7Bn%7D%7D%7B%281&plus;i_%7Bn%7D%29%5E%7Bn%7D%7D%29%20&plus;%20%5Csum_%7BN%7D%5E%7Bn%20%3D%201%7D%20%28%5Cfrac%7BC_%7BEnd%20of%20life%7D*%281&plus;k%29%5E%7Bn%7D%7D%7B%281&plus;i_%7Bn%7D%29%5E%7Bn%7D%7D%29) , where

k [%] - inflation rate;
![](https://latex.codecogs.com/gif.latex?i_%7Bn%7D) - discount rate(nominal);
N [years]  - time period of analysis;
k [years]  - replacement year.

Life cycle assessment

Life cycle assessment (LCA) is a methodology used to evaluate the environmental impacts over the whole life span of a building. The goal of the lca is to quantify the environmental impacts from the extraction and production of the materials through life cycle to the end of life.

The LCA calculation in this code is performed as following:

![](https://latex.codecogs.com/gif.latex?LCA_%7Bi%7D%20%3D%20LCA_%7Bembodied%2Ci%7D%20&plus;%20LCA_%7Boperation%7D%20&plus;%20LCA_%7Breplacement%2Ci%7D%20&plus;%20LCA_%7Bendoflife%2Ci%7D%20%3D%20m_%7Bembodied%2C%20i%7D*k_%7Bi%7D%20&plus;%20%5Cfrac%7BQ_H%7D%7BPF%7D%20*%20IF_%7Bo%7D*RSP%20&plus;%20m_%7Bembodied%2C%20i%7D*k_%7Bi%7D*%20n_%7Bi%7D%20&plus;%20m_%7Bendoflife%2C%20i%7D*k_%7Bi%7D), where

where ![](https://latex.codecogs.com/gif.latex?m_%7Bembodied%2C%20i%7D) is the environmental impact for the selected indicator associated with the production of the material i, ![](https://latex.codecogs.com/gif.latex?k_%7Bi%7D) is the amount of the material expressed in m2, ![](https://latex.codecogs.com/gif.latex?Q_%7BH%7D) is a yearly heating demand of a building, PF is the performance factor which includes the efficiency of the system or the COP of a heat pump, ![](https://latex.codecogs.com/gif.latex?IF_%7Bo%7D) is the operational impact factor. ![](https://latex.codecogs.com/gif.latex?n_%7Bi%7D) is a number of times the material has to be replaced during the building’s service life, ![](https://latex.codecogs.com/gif.latex?m_%7Bendoflife%2C%20i%7D) is the impact associated with the demolition of the material i.

The output from this assessment is the total LCC of the renovated building in CHF/m2,year and LCA in kg.CO2eq./m2,year.
