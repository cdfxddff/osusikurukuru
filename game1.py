import time
import view
import okuru

#main game1
conb=[0,0,0,0,0,0,1,0,0,0]
view.view(conb)
#止まり方によって1が重複する
while 1:
    time.sleep(0.3)
    okuru.okuru(conb)
    view.view2(conb)

for i in range(5):
    okuru.okuru(conb)
    print(conb)