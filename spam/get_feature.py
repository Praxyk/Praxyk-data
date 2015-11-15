import os
import sys
import getopt
import csv
if(len(sys.argv) < 2):
	raise RuntimeError("Filename required")
	exit()

#load feature list
features = []
try:
	features_file = open("features.txt", "r")
except IOError:
	raise RuntimeError("features.txt missing.")
	exit()
for line in features_file:
	features.append(line.strip())



for filename in sys.argv[1:]:
	#read file
	try:
		test_file = open(filename, "r").read()
	except IOError:
		continue
	test_entry = []
	for word in features:
	#	if word in test_file:
	#		test_entry.append(1)
	#	else:
	#		test_entry.append(0)
		test_entry.append(test_file.count(word))
	with open(filename+".csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows([test_entry])
