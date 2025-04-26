# InfraMeth Dashboard - Chicago

## Project Overview
This project visualizes methane emissions alongside critical infrastructure in the Chicago metropolitan area using GIS (Geographic Information Systems) tools.  
The interactive map provides insights into the spatial relationship between methane emissions and schools, pipelines, power plants, and industrial facilities.

The goal is to support environmental monitoring, infrastructure risk assessment, and urban planning.

---

## Demo
🚀 **Live Demo**: [Coming soon / or your AWS link]

---

## Data Sources
- **Emissions**: [EDF Methane LeakMap](https://www.edf.org/climate/methane-leak-map)
- **Facilities (Industrial Sites)**: [EPA TRI Facilities for Chicago](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files)
- **Power Plants**: [ArcGIS Hub – Power Plants in the U.S.](https://hub.arcgis.com/datasets/arcgis-content::power-plants-in-the-u-s-/about)
- **Pipelines**: [U.S. EIA Natural Gas Pipelines](https://atlas.eia.gov/datasets/eia::natural-gas-interstate-and-intrastate-pipelines/about)
- **School Districts**: [ArcGIS Hub – School District Boundaries](https://hub.arcgis.com/datasets/arcgis-content::school-district-boundaries/about)

---

## Technologies Used
- **GIS Tools**: GeoPandas, Folium, Shapely
- **Web Framework**: Flask
- **Containerization**: Docker
- **Deployment**: AWS Fargate
- **Concepts**: Spatial joins, Coordinate projections, Interactive GIS mapping

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
