# E484

Repo for the class E484 - Scientific Visualization, for the final project


## Project Purpose
Our team would like to explore the geographic and historic impacts of climate change will help to give context to this problem in order to improve the outcomes based on historic data and simulations. We are interested in metrics related to climate change that are tracked by several government agencies and various institutions, and are focusing on surface air temperature anomalies. The main purpose of this scientific visualization project will be to communicate the science of climate change to the general public.


## Data Source
This project uses data from the *NASA Goddard Institute for Space Studies* and we are analyzing the *Land-Ocean Temperature Index, ERSSTv5, 1200km smoothing* data to look at surface air temperature anomaly data. This data is an estimate of global surface temperature change. (https://data.giss.nasa.gov/gistemp/) 

## GISS Surface Temperature Analysis (GISTEMP)
The data set that is the center of our analysis requires a baseline period of comparison, where the temperature anomalies, or changes, are compared to a base period. Researchers typically use 30 year periods to review the baseline period and after reviewing several organization (NASA, Univeristy/Research Institutions) this project will use a base period of 1951-1980. This base period is used by NASA in their own research investigation, therefore we will use this as well. Temperatures are rising, Source: NASA ![NASAGif](https://earthobservatory.nasa.gov/ContentWOC/images/globaltemp/agreement_gis_2019.gif) (https://earthobservatory.nasa.gov/world-of-change/global-temperatures)

GISTEMP Team, 2021: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 2021-11-12 at https://data.giss.nasa.gov/gistemp/.

## Other Tools
Our main tool is Paraview and we are using the *NASA Goddard Institute for Space Studies* G.Projector - Map Projections as a resource inside of Paraview. The G.Projector transforms an input map image into any of about 200 global and regional map projections. This is being placed in the pipeline inside of Paraview as an overlay on the data to make the globe look like a map. (https://www.giss.nasa.gov/tools/gprojector/)
