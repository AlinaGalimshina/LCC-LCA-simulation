# LCC-LCA-simulation

The current code describes the analysis of Life cycle cost (LCC) and Life cycle assessment (LCA) for building renovation process. The analysis includes the following stages - A1-A3 (production), B4 (replacement), B6 (operational energy use) and C1-C4 (end of life). The data is taken from the .txt file where the input parameters are listed as well as the excel file (Components_catalog_data.xlsx) where the possible renovation measures for the envelope are listed. 

The code is divided into two big parts - The assessed building before renovation and after renovation. The building before renovation includes only the operational energy consumption(heating and electricity) as well as replacement and end of life.

The operational energy consumption is calculated according to the Swiss standard SIA 380/1. 
Heating demand is calculated as following:

![](https://latex.codecogs.com/gif.latex?Q_%7BH%7D%20%3D%20Q_%7BT%7D%20&plus;%20Q_%7BV%7D%20-%20%28Q_%7Bs%7D%20&plus;%20Q_%7Bint%7D%29*%5Ceta), where

![](https://latex.codecogs.com/gif.latex?Q_%7BT%7D) – transmission loss, 
![](https://latex.codecogs.com/gif.latex?Q_%7BV%7D) – ventilation loss, 
![](https://latex.codecogs.com/gif.latex?Q_%7Bs%7D) – solar heat gain, 
![](https://latex.codecogs.com/gif.latex?Q_%7Bint%7D) – internal heat gains, 
![](https://latex.codecogs.com/gif.latex?%5Ceta) – coefficient of utilization of the heat gains.

Transmission loss ![](https://latex.codecogs.com/gif.latex?Q_%7BT%7D) – heat transmission through the wall or any other type of construction (roof, ground, windows). 
It is calculated as: 

![](https://latex.codecogs.com/gif.latex?Q_T,_m%3D%20%5Csum%20%5Cfrac%7B%5Clambda%7D%7Bd%7D*A*%28T_%7Bin%7D%20-%20T_%7Bout%7D%29), where

U [W/m2K] – heat transfer coefficient, rate of the heat loss through the construction. 
U-value is calculated as ![](https://latex.codecogs.com/gif.latex?U%20%3D%20%5Cfrac%7B%5Clambda%20%7D%7Bd%7D), where ![](https://latex.codecogs.com/gif.latex?%5Clambda) – thermal conductivity [W/Km], ![](https://latex.codecogs.com/gif.latex?d) –thickness [m],

![](https://latex.codecogs.com/gif.latex?A) [m2] – surface area,
![](https://latex.codecogs.com/gif.latex?T_%7Bin%7D) - comfort temerature inside,
![](https://latex.codecogs.com/gif.latex?T_%7Bout%7D) - monthly mean temperature outside.

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


