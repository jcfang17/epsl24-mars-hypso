# epsl24-mars-hypso

This repository contains data and code for analyzing hypsometric curves of Martian and terrestrial surfaces. The analysis includes tools for calculating hypsometry parameters and performing statistical comparisons between different surfaces.

## Usage

```bash
git clone https://github.com/yourusername/epsl24-mars-hypso.git
cd epsl24-mars-hypso
```

## Project Structure

```
├── data/
│   └── data_all_surfaces.csv    # Contains calculated hypsometry parameters for all surfaces
├── examples/
│   ├── demo.ipynb              # Jupyter notebook demonstrating usage
│   └── HydroBasin_*.tif       # Example DEM files for demonstration
└── util/
    ├── __init__.py
    └── hypso.py               # Core functions for hypsometric analysis
```

## Usage

The main functionality is provided through the `util.hypso` module, which includes:

- `get_hypso_vector`: Calculate hypsometry vector from DEM array
- `plot_hypso_vector`: Visualize hypsometric curves
- `get_hypso_attributes_from_vector`: Extract hypsometric attributes

See the `examples/demo.ipynb` notebook for detailed usage examples.

## Data Description

- `data/data_all_surfaces.csv`: Contains all calculated hypsometry parameters used for plots and statistical tests in the paper.
- Example DEM files in `examples/` directory demonstrate the analysis workflow with real topographic data. Data from HydroBasins with their HYBAS_ID in the filename. The DEMs are void filled and clipped to the extent of the HydroBasin. 
