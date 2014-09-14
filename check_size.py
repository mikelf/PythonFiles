# -*- coding: utf-8 -*-
import os
import sys
print len(sys.argv)
if len(sys.argv) == 2:
	b = os.path.getsize(sys.argv[1])
	print b
else:
	print "use check_size file_to_tets"

