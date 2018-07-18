#coding=utf-8
import re 
import os
import json
def dirlist(path, allfile):  
	filelist =  os.listdir(path)
	for filename in filelist:  
		filepath = os.path.join(path, filename)  
		if os.path.isdir(filepath):
			dirlist(filepath, allfile)
		else:  
			allfile.append(filepath) 
	return allfile
def addlaji(File):
	#######添加 debug 
	#print(u"处理文件 "+File)
	# p = re.compile("((?<=\n)\s*?dump\([\s\S]*?\n|(?<=\n)\s*?print\([\s\S]*?\n)+")
	# #p = re.compile("dump([\s\S]*?)\n")

	f = open(File,"r+")
	file = f.read()
	file = "--[[IF laji THEN]]\n"+file+"\n--[[END]]"
	############删除重复的
	lenth = 1
	while(lenth>0):
		#print("lenth= ",lenth)
		p3 = re.compile("--\[\[IF\s*laji\s*THEN\]\]\s*--\[\[IF\s*laji\s*THEN\]\]")
		m = p3.match(file)
		if m:
			lenth = 1
		else:
			lenth =0
		if lenth>0 :
			p4 = re.compile("--\[\[END\]\]\s*--\[\[END\]\]$")
			me = p4.search(file)
			if me:
				file = "--[[IF laji THEN]]"+file[m.end():me.start()]+"--[[END]]"
			else:
				print(File+u"结尾缺少--[[END]]")
	###########
	f.seek(0)
	f.truncate()
	f.write(file)
	f.close()
##########################################################################################
def main():	
	flaji= open("laji.json")
	ff = flaji.read()
	flaji.close()
	lj = json.loads(ff)
	print(u"请输入要处理的文件:") 
	df = raw_input()
	print(u"处理中.....")
	df.replace("\\","/")
	if "*" in df:
		allfile = []
		path  = df[:df.rfind("*")-1]
		dirlist(path,allfile)
		for file in allfile:
			islaji = False
			for i in lj:
				if i in file:
					islaji=True
			if  islaji:
				addlaji(file)
			else:
				print(u"跳过"+file)
	else:
		islaji = False
		for i in lj:
			if i in df:
				islaji=True
			if  islaji:
				addlaji(df)
			else:
				print(df+u"不是垃圾文件！")
		
	print(u"处理完毕！！")
main()