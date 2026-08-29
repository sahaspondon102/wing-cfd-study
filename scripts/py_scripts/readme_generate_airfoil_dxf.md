### Airfoil to DXF converter

This script automates the preprocessing of the NACA 2412 airfoil coordinate files for CAD modelling. This script was created as a workaround to a project obstacle where I couldn't find any proper open-source .dat to .dxf converters.

**Capabilities**
- Reads NACA `.dat` airfoil coordinate files
- Visualizes the airfoil using Matplotlib
- Scales the airfoil to a user-defined chord length (200 mm in my case)
- Exports a CAD-ready `.dxf` file for use in Onshape

This utility supports the project workflow:

`.dat` → Python → `.dxf` → Onshape
