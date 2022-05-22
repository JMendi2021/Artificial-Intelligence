from array import array
from copy import deepcopy
import math

#Inputs
distances = dict()

total_attributes = 4
training_examples = [["male",33,28.8,"bristol","No"],
                    ["female",45,23.8,"london","No"],
                    ["female",68, 21.3,"edinburgh","Yes"],
                    ["male",21,22.6,"london","Yes"],
                    ["male",71,18.3,"birmingham","No"],
                    ["female",27,28,"birmingham","Yes"]]

new_query = ["female", 26, 20, "birmingham"]


#Normalising the Dataset
attribute_dict = {k: [] for k in range(total_attributes)}

#Places each of the data into their respective attributes
for a in range(total_attributes):
    for b in range(len(training_examples)):
            attribute_dict[a] += {training_examples[b][a]}

minmax_dict = {k: [] for k in range(total_attributes)}
values = attribute_dict.values()
values_list = list(values)

#Finding the Min and Max values for each attributes
for c in range(len(values_list)):
    if isinstance(values_list[c][0],str):
        next
    else:
        minmax_dict[c] = {min(values_list[c]),max(values_list[c])}

#Creating a Normalised Training Dataset
normalised_td = deepcopy(training_examples)
for d in range(len(training_examples)):
    for e in range(total_attributes):
        minmax = list(minmax_dict[e])
        if not isinstance(training_examples[d][e],str):
            value = training_examples[d][e]
            normalised_td[d][e] = (value - minmax[0]) / (minmax[1] - minmax[0])
            
normalised_nq = list(new_query)

#Creating a Normalised Input
for f in range(total_attributes):
    minmax = list(minmax_dict[f])
    if not isinstance(new_query[f],str):
        normalised_nq[f] = (new_query[f] - minmax[0])/(minmax[1]-minmax[0])
        

#k-NN
for i in range(len(normalised_td)):
    distance_component = 0
    distance = 0
    for j in range(total_attributes): #We exclude the last value as that's the class
        attribute = normalised_td[i][j]
        new_attribute = normalised_nq[j]
        if isinstance(attribute,str):
            if attribute.upper() == new_attribute.upper():
                distance_component = distance_component + 0
            else:
                distance_component = distance_component + 1
        else:
            distance_component = distance_component + (attribute - new_attribute)**2
    
    distance = round(math.sqrt(distance_component), 5) #Remove round or change if necessary

    distances[(i+1),normalised_td[i][-1]] = distance

sorted_values = sorted(distances.values())
sorted_distances = {}

print()
for i in sorted_values:
    for k in distances.keys():
        if distances[k] == i:
            sorted_distances[k] = distances[k]
            break

print("--------------------------------------------")
print("Data Set")
for i in training_examples:
    print(i)
print("\nNew Example")
print(new_query)
print("\n\n--------------------------------------------")
print("Normalised Dataset")
for i in normalised_td:
    print(i)
print("\nNormalised New Example")
print(normalised_nq)
print("\n\n--------------------------------------------")
print("Key:\n(Training Example, Class): Distance")
print("--------------------------------------------")
print("\nDistance from Training to New Example")
for key, value in distances.items():
    print(key, ' : ', value)

print("\nSorted Distances from Training to New Example")
for key, value in sorted_distances.items():
    print(key, ' : ', value)

print("\nNote:\nIf Regression, take the sum of the first k outputs and divde by k\n")
