#輝度8x8フレームから2値化画素を重複なしでかきこみ
#(y x r t) r:initial_radius,t:birth_time
import cv2
import numpy as np
input_file=r"C:\Users\nao\Documents\授業課題\研究室\研究\8x8_Basketball(decode_step3).npy"
output_file=r"C:\Users\nao\Documents\授業課題\研究室\研究\Basketball\11\zahyou.txt"
img_8x8=np.load(input_file)#img_8x8.shape=(135, 240, 900) (y,x,z)
MAX_TH=255#輝度値の最大
MAX_8x8_Z=img_8x8.shape[2]#総フレーム数900
R=0.5
y=0
x=0
z=0
vrb=[]#vertex(y,x),radius,birthTime
clearvrb=[]
#二値化した点の集合
while z<MAX_8x8_Z:
    vrb=clearvrb
    while threshold<=MAX_TH:
        p=np.where(img_8x8[:,:,z]==threshold)#p:タプル型
        max_i = len(p[1])
        while i<max_i:
            vrb.append([p[0][i],p[1][i],R,threshold])
            i=i+1;
        threshold = threshold+1
        i=0
    filename=output_file+"\\"+str(z)+".txt"
    with open(filename, 'w') as f:
        f.write()
    np.save(filename,vrb)
    threshold=0
    print(z)
    z=z+1


##二値化した点の集合
#while z<MAX_8x8_Z:
#    while threshold<=MAX_TH:
#        p=np.where(img_8x8[:,:,z]<=threshold)#p:タプル型
#        max_i = len(p[1])
#        pg_temp=pg.tolist()#Numpyの配列をlistに変換
#        while i<max_i:
#            pg_temp.append([p[0][i],p[1][i],threshold])
#            #pg_temp=np.append(pg,np.array([[p[0][i],p[1][i],threshold]]),axis = 0)
#            i=i+1;
#        pg=np.asarray(pg_temp)#listからNumpyの配列に変換
#        threshold = threshold+1
#        i=0
#        print(threshold)
#    threshold=0
#    print(z)
#    z=z+1
#    filename=output_file+"\\"+str(z)+".npy"
#    np.save(filename,pg)