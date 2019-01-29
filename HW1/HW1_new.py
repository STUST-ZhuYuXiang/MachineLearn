import csv
import numpy as np

#處理train.csv-----------------------------------------------------
with open('data\\train.csv', 'r') as csvfile:
    data_list = [[]for i in range(18)]
    
    index = 0
    for row in csv.reader(csvfile):
        if (index != 0):
            data_list[(index+17) % 18].extend(row[3:])
        index += 1

#將RAINFALL中NR的值轉換成0.0    
for i in range(len(data_list[10])):
    if (data_list[10][i] == "NR") : data_list[10][i] = "0.0"
    
#設定 y=w*x+b 的矩陣-----------------------------------------------
x = np.zeros(shape=(5751,163))
y = np.zeros(shape=(5751,1))
w = np.zeros(shape=(163, 1))    #權重 w 長度有162個，加上一個常數項 b

for i in range(x.shape[0]):
    index_1 = 0
    index_2 = 0
    for j in range(x.shape[1]):
        if (j < 162):
            #main handle area
            if ((i+index_2) > (i+8)):
                index_1 += 1
                index_2 = 0
                
            x[i, j] = data_list[index_1][i+index_2]
        else:
            x[i, j] = 1
            index_1 = 0
            index_2 = 0
        
        index_2 += 1

for i in range(0, len(y)):
    y[i] = data_list[9][i+9]
    
#套入公式----------------------------------------------------------
count = 100                                 #要更新的次數
learn_rate = 0.01                           #學習率，隨便設定的
pre_gradient = np.zeros(shape=(163,1))

for _ in range(count):
    y_head = np.dot(x, w)                   #將 x*w 預測 ŷ 的值
    
    loss = y - y_head                       #誤差是原始資料 y 減我算出來的 ŷ
    
    x_transpose = np.transpose(x)           #將 x 矩陣轉換成語 w 相同格式
    
    #lossFunction公式
    gradient = 2 * np.dot(x_transpose,loss) 
    pre_gradient += gradient ** 2
    adagrad = np.sqrt(pre_gradient)
    
    w = w - learn_rate * gradient / adagrad
    
#權重更新完成，表示學習完成...應該啦
#處理test.csv的資料------------------------------------------------
with open('data\\test_X.csv', 'r') as csvfile:
    test_list = [[]for i in range(240)]

    for row in csv.reader(csvfile):
        for i in range(240):
            if (row[0] == ("id_"+str(i))):
                test_list[i].extend(row[2:])

#將RAINFALL中NR的值轉換成0.0
for i in range(len(test_list)):
     for j in range(len(test_list[i])):
         if (test_list[i][j] == "NR"):
             test_list[i][j] = 0.0

#設定 test_x 矩陣，將每個 column 最後一個都設成 1
test_x = np.zeros(shape=(240, 163))
for i in range(test_x.shape[0]):
    for j in range(test_x.shape[1]):
        if (j == 162):
            test_x[i][j] = "1"
        else:
            test_x[i][j] = test_list[i][j]

#套入 w ，輸出預測的 PM2.5 數值--------------------------------------
predict_y = np.zeros(240)
predict_y = np.dot(test_x, w)

#將答案寫成 csv 檔，並儲存到 data 資料夾下----------------------------
with open('data\\answer.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "value"])
    for i in range(240):
        writer.writerow(["id_"+str(i), predict_y[i]])

