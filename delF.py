#coding=utf-8
####### 命令行  -u生成 update.zip文件  -j解密src下差异luac文件
import os 
import re
def dirlist(path, allfile):  
    filelist =  os.listdir(path)
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:  
            allfile.append(filepath) 
    return allfile
def clfile(File):
    print File
    f = open(File,"r+")
    file = f.read()
    F = file
    f.close()





    file=re.sub(r"--\[\[\s*IF\s*FuDuo.*?\]\\(((?!(ELSE|ELSEIF)).|\n)*?)--\[\[\s*END\s*\]\]",r"",file)
    file=re.sub(r"--\[\[\s*IF\s*NOT\s*CaiLai.*?\]\\(((?!(ELSE|ELSEIF)).|\n)*?)--\[\[\s*END\s*\]\]",r"",file)
    file=re.sub(r"--\[\[\s*IF\s*NOT\s*FuDuo.*?\]\](((?!(ELSE|ELSEIF)).|\n)*?)--\[\[\s*END\s*\]\]",r"\1",file)
    file=re.sub(r"--\[\[\s*IF\s*CaiLai.*?\]\](((?!(ELSE|ELSEIF)).|\n)*?)--\[\[\s*END\s*\]\]",r"\1",file)

    file=re.sub(r"--\[\[\s*IF\s*FuDuo.*\]\\((?!ELSEIF).|\n)*?--\[\[\s*ELSE\s*\]\]([\s\S]*?)--\[\[\s*END\s*\]\]",r"\2",file)
    file=re.sub(r"--\[\[\s*IF\s*NOT\s*CaiLai.*\]\\((?!ELSEIF).|\n)*?--\[\[\s*ELSE\s*\]\]([\s\S]*?)--\[\[\s*END\s*\]\]",r"\2",file)
    file=re.sub(r"--\[\[\s*IF\s*CaiLai.*\]\](((?!ELSEIF).|\s)*?)--\[\[\s*ELSE\s*\]\\[\s\S]*?--\[\[\s*END\s*\]\]",r"\1",file)
    file=re.sub(r"--\[\[\s*IF\s*NOT\s*FuDuo.*\]\](((?!ELSEIF).|\n)*?)--\[\[\s*ELSE\s*\]\\[\s\S]*?--\[\[\s*END\s*\]\]",r"\1",file)

    file=re.sub(r"--\[\[\s*IF\s*FuDuo.*\]\\[\s\S]*?--\[\[ELSEIF\s*CaiLai\s*THEN\]\]([\s\S]*?)--\[\[\s*END\s*\]\]",r"\1",file)
    file=re.sub(r"--\[\[\s*IF\s*CaiLai.*\]\]([\s\S]*?)--\[\[ELSEIF\s*FuDuo\s*THEN\]\]([\s\S]*?)--\[\[\s*END\s*\]\]",r"\1",file)
    if F != file:
        f = open(File,"r+")
        f.write(file)
        f.close()

def main():
    allfile= []
    print(u"请输入处理路径:\n")
    d = raw_input()
    dirlist(d, allfile)
    for f in allfile:
        f=f.replace("\\","/")
        if ".lua" in f:
            clfile(f)
  
G_DIR=[]
main()