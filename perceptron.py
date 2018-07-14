def train_model():
    n=2
    weight = [0 for s in range(n)]
    bias = 0
    threshold = 0.2
    alpha = 1
    n_weight, n_bias = [0 for s in range(n)], 0
    inputs=[[1,1], [1,0], [0,1], [0,0]]
    targets=[1,-1,-1,-1]
    delta_w = [ [ 0 for a in range(n+1) ] for b in range(4) ]
    x=[]
    t=0
    e=0
    while True:
        print("\nEpoch : "+str(e+1))
        e+=1
        #for each Training Pair
        for tp in range(4):
            x = inputs[tp]
            t = targets[tp]

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

            print("new weight : "+str(n_weight))
            print("weight : "+str(weight))    

            #create delta_w matrix
            for z in range(n):
                delta_w[tp][z] = n_weight[z] - weight[z]

            #updating the weights
            for i in range(n):
                weight[i]=n_weight[i]
            bias=n_bias
        print("weight change : "+str(delta_w))            
        #checking weight change    
        training=0  
        for p in range(4):
            for q in range(n+1):
                if not delta_w[p][q]==0:
                    training=1
                    break
            if training==1:
                break
        if training==0:
            return                    

train_model()