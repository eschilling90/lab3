from itertools import izip
from sets import Set

# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
	site_dict = dict()
	for site, user in izip(site_list, user_list):
		user_set = set()
		if site in site_dict:
			user_set = site_dict[site]
		user_set.add(user)
		site_dict[site] = user_set
	max_site1 = ""
	max_site2 = ""
	max_count = 0
	for site1 in site_dict:
		for site2 in site_dict:
			if (site1 != site2):
				user_set1 = site_dict[site1]
				user_set2 = site_dict[site2]
				test_count = len(user_set1.intersection(user_set2))
				if test_count > max_count:
					max_count = test_count
					if site1 < site2:
						max_site1 = site1
						max_site2 = site2
					else:
						max_site2 = site1
						max_site1 = site2
		
	# Returned string pair should be ordered by dictionary order
	# I.e., if the highest affinity pair is "foo" and "bar"
	# return ("bar", "foo"). 
	#print (max_site1, max_site2)
	return (max_site1, max_site2)
