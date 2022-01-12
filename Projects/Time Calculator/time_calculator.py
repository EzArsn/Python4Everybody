def add_time(start, duration,date_start=""):
  #segregating data from given
  sp=start.find(' ')
  s_c=start.find(':')
  h=int(start[:s_c])
  m=int(start[s_c+1:s_c+3])
  #s means session not seconds
  s=start[sp+1:]
  if s=='PM':
    h=h+12
  d_c=duration.find(':')
  d_h=int(duration[:d_c])
  d_m=int(duration[d_c+1:d_c+3])
  date=date_start.lower()
  
  #addition part
  n_m=m+d_m
  carry=0
  if n_m>60:
    n_m=n_m-60
    carry=1
  if n_m<10:
    n_m='0'+str(n_m)
  n_h=h+d_h+carry

  #formatting part
  car_day=0
  n_d=''
  if n_h>24:
    car_day=int(n_h/24)
    if car_day==1:
      n_d='(next day)'
    elif car_day>1:
      n_d= '('+str(car_day)+' days later)'
    n_h=n_h%24
  if n_h>=12:
      s='PM'
  else:
      s='AM'
  if n_h>12:
      n_h=n_h-12
  if n_h==0:
      n_h=12
  
  #finding day
  day=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
  Day=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  day_given=date_start.lower()
  num_day=0
  n_day=0
  for i in day:
    if i==day_given:
      break
    num_day+=1
  n_day=(num_day+car_day)%7
  date_end=Day[n_day]

  #final string output
  fin_tim=str(n_h)+':'+str(n_m)+' '+s
  if n_d=='' and date_start=="":
    new_time=fin_tim
  elif n_d!='' and date_start=="":
    new_time=fin_tim+' '+n_d
  elif n_d=='' and date_start!="":
    new_time=fin_tim+', '+date_start
  else:
    new_time=fin_tim+', '+date_end+' '+n_d
 
  return new_time

#add_time("11:30 PM", "03:30")