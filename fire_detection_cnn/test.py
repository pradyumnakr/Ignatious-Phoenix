import numpy as np
import cv2
import matplotlib.pyplot as plt

width = 400
height = 240
train_cnt = 0
val_cnt = 0
test_cnt = 0
def generate_dataset(no_fire1, fire2, fire3):
    ds_x = []
    ds_y = []
    sample = no_fire1 + fire2 + fire3
    cap1 = cv2.VideoCapture('nofire_400240.mp4')
    cap2 = cv2.VideoCapture('dalma_400240.mp4')
    cap3 = cv2.VideoCapture('gwanak_400240.mp4')
    
    mog = cv2.createBackgroundSubtractorMOG2()
    num_pt=0 
    cnt1 = 0
    while True:
        if cnt1 == no_fire1:
            break
        print("no_fire==={}".format(cnt1)) 
        ret, frame = cap1.read()
        if ret == False:
            break
        dst = cv2.fastNlMeansDenoisingColored(frame,None,25,25,7,21)    
        fgmask = mog.apply(dst)
        ds_y.append(num_pt)
        ds_x.append(fgmask)
        cnt1 += 1
    cap1.release()
#     return np.array(ds_x).reshape(no_fire1,width,height,1), np.array(ds_y).reshape(no_fire1, 1)
    cnt2 = 0
    cnti = 0
    num_pt = 1
    while True:
        ret, frame = cap2.read()
        if ret == False:
            break
        cnti += 1 
        if (cnti%10) == 0:    
            if cnt2 == fire2:
                break
            print("dalma==={}".format(cnt2)) 
            dst = cv2.fastNlMeansDenoisingColored(frame,None,25,25,7,21)    
            fgmask = mog.apply(dst)
            ds_y.append(num_pt)
            ds_x.append(fgmask)
            cnt2 += 1            
    cap2.release()
    cnt3 = 0
    cnti = 0
    num_pt = 1
    while True:    
        ret, frame = cap3.read()
        if ret == False:
            break
        cnti += 1
        if (cnti%20) == 0: 
            if cnt3 == fire3:
                break
            print("gwanak==={}".format(cnt3))    
            dst = cv2.fastNlMeansDenoisingColored(frame,None,25,25,21)    
            fgmask = mog.apply(dst)
            ds_y.append(num_pt)
            ds_x.append(fgmask)  
            cnt3 += 1
    cap3.release()
    return np.array(ds_x).reshape(sample,width,height,1), np.array(ds_y).reshape(sample, 1)
cv2.destroyAllWindows()   
X_train, y_train = generate_dataset(30,50,100)
X_test, y_test = generate_dataset(20,30,60)
X_val, y_val = generate_dataset(10,30,50)
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dropout
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(width, height, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, batch_size=32)
score = model.evaluate(X_test, y_test, batch_size=32)
print(score)

