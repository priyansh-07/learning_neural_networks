n=2
weight = [0 for s in range(n)]
old_weight = weight
bias = 0
old_bias = 0
threshold = 2
alpha = 1
inputs=[[1,1], [1,0], [0,1], [0,0]]
targets=[1,-1,-1,-1]
epoch=3

for e in range(epoch):
    #while stopping condition is false
    while True:
        #for each training pair
        for p in range(4):
            x = inputs[p]
            t = targets[p]
            
            #where do i put this line
            #old_weight, old_bias = weight, bias

            #compute the response
            sum=0
            for j in range(n):
                sum+=(x[j]*weight[j])
            y_in=bias+sum

            #calculate y
            if y_in > threshold:
                y=1
            elif y_in>=(-threshold) and y_in<=threshold:
                y=0
            elif y_in<(-threshold):
                y=-1

            #updating weights and biases
            if not y==t:
                for i in range(n):
                    weight[i]=old_weight[i] + alpha*t*x[i]                    
                bias = old_bias + alpha*t
                
            else :
                for i in range(n):
                    weight[i]=old_weight                    
                bias=old_bias
        
        #testing stopping condition
        if weight == old_weight:
            break
    print("epoch "+str(e)+" out of 3")         
    print(weight)
print(bias)
