#coding=utf-8
import re 
# import os
import sys
import json
import urllib
import datetime
# def dirlist(path, allfile):  
# 	filelist =  os.listdir(path)
# 	for filename in filelist:  
# 		filepath = os.path.join(path, filename)  
# 		if os.path.isdir(filepath):
# 			dirlist(filepath, allfile)
# 		else:  
# 			allfile.append(filepath) 
# 	return allfile




url = ("http://58.82.245.249/api.php?action=Error&pass=11","http://api.guangdong666.com/api.php?action=Error&pass=11")
date = len(sys.argv)>1 and sys.argv[1] or datetime.datetime.now().strftime('%Y-%m-%d')
md5js= open("md5Paths.json")
ff = md5js.read()
md5js.close()
md5data = json.loads(ff)
print "date:  "+date
page = urllib.urlopen(url[1])
htmlcode = page.read()
for key in md5data:
	print key + "_____+++++++++++_____"+md5data[key]
	htmlcode = htmlcode.replace(key,md5data[key])
# print htmlcode
r1 = re.compile("\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\][\s\S]*?(?=<br>)")
alldata =r1.findall(htmlcode) 

if len(alldata)>0:
	for i in alldata:
		print "_______________________________________"+i
