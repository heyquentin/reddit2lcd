#! /usr/bin/python
import serial
import time
import feedparser

# ---- RSS Feed Parser
d = feedparser.parse('http://www.reddit.com/r/vancouver/new/.rss')
latestpost = d['entries'][0]['title'].encode('utf-8')
#latestpost = "This sentence is exactly two-hundred and forty characters long. It represents the length of a twitter message. Twitter changed the length of their messages from one-hundred and twenty to two-hundred and forty some time ago. Testing 1 2 3 4"
latestpost = "     " + latestpost
chars_int = len(latestpost)
chars_str = str(chars_int)

# ---- Set up the serial connection 
s = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
)

# ---- Initialize array
ary = []

# ---- Add some spaces to the first and last positions in the array

# ---- Character counters
char_count1 = int("0")
char_count2 = int("16")

# ---- Loop counter
loop_counter = int("0")

while char_count2 < chars_int+6:
	ary.append(latestpost[int(char_count1):int(char_count2)])
	char_count1 = char_count1 + 2
	char_count2 = char_count2 + 2

#print ary
#blah = "\n".join(ary)

while loop_counter < 2:
	for each_element in ary:
		time.sleep(0.3)
		s.write(each_element)
#		time.sleep(0.3)
	loop_counter = loop_counter + 1
	print loop_counter
	s.flushInput()
	s.flushOutput()
	time.sleep(1.5)