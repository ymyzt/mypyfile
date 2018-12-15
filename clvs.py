#coding=utf-8
import os 
import sys
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
    print(File)
    f = open(File,"r+")
    file = f.read()
    F = file
    f.close()
    
    file=re.sub("<RootNamespace>(.*?)</RootNamespace>\s+</PropertyGroup>",r"<RootNamespace>\1</RootNamespace>\n     <WindowsTargetPlatformVersion>10.0.16299.0</WindowsTargetPlatformVersion>\n</PropertyGroup>",file)
    # print file
    b = file.find("<PropertyGroup Condition=\"'$(Configuration)|$(Platform)'=='Debug|Win32'\" Label=\"Configuration\">")
    print "b=",b
    if b!=-1:
        b2 = file.find("<PlatformToolset Condition=\"'$(VisualStudioVersion)' == '15.0' and exists('$(MSBuildProgramFiles32)\\Microsoft SDKs\\Windows\\v7.1A')\">v140_xp</PlatformToolset>",b)
        print "b2=",b2
        if b2!= -1:
            b3 = file.find("v140_xp",b2)
            print "b3 =", b3
            if b3!=-1:
                file = file[:b3+3]+"1"+file[b3+7:]
    # file=re.sub("([\.\[\]\w]+?:getTouchMovePosition\(\))",r"self.resourceNode_:convertToNodeSpace(\1)",file)
    # file=re.sub("([\.\[\]\w]+?:getTouchBeganPosition\(\))",r"self.resourceNode_:convertToNodeSpace(\1)",file)
    # file=re.sub("([\.\[\]\w]+?):convertToWorldSpaceAR\((cc\.p\(.*?\))\)",r"self:convertToWorldSpaceAR(\1,\2)",file)
    # if "PageTurn" in File:
    #     file=re.sub('([\.\[\]\w]+?|panel:getChildByName\("Image_photo"\)):convertToWorldSpace\((cc\.p\(.*?\))\)',r"self.m_UIManager:getCurScene():convertToWorldSpace(\1,\2)",file)
    # else:
    #     file=re.sub('([\.\[\]\w]+?|panel:getChildByName\("Image_photo"\)):convertToWorldSpace\((cc\.p\(.*?\))\)',r"self:convertToWorldSpace(\1,\2)",file)
   
    if F != file:
        print "write"
        f = open(File,"r+")
        f.write(file)
        f.close()
def main():
    # allfile= []
    # dirlist("./", allfile)
    # for f in allfile:
    #     f=f.replace("\\","/")
    #     if "/app/" in f:
    #         clfile(f)
    clfile("./build/jsb-link/frameworks/runtime-src/proj.win32/JBC.vcxproj")
G_DIR=[]
#print(sys.getfilesystemencoding())
main()