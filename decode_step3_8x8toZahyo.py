import cv2
import numpy as np
input_file = r"C:\Users\kawahara15\Desktop\研究\8x8_Basketball(decode_step3).npy"
output_file = r"C:\Users\kawahara15\Desktop\研究\Basketball\11"
img_8x8=np.load(input_file)#img_8x8.shape=(135, 240, 900) (y,x,z)
MAX_TH=255#輝度値の最大
MAX_8x8_Z=img_8x8.shape[2]#総フレーム数900
R=0.5
y=0
x=0
z=0
i=0
threshold=0
vrb=[]#vertex(y,x),radius,birthTime
#clearvrb=[]
#二値化した点の集合
while z<MAX_8x8_Z:
    vrb.clear()#list_vrbを空にする
    while threshold<=MAX_TH:
        p=np.where(img_8x8[:,:,z]==threshold)#p:タプル型
        max_i = len(p[1])
        while i<max_i:
            #vrb.append(p[0][i],p[1][i],R,threshold)
            vrb.append([p[0][i],p[1][i],R,threshold])
            i=i+1;
        threshold = threshold+1
        i=0
    filename=output_file+"\\"+str(z)+"_zhahyo.txt"
    with open(filename, 'w') as f:#zahyouを書き込み
        k=0
        max_k=len(vrb)
        f.write("2"+"\n")
        while k<max_k:
            text=""
            text=str(vrb[k])+"\n"
            table = text.maketrans({
             ',': '', #左が置換したい文字、右が新しい文字。
             '[': '', #左が置換したい文字、右が新しい文字。
             ']': '', #左が置換したい文字、右が新しい文字。
            })
            f.write(text.translate(table))
            #f.write(str(vrb[k])+"\n")
            k=k+1
    threshold=0
    print(z)
    z=z+1
