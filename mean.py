print " Workout the quantity of earth for an embankment 150m long Wide at the top.Side slope is 2:1"
print "and depts at each 30m interval are 0.60,.1.2,1.4,1.6,1.4, and 1.6 m "

Station=int(input("Enter Your Station:"))
width=int(input("Enter Your Wide:"))
side=int(input("Enter Your Side:"))
depth1=float(input("Enter Your depth1:"))
depth2=float(input("Enter Your depth2:"))
depth3=float(input("Enter Your depth3:"))
depth4=float(input("Enter Your depth4:"))
depth5=float(input("Enter Your depth5:"))
depth6=float(input("Enter Your depth6:"))
interval=int(input("Enter Your Enterval:"))

#Solutuon:
# since 150 long and depth(differenence) in 30m then

print "....................................................."
Station1=30+Station
Station2=Station1+30
Station3=Station2+30
Station4=Station3+30
Station5=Station4+30
print "Starting station is=", Station
print "First Station is   =",Station1    
print "second Station is  =",Station2
print "Third Station is   =",Station3
print "Fourth Station is  =",Station4
print "Fivth Station is   =",Station5
print "......................................................"

# Given width is 10 means W=10.

#width=int(input("Enter Your Wide:"))

# since Depth is given D=[.60,1.2,1.4,1.6,1.4,1.6]

#depth1=float(input("Enter Your depth1:"))
#depth2=float(input("Enter Your depth2:"))
#depth3=float(input("Enter Your depth3:"))
#depth4=float(input("Enter Your depth4:"))
#depth5=float(input("Enter Your depth5:"))
#depth6=float(input("Enter Your depth6:"))

print "Depth 1 is=",depth1
print "Depth 2 is=",depth2
print "Depth 3 is=",depth3
print "Depth 4 is=",depth4
print "Depth 5 is=",depth5
print "Depth 6 is=",depth6
print "........................................................"
CenterArea1=width*depth1
CenterArea2=width*depth2
CenterArea3=width*depth3
CenterArea4=width*depth4
CenterArea5=width*depth5
CenterArea6=width*depth6

print "Center area WD1=", CenterArea1
print "Center area WD2=", CenterArea2
print "Center area WD3=", CenterArea3
print "Center area WD4=", CenterArea4
print "Center area WD5=", CenterArea5
print "Center area WD6=", CenterArea6

print "........................................................."
# since the given slove Side is 2:1 then Formula s*d*d means(2*depth)
#side=int(input("Enter Your Side:"))  #2:1 means 2
Area_of_side1=side*depth1*depth1
Area_of_side2=side*depth2*depth2
Area_of_side3=side*depth3*depth3
Area_of_side4=side*depth4*depth4
Area_of_side5=side*depth5*depth5
Area_of_side6=side*depth6*depth6

print "Side of Area1 Sd^2=",Area_of_side1
print "Side of Area2 Sd^2=",Area_of_side2
print "Side of Area3 Sd^2=",Area_of_side3
print "Side of Area4 Sd^2=",Area_of_side4
print "Side of Area5 Sd^2=",Area_of_side5
print "Side of Area6 Sd^2=",Area_of_side6

print ".........................................................."
# Calculate for Total area...
total_area1=CenterArea1+Area_of_side1
total_area2=CenterArea2+Area_of_side2
total_area3=CenterArea3+Area_of_side3
total_area4=CenterArea4+Area_of_side4
total_area5=CenterArea5+Area_of_side5
total_area6=CenterArea6+Area_of_side6
print "Total Area A1=WD+Sd^2 is", total_area1
print "Total Area A2=WD+Sd^2 is",total_area2
print "Total Area A3=WD+Sd^2 is",total_area3
print "Total Area A4=WD+Sd^2 is",total_area4
print "Total Area A5=WD+Sd^2 is",total_area5
print "Total Area A6=WD+Sd^2 is",total_area6

print "............................................................"
# Calculate for Mean Area....
mean_area1=(total_area1+total_area2)/2
mean_area2=(total_area2+total_area3)/2
mean_area3=(total_area3+total_area4)/2
mean_area4=(total_area4+total_area5)/2
mean_area5=(total_area5+total_area6)/2

print "Mean area MA1=A1+A2/2 is",mean_area1
print "Mean area MA2=A1+A2/2 is",mean_area2
print "Mean area MA3=A1+A2/2 is",mean_area3
print "Mean area MA4=A1+A2/2 is",mean_area4
print "Mean area MA5=A1+A2/2 is",mean_area5

print "..........................................................."
# Since interval is 30 then
#interval=int(input("Enter Your Enterval:"))

Quantity1=interval*mean_area1
Quantity2=interval*mean_area2
Quantity3=interval*mean_area3
Quantity4=interval*mean_area4
Quantity5=interval*mean_area5

print "The Quantity Q1=interval*MA1 is", Quantity1
print "The Quantity Q2=interval*MA2 is",Quantity2
print "The Quantity Q3=interval*MA3 is",Quantity3
print "The Quantity Q4=interval*MA4 is",Quantity4
print "The Quantity Q5=interval*MA5 is",Quantity5

print "............................................................"
# Calculate Total Quantity...
Total_Quantity=Quantity1+Quantity2+Quantity3+Quantity4+Quantity5
print "Total Embankment Quantity Q=Q1+Q2+Q3+Q4+Q5 is",Total_Quantity,"m^3"




            
