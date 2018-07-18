#encoding=utf-8
import os,Image,sys
from xml.etree import ElementTree
filenames=os.listdir(os.getcwd())
i=0
if len(sys.argv)==2:
    filepath=sys.argv[1]
    for filename in filenames:
        if (filename==filepath+'.png') or (filename==filepath+'.plist'):
            i +=1
    if i==0:
        print("No such file or directory!")
    elif i==1:
        print("Both .png and .plist are need!")
    else:
        treeroot=ElementTree.parse(filepath+'.plist').getroot()
        #p=list(per.iter("key"))
        image=Image.open(filepath+'.png')  #open image
        sizelist=(0,0)
 
        #box=(0,0,0,0)
 
        for dict1 in treeroot:
            for index1,item1 in enumerate(dict1): #
        #        print (item1.tag,item1.attrib,item1.text)
                if item1.text=='frames':  #get node who Value=frames 
        #            print (index1)
                    i=0
                    dict2 = dict1[index1+1]
        #            print(len(dict2))
        #            for index2,item2 in enumerate(dict2):
        #                print(item2.tag,item2.attrib,item2.text)
                    while i<len(dict2):
                        print("name:"+dict2[i].text)
                        picname=dict2[i].text
                        dict3 = dict2[i+1]
                        for index3,item3 in enumerate(dict3):
        #                    print(item3.tag,item3.attrib,item3.text)
                            if item3.text=='spriteSourceSize':
        #                        print(dict3[index3+1].text)
                                size=dict3[index3+1].text
                                sizelist = size.replace('{','').replace('}','').split(',')
                                sizelist=(int(sizelist[0]),int(sizelist[1]));
                                #print(sizelist)
                                 
                            if item3.text=='textureRect':
        #                        print(dict3[index3+1].text)
                                rect=dict3[index3+1].text
                                rectlist = rect.replace('{','').replace('}','').split(',')
        #                        print(rectlist)
                                box=(int(rectlist[0]),int(rectlist[1]),int(rectlist[0])+int(rectlist[2]),int(rectlist[1])+int(rectlist[3]))
                                print("size:")
                                print(sizelist)
                                print("onBig:")
                                print(box)
                                xim=image.crop(box)
                                xxim=Image.new('RGB',sizelist,(255,255,255))
                                box1=((sizelist[0]-box[2]+box[0])/2,(sizelist[1]-box[3]+box[1])/2,(sizelist[0]+box[2]-box[0])/2,(sizelist[1]+box[3]-box[1])/2)
                                print("onNew:")
                                print(box1)
                                xxim.paste(xim,box1,mask=0)
                                if os.path.isdir(filepath):
                                    pass
                                else:
                                    os.mkdir(filepath)
                                outfile=filepath+'/'+picname
                                print("newPath:"+outfile)
                                xxim.save(outfile)
                        i +=2
else:
    print("Please enter only one parameter!")