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

where <a href="https://www.codecogs.com/eqnedit.php?latex=T_i_n,[^{\circ}C]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_i_n,[^{\circ}C]" title="T_i_n,[^{\circ}C]" /></a> is the operating temperature inside, <a href="https://www.codecogs.com/eqnedit.php?latex=T_{out},[^{\circ}C]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{out},[^{\circ}C]" title="T_{out},[^{\circ}C]" /></a> is the mean outside dry-bulb temperature during a month, <a href="https://www.codecogs.com/eqnedit.php?latex=U_i&space;[W/m^2&space;K]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_i&space;[W/m^2&space;K]" title="U_i [W/m^2 K]" /></a> is the heat transfer coefficient of the component i, <a href="https://www.codecogs.com/eqnedit.php?latex=k_i&space;[m^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_i&space;[m^2]" title="k_i [m^2]" /></a>  is a surface area of the component i,  <a href="https://www.codecogs.com/eqnedit.php?latex=z[days]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z[days]" title="z[days]" /></a> is the number of days in the current  month and <a href="https://www.codecogs.com/eqnedit.php?latex=ERA&space;[m^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ERA&space;[m^2]" title="ERA [m^2]" /></a> is the energy reference area that represents the heated floor area of a building.

In the current calculations, symbol i represents the components of the envelope and j represents the materials of the component i. The heat transfer for a component i <a href="https://www.codecogs.com/eqnedit.php?latex=U_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_i" title="U_i" /></a> is calculated as <a href="https://www.codecogs.com/eqnedit.php?latex=U_i&space;=&space;1/R_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_i&space;=&space;1/R_i" title="U_i = 1/R_i" /></a>. <a href="https://www.codecogs.com/eqnedit.php?latex=R_{i}&space;[(m^2*K)/W]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R_{i}&space;[(m^2*K)/W]" title="R_{i} [(m^2*K)/W]" /></a> is the thermal resistance of the component i:

<a href="https://www.codecogs.com/eqnedit.php?latex=R_i&space;=&space;\sum_{j}^{}(d_j/\lambda_j)&plus;1/U_{ex,i}&plus;R_s_e&plus;R_s_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R_i&space;=&space;\sum_{j}^{}(d_j/\lambda_j)&plus;1/U_{ex,i}&plus;R_s_e&plus;R_s_i" title="R_i = \sum_{j}^{}(d_j/\lambda_j)+1/U_{ex,i}+R_s_e+R_s_i" /></a>

Ventilation loss ![](https://latex.codecogs.com/gif.latex?Q_%7BV%7D)  – heat loss due to ventilation system. 
It is calculated as: ![](https://latex.codecogs.com/gif.latex?Q_%7BV%7D%20%3D%20c_%7Bp%2Cair%7D%20*%20q_%7Bvent%7D*%28T_%7Bin%7D%20-%20T_%7Bout%7D%29), where
<a href="https://www.codecogs.com/eqnedit.php?latex=c_{p,air}&space;[Wh/(m^3*K]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{p,air}&space;[Wh/(m^3*K]" title="c_{p,air} [Wh/(m^3*K]" /></a> – air specific heat capacity
<a href="https://www.codecogs.com/eqnedit.php?latex=q_{vent}[m^3/(m^2*h)]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?q_{vent}[m^3/(m^2*h)]" title="q_{vent}[m^3/(m^2*h)]" /></a> – outside air volume flow
![](https://latex.codecogs.com/gif.latex?T_%7Bin%7D) [![](https://latex.codecogs.com/gif.latex?%7B%5Ccirc%7D_%7BC%7D)]- comfort temerature inside,
![](https://latex.codecogs.com/gif.latex?T_%7Bout%7D) [![](https://latex.codecogs.com/gif.latex?%7B%5Ccirc%7D_%7BC%7D)] - monthly mean dry-bulb temperature outside.	
 
For the calculation of the outside air volume flow in buildings with mechanical ventilation during the operating time of the ventilation, the larger value between the outside air and exhaust air volume flow of the ventilation system is used. To do this, the outside air volume flow due to the air permeability of the building envelope with running ventilation system is added. In buildings whose air permeability meets the requirements of SIA 180, it can be neglected.
A possible heat recovery with a temperature recovery efficiency can be taken into account.

Heat gains (internal gains) – heat which is released by the occupants, equipment, lighting. It is defined by static values of SIA 380/1. It is defined as:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{int,m}=Q_{icc,m}&space;&plus;&space;Q_{iel,m}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{int,m}=Q_{icc,m}&space;&plus;&space;Q_{iel,m}" title="Q_{int,m}=Q_{icc,m} + Q_{iel,m}" /></a> , where

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{icc,m}[kWh/m^2,month]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{icc,m}[kWh/m^2,month]" title="Q_{icc,m}[kWh/m^2,month]" /></a> is the monthly occupancy heat gain, which is calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{icc,m}=Q_{g,occ,m}*t_{occ}*t/(A_p*1000)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{icc,m}=Q_{g,occ,m}*t_{occ}*t/(A_p*1000)" title="Q_{icc,m}=Q_{g,occ,m}*t_{occ}*t/(A_p*1000)" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=Q_{g,occ}[W/P]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{g,occ}[W/P]" title="Q_{g,occ}[W/P]" /></a> is the heat gain per person defined by SIA 380/1, <a href="https://www.codecogs.com/eqnedit.php?latex=t_{occ}[h/day]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t_{occ}[h/day]" title="t_{occ}[h/day]" /></a> is the occupancy time during the day, t is the number of days in a month, and <a href="https://www.codecogs.com/eqnedit.php?latex=A_p&space;[m^2/P]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A_p&space;[m^2/P]" title="A_p [m^2/P]" /></a> is the area per person. 

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{iel,m}&space;[kWh/m^2,month]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{iel,m}&space;[kWh/m^2,month]" title="Q_{iel,m} [kWh/m^2,month]" /></a> is the monthly heat gains from the electricity, e.g. lighting and equipment.

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{iel,m}=Q_{el,m}*f_{el}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{iel,m}=Q_{el,m}*f_{el}" title="Q_{iel,m}=Q_{el,m}*f_{el}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex==Q_{el}&space;[kWh/m^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=Q_{el}&space;[kWh/m^2]" title="=Q_{el} [kWh/m^2]" /></a> is the monthly electricity heat gains defined by SIA 380/1 and <a href="https://www.codecogs.com/eqnedit.php?latex=f_{el}[-]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{el}[-]" title="f_{el}[-]" /></a> is a  reduction factor defined by SIA 380/1.

Solar heat gains <a href="https://www.codecogs.com/eqnedit.php?latex=Q_{s,m}[kWh/m^2,month]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{s,m}[kWh/m^2,month]" title="Q_{s,m}[kWh/m^2,month]" /></a> - heat gains coming from solar to the building through the transparent surfaces (windows). It is calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{s,m}=&space;\sum_{q}^{}Q_{s,m,q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{s,m}=&space;\sum_{q}^{}Q_{s,m,q}" title="Q_{s,m}= \sum_{q}^{}Q_{s,m,q}" /></a>, where

where <a href="https://www.codecogs.com/eqnedit.php?latex=Q_{s,m,q}[kWh/m^2,month]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{s,m,q}[kWh/m^2,month]" title="Q_{s,m,q}[kWh/m^2,month]" /></a> is the solar heat gains for month m for the q-th window. It is calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{s,m,q}=&space;I_{sol}*A_q*g_q*f_q*f_{s1,q}*f_{s2,q}*f_{s3(I),q}*f_{s3(II),q}/ERA" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{s,m,q}=&space;I_{sol}*A_q*g_q*f_q*f_{s1,q}*f_{s2,q}*f_{s3(I),q}*f_{s3(II),q}/ERA" title="Q_{s,m,q}= I_{sol}*A_q*g_q*f_q*f_{s1,q}*f_{s2,q}*f_{s3(I),q}*f_{s3(II),q}/ERA" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=g_{q}&space;[-]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_{q}&space;[-]" title="g_{q} [-]" /></a> - solar heat gain coefficient 

![](https://latex.codecogs.com/gif.latex?A_%7Bwindow%7D) [m2] - Window area

f [%] - glazing percentage
 
![](https://latex.codecogs.com/gif.latex?I_%7Bsol%7D) [kWh/m2] - monthly solar irradiation

![](https://latex.codecogs.com/gif.latex?f_%7Bs1%7D) - shading factor for horizon

![](https://latex.codecogs.com/gif.latex?f_%7Bs2%7D) - shading factor for overhang

![](https://latex.codecogs.com/gif.latex?f_%7Bs3%28I%29%29%7D), ![](https://latex.codecogs.com/gif.latex?f_%7Bs3%28II%29%29%7D) - shading factors for side blinds

The assumptions taken for the shading factors can be seen in SIA 380/1 (2016), pages 37-38.

Finally, the annual heating demand is calculated by summing the monthly heating demand:
<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{H,a}=\sum_{m=1}^{12}Q_{H,m}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{H,a}=\sum_{m=1}^{12}Q_{H,m}" title="Q_{H,a}=\sum_{m=1}^{12}Q_{H,m}" /></a>

After it is defined, the heating source is selected (heatpump, electricity, gas, oil, wood). For example, geothermal (ground source heat pump GSHP) can have a coefficient of performance (COP) as 3.5 which would mean that for 1 kWh of electricity we get 3.5 kWh of heating. For electricity COP is usually 1. For gas heating systems, there is another factor which is called AFUE – annual fuel utilization efficiency which can be between 70-97%. In this analysis, this factor is defined as PF (performance factor). Once the source is selected, the final energy demand is eventually calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=Q_{F,a}=&space;Q_{H,a}/PF" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q_{F,a}=&space;Q_{H,a}/PF" title="Q_{F,a}= Q_{H,a}/PF" /></a>

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
