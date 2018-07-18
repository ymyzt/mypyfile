#coding=utf-8
import re 
import os
import sys
import shutil
def dirlist(path, allfile):  
	filelist =  os.listdir(path)
	for filename in filelist:  
		filepath = os.path.join(path, filename)  
		if os.path.isdir(filepath):
			dirlist(filepath, allfile)
		else:  
			filepath=os.path.abspath(filepath)
			allfile.append(filepath) 
	return allfile
def moveres():  
	global G_MOVEDIR
	global G_CURDIR
	global G_NAME
	global G_MOVEDIRNAME
	global G_CURDIRNAME
	p = re.compile(G_NAME,re.I)
	for curfile in G_CURDIR:
		m = p.search(curfile)
		if m:
			curfile = curfile.replace('\\','/')
			tempdir = curfile.replace(G_CURDIRNAME,G_MOVEDIRNAME)
			# tempdir = curfile[curfile.find('src/')+4:]
			# tempdir = G_MOVEDIRNAME+"/src/"+tempdir
			print(curfile)
			# print(tempdir)
			dirname,name = os.path.split(tempdir)
			if not os.path.exists(dirname):
				os.makedirs(dirname)
			shutil.copy(curfile,tempdir)

# (View_Layer =[\s\S]*}\s*,\s*--\s*[^\n]*\s})|(View_Layer =[\s\S]*}\s*--\s*[^\n]*\s})			
def main():	
	##print(u"请输入要处理的文件:") 
	##df = raw_input()
	##print(u"处理中.....")
	global G_MOVEDIR
	global G_CURDIR
	global G_NAME
	global G_MOVEDIRNAME
	global G_CURDIRNAME
	if len(sys.argv)!=3:
		print(u"参数错误")
		sys.exit(0)
	G_MOVEDIRNAME = sys.argv[1]
	G_CURDIRNAME = sys.argv[2].replace('\\','/')
	print(G_CURDIRNAME)
	G_CURDIRNAME = G_CURDIRNAME[G_CURDIRNAME.rfind('/')+1:]
	print(G_CURDIRNAME)
	print(u"请输入要移植游戏关键字:")
	G_NAME =  raw_input()
	dirlist("../",G_CURDIR)
	dirlist("../../"+G_MOVEDIRNAME,G_MOVEDIR)
	moveres()
	#print(u"处理完毕！！")
G_MOVEDIR=[]
G_CURDIR=[]
G_NAME= ''
G_MOVEDIRNAME=''
G_CURDIRNAME = ''
main()