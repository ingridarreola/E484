# E484

Repo for the class E484 - Scientific Visualization, for the final project


## Project Purpose
Many different climate model simulations suggest that our planet’s average temperature could
be between 2 and 9.7°F (1.1 to 5.4°C) warmer in 2100 than it is today. Understanding the
geographic and historic impacts of climate change will help to give context to this problem in
order to improve the outcomes based on historic data and simulations. Our team would like to
explore this area of science due to the wide availability of data across time, by location, and
other metrics related to the changing climate. Metrics related to climate change are tracked by
several government agencies and various institutions.

The main purpose of this scientific visualization project will be to communicate the science of
climate change to the general public. Specifically, a non-expert audience who has enough data
literacy to explore stories typically covered by science journalism. News organizations are
covering these topics more, and the project purpose would be to educate about a specific metric that highlights climate change. The impact of climate change is
a topic that our team finds very interesting and it has a growing impact on our environment and
daily lives.


## Data Source and Proposed Visualization Solution
Our team will be using data from NASA, from the Goddard Institute for Space Studies, and
using the GISS Surface Temperature Analysis data sets. This institution has data on surface
temperate that spans across several years.

This project uses data from the *NASA Goddard Institute for Space Studies* and we are analyzing the *Land-Ocean Temperature Index, ERSSTv5, 1200km smoothing* data to look at surface air temperature anomaly data. This data is an estimate of global surface temperature change. (https://data.giss.nasa.gov/gistemp/) 

This data set looks at average temperature (Celsius) over an average period and time relative to a
base period. The trends data sets look at temperature change (Celsius) over an average period
of time based on local trends. The data has mean temperature, latitude and longitude to
produce a geographic representation.

We are interested at looking at the change over time and we may need to combine several
years worth of information inside of Paraview. The file size for a netCDF, for a year of data, is
about 70kB. We would be interested in doing an analysis of several years/decades. We are also
interested in an analysis of both Trends and Anomalies and will need to see how these are
combined inside of Paraview.

## GISS Surface Temperature Analysis (GISTEMP)
The data set that is the center of our analysis requires a baseline period of comparison, where the temperature anomalies, or changes, are compared to a base period. Researchers typically use 30 year periods to review the baseline period and after reviewing several organization (NASA, Univeristy/Research Institutions) this project will use a base period of 1951-1980. This base period is used by NASA in their own research investigation, therefore we will use this as well. Temperatures are rising, Source: NASA ![NASAGif](https://earthobservatory.nasa.gov/ContentWOC/images/globaltemp/agreement_gis_2019.gif) (https://earthobservatory.nasa.gov/world-of-change/global-temperatures)

GISTEMP Team, 2021: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 2021-11-12 at https://data.giss.nasa.gov/gistemp/.

## Other Tools
Our main tool is Paraview and we are using the *NASA Goddard Institute for Space Studies* G.Projector - Map Projections as a resource inside of Paraview. The G.Projector transforms an input map image into any of about 200 global and regional map projections. This is being placed in the pipeline inside of Paraview as an overlay on the data to make the globe look like a map. (https://www.giss.nasa.gov/tools/gprojector/)

## Project Timeline
| Date | Task/Goal |
| --- | --- |
| Tuesday 11/2 | Verify tools & data sources (Cal) |
| Wednesday 11/3 | Data sources at office hours (Ingrid) & Review full project proposal before turning in the final version (Cal & Ingrid) |
| Thursday 11/4 | Follow-up questions after class (Cal) |
| Tuesday 11/9 | Work one data set through the complete pipeline & follow up with classes after class (Cal & Ingrid) |
| Wednesday 11/10 | Open Questions about project at Office Hours (Ingrid) |
| Thursday 11/11 | Look at data set in Paraview (Cal & Ingrid) |
| Saturday 11/13 | Review Midpoint Demonstration (Cal & Ingrid) |
| Monday 11/15 | Review Midpoint Demonstration (Cal & Ingrid) |
| Thursday 11/18 | Midpoint Presentation (Cal & Ingrid) |
| Saturday 11/20 | Presentation Debrief & follow up on open project tasks (Cal & Ingrid) |
| Saturday 11/27 | Follow up on open tasks & plan for the following week tasks (Cal & Ingrid) |
| Monday 11/29 | Review final project details & open tasks (Cal & Ingrid) |
| Tuesday 11/30 | Follow up on open tasks & question about Paraview after class (Cal & Ingrid) |
| Wednesday 12/1 | Review Python annotation filter in Paraview in global data & usa data (Cal & Ingrid) |
| Thursday 12/2 | Review global view after class, Ingrid to review geoPandas, Cal to polish look inside of Paraview (Cal & Ingrid) |
| Friday 12/3 | Ingrid to review global emissions data in Jupyter Notebook, Cal to review Paraview output (Cal & Ingrid) |
| Saturday 12/4 | Ingrid to create an output that can be fed into Mapbox, Cal to export time step as animations from Paraview (Cal & Ingrid) |
| Sunday 12/5 | Review final project details & open tasks (Cal & Ingrid) |
| Monday 12/6 | Ingrid to be in Mapbox looking at Storytelling map (Cal & Ingrid) |
| Tuesday 12/7 | Final countdown, reviewing what is plausible to turn in for the final presentation (Cal & Ingrid) |
| Wednesday 12/8 | Final presentation and dividing up the talking points at the CIB (Cal & Ingrid) |
| Thursday 12/9 | Final Presentation (Cal & Ingrid) |