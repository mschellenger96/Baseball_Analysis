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


ba = []
iso = []
babip = []
slg = []
woba = []
xwoba = []
xba = []
hits = []
launch_speed = []
launch_angle = []
spin_rate = []
velocity = []
effective_speed = []
whiffs = []
swings = []
takes = []

totals = dict((name, eval(name)) for name in ['ba', 'iso', 'babip', 'slg', 'woba', 'xwoba', 'xba', 'hits', 'launch_speed', 'launch_angle', 'spin_rate',
	'velocity', 'effective_speed', 'whiffs', 'swings', 'takes'])


for player, statistics in results.items():
	for cat, val in totals.items():
		val.append(float(statistics[cat]))

for total in totals.values():
	total = np.array(total)

print(totals['launch_speed'])


for cat, total in totals.items():
	slope, intercept, r_value, p_value, std_err = stats.linregress(totals['launch_speed'], totals[cat])
	print("r_squared " + cat + ": ", r_value**2)