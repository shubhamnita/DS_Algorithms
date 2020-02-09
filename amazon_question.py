def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                     numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    d={}
    for i in possibleFeatures:
        d[i]=0
    for i in featureRequests:
       
        for word in possibleFeatures:
            if word.lower() in i or word.upper() in i:
                d[word]+=1
                continue
    
    b= sorted(d.items(), key=lambda x: x[1], reverse=True)            
   
    #print(b)
    a=[i[0] for i in sorted(d.items(), key=lambda x: x[1], reverse=True)]
    #print(a)
    if topFeatures<=len(possibleFeatures):
        return a[:topFeatures]
    else:
        return a[:len(possibleFeatures)]