#coding=utf-8
import sys
import os
import copy
def dump(obj,str):
	print(str + " = " + obj)

def DoFile(allfile):
	#print allfile
	if len(allfile) == 0 :
		return
	global G_MOS
	global G_str
	global G_rstr
	ALLFile = copy.deepcopy(allfile)
	for i in range(0,len(ALLFile)):#
			ALLFile[i] = ALLFile[i].replace("\\","/")
			allfile[i] = allfile[i].replace("\\","/")
			allfile[i] = allfile[i][allfile[i].rfind("/")+1:]##文件名
	if G_MOS == 1:
		lenth = len(allfile[0])
		publicmax = ""
		for i in range(0,lenth):
			public = allfile[0][:i]
			ispublic = True
			for obj in allfile:
				if public not in obj:
					ispublic = False
			if ispublic:
				publicmax = len(publicmax)<len(public) and public or publicmax
			else:
				publen = len(publicmax)
				for i in range(0,len(allfile)):#
					allfile[i] = allfile[i][publen:]
				break
		for n in range(0,len(ALLFile)):
			file = ALLFile[n][:ALLFile[n].rfind("/")+1]+allfile[n]
			os.rename(ALLFile[n],file)
	elif G_MOS == 2:
		for n in range(0,len(ALLFile)):
			file = ALLFile[n][:ALLFile[n].rfind("/")+1]+G_qname+allfile[n]
			os.rename(ALLFile[n],file)
	elif G_MOS == 3:
		for n in range(0,len(ALLFile)):
			file = ALLFile[n][:ALLFile[n].rfind("/")+1]+allfile[n].replace(G_str,G_rstr)
			os.rename(ALLFile[n],file)
def dirlist(path):  
	allfile = []
	filelist =  os.listdir(path)
	for filename in filelist:  
		filepath = os.path.join(path, filename)  
		if os.path.isdir(filepath):
			dirlist(filepath)
		else:  
			allfile.append(filepath) 
	DoFile(allfile)	
def main():
	print(u"要处理的模式：\n1、删除相同前缀\n2、添加前缀\n3、替换相应字符串")
	num = raw_input()
	global G_MOS
	global G_qname
	global G_str
	global G_rstr
	if num == '1' :
		G_MOS = 1
	elif num == '2':
		G_MOS = 2
		print(u"请输入添加的前缀：")
		G_qname = raw_input()
	elif num == '3':
		G_MOS = 3
		print(u"请输入要替换的字符串：")
		G_str = raw_input()
		print(u"请输入替换的字符串：")
		G_rstr = raw_input()
	print(u"请输入处理路径：")
	dir = raw_input()
	dirlist(dir)
	
		
##############################	
G_MOS = 1	
G_qname = ""
main()