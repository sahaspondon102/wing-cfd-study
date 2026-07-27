# This log will keep track of my progress since the start of the project. Detailed notes will be in theory/ of this repository.

---

## June 12th - June 29th

* Self-directed theoretical study of the following topics:
1. Aerodynamics of Aircraft Flight
2. Wings & its Generation Of Lift
3. The Lift Formula: $Lift= \frac{1}{2} \rho V^2 S C_L$
4. Different Forms Of Drags That Affect Produced Lift
5. How Optimal Flight Speed is Obtained
6. Rectangular, Tapered, Elliptical & Swept-Back Wings
7. Desirable & Undesirable Stall Characteristics
8. Mach as a Unit Of Speed
9. The mathematical relationship: $Glide Ratio = Airspeed/Sink Rate$
10. Axes of Rotation in Flight
11. Stability Of an Aircraft in Flight

*Please note that detailed notes for the theoretical concepts is posted as a pdf*

---

## June 29th - July 6th

* Decided on using the NACA 2412 Airfoil (Airfoil will remain constant; Only planforms will change)
* Familiarized myself with Onshape. Onshape will be used for CAD Modelling in this project.
* For the initial airfoil design, a reference image is shown:

<img width="800" height="295" alt="image" src="https://github.com/user-attachments/assets/e5c93ebf-8016-4986-84d3-02a69115c9fc" />

Sketched a few reference lines in the front plane. We will be using a 200 mm chord length for the wing in this project. The remaining values are in reference to the chord length and the NACA 2412 airfoil.

<img width="506" height="377" alt="image" src="https://github.com/user-attachments/assets/da4751e2-9f5f-4945-ae86-6aead1665500" />

Ran into an issue where I couldn't find a proper .dat to .dxf converter. So I wrote a short script in order to read, plot and generate a .dxf for the NACA 2412 airfoil. The full .py file can be found in /scripts. Final dxf file is also in /cad of this repository and it is scaled to the 200 mm chord we're using for this project.

<img width="800" height="470" alt="image" src="https://github.com/user-attachments/assets/c988a109-5443-42eb-9d09-0ed6f0e6188e" />

Imported the airfoil into Onshape and extruded with #Span (Note that we are using parametric CAD) to create the first rectangular wing. Points were connected with splines in order to ensure a CFD-ready CAD model. CAD files can be found in /cad.

<img width="719" height="356" alt="image" src="https://github.com/user-attachments/assets/01266348-3a90-4172-97d6-57afff7b6e49" />

<img width="719" height="356" alt="image" src="https://github.com/user-attachments/assets/ad26f1da-b81c-45d7-85d9-cd76f260dc46" />

---

## July 7th - July 14th

Drifted off the project due to unavoidable responsibilities & travel

---

## July 15th - July 17th

* Completed a self-directed CFD crash course
* Learned in detail about the pre-processing, solver & post-processing stages
* Navier Stokes Equation & it's discretization
* Computational Domain/Grid Generation
* Convergence and it's relations with Stability & Consistency
* Types of visualizations & analysis of results

*Please note that detailed notes for the theoretical concepts is posted as a pdf*

---

## July 18th - Present

* Started off by completing the pre-processing, running the solver, post-processing & analyzing the airflow using ParaView. I did this on the "pitzDaily" OpenFOAM tutorial in order to get comfortable with Linux commands (I'm using WSL + Ubuntu) & OpenFOAM folder structure.
* Only after a few attempts, I have got the correct airflow visulaization:
<img width="835" height="488" alt="Screenshot 2026-07-21 140954" src="https://github.com/user-attachments/assets/8f1cd6c4-c9fc-4cf8-9bd1-bec945c886ea" />

* Trying to solve my own CFD case before properly learning about it was evidently a very bad idea. Mesh being too coarse, setting addLayers as true causing whatever that is, and an overall mess of a simulation. I've refined the .stl over 10 times and ran the solver over and over again, only to realize I definitely need to learn a lot more before stepping in again and leaving with the same results. Here are snapshots of some of the issues I ran into:

<img width="835" height="488" alt="WhatsApp Image 2026-07-28 at 1 41 23 AM" src="https://github.com/user-attachments/assets/dde106df-9d71-4036-8601-1349bd8977c4" />

<img width="835" height="488" alt="WhatsApp Image 2026-07-28 at 1 41 23 AM (1)" src="https://github.com/user-attachments/assets/55580a8a-8b44-4c01-aa60-37d9519575d2" />

<img width="835" height="488" alt="WhatsApp Image 2026-07-28 at 1 41 23 AM (2)" src="https://github.com/user-attachments/assets/e3da2d40-3287-45b6-9c4f-f90a3d440db9" />

*Pressure contours were somewhat accurate*

<img width="835" height="488" alt="WhatsApp Image 2026-07-28 at 1 41 23 AM (4)" src="https://github.com/user-attachments/assets/5c38d39d-0435-44b4-9a48-98fde77116b4" />

<img width="835" height="488" alt="WhatsApp Image 2026-07-28 at 1 41 23 AM (3)" src="https://github.com/user-attachments/assets/e38216d7-9f18-42e9-87c9-14a2037c99d7" />

---
## July 28th - Present

I've decided to learn Fluid Dynamics & OpenFOAM in intricate detail before my next attempt. This might take a while but I don't see another path forward that will lead to the success of this project.
