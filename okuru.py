#model
def okuru(conb):
    ii=conb.index(1)
    conb[ii]=0
    if ii == 9:
        conb[0]=1
    else:
        conb[ii+1]=1
    return conb

def okuru1(conb):
    ii=conb.index(1)
    conb[ii]=0
    if ii < len(conb)-1:
        conb[ii+1]=1
    else:
        conb[0]=1
    return ii
