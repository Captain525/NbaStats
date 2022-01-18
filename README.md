

PARAMETERS:
The NBA's Game ID, 0021400001, is a 10-digit code: XXXYYGGGGG, 
where XXX refers to a season prefix, 
YY is the season year (e.g. 14 for 2014-15), 
and GGGGG refers to the game number (1-1230 for a full 30-team regular season).

season prefixes: 001 preseason, 002 regular season, 003 all star, 004 post season. 


EXPECTING VALUE JSON DECODE ERROR - means that something you inputted was null, so it couldn't get a response
from the nba api. 

FINDING GAMES - used in videoPBP 

https://github.com/swar/nba_api/blob/master/docs/examples/Finding%20Games.ipynb






PLAY BY PLAY DATA
Event num - a count of events approximately, but goes above indices. 
EVENTMSGTYPE - says what TYPE of action happens

1- shot make
2- shot miss
3- free throw
4 - rebound. 
5- turnover
6 - foul
7- tecch????
8- substitution
9-timeout
10 - beginning of game?
11 - end of game?
12  - start of period. 
13 - end of period. 
18 -support ruling



EVENTMSGACTIONTYPE:
0 - when a rebound or something. 
79(with 1 three pointer) goes in. 
1 - with 1 shot attempt - went in
1- also a bad pass turnover/steal. 
5 - layup went in. 
 12 - free throw second
 29 - shooting block foul with 6. 
 87 - dunk
 0 - substitution. 
 1- midrange miss
 1- short miss. 
 2 - shooting foul
 79 - pull up ump shot goes in. 
 always 0 for substitution
 97 tip layup shot. 
 57 - driving hook shot. 
 72 miss putback layup. 
 1- miss jump shot. 
 
 
 
 stats.nba.com/stats/{endpoint}/?{params}
 