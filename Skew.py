def skew(Seq):
    sk = 0
    location = []
    sk_list = []
    
    for i in range(len(Seq)):
        location = []
        if Seq[i] == "C":
            sk = sk -1
        if Seq[i] == "G":
            sk = sk +1
        # (i,sk)
        location.append(i)
        location.append(sk)
        sk_list.append(location)

    print(sk_list)
    print(location)
    return ""


Seq = "CATGGGCATCGGCCATACGCC"
#Seq = "AACAAGCATAAACATTAAAGAG"
pattern = "AAAAA"

print(skew(Seq))