import serial
import matplotlib.pyplot as plt
import numpy  as np
import sys

if not "C:\\ProgramData\\Anaconda3\\Lib\\site-packages" in sys.path:

 PkPath = "C:\\ProgramData\\Anaconda3\\Lib\\site-packages"

 sys.path.append(PkPath)
# 打开 COM17，将波特率配置为115200, 读超时时间为1秒
def readin():
    ser = serial.Serial(port="COM6", baudrate=460800, bytesize=8, parity='N', stopbits=1, timeout=1)
# 读取串口输入信息并输出。
    arr = [0 for i in range(16)]
    to_draw = [[] for k in range(2501)]
    thetime = 0
    while True:
        com_input = ser.read(52)
        if com_input:   # 如果读取结果非空，则输出
            # print(com_input)
            # print("===============================================")
            # print(com_input[0])
            # print(com_input[1])
            # print("===============================================")
            cnt = 0
            for i in range(52):
                cnt = 0
                if(i == 0 or i == 1 or i == 50 or i == 51):
                    continue
                else:
                    tempdata = 0
                    for j in range(i, i+3):
                        inbyte = com_input[j]
                        tempdata = tempdata << 8 + inbyte
                        if((tempdata & 0x00800000) == 0x00800000):
                         tempdata |= 0xFF000000
                        else:
                         tempdata &= 0x00FFFFFF
                        arr[cnt] = tempdata * 0.02235174
                        cnt += 1
                        i = j - 1
            to_draw[thetime] = arr
            if(thetime > 2500):
                to_draw = to_draw[1:]
            #fig = plt.figure()
           # plt.rcParams['font.sans-serif'] = [''] # 正常显示中文字体
            plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
            x = np.linspace(0,5,2500)
            tmpx = thetime
            y_0 = to_draw[tmpx][0]
            y_1 = to_draw[tmpx][1]
            y_2 = to_draw[tmpx][2]
            y_3 = to_draw[tmpx][3]
            y_4 = to_draw[tmpx][4]
            y_5 = to_draw[tmpx][5]
            y_6 = to_draw[tmpx][6]
            y_7 = to_draw[tmpx][7]
            y_8 = to_draw[tmpx][8]
            y_9 = to_draw[tmpx][9]
            y_10 = to_draw[tmpx][10]
            y_11 = to_draw[tmpx][11]
            y_12 = to_draw[tmpx][12]
            y_13 = to_draw[tmpx][13]
            y_14 = to_draw[tmpx][14]
            y_15 = to_draw[tmpx][15]
            fig,(ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13,ax14,ax15,ax16) = plt.subplots(16,16,
                                    figsize=(5,6),
                                    dpi=1000,
                                    # 共享x轴
                                   sharex=True)
            # ax1.plot(x,y_0,c='blue',linestyle=':')
            # ax2.plot(x,y_1,c='blue',linestyle=':')
            # ax3.plot(x,y_2,c='blue',linestyle=':')
            # ax4.plot(x,y_3,c='blue',linestyle=':')
            # ax5.plot(x,y_4,c='blue',linestyle=':')
            # ax6.plot(x,y_5,c='blue',linestyle=':')
            # ax7.plot(x,y_6,c='blue',linestyle=':')
            # ax8.plot(x,y_7,c='blue',linestyle=':')
            # ax9.plot(x,y_8,c='blue',linestyle=':')
            # ax10.plot(x,y_9,c='blue',linestyle=':')
            # ax11.plot(x,y_10,c='blue',linestyle=':')
            # ax12.plot(x,y_11,c='blue',linestyle=':')
            # ax13.plot(x,y_12,c='blue',linestyle=':')
            # ax14.plot(x,y_13,c='blue',linestyle=':')
            # ax15.plot(x,y_14,c='blue',linestyle=':')
            # ax16.plot(x,y_15,c='blue',linestyle=':')
            fig.subplots_adjust(hspace=0.1)
            plt.show()

    ser.close()

if __name__ == '__main__':
    readin()