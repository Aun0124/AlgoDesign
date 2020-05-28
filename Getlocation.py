
import webbrowser

import googlemaps
from gmplot import gmplot
import os
path = 'options'
colors = ['red','blue','gray','purple','fuchsia','gold','pink','white']
files = os.listdir(path)
# center of map
gmap = gmplot.GoogleMapPlotter(4.144082, 101.081438, 8)
gmap.apikey='AIzaSyB-T4FGL-A6zZ_p6lbNgD4eHtjnV9b44a0'


for (ind,f) in enumerate (files,1):
	print("Option ",ind," (",colors[ind-1],") = ",f.split('.')[0])

strr = ""
count=0;
for ls in files:

    data = open("options/" + ls, 'r').read().replace("\n", "")
    strr = ' '.join(data.split())
    strr = strr.replace(" ", "&")
    fullcoordinatex = []
    fullcoordinatey = []
    coor = strr.split("&")
    coordinatex = []
    coordinatey = []
    for (ind, i) in enumerate(coor, 0):
        temp = i.split(',')
        coordinatey.append((float)(temp[0]))
        coordinatex.append((float)(temp[1]))
    fullcoordinatex.append(coordinatex)
    fullcoordinatey.append(coordinatey)
    gmap.plot(coordinatex, coordinatey, colors[count], edge_width=6)
    count+=1

# Draw
gmap.draw("my_map.html")
url = "my_map.html"
webbrowser.open(url)
distance=[]
for i in len(fullcoordinatex):
    for k in len(fullcoordinatex[i])-1:
        #temp= getdistance(fullcoordinatex[i][k],fullcoordinatey[i][k]) between (fullcoordinatex[i][k+1],fullcoordinatey[i][k+1])
        temp+=temp
    distance.append(temp)

#//find shortest distance and show graph
