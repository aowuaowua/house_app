# Common Libraries used
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Xinyue Cao')
df = pd.read_csv('housing.csv')

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(), 
     df.ocean_proximity.unique())  

dfa = df[df.ocean_proximity.isin(location_filter)]

level_fliter = st.sidebar.radio(
    'choose income level',
    ('low','medium','high')
    )

if level_fliter == 'low':
    dfb = dfa[df.median_income <= 2.5]
elif level_fliter == 'medium':
    dfb = dfa[df.median_income <= 4.5]
elif level_fliter == 'high':
    dfb = dfa[df.median_income > 4.5]
    

price_filter = st.slider('Median House Price:', 0, 500001, 200000)  # min, max, default

dfc = dfb[dfb.median_house_value <= price_filter]

st.map(dfc)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
ax.hist(dfc['median_house_value'], bins=30)
st.pyplot(fig)
