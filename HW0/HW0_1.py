import numpy as np

ListData = []
#打開檔案
infile = open("hw0_data.dat", 'r')
for line in infile:
    line = line.strip().split(' ')
    ListData.append(line)
    
#將其值指派到array
ArrayData = np.array(ListData)
print(ArrayData)

#寫一個泡沫排序的方法
def bubble_sort (int):
    for i in range (0, len(ArrayData)-1):
        for j in range (0, len(ArrayData)-1-i):
            if (ArrayData[j, int] > ArrayData[j+1, int]):
                ArrayData[j, int], ArrayData[j+1, int] = ArrayData[j+1, int], ArrayData[j, int]
          
    #將使用者輸入的列，全部印出來
    print(ArrayData[:, int])

#main code，使用者輸入一個數字，指定column
in_column = int(input("Input column : "))
bubble_sort(in_column)
            