clear all

% folder of results
fdir_results='/Volumes/BigSur_2022/FRF_TIDE/Case_15deg/';

% file range
files=[1:13];

fig=figure(1);
clf
colormap jet
wid=12;
len=10;
set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);


for k=1:length(files) 

numb=files(k);

fnum=sprintf('%.4d',numb);

% read files -----------------------
fname=[fdir_results 'sta_' fnum];

sta=load(fname);

sta(sta(:,2)==0)=NaN;

subplot(5,3,k)
plot(sta(:,1),sta(:,2))
sta=['G ' num2str(k,'%d')];
text(21000,3.,sta)
grid
axis([0 24000 -1 3.5])

if (k == 1 || k==4 || k==7 || k==10 || k==13)
ylabel('\eta')
end
if (k == 11 || k== 12 || k== 13 )
xlabel('time (s)')
end
end

print -djpeg100 plots_movies/time_ser.jpg
print -depsc2 plots_movies/time_ser.eps




