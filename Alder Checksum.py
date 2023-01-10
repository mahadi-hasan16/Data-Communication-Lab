def checksum(s):
    l=len(s)
    L=[]
    R=[]
    R.append(ord(s[0])+1)  #As R=1 and L=0 for Alder Checksum
    for i in range(1,l):
        R.append((R[i-1]+ord(s[i]))%65536)
    L.append(R[0])
    for i in range(1,len(R)):
        L.append((R[i]+L[i-1])%65536)
    Checksum=L[len(L)-1]*65536+R[len(R)-1]
    return Checksum
        
def main():
    print(checksum('Forouzan'))
main()