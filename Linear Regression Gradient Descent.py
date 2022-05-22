a = 0.1
w_0 = 0
w_1= 0

data = [[1,1],[2,5], [3,11]]

print("")
for i in range(len(data)):
    x = data[i][0]
    y = data[i][1]
    
    #Gradient Descent Step
    f = (w_1 * x) + w_0
    w_0 = w_0 - a * (f - y)
    w_1 = w_1 - a * (f - y) * x
    
    #Mean Square Cost of Current Iteration
    cost = 0
    for j in range(len(data)):
        x_2 = data[j][0]
        y_2 = data[j][1]
        f_2 = (w_1 * x_2) + w_0
        cost = cost + (f_2-y_2)**2
        
    mean_cost = cost/len(data)

    print("Iteration", (i+1))
    print("Data Point: ", data[i])
    print("w_0 = ", w_0)
    print("w_1 = ", w_1)
    print("Total Square Cost = ", cost)
    print("Mean Square Cost = ", mean_cost)
    print("")
