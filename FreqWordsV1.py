#**************************
#Name: Hideki Nakazawa
# ....
#**************************
def readData(filename):
    f = open(filename, "r")
    data = f.read()
    return data

def PatternCount(Seq, pattern):
    count = 0
    for i in range(0,(len(Seq) - len(pattern)) + 1):
        if (Seq[i:i+len(pattern)] == pattern):
            count = count + 1
    return count

def FindMax(Count):
    max = Count[0]
    for item in Count:
        if item > max:
            max = item
    return max


def FrequentWords(Seq, k):
    FrequentPattern = []
    count = []
    maxCount = 0
    MotifCountDict = {}
    m_count = 0

    for i in range(0, (len(Seq) - k) + 1):
        motif = Seq[i:i + k]
        m_count = PatternCount(Seq, motif)
        count.append (m_count)
        MotifCountDict[motif] = m_count

    maxCount = FindMax(count)
    for i in range(0, (len(Seq) - k) + 1):
       if (count[i] == maxCount):
           pattern = Seq[i:i+k]
           print (MotifCountDict[pattern])

    return pattern

Text = readData("data.txt")
FrequentWords(Text,3)
