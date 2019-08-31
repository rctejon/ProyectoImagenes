import os
import requests
import numpy as np
import glob
import random
import pandas as pd
import skimage.io as io
import matplotlib.pyplot as plt


families = list(glob.glob(os.path.join('train','*')))
pairs = []
relationships = pd.read_csv('train_relationships.csv', sep=',',header=0)

kinPath = list(glob.glob(os.path.join('labels','kin.jpg')))[0]
notkinPath = list(glob.glob(os.path.join('labels','notkin.jpg')))[0]
kin = io.imread(kinPath)
notkin = io.imread(notkinPath)

figureOpen = True
def closeFigure(evt):
    global figureOpen
    figureOpen = False

for i in range(2):
    rand = random.randint(0,len(families)-1)
    family = families[rand]
    conds = os.path.split(family)[1]==relationships['p1'].str.split('/').str.get(0)
    indKins = relationships[conds]
    ind1=indKins.iloc[0].p1.split('/')
    ind2=indKins.iloc[0].p2.split('/')
    print(ind1,ind2)
    imgInd1 = list(glob.glob(os.path.join('train',ind1[0],ind1[1],'*')))
    imgInd2 = list(glob.glob(os.path.join('train',ind2[0],ind2[1],'*')))
    print(imgInd1,imgInd2)
    individual1 = []
    individual2 = []
    for img in imgInd1:
        image = io.imread(img)
        individual1.append(image)
    for img in imgInd2:
        image = io.imread(img)
        individual2.append(image)
    pair = (individual1,individual2)
    pairs.append(pair)

for i in range(2):
    rand1 = random.randint(0,len(families)-1)
    family1 = families[rand1]
    rand2 = random.randint(0,len(families)-1)
    family2 = families[rand2]
    listF1 = list(glob.glob(os.path.join(family1,'*')))
    listF2 = list(glob.glob(os.path.join(family2,'*')))
    ind1=listF1[random.randint(0,len(listF1)-1)]
    ind2=listF2[random.randint(0,len(listF2)-1)]
    print(ind1,ind2)
    imgInd1 = list(glob.glob(os.path.join(ind1,'*')))
    imgInd2 = list(glob.glob(os.path.join(ind2,'*')))
    print(imgInd1,imgInd2)
    individual1 = []
    individual2 = []
    for img in imgInd1:
        image = io.imread(img)
        individual1.append(image)
    for img in imgInd2:
        image = io.imread(img)
        individual2.append(image)
    pair = (individual1,individual2)
    pairs.append(pair)

i=0
fig, ax = plt.subplots(nrows=4, ncols=3)
fig.canvas.mpl_connect('close_event', closeFigure)
while figureOpen:
    k=0
    d=0
    for row in ax:
        x=0
        if(k==1):
            d=2
        elif(k==2):
            d=1
        elif(k==3):
            d=3
        for col in row:
            col.axis('off')
            if(x==2):
                if(k%2==0):
                    col.imshow(kin)
                else:
                    col.imshow(notkin)
                continue
            col.imshow(pairs[d][x][i%len(pairs[d][x])])
            x+=1
        k+=1
    i+=1
    plt.draw()
    plt.pause(1)
