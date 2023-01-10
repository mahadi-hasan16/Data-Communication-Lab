def xor(s1,s2):
    r=''
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            r+='0'
        else:
            r+='1'
    return r 
# For finding the Remainder
def moduloTwo(divident,divisor): 
    l=len(divisor) #Length of the divisor
    tem_divident=divident
    for j in range(l):
        quotient=''
        if tem_divident [0]=='1':
            quotient+='1'
        else:
            quotient+='0'
        a=[]
        if quotient[len(quotient)-1]=='1':
            a=divisor
        else:
            for i in range(l):
                a.append('0')
        remainder=xor(a[1:],tem_divident[1:])
        tem_divident=remainder+'0'
    return remainder

# Codeword Generator
def generator(data,divisor):
    remainder=moduloTwo(data,divisor)
    return data+remainder

# For finding the Syndrome
def errorCheck(codeword,divisor):
    l=len(divisor)
    tem_divident=codeword[:l]
    diff=len(codeword)-l #Diffenence of the lengths of the codeword and divisor
    for j in range(diff+1):
        quotient=''
        if tem_divident [0]=='1':
            quotient+='1'
        else:
            quotient+='0'
        a=[]
        if quotient[len(quotient)-1]=='1':
            a=divisor
        else:
            for i in range(l):
                a.append('0')
        syndrome=xor(a[1:],tem_divident[1:])
        if j!=diff:
            tem_divident=syndrome+codeword[l+j]
    return syndrome

# Decision Logic
def decisionLogic(syndrome):
    syndrome=int(syndrome)
    if syndrome==0:
        print("There is no error. So, the Data is not corrupted.")
    else:
        print("There is a error. So, the Data is corrupted.")

# Main Function
import time
def main():
    data=input('Insert the data: ')
    divisor=input('Insert the divisor: ')
    codeword=generator(data,divisor)
    print("The Codeword is: ",codeword)
    syndrome=int(errorCheck(codeword,divisor))
    decisionLogic(syndrome)


main()


