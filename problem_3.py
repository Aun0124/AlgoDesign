from SemanticAnalysis import positiveword,negativeword
from Getlocation import distance,files




# distances= ranking of path according to distance in Shortest Path
distances = [0] * 7

# the first element of distances =7 and the last =1
for i in range(7):
    distances[i] = i

preference = [0] *( len(files)-1)

car = 10
flight = 10
bus = 10
ktm = 10
lrt_mrt = 10
grab = 10
taxi = 10
ferry = 10
walk = 5

# calculate level of preference for each transportation, if negative then tranportation-=1
for i in range(3):
    if positiveword[i]<negativeword[i]:
        bus-=1

    if positiveword[i+3]<negativeword[i+3]:
        ferry-=1
    if positiveword[i+6]<negativeword[i+6]:
        lrt_mrt-=1

    if positiveword[i+9]<negativeword[i+9]:
        ktm-=1

    if positiveword[i+12] < negativeword[i+12]:
        grab -= 1

    if positiveword[i+15] < negativeword[i + 15]:
        taxi-= 1
    if positiveword[i+18] < negativeword[i + 18]:
        flight -= 1


#calculate total preference of transportation used in each option
for (ind,f) in enumerate (files,1):
    sub_option=f.split(',')
    for x in range(len(sub_option)):
        if str(sub_option[j]).__contains__('car'):
            temp += car
        elif str(sub_option[j]).__contains__('ferry'):
            temp += ferry
        elif str(sub_option[j]).__contains__('bus'):
            temp += bus
        elif str(sub_option[j]).__contains__('flight'):
            temp += flight
        elif (str(sub_option[j]).__contains__('komuter') or str(sub_option[j]).__contains__('ets')):
            temp += ktm
        elif str(sub_option[j]).__contains__('lrt') or str(sub_option[j]).__contains__('ets'):
            temp += lrt_mrt
        elif str(sub_option[j]).__contains__('grab'):
            temp += grab
        elif str(sub_option[j]).__contains__('taxi'):
            temp += taxi
        elif str(sub_option[j]).__contains__('walk'):
            temp += walk
    preference[i] = temp / len(path)


#distance = distance of path from Getlocation,sort option accendingly according to distance
for i in range(len(distances)):
    for j in range(0, len(distances) - 1 - i):
        if distance[j] < distance[j + 1]:
            distances[j],distances[j + 1] =distances[j + 1],distances[j]
            distance[j], distance[j + 1] = distance[j + 1], distance[j]
            preference[j], preference[j + 1] = preference[j + 1], preference[j]
            files[j], files[j + 1] = files[j + 1], files[j]

# add distances to preference, preference=ranking of path according to distance and preference of article
for i in range(len(distances)):
    preference[i]+=distances[i]


max=0

for i in range (len(distances)-1):

    if(preference[i]<preference[i+1]):
        max=i+1

print('the best option is taking',files[max])