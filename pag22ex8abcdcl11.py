t=[7,7,5,6,5,5,6,7,8,8,11,11,10,13,11,12,12,12,11,10,10,9,8,6]
h=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
print('Temperatura medie este',sum(t)/24)
print('Temperatura maxima este', max(t))
print('Temperatura minima este ', min(t))
max=t.index(max(t))
print('Ora cand s-a inregistrat temperatura maxima este', max)
min=t.index(min(t))
print('Ora cand s-a inregistrat temperatura minima este', min)