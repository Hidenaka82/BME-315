def readData(filename):
    f=open(filename,"r") # "r" means read
    data = f.read()
    return data


def PatternCount(Seq,Pattern):
    motif = ""
    count=0
    for i in range(0,(len(Seq)-len(Pattern))+1):
        motif = Seq[i:i+len(Pattern)]
#        print(motif)
        if(motif==Pattern):
            count= count+1
    return count


def FindMax(Count):  
    max_num= count[0]
    for item in A:
        if item > max_num:
            max_num=item
    return(max_num)
            

def FrequentWords(Seq,k):
    FrequentPattern = []
    count=[]
    max = 0
    maxCount =0
    for i in range(0,(len(Seq)-K)+1):
        motif = Seq[i:i+K]
        count.append (PatternCount(Seq, motif))
    

    maxCount = FindMax(count)
    for i in range(0,(len(Seq)-K)+1):
        if (count[i] == maxCount):
            pattern = Seq[i:i:k]
        
        if len(FrequentPattern) == 0:
            FrequentPattern.append(pattern)
        
        for item in FrequentPattern:
            if item == pattern:
                #do not add this item into the list
                continue
            else:
                # add the item into the list 
                FrequentPattern.append(item)

    print(FrequentPattern)
#print(Seq)
#print(Count)
#print("max is:",str(maxCount) )



def FrequentWorkds(seq,l):
    text = readData("data.txt")
    FrequentWords(Text,3)
