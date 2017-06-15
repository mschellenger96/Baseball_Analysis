import csv
import numpy as np
from scipy import stats


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
		if pitch_type in ipp_dict:
			ipp_dict[pitch_type]['tot'] += 1
			if desc != "ball":
				ipp_dict[pitch_type]['pos'] += 1
		else:
			ipp_dict[pitch_type] = {}
			ipp_dict[pitch_type]['tot'] = 1
			ipp_dict[pitch_type]['pos'] = 0
			if desc != "ball":
				ipp_dict[pitch_type]['pos'] += 1
	for pitch_type, vals in ipp_dict.items():
		print("IPP vs " + pitch_type + ": " + str(vals['pos']/vals['tot']))

find_ipp_vs_pitch(results)