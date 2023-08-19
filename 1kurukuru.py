import time

#model
def okuru(conb):
    ii=conb.index(1)
    conb[ii]=0
    if ii == 9:
        conb[0]=1
    else:
        conb[ii+1]=1
    return conb

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

#main
conb=[0,0,0,0,0,0,1,0,0,0]
view(conb)
#止まり方によって1が重複する
while 1:
    time.sleep(0.3)
    okuru(conb)
    view2(conb)

# for i in range(5):
#     okuru(conb)
#     print(conb)