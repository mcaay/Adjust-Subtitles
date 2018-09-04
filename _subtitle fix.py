# a program that adjusts subtitles by moving them XX.XXX seconds 
# forward or backward

# creates a copy shadow file and writes things into original file
# with normal print() command
import fileinput 

# timedelta is needed to do datetime additions easily
from datetime import datetime, time, timedelta



change = input("move subtitles XX.XXX seconds: ")


# cut the possible minus sign and remember it
minus = False
if change[0] == '-':
	minus = True
	change = change[1:]

change_s = int(change[:2])
change_ms = int(change[3:6])

if minus:
	change_s = - change_s
	change_ms = - change_ms


j = 1

# in this case line is really a line from the file
for line in fileinput.input("source.srt", inplace=True):
	if line == '\n':
		j = 0

	if j == 2:
		time_1 = datetime(2000, 1, 1, int(line[:2]), int(line[3:5]), int(line[6:8]), 1000*int(line[9:12]) )
		time_2 = datetime(2000, 1, 1, int(line[17:19]), int(line[20:22]), int(line[23:25]), 1000*int(line[26:29]) )
		
		time_1 = time_1 + timedelta(seconds=change_s, milliseconds=change_ms)
		time_2 = time_2 + timedelta(seconds=change_s, milliseconds=change_ms)
		
		time_1 = time_1.strftime('%H:%M:%S,%f')[:-3]
		time_2 = time_2.strftime('%H:%M:%S,%f')[:-3]

		print(time_1, '-->', time_2)
	else:
		print(line, end='')
	
	j += 1



