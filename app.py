import streamlit as st
import time
import numpy as np
from random import randrange
import datetime
import pickle
import sklearn


st.title("Flight Price Prediction")
airline = st.selectbox('Select airline',('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'))
source  = st.selectbox('Select source',('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'))
Destination  = st.selectbox('Select Destination',('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'))


Additional_Info = st.selectbox('Select additional info',('In-flight meal not included','No check-in baggage included', '1 Short layover', 'No Info',
                                                         '1 Long layover', 'Change airports', 'Business class','Red-eye flight', '2 Long layover'))



#encode source
if source == 'Banglore':
    s = 0
elif source == 'Kolkata':
    s = 3
elif source == 'Delhi':
    s = 2
elif source == 'Chennai':
    s = 1
else:
    s = 4
    
#encode airline
    
if source == 'IndiGo':
    a = 3
elif source == 'Air India':
    a = 1
elif source == 'Jet Airways':
    a = 4
elif source == 'SpiceJet':
    a = 8
elif source == 'Vistara':
    a = 10
elif source == 'Air Asia':
    a = 8
elif source == 'Trujet':
    a = 2
elif source == 'GoAir':
    a = 6
else:
    a = 5
    
    
#encode Destination

if source == 'Delhi':
    d = 2
elif source == 'New Delhi':
    d = 5
elif source == 'Banglore':
    d = 0
elif source == 'Cochin':
    d = 1
elif source == 'Kolkata':
    d = 4
elif source == 'Hyderabad':
    d = 3
else:
    d = 3


#encode additional info
if source == 'In-flight meal not included':
    ai = 5
elif source == 'No check-in baggage included':
    ai = 2
elif source == '1 Short layover':
    ai = 4
elif source == 'No Info':
    ai = 8
elif source == '1 Long layover':
    ai = 3
else:
    ai = 1

    

r1 = d
r2 = randrange(45)

r3 = randrange(30)
r4 = randrange(13)
r5 = randrange(5)
Stop = 2
Arrival_Minute = 10
Departure_Minute = 10
Arrival_Hour  = 1
Departure_Hour = 22

date = st.date_input('Pick date of flight')
e = str(date)
x = e.replace("-", "/")
li = x.split("/")

year = int(li[0])
day = int(li[2])
month = int(li[1])
z = datetime.date(year,month,day)
s = int(z.weekday())

if s > 5:
  day_type = 1 
else:
  day_type = 2


model2 = pickle.load(open('ext_tree_without_pycaret1.pkl','rb'))
b = model2.predict([[a,s,d,ai,day,month,day_type,Stop,Arrival_Hour,Arrival_Minute,Departure_Hour,Departure_Minute,r1,r2,r3,r4,r5]])

if st.button('Check your bill'):
    st.write('Your bill is')
    b = model2.predict([[a,s,d,ai,day,month,day_type,Stop,Arrival_Hour,Arrival_Minute,Departure_Hour,Departure_Minute,r1,r2,r3,r4,r5]])
    st.write(b)
else:
    pass
