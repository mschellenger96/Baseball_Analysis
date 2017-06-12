import csv
import numpy as np
from scipy import stats

results_file = "/Users/mitchellschellenger/Baseball_Analysis/statcast_data/r_vs_r_results.csv"
results = {}
with open(results_file, 'r') as results_csv:
	raw_results = csv.DictReader(results_csv)
	for row in raw_results:
		results[row['player_name']] = row

categories = []
for cat in row.keys():
	categories.append(cat)

babip = []
exit_velo = []
ba = []

for player, statistics in results.items():
	babip.append(float(statistics['babip']))
	exit_velo.append(float(statistics['launch_speed']))
	ba.append(float(statistics['ba']))

babip = np.array(babip)
exit_velo = np.array(exit_velo)

slope, intercept, r_value, p_value, std_err = stats.linregress(exit_velo, ba)

print("r_squared: ", r_value**2)