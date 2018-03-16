#! /usr/bin/python
import serial
import time
import feedparser

# ---- RSS Feed Parser
d = feedparser.parse('http://www.reddit.com/r/vancouver/new/.rss')
latestpost = d['entries'][0]['title'].encode('utf-8')
chars_int = len(latestpost)
chars_str = str(chars_int)

# ---- Character counters
char_count1 = int("0")
char_count2 = int("16")

# ---- Output to serial connection (Arduino) 
s = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)
s.close()
time.sleep(2)    #wait for the Serial to initialize

if chars_int > 16:
	
	s.open()
	time.sleep(2)
	
	while char_count2 < chars_int+4:
		s.write(latestpost[int(char_count1):int(char_count2)])
#		print char_count1, char_count2
		char_count1 = char_count1 + 2
		char_count2 = char_count2 + 2
		time.sleep(0.35)
		
	print "----- Diagnostic Information -----"
	print "Characters: " + chars_str
	print "Serial Information: " + str(s)
	s.close()
	print "Serial port open: " + str(s.is_open)

else:
	s.open()
	s.write(latestpost[0:16])
	print "----- Diagnostic Information -----"
	print "Characters: " + chars_str
	print "Serial Information: " + str(s)
	s.close()
	print "Serial port open: " + str(s.is_open)






	
	
	
	
	
	

	
	
	
	
	
	

#s.write('latestpost')

'''
while True:
    str = raw_input('Enter text: ')
    str = str.strip()
    if str == 'exit' :
        break
    s.write(str)
'''
