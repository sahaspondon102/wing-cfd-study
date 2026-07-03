#plot_airfoil.py
# Desired chord length (mm)
CHORD = 200
# import necessary libraries for dxf conversion
import ezdxf
# Path to airfoil data file
import os
# Gets the directory where plot_airfoil.py lives, then goes up one level to the root
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "..", "airfoil", "naca2412.dat")
#Open the file
with open(filename, 'r') as file:
    lines = file.readlines()
#Print every line
#for line in lines:
 #   print(line)
import matplotlib.pyplot as plt
x = []
y = []
with open(filename, 'r') as file:
    lines = file.readlines()
for line in lines[1:]: #Skip the NACA 2412 header line
    values = line.split()
    if len(values) == 2:
        x_coord = float(values[0]) * CHORD
        y_coord = float(values[1]) * CHORD
        x.append(float(x_coord))
        y.append(float(y_coord))
plt.figure(figsize=(8, 3))
plt.plot(x, y)

plt.axis("equal")
plt.grid(True)

plt.xlabel("x")
plt.ylabel("y")
plt.title("NACA 2412 Airfoil")

# plt.show()
# Remove the hashtag from the line above to plot the airfoil. The line is commented out to avoid opening a plot window when running the script in a non-interactive environment.
# ---
# Export airfoil to dxf file
CHORD = 200.0 #mm
#Scale coordinates to desired chord length
scaled_x = [coord * CHORD for coord in x]
scaled_y = [coord * CHORD for coord in y]

doc = ezdxf.new()
msp = doc.modelspace()
#Add polyline
msp.add_lwpolyline(list(zip(scaled_x, scaled_y)), close=True)
#Save file
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, "..", "cad", "naca2412_200mm.dxf")

doc.saveas(output_file)

print(f"Saved to: {output_file}")