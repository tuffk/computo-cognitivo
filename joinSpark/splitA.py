def split_fileA(line):
	# split the input line in word and count on the comma
	t = line.split(",")
	# turn the count to an integer  
	word = t[0]
	count = int(t[1])
	return (word, count)


#sc.setLogLevel("ERROR")


def split_fileB(line):
# split the input line into word, date and count_string
	t = line.split(",")
	worddate = t[0]
	count_string = t[1]
	t = worddate.split(" ")
	word = t[1]
	date = t[0]
	return (word, date + " " + count_string)

#out put for actor
# (u'actor', (u'Feb-22 3', 22))

"""
output del join
[(u'able', (u'Jan-01 5', 991)),
 (u'able', (u'Apr-04 13', 991)),
 (u'able', (u'Dec-15 100', 991)),
 (u'burger', (u'Feb-23 5', 15)),
 (u'burger', (u'Mar-08 2', 15)),
 (u'about', (u'Feb-02 3', 11)),
 (u'about', (u'Mar-03 8', 11)),
 (u'actor', (u'Feb-22 3', 22))]
"""
