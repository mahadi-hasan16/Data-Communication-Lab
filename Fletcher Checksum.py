def checksum(s):
    l=len(s)
    L=[]
    R=[]
    R.append(ord(s[0]))
    for i in range(1,l):
        R.append((R[i-1]+ord(s[i]))%256)
    L.append(R[0])
    for i in range(1,len(R)):
        L.append((R[i]+L[i-1])%256)
    Checksum=L[len(L)-1]*256+R[len(R)-1]
    return Checksum
        
def main():
    print(checksum('Forouzan'))
main()