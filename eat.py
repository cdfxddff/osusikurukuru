import noWaitInput as nrk

def eat(susi_posi):
    a=nrk.getkey()
    if a and susi_posi == 2:
        return 1
    else:
        return 0