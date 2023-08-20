import time
import okuru
import view

#main game2
conb=[0,0,0,0,1]
view.viewfastyoko1retu(conb)
while 1:
    time.sleep(1)
    okuru.okuru1(conb)
    view.viewyoko1retu(conb)