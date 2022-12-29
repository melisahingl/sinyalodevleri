import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.ndimage.interpolation import shift
import time

# Birinci soru

def shift2(arry, n=0):
    if n==0:
        return arry
    elif n==np.size(arry):
        return [0 for i in range(np.size(arry))]
    else:
        a=n%(np.size(arry))
        s=np.array([0 for i in range(a)])
        return np.concatenate((s,arry[:-a]))

def MyConv(x,y,n,m):


    n=np.size(x)
    m=np.size(y)
    if n==m:
        x=np.flip(x)
        for i in range(n-1):
            x=np.append(x,0)
        for i in range(m-1):
            y=np.insert(y,0,0)
        tempor=[]
        t=np.zeros(np.size(x))
        for i in range(np.size(x)+1):
            a=shift2(x,i)
            sum=0
            for j in range(np.size(x)):
                sum=sum+a[j]*y[j]   
            tempor.append(sum)
        tempor.pop()
        t=np.array(tempor)
    elif m>n:
        x=np.flip(x)
        for i in range(m-1):
            x=np.append(x,0)
        for i in range(n-1):
            y=np.insert(y,0,0)
        tempor=[]
        for i in range(np.size(x)+1):
            a=shift2(x,i)
            sum=0
            for j in range(np.size(x)):
                sum=sum + a[j]*y[j]    
            tempor.append(sum)
        tempor.pop()
        t=np.array(tempor) 
    else:
        y=np.flip(y)
        for i in range(n-1):
            y.append(y,0)
        for i in range(m-1):
            x.insert(0,0)
        t=[]
        for i in range(np.size(x)+1):
            a=shift2(x,i)
            sum=0
            for j in range(np.size(x)):
                sum=sum + a[j]*y[j]    
            tempor.append(sum)
        tempor.pop()
        t=np.array(tempor) 
    return t

# İkinci soru

n=int(input("1. listenin boyutunu giriniz: "))
x=np.zeros(n)
for i in range(n):
    x[i]= (int(input("1. listeyi giriniz: ")))
x1=x.copy()
m=int(input("2. listenin boyutunu giriniz: "))
y=np.zeros(m)
for i in range(m):    
    y[i]= (int(input("2. listeyi giriniz: ")))
y1=y.copy()
k=np.convolve(x,y)
mconv=MyConv(x1,y1,len(x),len(y))
fig,axs = plt.subplots(2,2)
fig.suptitle("Grafikler")
axs[0,0].stem([(i-1) for i in range(n)],x)
axs[0,1].stem([(i) for i in range(m)],y)
axs[1,0].stem([(i-1) for i in range(len(mconv))],mconv)
axs[1,1].stem([(i-1) for i in range(len(k))],k)
plt.show()
print("X[n]:",x)
print("Y[n]:",y)
print("MyConv:",mconv)
print("Hazır fonksiyon:",k)

# Üçüncü soru

freq = 44100
duration = 5
print("Birinci ses kaydı kaydediliyor.")
recording1 = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()
print("Kayıt bitti.")

duration = 10
print("İkinci ses kaydı kaydediliyor.")
recording2 = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()
print("Kayıt bitti.")


# Dördüncü soru

def shift3(arry, adım):
    for i in range(adım):
        arry=np.append(arry,0)
    return arry

newrecording1=recording1.copy()
newrecording2=recording2.copy()

#m=2 için 

m=2
############# 5 sn 
recodring1_vol2 = shift3(newrecording1,m*400)
sum=np.zeros(np.size(recodring1_vol2))
for i in range(m):  
    sum=sum+ (shift(recodring1_vol2, 400))*(m+1)
Y1_1 =  np.add(recodring1_vol2,sum*0.8)
final1 = np.convolve(recodring1_vol2, Y1_1)

sd.play(final1, samplerate=freq)
time.sleep(20)
sd.stop()

my1= MyConv(recodring1_vol2, Y1_1, np.size(recodring1_vol2),np.size(Y1_1))
sd.play(my1, samplerate=freq)
time.sleep(20)
sd.stop()

############# 10 sn 
recodring2_vol2 = shift3(newrecording2,m*400)
sum=np.zeros(np.size(recodring2_vol2))
for i in range(m):   
    sum=sum+ (shift(recodring2_vol2, 400))*(m+1)
Y2_1 =  np.add(recodring2_vol2,sum*0.8)
final2 = np.convolve(recodring2_vol2, Y2_1)

sd.play(final2, samplerate=freq)
time.sleep(20)
sd.stop()

my2= MyConv(recodring2_vol2, Y2_1, np.size(recodring2_vol2),np.size(Y2_1))
sd.play(my2, samplerate=freq)
time.sleep(20)
sd.stop()

# bilgisayara kaydetmek için yazmıştım
"""
write("MYnp_10_m_2.wav", freq, my2)
write("np_10_m_2.wav", freq, final2)
write("np_5_m_2.wav", freq, final1)  
write("MYnp_5_m_2.wav", freq, my1) 
"""


#m=3 için 

m=3

############# 5 sn 
recodring1_vol3 = shift3(newrecording1,m*400)
sum=np.zeros(np.size(recodring1_vol3))
for i in range(m):  
    sum=sum+ (shift(recodring1_vol3, 400))*(m+1)
Y1_3 =  np.add(recodring1_vol3,sum*0.8)
final3 = np.convolve(recodring1_vol3, Y1_3)
sd.play(final3, samplerate=freq)
time.sleep(20)
sd.stop()

my3= MyConv(recodring1_vol3, Y1_3, np.size(recodring1_vol3),np.size(Y1_3))
sd.play(my3, samplerate=freq)
time.sleep(20)
sd.stop()

############# 10 sn 
recodring2_vol4 = shift3(newrecording2,m*400)
sum=np.zeros(np.size(recodring2_vol4))
for i in range(m): 
    sum=sum+ (shift(recodring2_vol4, 400))*(m+1)
Y1_4 =  np.add(recodring2_vol4,sum*0.8)
final4 = np.convolve(recodring2_vol4, Y1_4)
sd.play(final4, samplerate=freq)
time.sleep(20)
sd.stop()

my4= MyConv(recodring2_vol4, Y1_4, np.size(recodring2_vol4),np.size(Y1_4))
sd.play(my4, samplerate=freq)
time.sleep(20)
sd.stop()


"""
write("MYnp_10_m_3.wav", freq, my4)
write("np_10_m_3.wav", freq, final4)
write("MYnp_5_m_3.wav", freq, my3)
write("np_5_m_3.wav", freq, final3)
"""


#m=4 için 

m=4
############# 5 sn 
recodring1_vol5 = shift3(newrecording1,m*400)
sum=np.zeros(np.size(recodring1_vol5))
for i in range(m):   
    sum=sum+ (shift(recodring1_vol5, 400))*(m+1)
Y1_5 =  np.add(recodring1_vol5,sum*0.8)
final5 = np.convolve(recodring1_vol5, Y1_5)
sd.play(final5, samplerate=freq)
time.sleep(20)
sd.stop()

my5= MyConv(recodring1_vol5, Y1_5, np.size(recodring1_vol5),np.size(Y1_5))
sd.play(final4, samplerate=freq)
time.sleep(20)
sd.stop()

############# 10 sn 
recodring2_vol6 = shift3(newrecording2,m*400)
sum=np.zeros(np.size(recodring2_vol6))
for i in range(m):   
    sum=sum+ (shift(recodring2_vol6, 400))*(m+1)
Y2_6 =  np.add(recodring2_vol6,sum*0.8)
final6 = np.convolve(recodring2_vol6, Y2_6)
sd.play(final6, samplerate=freq)
time.sleep(20)
sd.stop()

my6=MyConv(recodring2_vol6, Y2_6, np.size(recodring2_vol6),np.size(Y2_6))
sd.play(final4, samplerate=freq)
time.sleep(20)
sd.stop()

"""
write("MYnp_10_m_4.wav", freq, my6)
write("np_10_m_4.wav", freq, final6)
write("MYnp_5_m_4.wav", freq, my5)
write("np_5_m_4.wav", freq, final5)
"""