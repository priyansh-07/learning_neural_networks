def train_model(n, threshold, alpha, inputs, targets, n_tp):
    weight, bias = [0 for s in range(n)], 0
    n_weight, n_bias = [0 for s in range(n)], 0    
    delta_w = [ [ 0 for a in range(n+1) ] for b in range(n_tp) ]
    t=0
    e=0
    while True:
        e+=1
        #for each Training Pair
        for tp in range(n_tp):
            x, t = inputs[tp], targets[tp]

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
                    n_weight[i]=weight[i] + alpha*t*x[i]                    
                n_bias = bias + alpha*t        
            else :
                for i in range(n):
                    n_weight[i]=weight[i]
                n_bias=bias
            
            #create delta_w matrix
            for z in range(n):
                delta_w[tp][z] = n_weight[z] - weight[z]

            #updating the weights
            for i in range(n):
                weight[i]=n_weight[i]
            bias=n_bias

        #checking weight change    
        training=0  
        for p in range(n_tp):
            for q in range(n+1):
                if not delta_w[p][q]==0:
                    training=1
                    break
            if training==1:
                break
        if training==0:
            return weight, bias, e 


inputs=[[1,1], [1,-1], [-1,1], [-1,-1]]
targets=[1,-1,-1,-1]
weights, bias, epoch = train_model(2, 0.2, 1, inputs, targets, 4)
print(weights, bias, epoch)


x = [0,0]

sum = 0
for i in range(2):
    sum+=x[i]*weights[i]
y_in = bias + sum

if y_in>0.2:
    y=0
elif y_in>=-0.2 and y_in<=0.2:
    y=0
elif y_in<-0.2:
    y=-1
print(y)            
