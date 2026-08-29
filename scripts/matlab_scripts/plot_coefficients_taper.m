% This plots the OpenFOAM simpleFoam run coefficients in order
% to visualize solver convergence.

clear; clc; close all
tapered_data = 'coefficient_taper.dat';

raw = importdata(tapered_data);

if isstruct(raw)
    data = raw.data;
else
    data = raw;
end

time = data(:,1); % 1st column holds time
Cd = data(:,2); % 2nd column holds drag coefficients
Cl = data(:,5); % 5th column holds lift coefficient

ClCd = Cl ./ Cd; % Computation of lift-to-drag ratio

% Plotting

figure('Name','Convergence Proof | Tapered','Color','w','Position',[100 100 800 700]);

subplot(3,1,1);
plot(time, Cl, 'LineWidth', 1.3, 'Color', [0 0.447 0.741]);
ylabel('C_L','Color', 'k');
title('Lift Coefficient Convergence','Color', 'k');
grid on;
ax1 = gca;
ax1.XColor = 'k';
ax1.YColor = 'k';

subplot(3,1,2);
plot(time, Cd, 'LineWidth', 1.3, 'Color', [0.850 0.325 0.098]);
ylabel('C_D','Color', 'k');
title('Drag Coefficient Convergence','Color', 'k');
grid on;
ax2 = gca;
ax2.XColor = 'k';
ax2.YColor = 'k';

subplot(3,1,3);
plot(time, ClCd, 'LineWidth', 1.3, 'Color', [0.466 0.674 0.188]);
xlabel('Iteration / Time','Color', 'k');
ylabel('C_L / C_D', 'Color', 'k');
title('Lift-to-Drag Ratio Convergence','Color', 'k');
grid on;
ax3 = gca;
ax3.XColor = 'k';
ax3.YColor = 'k';

sgtitle('Convergence Proof | Tapered','Color', 'k');