Major League Baseball Analysis Project
---------------------------------------

Following is a description of my analysis of results from the 2016 season.
App1 was a mini "project" to answer a question I had for a long time: does how hard you hit the ball on average correlate to your batting average? The purpose of this program was more to familiarize myself with some of the csv import tools and reading in data. App2 is the larger and more detailed project.


App1 (aka HelloWorlding):
	
	Data is from right handed hitters vs right handed pitchers with min. 200 PA from the 2016 season.
	- Does exit velocity correlate with other outcome statistics?
		r_squared woba:  0.193797297198
		r_squared xwoba:  0.436675012661
		r_squared swings:  0.045913199041
		r_squared spin_rate:  0.00196997773928
		r_squared babip:  0.017611788824
		r_squared velocity:  0.005777216046
		r_squared whiffs:  0.163971763906
		r_squared takes:  0.102800689171
		r_squared ba:  0.0291123323927
		r_squared iso:  0.298195416685
		r_squared hits:  0.0641473647931
		r_squared launch_speed:  1.0
		r_squared launch_angle:  0.0125656268517
		r_squared xba:  0.143350021382
		r_squared effective_speed:  0.00905028893247
		r_squared slg:  0.28470080813

	Exit Velocity is weakly correlated with slugging and xba, which makes intuitive sense, interesting that it is not strongly correlated with any other stats.


App2 (long term project):

	- Use statcast data to find good hitting matchups.
		- Given a player, find the pitches he has the most succes with. (what stat to use? hit probability?)
		- Given the pitch with most succes, find a pitcher with pitch most similar to that.
				- Need to develop a pitch similarity score.
	- Flip to find pitcher matchups. 
		- Given a plater, find the type of pitch that player has the least success with.
		- Find a pitcher with the most similar type of pitch.