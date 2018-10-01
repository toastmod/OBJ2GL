#TOASTMOD OBJ TO OPENGL/C++ FILE GENERATOR
#This version converts the OBJ to primitive OpenGL functions
#=================================================
#Generates a CPP files containing all model data written in C++
#along with a switch case that will process which model to select and load
#The loadModel("modelname") function will contain this switch/case process
#and be linked in a Header file.
#EXAMPLE IN C++
#   //loading a monkey model
#   loadModel("monkey");
#=================================================
#global vars

Normals = []
Verticies = []
Colors = []

#=================================================
#imports

import os
import re
import time

#=================================================
getDocName = raw_input("Enter OBJ File Name (without '.obj'): ")

try:
    os.stat("./output/")
except:
    os.mkdir("output")
    
outfile = open("output/"+(getDocName+".cpp"),"w")
#TODO: add extra settings for toggling writing normals and etc
#=================================================

def addIncludes(input):
    #UNFINISHED FUNCTION
    #DO NOT USE
    #===================
    print("Here you can add extra includes \nif you dont need to add any or are done adding then just leave it blank.")
    ask = raw_input("#include ")
    if ask != "":
        outfile.write("#include "+input)
    #===================
        

def endFile():
    outfile.write("\tglEnd(); \n}");
    outfile.close()

def writeVector(x,y,z):
    outfile.write("\t\tglVertex3f("+str(x)+","+str(y)+","+str(z)+"); \n")
    
def writeNormal(x,y,z):
    outfile.write("\t\tglNormal3f("+str(x)+","+str(y)+","+str(z)+"); \n")

def writeColor(r,g,b):
    outfile.write("\t\tglColor3f("+str(x)+","+str(y)+","+str(z)+"); \n")

def readOBJ(input):
    #read and collect verticies
    f = open(input,"r")

    allines = f.readlines()

    #print allines

    writenow = False
    waitoutthisline = False
    lineindex = 0
    
    #for example one element in this array would look like
    #v 0.437500 0.164062 0.765625
    for line in allines:
        if writenow == True and waitoutthisline == False:
            #writeVector(vx,vy,vz)
            Verticies.append([vx,vy,vz])
            
        print "LINE==========================="
        lineindex = 0
        waitoutthisline = False
        vx = 0
        vy = 0
        vz = 0
        linesegs = line.split("v")
        for seg in linesegs:
            for s in seg.split():

                if s == "n" or s == "f" or s == "#" or s == "o" or s == "s":
                    waitoutthisline = True
                    
                if waitoutthisline == False:
                    
                    print ("VECTOR"+str(lineindex)+":"+s)

                    if lineindex == 0:
                        vx = s
                    if lineindex == 1:
                        vy = s
                    if lineindex == 2:
                        vz = s
                writenow = True
                lineindex += 1
def readNORMS(input):
    #read and collect normals
    f = open(input,"r")

    allines = f.readlines()

    #print allines

    writenow = False
    waitoutthisline = False
    lineindex = 0
    
    #for example one element in this array would look like
    #v 0.437500 0.164062 0.765625
    for line in allines:
        if writenow == True and waitoutthisline == False:
            #writeVector(vx,vy,vz)
            Normals.append([vx,vy,vz])
            
        print "LINE==========================="
        lineindex = 0
        waitoutthisline = False
        vx = 0
        vy = 0
        vz = 0
        linesegs = line.split("vn")
        for seg in linesegs:
            for s in seg.split():

                if s == "v" or s == "f" or s == "#" or s == "o" or s == "s":
                    waitoutthisline = True
                elif s == "vn":
                    waitoutthisline = False
                    
                if waitoutthisline == False:
                    
                    print ("NORMAL"+str(lineindex)+":"+s)

                    if lineindex == 0:
                        vx = s
                    if lineindex == 1:
                        vy = s
                    if lineindex == 2:
                        vz = s
                writenow = True
                lineindex += 1



vertindex = 0
outfile.write("//TOASTMOD OBJ2GL++ \n")
outfile.write("//GENERATED ON ["+time.strftime("%c")+"]\n\n")
outfile.write("#include <SDL2/SDL.h> \n")
outfile.write("#include <SDL2/SDL_opengl.h> \n\n")
outfile.write("void load"+getDocName+"(){\n")
outfile.write("\tglBegin( GL_TRIANGLES);\n")
readOBJ(getDocName+".obj")
readNORMS(getDocName+".obj")
for vert in Verticies:
    writeNormal(Normals[vertindex][0],Normals[vertindex][1],Normals[vertindex][2])
    writeVector(vert[0],vert[1],vert[2])
    vertindex += 1
endFile()





