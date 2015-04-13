from Tkinter import *
import ttk
from priodict import priorityDictionary
import json

window = Tk()
window.title('shortest route finder')
window.geometry('1024x800')
window.configure(background='black')
# directions should be set to ''
directions = ''
label = ttk.Label(window, text='', background='black', foreground='white')
label.grid(row=2, column=0)






def Dijkstra(G,start,end=None):
  D = {}  # dictionary of final distances
  P = {}  # dictionary of predecessors
  Q = priorityDictionary()   # est.dist. of non-final vert.
  Q[start] = 0
  
  for v in Q:
    D[v] = Q[v]
    if v == end: break
    
    for w in G[v]:
      vwLength = D[v] + G[v][w]
      if w in D:
        if vwLength < D[w]:
          raise ValueError, "Dijkstra: found better path to already-final vertex"
      elif w not in Q or vwLength < Q[w]:
        Q[w] = vwLength
        P[w] = v
  
  return (D,P)
      
def shortestPath(G,start,end):
  D,P = Dijkstra(G,start,end)
  Path = []
  while 1:
    Path.append(end)
    if end == start: break
    end = P[end]
  Path.reverse()
  return Path

# Logic for generating graph from an input file starts here


places = ['Academic Affairs Building(JEE/GATE)','ACES Extn','ACMS Builiding','Aerodynamics Lab','Aerospace Department','Aerospace Lab Extn','Atmospheric Monitoring Station','Auditorium','Bio Science and Bio Engg.(BSBE)','Central Store','Computer Centre Canteen(CCC)','Computer Centre(CC)','Core Lab Building','Crystal Growth Lab','CSE Building','ECES Extn','Env. Engg. Ctr (CERE)','Faculty Building','Faculty Canteen','Gate 1','Gate 2','Gate 3','Gate 4','GEnerator Room','Geoinformatics Lab','Helicopter Building','IME Lab','Lecture Hall Complex','Library','Mech. Engg. Lab Extn.','Mechanical Lab','New Core Lab Building','New Lecture Hall Complex','Nothern Lab','Nuclear Physics Lab','NW Lab 1','NW Lab 2','NW Lab 2 Extn','Office of IWD','Old Lecture Hall Complex','Propulsion Lab','SAMTEL','Southern Lab','Structures Lab','Substation','Telephone Exchange','Tutorial Complex','Wind tunnel','Air Strip','ATMs(SBI & UBI)','Community Centre Type-1','Community Centre Type-2','Dhobi Ghat','EB Substation-1','EB Substation-3','EB Substation-4','EB Substation-5','Gym','Health Centre','Indoor Stadium','Indoor Stadium','IWD Store','IWD Store','Media Centre','NCC Office','New Indoor Stadium','Nursery','Open Air Threatre(OAT)','Out Reach Building','Petrol Pump','Railway Reservation Centre','SAC','Security Office','Shopping Complex(Shop C)','SIIC(SIDBI Building)','Geokno','SIS 1','SIS 2','Swimming Pool','TA-Canteen(Academic Canteen)','Union Bank Of India','GH1','GH','HALL 1','HALL 2','HALL 3','HALL 4','HALL 5','HALL 7','HALL 8','HALL 9','HALL 10',' HALL 11','New RA Hostel','New SBRA Hostel','Old RA Hostel','Old SBRA Hostel','Visitors Hostel','Visitors Hostel Extn.','ACS Ground','Basketball Court 1','Basketball Court 2','Basketball Court 3','Campus School Basketball Court','Central School Basketball Court','Central School Play Ground','Central School Tennis Court','Cricket Pitch','Football Ground','GH 1 Badminton Court','GH 1 Basketball Court','Hall 1 Basketball Court','Hall 1 PlayGround','Hall 2 Basketball Court','Hall 4 Basketball Court','Hall 4 Volleyball Court','Hall 5 Basketball Court','Hall 5 Playground','Hall 7 Basketball Court','Hall 7 Playground','Hall 8 Basketball Court','Hall 8 Playground','Hall 8 Volleyball Court','Hall 9 Basketball Court','Hall 9 Play Ground','Hockey Ground','Karamchari Ground','Open Squash Court','Pavilion','Ramleela Ground','Stadium','Tennis Court','Volleyball Court','Campus School','Central & Opportunity School']


# Mapping for each node string to a number
placesHashMap = {'Academic Affairs Building(JEE/GATE)' : 1,'ACES Extn' : 2,'ACMS Builiding' : 3,'Aerodynamics Lab' : 4,'Aerospace Department' : 5,'Aerospace Lab Extn' : 6,'Atmospheric Monitoring Station' : 7,'Auditorium' : 8,'Bio Science and Bio Engg.(BSBE)' : 9,'Central Store' : 10,'Computer Centre Canteen(CCC)' : 11,'Computer Centre(CC)' : 12,'Core Lab Building' : 13,'Crystal Growth Lab' : 14,'CSE Building' : 15,'ECES Extn' : 16,'Env. Engg. Ctr (CERE)' : 17,'Faculty Building' : 18,'Faculty Canteen' : 19,'Gate 1' : 20,'Gate 2' : 21,'Gate 3' : 22,'Gate 4' : 23,'GEnerator Room' : 24,'Geoinformatics Lab' : 25,'Helicopter Building' : 26,'IME Lab' : 27,'Lecture Hall Complex' : 28,'Library' : 29,'Mech. Engg. Lab Extn.' : 30,'Mechanical Lab' : 31,'New Core Lab Building' : 32,'New Lecture Hall Complex' : 33,'Nothern Lab' : 34,'Nuclear Physics Lab' : 35,'NW Lab 1' : 36,'NW Lab 2' : 37,'NW Lab 2 Extn' : 38,'Office of IWD' : 39,'Old Lecture Hall Complex' : 40,'Propulsion Lab' : 41,'SAMTEL' : 42,'Southern Lab' : 43,'Structures Lab' : 44,'Substation' : 45,'Telephone Exchange' : 46,'Tutorial Complex' : 47,'Wind tunnel' : 48,'Air Strip' : 49,'ATMs(SBI & UBI)' : 50,'Community Centre Type-1' : 51,'Community Centre Type-2' : 52,'Dhobi Ghat' : 53,'EB Substation-1' : 54,'EB Substation-3' : 55,'EB Substation-4' : 56,'EB Substation-5' : 57,'Gym' : 58,'Health Centre' : 59,'Indoor Stadium' : 60,'Indoor Stadium' : 61,'IWD Store' : 62,'IWD Store' : 63,'Media Centre' : 64,'NCC Office' : 65,'New Indoor Stadium' : 66,'Nursery' : 67,'Open Air Threatre(OAT)' : 68,'Out Reach Building' : 69,'Petrol Pump' : 70,'Railway Reservation Centre' : 71,'SAC' : 72,'Security Office' : 73,'Shopping Complex(Shop C)' : 74,'SIIC(SIDBI Building)' : 75,'Geokno' : 76,'SIS 1' : 77,'SIS 2' : 78,'Swimming Pool' : 79,'TA-Canteen(Academic Canteen)' : 80,'Union Bank Of India' : 81,'GH1' : 82,'GH' : 83,'HALL 1' : 84,'HALL 2' : 85,'HALL 3' : 86,'HALL 4' : 87,'HALL 5' : 88,'HALL 7' : 89,'HALL 8' : 90,'HALL 9' : 91,'HALL 10' : 92,' HALL 11' : 93,'New RA Hostel' : 94,'New SBRA Hostel' : 95,'Old RA Hostel' : 96,'Old SBRA Hostel' : 97,'Visitors Hostel' : 98,'Visitors Hostel Extn.' : 99,'ACS Ground' : 100,'Basketball Court 1' : 101,'Basketball Court 2' : 102,'Basketball Court 3' : 103,'Campus School Basketball Court' : 104,'Central School Basketball Court' : 105,'Central School Play Ground' : 106,'Central School Tennis Court' : 107,'Cricket Pitch' : 108,'Football Ground' : 109,'GH 1 Badminton Court' : 110,'GH 1 Basketball Court' : 111,'Hall 1 Basketball Court' : 112,'Hall 1 PlayGround' : 113,'Hall 2 Basketball Court' : 114,'Hall 4 Basketball Court' : 115,'Hall 4 Volleyball Court' : 116,'Hall 5 Basketball Court' : 117,'Hall 5 Playground' : 118,'Hall 7 Basketball Court' : 119,'Hall 7 Playground' : 120,'Hall 8 Basketball Court' : 121,'Hall 8 Playground' : 122,'Hall 8 Volleyball Court' : 123,'Hall 9 Basketball Court' : 124,'Hall 9 Play Ground' : 125,'Hockey Ground' : 126,'Karamchari Ground' : 127,'Open Squash Court' : 128,'Pavilion' : 129,'Ramleela Ground' : 130,'Stadium' : 131,'Tennis Court' : 132,'Volleyball Court' : 133,'Campus School' : 134,'Central & Opportunity School' : 135}


# Open the input file
f = open('input.txt', 'r')

# G is a dictionary of dictionaries
G = {}

nodesLength = 600

# Initialize G
for i in range(nodesLength):
  dict = {}
  G[i] = dict

# Parse each line of input file and fill G
for line in f:
  row = line.split()
  v1 = int(row[0])
  v2 = int(row[1])
  w = int(row[2])
  G[v1][v2] = w


# Create a dictionary 'nodes' from nodeinfo.json file
# Each node contains the following information :
# parent : The node used to reach the current node (generally)
# left : Node to the left
# right : Node to the right
nodeInfo = open('nodeinfo.json', 'r')
nodes = json.loads(nodeInfo.read())


# utility function to get node name from placesHashMap {'placeName' : ind }
def getNodeName(placesHashMap, index):
  for name,i in placesHashMap.iteritems():
    if i == index:
      return name

  return None

# utility function to get directions using
#  nodes  { "index" : { "left" : value, "right": value, "parent": value} }
def getDirection(nodes, v1, v2, previousNode):
  current = nodes[str(v1)]
  if (previousNode):
    if previousNode == current['parent']:
      return "left" if v2 == current['left'] else "right"

    if previousNode == current['left']:
      return "right" if v2 == current['parent'] else None

    if previousNode == current['right']:
      return "left" if v2 == current['parent'] else None
  else:
    # In case of first node, there is no previous node
    return "left" if v2 == current['left'] else "right"



#Function to generate textual directions using the path array
def generateDirections(G, nodes, path):
  pathString = ''
  cumulativeD = 0
  for i in xrange(len(path)):
   
    # Pick 2 adjacent nodes
    v1 = path[i]
    if (i == len(path)-1):
      break
    v2 = path[i+1]
    previousNode = path[i-1] if (i > 0) else None

    # Get distance between v1 and v2
    distance = G[v1][v2]
  
    # Get direction of v2 (left or right)
    direction = getDirection(nodes, v1, v2, previousNode)
    if(direction):
      if cumulativeD != 0:
        pathString += 'Walk ' + str(cumulativeD) + ' metres\n'
      pathString += "Turn " + direction + "\n"
      cumulativeD = distance
    else:
      cumulativeD += distance


    nodeName = getNodeName(placesHashMap, v2)

    
    # if v2 node has a name, update the path string accordingly
    if (nodeName):
      pathString += ' Keep walking till you reach ' + nodeName + "\n"


  return pathString


# Callback function for Go Button ( Main logic goes here)
def generatePath(G, source, destination):
  # TODO 2 :
  # Make a mapping from a 'source/destination' to corresponding node number in G. 


  # Find the values of 'source' and 'destination' in the node dictionary
  label.configure(text='')
  start = placesHashMap[source]
  end = placesHashMap[destination]

  print start,end
  if start == end:
    label.configure(text='You are at the same place')
    return

  # Run Dijkstra on G and find the shortest path
  path = shortestPath(G, start, end) 
  print path
  directions = generateDirections(G, nodes, path)
  print directions
  label.configure(text=directions)




# Resets the values of the drop down lists
def resetValues(source, destination, label):
  source.set("Select Destination")
  destination.set("Select source")
  label.configure(text='')




# create a drop down list for source locations	
source = ttk.Combobox(window)
source.set("Select Source")
source["values"] = places
#place this widget in the window
source.grid(row=1, column=0, padx=20)

# create a drop down list for destination locations
destination = ttk.Combobox(window)
destination.set("Select Destination")
destination["values"] = places
#place this widget in the window
destination.grid(row=1, column=2, padx=20)

# create a Go button
goButton = ttk.Button(window, text='Go!', command= lambda : generatePath(G, source.get(), destination.get()))
goButton.grid(row=1, column=3, padx=20, pady=20)

# create a Reset button
resetButton = ttk.Button(window, text='Reset', command= lambda : resetValues(source, destination, label))
resetButton.grid(row=1, column=4)

# Insert the campus map image
helperButton = ttk.Button(window)
campusMap = PhotoImage(file='map3.gif')
helperButton.image = campusMap
helperButton.configure(image=campusMap)
helperButton.grid(row=2, column=3, pady=50)
	
window.mainloop()


