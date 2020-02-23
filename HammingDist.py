def HammingDist(pattern1,pattern2):
    dist = 0
    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            dist += 1
    return dist

def APC(Seq,pattern,d):    #Approximate Pattern Count 
    count = 0
    patterns = []
    for i in range(0,(len(Seq) - len(pattern)) + 1):
        pattern_prime = Seq[i:i+len(pattern)]
        if(HammingDist(pattern,pattern_prime)) <=d:
            count += 1
            
            patterns.append(pattern_prime)
        #print(pattern_prime)
        #if (Seq[i:i+len(pattern)] == pattern):
    return count, patterns


Seq = "AACAAGCATAAACATTAAAGAG"
pattern = "AAAAA"
d = 1

print(APC(Seq,pattern,d))

#Pattern1 = "ACTGTTA"
#Pattern2 = "ACAGTTA"
#print(HammingDist(Pattern1,Pattern2))