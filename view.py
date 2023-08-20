import sys
#view
def view(conb):
    conb=[str(a) for a in conb]
    #print('\n')
    print(' ',*conb[:3])
    print(' ',conb[9]+'\u3000'+'\u0020'+conb[3])
    print(' ',conb[8]+'\u3000'+'\u0020'+conb[4])
    print(' ',*conb[8:5:-1])

def view2(conb):
    conb=[str(a) for a in conb]
    print('\033[4A','',*conb[:3])
    print(' ',conb[9]+'\u3000'+'\u0020'+conb[3])
    print(' ',conb[8]+'\u3000'+'\u0020'+conb[4])
    print(' ',*conb[8:5:-1])
#奇数だけ対応
def viewyoko1retu(conb):
    if len(conb)%2 == 0:
        print("conbが奇数でないよ")
        sys.exit()
    #a=' '*(len(conb)//2)
    b=[]
    for i in range(len(conb)):
        if i == len(conb) // 2:
            b.append('u')
        else:
            b.append(' ')
    print('\033[2A',*conb)
    print('',*b)
    #print('','',a,'口',a)

def viewfastyoko1retu(conb):
    print('\n')
    print(*conb)
