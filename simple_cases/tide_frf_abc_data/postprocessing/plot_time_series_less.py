clear all

% folder of results
fdir_results='/Volumes/BigSur_2022/FRF_TIDE/Case_15deg_longrun/';

% file range
files=[1 4 7 10 12 13];

fig=figure(1);
clf
colormap jet
wid=12;
len=9;
set(fig,'units','inches','paperunits','inches','papersize', [wid len],'position',[1 1 wid len],'paperposition',[0 0 wid len]);


for k=1:length(files) 

numb=files(k);

fnum=sprintf('%.4d',numb);

% read files -----------------------
fname=[fdir_results 'sta_' fnum];

sta=load(fname);

sta(sta(:,2)==0)=NaN;

subplot(2,3,k)
plot(sta(:,1)/3600,sta(:,2))
sta=['G ' num2str(k,'%d')];
text(24.0,3.,sta)
grid
axis([0 26.6 -2 3.5])

if (k == 1 || k==4)
ylabel('\eta')
end
if (k == 4 || k== 5 || k== 6 )
xlabel('time (hr)')
end
end

print -djpeg100 plots_movies/time_ser_less.jpg
print -depsc2 plots_movies/time_ser_less.eps




