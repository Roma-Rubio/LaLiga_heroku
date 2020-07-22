#%%
import pandas as pd 
df = pd.read_csv("/Users/romacencerradorubio/Desktop/MLprojects/laligacampeones/LaLiga.csv") 
print(df.head())

import streamlit as st
import pandas as pd
import numpy 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

'''
Season - period of the match

Date - date of the match

HomeTeam - the name of the home team

AwayTeam - the name of the away team

FTHG (Full-time home goals) 

FTAG (Full time away goals)

FTR (Full-time result)
H: Home team won
A: Away team won
D: Draw

HTHG (Half time home goals)

HTAG (Half time away goals) 

HTR (half time result)
H: Home team won
A: Away team won
D: Draw
'''

st.title('La Liga match results')
df = pd.read_csv("/Users/romacencerradorubio/Desktop/MLprojects/laligacampeones/LaLiga.csv")

if st.checkbox('Show all data'):
    st.write(df)

st.subheader('Choose your team')
teams = st.multiselect('Pick your teams', df['HomeTeam'].unique())
#unique asi no se puede elegir el mismo equipo otra vez en la seleccion
new_df = df[(df['HomeTeam'].isin(teams)) | (df['AwayTeam'].isin(teams))]



st.subheader('Show only matches from the Home team, or just Away team? your choice!')

if st.checkbox('Show only home matches from the picked team/teams'):
    st.write(df[(df['HomeTeam'].isin(teams))])
if st.checkbox('Show only away matches from the picked team/teams'):
    st.write(df[(df['AwayTeam'].isin(teams))])
if st.checkbox('Show all the matches with the picked team'):    
    st.write(new_df)




st.subheader('Choose season')
dato = st.multiselect('Choose a season',df['Season'].unique())

st.subheader('Choose dato')
dato = st.multiselect('Choose a date',df['Date'].unique())


#team_wins = st.selectbox('Pick your teams', df['HomeTeam'].unique()) 
#new_df_wins = df[(df['home_team']==team_wins)|(df['away_team']==team_wins)]
#new_df_wins=new_df_wins.reset_index(drop=True)


#fig, ax= plt.subplots()
#ax.plot(x,y)

# %%
#df.groupby('FTAG').mean()
#df2=df.groupby('FTR').count()
#print(df2)
st.subheader('Comparing 2 teams')
teams_to_compare= st.multiselect('Pick your teams(en script solo home y unoque)',
df['HomeTeam'].unique())
comparision= df["HomeTeam"].isin(teams)
comparision2= df["AwayTeam"].isin(teams)
st.write(comparision)
st.write(comparision2)



# %%
