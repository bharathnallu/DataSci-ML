# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:19:05 2018

@author: Reddy
"""

#gradient descent in python
#for the function y = (x+5)^2 lets find the gobal minimum starting from the point x =3
"""Step 1:
     intialize x =3. Then find the gradient descent of the function, dy/dx = 2*(x+5)
    Step 2:
        move in the negative direction of the gradient descent. But how much to move?
        For that,we require a learning rate.
        Let us assume the learning rate is 0.001
    Step 3:
        Lets perform the gradient descent for three iterations
    Step 4:
        We observe that x value is slowly decreasing and should converge to -5{local minimum}.
        HOW EVER HOW MANY ITERATIONS WE SHOULD PERFORM?
        SO LETS US SET THE PRECISION VARIABLE TO SOME VALUE SAY 0.000001"""
#STEP1
#the algo starts at the x =3
current_x = 3 
#setting up the learning rate of the algo
rate =0.01
#precision value setup,which tells us when to stop the algo
precision = 0.000001
#step counter
previous_step_size = 1
#maximum number of iterations
max_iters = 10000
#iter counter
iters = 0
#gradient descent of our function
df = lambda x: 2*(x+5)

#STEP2
while (previous_step_size>precision and iters<max_iters):
    previous_x = current_x #storing the current value of x to previous value of x
    current_x = current_x-rate*df(previous_x) #gradient descent
    previous_step_size = abs(current_x - previous_x) #change in x
    iters=iters+1
    print("iteration: {}\n,x value is: {}\n,The local minimum of the x is: {}\n".format(iters,current_x,current_x))
    

        