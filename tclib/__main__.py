import sys
from . import *
if sys.argv[1]=='download':
	print(sys.argv)
	if len(sys.argv)==4:
		url,path=ssy.argv[2:]
		download(url,path)
	else:
		url,path,check=sys.argv[2]
		download(url,path,check)
