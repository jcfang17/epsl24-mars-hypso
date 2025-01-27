# Data and Codes for the paper: Global Comparative Basin Hypsometric Analysis of Earth and Mars: Implications for Early Mars Climate

[Paper](https://doi.org/10.1016/j.epsl.2025.119226)

## Usage

```bash
git clone https://github.com/jcfang17/epsl24-mars-hypso.git
cd epsl24-mars-hypso
```

### Requirements
- numpy
- pandas
- matplotlib
- scipy
- rasterio
- jupyter

## Project Structure

```
├── data/
│   └── data_all_surfaces.csv    # Contains calculated hypsometry parameters for all surfaces
├── examples/
│   ├── hypsometry-demo.ipynb    # Demo of hypsometric curve calculation and metrics
│   ├── box-plot.ipynb          # Recreation of Figure 4 from the paper
│   ├── t-test.ipynb           # Recreation of Table 2 from the paper
│   └── HydroBasin_*.tif       # Example DEM files for demonstration
└── util/
    ├── __init__.py
    └── hypso.py               # Core functions for hypsometric analysis
```

## Core Functionality

The main functionality is provided through the `util.hypso` module. Which is used to calculate all the hypsometric data used in the paper. Key functions include:

- `get_hypso_vector`: Calculate hypsometry vector from DEM array
- `plot_hypso_vector`: Visualize hypsometric curves
- `get_hypso_attributes_from_vector`: Extract hypsometric attributes

## Examples

The repository includes several example notebooks demonstrating different aspects of the analysis:

1. `hypsometry-demo.ipynb`: Demonstrates how to use the core functions to:
   - Load and process DEM data
   - Calculate hypsometric curves
   - Display curves and compute metrics
   - Two example DEMs provided in the examples folder

2. `box-plot.ipynb`: Recreation of Figure 4 from the paper

3. `t-test.ipynb`: Recreates Table 2 from the paper

## Data Description

- `data/data_all_surfaces.csv`: Contains all pre-calculated hypsometry parameters used for plots and statistical tests in the paper. This dataset is used directly by the box-plot and t-test example notebooks.
- Example DEM files in `examples/` directory demonstrate the analysis workflow with real topographic data. Data from HydroBasins with their HYBAS_ID in the filename. The DEMs are void filled and clipped to the extent of the HydroBasin. 
