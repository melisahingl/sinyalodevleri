clc; clear all; close all;
                                     %%%%%%%%%%%%% 1. kısım %%%%%%%%%%%%%
tuslar = {'1','2','3';'4','5','6';'7','8','9';'*','0','#'};
satirlar = [697 770 852 941]; 
sutunlar = [1209 1336 1477];  

Fsample  = 8000;       
N = 1700;          
t   = (0:N-1)/Fsample;
pit = 2*pi*t;
A = 0.3;
sinfonk  = [];

for r=1:4
    for c=1:3
        sinfonk = [sinfonk; A*sin(pit*satirlar(r))+A*sin(pit*sutunlar(c)) ];
    end
end

nsinfonk = sinfonk.';

% 0 is 11
myphone = [nsinfonk(:,11) ; zeros(2000,1);nsinfonk(:,5);zeros(2000,1);nsinfonk(:,3);zeros(2000,1);nsinfonk(:,9);zeros(2000,1);nsinfonk(:,6);zeros(2000,1);nsinfonk(:,8);zeros(2000,1);nsinfonk(:,11);zeros(2000,1);nsinfonk(:,3);zeros(2000,1);nsinfonk(:,9);zeros(2000,1);nsinfonk(:,7);zeros(2000,1);nsinfonk(:,5)];
%audiowrite("Numaram.wav",myphone,Fsample);



                                     %%%%%%%%%%%%% 2. kısım %%%%%%%%%%%%%
[num,fs] = audioread('Numaram.wav');

%    tSampling=1/fs;
%n=numel(num);
%t=-0.005:tSampling:-0.005+(n-1)*tSampling;
%plot(t,num);
%xlabel("Time");
%ylabel("Amplitude");


%11 rakam var
d = floor(length(num)/11);

num1=num(1:d);
num2=num(d+1:2*d);
num3=num(2*d+1:3*d);
num4=num(3*d+1:4*d);
num5=num(4*d+1:5*d);
num6=num(5*d+1:6*d);
num7=num(6*d+1:7*d);
num8=num(7*d+1:8*d);
num9=num(8*d+1:9*d);
num10=num(9*d+1:10*d);
num11=num(10*d+1:11*d);
bolelim=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11];
benimnumdogrumu =[];

for i=1:11

fA=fftshift(fft(bolelim(:,i)))*(1/fs);              
f=-fs/2:fs/length(fA):fs/2-fs/length(fA);

fsec = sort(unique(abs(fA)),"descend");
fsec = fsec(1:2);
kucuk=min(fsec);
buyuk=max(fsec);

ind = find(abs(fA) == buyuk); 
f2= abs(f(ind));
f2=f2(1);

ind2 = find( abs(fA) == kucuk); 
f1= abs(f(ind2));
f1=f1(1);

if f1>f2
    temp=f2;
    f2=f1;
    f1=temp;
end

if ((f1>692) & (f1<720))
    row=1;
elseif ((f1>765) & (f1<800))
    row=2;
elseif ((f1>847) & (f1<880))
    row=3;
elseif ((f1>936) & (f1<960))
    row=4;
end

if ((f2>1204) & (f2<1240))
    col=1;
elseif ((f2>1331) & (f2<1360))
    col=2;
elseif ((f2>1472) & (f2<1500))
    col=3;
elseif ((f2>1628) & (f2<1660))
    col=4;
end

numara = tuslar{row,col};
%plot(abs(f),abs(fA));
%title(numara);
%xlabel("Frequency");
%ylabel("Amplitude");
%figure();

benimnumdogrumu = [benimnumdogrumu numara];
benimnumdogrumu
%dogru:))
end


                                     %%%%%%%%%%%%% 3. kısım %%%%%%%%%%%%%
[tel,fs] = audioread('Ornek.wav');

%Duration = (length(tel))/fs;
%ti = 0:seconds(1/fs):seconds(Duration);
%ti = ti(1:end-1);
%stem(ti,tel)
%xlabel("Time")
%ylabel("Amplitude")

%11 peaks, which means 11 numbers
d = floor(length(tel)/11);

tel1=tel(1:d);
tel2=tel(d+1:2*d);
tel3=tel(2*d+1:3*d);
tel4=tel(3*d+1:4*d);
tel5=tel(4*d+1:5*d);
tel6=tel(5*d+1:6*d);
tel7=tel(6*d+1:7*d);
tel8=tel(7*d+1:8*d);
tel9=tel(8*d+1:9*d);
tel10=tel(9*d+1:10*d);
tel11=tel(10*d+1:11*d);
parcaparca=[tel1,tel2,tel3,tel4,tel5,tel6,tel7,tel8,tel9,tel10,tel11];
numaralar =[];

for i=1:11

fA=fftshift(fft(parcaparca(:,i)))*(1/fs);             
f=-fs/2:fs/length(fA):fs/2-fs/length(fA);

fsec = sort(unique(abs(fA)),"descend");
fsec = fsec(1:2);
kucuk=min(fsec);
buyuk=max(fsec);

ind = find(abs(fA) == buyuk); 
f2= abs(f(ind));
f2=f2(1);

ind2 = find( abs(fA) == kucuk); 
f1= abs(f(ind2));
f1=f1(1);

if f1>f2
    temp=f2;
    f2=f1;
    f1=temp;
end

if ((f1>692) & (f1<720))
    row=1;
elseif ((f1>765) & (f1<800))
    row=2;
elseif ((f1>847) & (f1<880))
    row=3;
elseif ((f1>936) & (f1<960))
    row=4;
end

if ((f2>1204) & (f2<1240))
    col=1;
elseif ((f2>1331) & (f2<1360))
    col=2;
elseif ((f2>1472) & (f2<1500))
    col=3;
elseif ((f2>1628) & (f2<1660))
    col=4;
end
numara = tuslar{row,col};
%plot(abs(f),abs(fA));
%title(numara);
%xlabel("Frequency");
%ylabel("Amplitude");
%figure();
numaralar = [numaralar numara];
end
numaralar