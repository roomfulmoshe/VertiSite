# Transit / Demand Data Processing (CSE6242)

This repository contains scripts and notebooks used to process, join, and visualize New York City spatial and trip-demand datasets (ACS, LODES, TLC, taxi zones). The code was developed for a class project and includes data preparation, neighbor generation, demand aggregation, and map visualization outputs.

**Contents**

- `ACS_demographics_tract_level.py` / `.ipynb` — Clean and aggregate ACS demographics at census tract level.
- `GenerateNeighborsCSVJSON.py` / `.ipynb` — Generate neighbor lists and neighbor GeoJSON/CSV for tracts.
- `geospatial_join.py` — Helper for spatial joins between zones and tracts.
- `LODES_2020_2022_OD_DEMAND.py` / `.ipynb` — Process LODES OD demand and aggregate to zones/tracts.
- `TLC_2020_2024_OD_DEMAND.py` / `.ipynb` — Process taxi/for-hire vehicle OD demand (TLC dataset).
- `UniversalDemand.py` / `.ipynb` — Produce a universal demand mapping across sources.
- `add_distance_to_demand_map.py` — Add distance metrics to demand map outputs.
- `GenerateNeighborsCSVJSON.ipynb` — Jupyter workflow for neighbor generation.
- `visualize_greedy.html` & `zones_tracts.html` — Visual outputs for quick inspection.

Data folders

- `nyc_tracts/` — Census tract shapefiles and GeoJSON (`nyc_tracts.json`, shapefiles).
- `taxi_zones/` — Taxi zone shapefiles and GeoJSON.
- `images/` — Supporting images used in notebooks or documentation.
- `output/` — Generated CSV/JSON outputs from scripts (examples below).

Getting started
-----------------

Prerequisites

- macOS or Linux (Windows is possible but commands here assume zsh/bash).
- Python 3.11
- `requirements.txt` lists Python package dependencies.

Using the included virtual environment (recommended)

1. Activate your virtualenv

2. (Optional) If you prefer creating your own environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Install dependencies

```bash
# with the active venv
pip install -r requirements.txt
```

Running notebooks

Start JupyterLab or Notebook and open the `.ipynb` files:

```bash
jupyter notebook
```

Running the Python scripts

Most scripts can be run directly from the command line. Examples:

```bash
# Clean ACS demographics
python ACS_demographics_tract_level.py

# Generate neighbor CSV/JSON
python GenerateNeighborsCSVJSON.py

# Process LODES OD demand
python LODES_2020_2022_OD_DEMAND.py

# Process TLC/Taxi OD demand
python TLC_2020_2024_OD_DEMAND.py

# Create universal demand map
python UniversalDemand.py
``

Outputs
--------

Produced files appear in `output/`. Notable outputs:

- `nyc_census_tract_demographics.csv` — cleaned ACS demographics.
- `nyc_tract_neighbors_1mile.csv` / `.json` — neighbor lists and neighbor GeoJSON.
- `OD_demand_LODES.csv` / `OD_demand_LODES_nonneighbors.csv` — LODES demand outputs.
- `OD_demand_TLC.csv` / `OD_demand_TLC_nonneighbors.csv` — TLC demand outputs.
- `Universal_Demand_Map.csv` — combined demand map.

Developer notes
---------------

- The repository includes a pre-built virtualenv at `team10project/`. Use it for reproducibility, or recreate an environment locally.
- Spatial files live in `nyc_tracts/` and `taxi_zones/`. These include shapefiles and GeoJSON used for joins.
- Many notebooks rely on interactive plotting (Folium, etc.) and may open HTML outputs in `visualize_greedy.html`.

Troubleshooting
---------------

- If you hit package errors, confirm your active Python interpreter and reinstall from `requirements.txt`.
- If a script cannot find input shapefiles, confirm you are running from the `code/` directory and that `nyc_tracts/` and `taxi_zones/` directories are present.

Contributing
-------------

- Make improvements via pull requests or branches. Keep changes focused and include tests/notebook examples where helpful.
- If you add large or external datasets, do not commit them to the repo—store them externally and document how to fetch them.

Contact / Authors
------------------

Acknowledgements
-----------------
Developed as part of Georgia Tech CSE6242 course work.
