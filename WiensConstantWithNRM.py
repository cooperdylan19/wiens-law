import numpy as np
import matplotlib.pyplot as plt

#Define continous function and its derivative for which want to find roots
def f(x):
    return np.exp(x)*(5-x) - 5
     
def df(x):
    return np.exp(x)*(4-x)


#Create array of 100 x-values between -5, +5, find corresponding y-values
i = np.linspace(-5,+5,100)
k = f(i)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#Plot graph, helps find good first guess for Newton-Raphson formula
plt.plot(i,k, 'g')
plt.show()
#Intercept ~ 5. Reject intercept at 0

#Define accepted constants
h = 6.63e-34
c = 3e8
k = 1.38e-23

#Create function to estimate the root - main function
def newton_raphson(x, error, max_iterations):
      
    z = f(x) / df(x)
    i = 0
#Determine the precision needed to get accurate solution for x    
    while abs(z) > error:

        
        z = f(x) / df(x)    
        x = x - z
#Newton-Raphson formula ^        
        wiens_constant = (h * c) / (x * k)
#Wien's law => lambda * T = 2.898 * 10-3. Expressed in terms of x ^  
        i = i + 1
        
        if i > max_iterations:
            break
        
    #print(f"{i}")

    if i < max_iterations:          
        print(f"The value of the root is {x:.3f}, this gives an approximation for Wiens constant {wiens_constant:.6f}")
    else:
        print(f"This function has not converged on a root after {i} iterations to a desirable degree of accuracy")
      

#call Newton-Raphson function
newton_raphson(5, 0.0001, 1000)
