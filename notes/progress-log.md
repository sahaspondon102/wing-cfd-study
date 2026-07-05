# This log will keep track of my progress since the start of the project. Detailed notes will be in theory/ of this repository.
---
## June 12th - June 29th
* Self-directed theoritical study of the following topics:
1. Aerodynamics of Aircraft Flight
2. Wings & its Generation Of Lift
3. The Lift Formula: $Lift= \frac{1}{2} \rho V^2 S C_L$
4. Different Forms Of Drags That Affect Produced Lift
5. How Optimal Flight Speed is Obtained
6. Rectangular, Tapered, Elliptical & Swept-Back Wings
7. Desirable & Undesirable Stall Characterisitcs
8. Mach as an Unit Of Speed
9. The mathematical relationship: $Glide Ratio = Airspeed/Sink Rate$
10. Axes of Rotation in Flight
11. Stability Of an Aircraft in Flight

*Please note that detailed notes for the theoritical concepts will be posted on the theory/ folder*
___
## June 29th - Present
* Decided on using the NACA 2412 Airfoil (Airfoil will remain constant; Only planforms will change)
* Familiatized myslef with Onshape. Onshape will be used for CAD Modelling in this project.
* For the initial airfoil design, a reference image is shown:

<img width="800" height="295" alt="image" src="https://github.com/user-attachments/assets/e5c93ebf-8016-4986-84d3-02a69115c9fc" /> <br>

Sketched a few reference lines in the front plane. We will be using a 200 mm chord lenght for the wing in this project. The remaining values are in reference to the chord lenght and the NACA 2412 airfoil. <br>
<img width="506" height="377" alt="image" src="https://github.com/user-attachments/assets/da4751e2-9f5f-4945-ae86-6aead1665500" /> <br>

Ran into a issue where I couldn't find a proper .dat to .dxf converter. So I wrote a short script in order to read, plot and generate a .dxf for the NACA 2412 airfoil. The full .py file can be found in /scripts. Final dxf file is also in /cad of this repository and it is scaled to the 200 mm chord we're using for this project. <br>

<img width="800" height="469.5" alt="image" src="https://github.com/user-attachments/assets/c988a109-5443-42eb-9d09-0ed6f0e6188e" />

Imported the airofil into Onshape and extruded with #Span (Note that we are using parametric CAD) to create the first rectangular wing. Points were connected with splines in order to ensure a CFD-ready CAD model. CAD files can be found in /cad.
  
<img width="958" height="475" alt="image" src="https://github.com/user-attachments/assets/01266348-3a90-4172-97d6-57afff7b6e49" />

<img width="958" height="475" alt="image" src="https://github.com/user-attachments/assets/ad26f1da-b81c-45d7-85d9-cd76f260dc46" />


