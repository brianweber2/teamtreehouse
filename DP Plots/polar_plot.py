# This script reads an excel file and prints a polar plot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Read data from file
data = np.genfromtxt('mrts_test.csv', delimiter=',', skip_header=3, names=['heading', 'Hs', 'Vw'])

# Create theta data for limiting Hs and Vw
total_angles = int(raw_input("\nHow many total angles were analyzed?"))
increment = 360/total_angles
headings_analyzed = np.radians(np.arange(0, 370, increment))

# Generate data for the limiting Hs and Vw
limiting_Hs = float(raw_input("\nWhat is the limiting significant wave height (Hs) in meters?"))
limiting_Vw = float(raw_input("\nWhat is the limiting wind speed (Vw) in meters/second?"))
plot_Hs = limiting_Hs * np.ones(len(headings_analyzed))
plot_Vw = limiting_Vw * np.ones(len(headings_analyzed))

# Setup plot for Hs values
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, polar=True)
ax1.plot(np.radians(data['heading']), data['Hs'], color='b', lw=2, label='Case 3-I (no tug)')
ax1.set_title("Jascon 18 Heading v.s. Significant Wave Height (Dry Pipeline)", fontsize=20, y=1.08)
ax1.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax1.set_ylim(0,6)
ax1.set_theta_zero_location('S')
ax1.set_theta_direction(1)
ax1.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m'))
ax1.set_rgrids([0.1,1,2,3,4,5,6], angle=170.)
# Plot limiting Hs value
plt.plot(headings_analyzed, plot_Hs, color='r', lw=2, label='Limiting Hs (2.5 m)')
plt.legend(bbox_to_anchor=(0.35,0.12), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()

# Setup plot for Vw values
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, polar=True)
ax2.plot(np.radians(data['heading']), data['Vw'], color='b', lw=2, label='Case 3-I (no tug)')
ax2.set_title("Jascon 18 Heading v.s. Wind Speed (Dry Pipeline)", fontsize=20, y=1.08)
ax2.set_xlabel('Vessel Heading [deg]', fontsize=15)
ax2.set_ylim(0,20)
ax2.set_theta_zero_location('S')
ax2.set_theta_direction(1)
ax2.set_thetagrids(np.arange(0,360,30), frac=1.1)
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d m/s'))
ax1.set_rgrids([0.1,5,10,15,20], angle=170.)
# Plot limiting Hs value
plt.plot(headings_analyzed, plot_Vw, color='r', lw=2, label='Limiting Vw (15.44 m/s)')

# Show plot
plt.legend(bbox_to_anchor=(0.35,0.12), bbox_transform=plt.gcf().transFigure)
plt.tight_layout()
plt.show()


