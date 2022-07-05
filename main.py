import serial
import matplotlib.pyplot as plt
import numpy  as np
import multiprocessing
import threading
import sys

if not "C:\\ProgramData\\Anaconda3\\Lib\\site-packages" in sys.path:

 PkPath = "C:\\ProgramData\\Anaconda3\\Lib\\site-packages"

 sys.path.append(PkPath)
# 打开 COM17，将波特率配置为115200, 读超时时间为1秒
arr = [0 for i in range(16)]
to_draw1 = [arr for k in range(2501)]
to_draw = np.array(to_draw1)
thetime = 0
def readin():
    ser = serial.Serial(port="COM6", baudrate=460800, bytesize=8, parity='N', stopbits=1, timeout=1)
# 读取串口输入信息并输出。
    global arr 
    arr = [0 for i in range(16)]
    global to_draw 
    
    global thetime 
    thetime = 0
    while True:
        com_input = ser.read(52)
        if com_input:   # 如果读取结果非空，则输出
            cnt = 0
            i = 0
            while(i < 52):
                #print(i)
                if(i == 0 or i == 1 or i == 50 or i == 51):
                    i += 1
                    continue
                else: 
                    tempdata = 0
                    for j in range(i, i+3):
                        inbyte = com_input[j]
                        #print(type(inbyte))
                        tempdata = tempdata << 8 | inbyte
                        #print(tempdata)
                    if((tempdata & 0x00800000) == 0x00800000):
                         tempdata |= 0xFF000000
                    else:
                         tempdata &= 0x00FFFFFF
                    #print(tempdata)
                    arr[cnt] = tempdata * 0.02235174
                    cnt = cnt + 1
                    #print(j)
                    #print(cnt)
                    i = j + 1
                
            print( arr )
            to_draw[thetime] = arr
            if(thetime > 2500):
                to_draw = to_draw[1:]
                thetime = 2500
            #fig = plt.figure()
           
    ser.close()
def draw():
            global arr
            global thetime
            global to_draw
            plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
            x = np.linspace(0,5+1/2500,2501).tolist()
            y_0 = to_draw.T[0].tolist()
            y_1 = to_draw.T[1].tolist()
            y_2 = to_draw.T[2].tolist()
            y_3 = to_draw.T[3].tolist()
            y_4 = to_draw.T[4].tolist()
            y_5 = to_draw.T[5].tolist()
            y_6 = to_draw.T[6].tolist()
            y_7 = to_draw.T[7].tolist()
            y_8 = to_draw.T[8].tolist()
            y_9 = to_draw.T[9].tolist()
            y_10 = to_draw.T[10].tolist()
            y_11 = to_draw.T[11].tolist()
            y_12 = to_draw.T[12].tolist()
            y_13 = to_draw.T[13].tolist()
            y_14 = to_draw.T[14].tolist()
            y_15 = to_draw.T[15].tolist()
            plt.subplots(16,1,1)
            plt.subplots(16,1,2)
            plt.subplots(16,1,3)
            plt.subplots(16,1,4)
            plt.subplots(16,1,5)
            plt.subplots(16,1,6)
            plt.subplots(16,1,7)
            plt.subplots(16,1,8)
            plt.subplots(16,1,9)
            plt.subplots(16,1,10)
            plt.subplots(16,1,11)
            plt.subplots(16,1,12)
            plt.subplots(16,1,13)
            plt.subplots(16,1,14)
            plt.subplots(16,1,15)
            plt.subplots(16,1,16)
            #plt.ylim(-0.01, 0.01 )
            plt.plot(x,y_0,c='blue')
            plt.plot(x,y_1,c='blue',linestyle=':')
            plt.plot(x,y_2,c='blue',linestyle=':')
            plt.plot(x,y_3,c='blue',linestyle=':')
            plt.plot(x,y_4,c='blue',linestyle=':')
            plt.plot(x,y_5,c='blue',linestyle=':')
            plt.plot(x,y_6,c='blue',linestyle=':')
            plt.plot(x,y_7,c='blue',linestyle=':')
            plt.plot(x,y_8,c='blue',linestyle=':')
            plt.plot(x,y_9,c='blue',linestyle=':')
            plt.plot(x,y_10,c='blue',linestyle=':')
            plt.plot(x,y_11,c='blue',linestyle=':')
            plt.plot(x,y_12,c='blue',linestyle=':')
            plt.plot(x,y_13,c='blue',linestyle=':')
            plt.plot(x,y_14,c='blue',linestyle=':')
            plt.plot(x,y_15,c='blue',linestyle=':')
            plt.show()
if __name__ == '__main__':
    readin_process = multiprocessing.Process(target=readin)
    draw_process = multiprocessing.Process(target=draw)
 
    readin_process.start()
    draw_process.start()
