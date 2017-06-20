import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as patches


data_file = "/Users/mitchellschellenger/baseball_Analysis/statcast_data/mookie_betts_data.csv"


results = {}
with open(data_file, 'r') as data_csv:
	raw_data = csv.DictReader(data_csv)
	for row in raw_data:
		results[row['sv_id']] = row

#finds the hoe often a player puts a given pitch type in the strike zone in play
def find_ipp_vs_pitch(results):
	ipp_dict = {}
	for _id, vals in results.items():
		pitch_type = vals['pitch_type']
		desc = vals['description']
		events = vals['events']
		if pitch_type in ipp_dict:
			ipp_dict[pitch_type]['tot'] += 1
			if desc != "ball" and events != 'null' and events != 'walk':
				ipp_dict[pitch_type]['pos'] += 1
		else:
			ipp_dict[pitch_type] = {}
			ipp_dict[pitch_type]['tot'] = 1
			ipp_dict[pitch_type]['pos'] = 0
			if desc != "ball" and events != 'null' and events != 'walk':
				ipp_dict[pitch_type]['pos'] += 1
	for pitch_type, vals in ipp_dict.items():
		print("IPP vs " + pitch_type + ": " + str(vals['pos']/vals['tot']))
	return ipp_dict

ipp_dict = find_ipp_vs_pitch(results)
print(ipp_dict)

def plot_heat_zones(results):
	labelColor = {'single' : 'g', 'double' : 'g', 'triple' : 'g', 'home_run' : 'g'}

	fig = plt.figure(figsize=(5, 3), dpi=300)

	ax1 = fig.add_subplot(2, 2, 1)
	ax1.add_patch(patches.Rectangle((-(17/24), 1.5), (17/12), 2, fill=False))
	ax1.set_xlim(-4, 4)
	ax1.set_ylim(0, 7)
	ax1.plot()

	ax1 = fig.add_subplot(2, 2, 2)
	ax1.add_patch(patches.Rectangle((-(17/24), 1.5), (17/12), 2, fill=False))
	ax1.set_xlim(-4, 4)
	ax1.set_ylim(0, 7)
	ax1.plot()

plot_heat_zones(results)
plt.show()