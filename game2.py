import time
import okuru
import view
import eat
import noWaitInput as nw
#main game2
conb=[0,0,0,0,1]
count=0
susi_posi=conb.index(1)
view.viewfastyoko1retu(conb,count)
while 1:
    b=eat.eat(susi_posi)
    count+=b
    time.sleep(1)
    susi_posi=okuru.okuru1(conb)
    view.viewyoko1retu(conb,count)
    b=0