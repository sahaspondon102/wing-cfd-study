# Comparative Aerodynamic Analysis of Wing Planforms

### Objective & Current Standing

This is a pre-university project + study designed to be a learning experience for an end-to-end workflow in my field of specialization & interest. This is a comparative RANS study of planform effects on finite-wing aerodynamics for three different planforms following the same airfoil profile (NACA 2412). The workflow for the project is demonstrated at the end of this readme in the form of a checklist. The *notes/* folder contains a documentation pdf which includes intricate technical details of the project.

### Repository Structure
```text
wing-cfd-study/
├── airfoil/         # .dat files for NACA 2412, .dxf files for all dimensions
├── cad/             # .stl & .step files of all designs, marked design drawings
├── cfd/             # OpenFOAM file configurations, folder structure & post-processed visuals
├── notes/           # Additional notes & the final PDF documentation
├── scripts/         # All Python & MATLAB scripts used in this project
└── readme.md        # This file
```

*Last Updated: August 26th, 2026*

### Software Stack
<img width="172.8" height="97.2" alt="openfoam logo" src="https://github.com/user-attachments/assets/1032c980-45f2-4c49-9fbf-6761effc7bc1" />
<img width="97.2" height="97.2" alt="onshape logo" src="https://github.com/user-attachments/assets/20f451c6-619a-41e4-aada-8fe2c11e666a" />
<img width="97.2" height="97.2" alt="python logo" src="https://github.com/user-attachments/assets/704de866-b7b2-4c09-bddb-d3181fd07601" />
<img width="172.8" height="97.2" alt="matlab logo" src="https://github.com/user-attachments/assets/c8015ec6-da89-4b60-8523-6f7a329225b2" />



### Wing Planforms To Be Investigated

- Rectangular Wings
<img width="480" height="320" alt="rectangular" src="https://github.com/user-attachments/assets/d802ae87-f7fa-42be-9a40-7d3c697d101c" />

- Tapered Wings
<img width="480" height="320" alt="tapered" src="https://github.com/user-attachments/assets/a4efa9bd-8924-461b-8c2c-581ba67839a3" />

- Constant Chord Swept Back Wings
<img width="480" height="320" alt="constant_chord_swept_back" src="https://github.com/user-attachments/assets/e9b3192e-8eb2-4f05-88ba-eca0467cc3e4" />

*These are reference images only. They do not represent the model used in this project accurately (check cad/ for design drawings and OnShape screenshots), but is rather meant to provide a visual cue concerning the real-world application of the wing planforms investigated in this study.*

### Status

Project Started: June 2026
Project Completed: August 2026

Phase Tracking:
- [x] Theory
- [x] CAD Modelling
- [x] CFD Simulation *(In progress)*
- [x] Post-Processing
- [x] Report Writing
