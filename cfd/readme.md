### Fluid Simulation

The CFD simulation for this study was carried out using the open-source software OpenFOAM.

<img width="297" height="187.2" alt="velocity_contours" src="https://github.com/user-attachments/assets/9f7d04bb-3415-4b08-ac14-617b9060313f" />


Physics: Incompressible, steady-state (simpleFoam), k-omega SST turbulence model, & constant fluid properties.

* The coefficients_log folder contains the coefficients for every iteration of the solver as a .dat file. It also contains convergence plots that were generated using MATLAB scripts.
The scripts can be found in */scripts/matlab_scripts*
* The openFoam folder contains the OpenFOAM file configurations. **Run order: blockMesh -> surfaceFeatureExtract -> snappyHexMesh -overwite -> checkMesh -> simpleFoam**
* The visualizations_paraview folder contains all the graphical post-processing data for all three wing cases
