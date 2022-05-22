import math

#Change according to requirements!
data = [[1,1],[2,5], [3,11]]
a = 0.1

#Gradient Descent
w_0 = 0
w_1= 0
print("")
for i in range(len(data)):
    #Attribute(s)
    x_1 = data[i][0]

    #Desired Label
    y = data[i][1]
    
    #Gradient Descent Step
    f = (w_1 * x_1) + w_0
    h = 1/(1+math.e**(-f))
    w_0 = w_0 - a * (f - h)

    #Copy paste if there are more attributes!
    w_1 = w_1 + a * (y - h) * x_1
    
    #Cross Entropy of current model
    cost = 0
    for j in range(len(data)):
        x_j = data[j][0]
        y_j = data[j][1]
        f_j = (w_1 * x_j) + w_0
        h_j = 1/(1+math.e**(-f_j))
        cost = cost + (y_j * math.log(h_j) + (1-y) * math.log(1-f))
    mean_cost = cost/len(data)

    print("Iteration", (i+1))
    print("Data Point: ", data[i])
    print("w_0 = ", w_0)
    print("w_1 = ", w_1)
    print("Total CE Cost = ", cost)
    print("Average Cost = ", mean_cost)
    print("")