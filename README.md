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

U[W/m2*K] – heat transfer coefficient, rate of the heat loss through the construction. 
U-value is calculated as ![](https://latex.codecogs.com/gif.latex?U%20%3D%20%5Cfrac%7B%5Clambda%20%7D%7Bd%7D), where ![](https://latex.codecogs.com/gif.latex?%5Clambda) – thermal conductivity [W/K*m], ![](https://latex.codecogs.com/gif.latex?d) –thickness [m],

![](https://latex.codecogs.com/gif.latex?A) [m2] – surface area,
![](https://latex.codecogs.com/gif.latex?T_%7Bin%7D) - comfort temerature inside,
![](https://latex.codecogs.com/gif.latex?T_%7Bout%7D) - monthly mean temperature outside.

After the transmission losses are calculated, the final transmission loss is 
Thermal bridge -  an area of the building envelope where the heat flow is increased in comparison with adjacent areas (if there is a difference in temperature between the inside and the outside).
Thermal bridge can be calculated or can be assumed to have a certain percentage depending on the type/age/construction of the building as it is defined by SIA 380. 


