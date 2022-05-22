#Change as required
data = [[1,1],[2,5], [3,11]]
a = 0.1

#Gradient Descent
w_0 = 0
w_1= 0
print("")
for i in range(len(data)):
    #Input Attributes
    x_1 = data[i][0]

    #Desired Output
    y = data[i][1]
    
    #Gradient Descent Step
    f = (w_1 * x) + w_0
    w_0 = w_0 - a * (f - y)

    #Put other w's in this section below if Number of Attributes > 1 (Remember Partial Derviatives)
    w_1 = w_1 - a * (f - y) * x_1
    
    #Mean Square Cost of Current Model
    cost = 0
    for j in range(len(data)):
        x_j = data[j][0]
        y_j = data[j][1]
        f_j = (w_1 * x_j) + w_0
        cost = cost + (f_j-y_j)**2
    mean_cost = cost/len(data)

    print("Iteration", (i+1))
    print("Data Point: ", data[i])
    print("w_0 = ", w_0)
    print("w_1 = ", w_1)
    print("Total Square Cost = ", cost)
    print("Mean Square Cost = ", mean_cost)
    print("")
