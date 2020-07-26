# %%
⚽️
import pandas as pd 

url= "https://raw.githubusercontent.com/Roma-Rubio/LaLiga_heroku/master/LaLiga.csv"
df = pd.read_csv("https://raw.githubusercontent.com/Roma-Rubio/LaLiga_heroku/master/LaLiga.csv",sep=",")
print(df.head())

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#from PIL import Image
#image = Image.open("stadium.png")
#"File-Santiago Bernabeu Stadium - panoramio.jpg" by AudaCity3371 is licensed under CC BY-SA 3.0
#st.image(image, caption='',
#          use_column_width=True)
#la imagen tiene que estar guardada en la misma carpeta que el python, en este caso esta en el folder
#de heroku que esta en el escritorio



st.title('La Liga de Campeones results')
df = pd.read_csv("https://raw.githubusercontent.com/Roma-Rubio/LaLiga_heroku/master/LaLiga.csv",sep=",")

if st.checkbox('Show dataframe'):
    st.write(df)


st.subheader('Filtering dataset per team')
teams = st.multiselect('Pick your teams', df['HomeTeam'].unique())
new_df = df[(df['HomeTeam'].isin(teams)) | (df['AwayTeam'].isin(teams)) ]
if st.checkbox('Show only home matches'):
    st.write(df[(df['HomeTeam'].isin(teams))])
if st.checkbox('Show only away matches'):
    st.write(df[(df['AwayTeam'].isin(teams))])
if st.checkbox('Show entire dataset'):    
    st.write(new_df)
    


st.subheader('Filtering dataset per season')
events = st.multiselect('Pick your season', df['Season'].unique())
new_df_season = new_df[(new_df['Season'].isin(events))]
st.write(new_df_season)
st.write(new_df)



st.subheader('Choose a team to see their performance classification')


st.subheader('Classification of wins, losses and draws per team')
team_wins = st.selectbox('Pick your teams', df['HomeTeam'].unique()) 
new_df_wins = df[(df['HomeTeam']==team_wins)|(df['AwayTeam']==team_wins)]
new_df_wins=new_df_wins.reset_index(drop=True)
    
    
wins = 0
losses = 0
draw = 0
x = []    
    
for i in range(len(new_df_wins)):
    if new_df_wins['HomeTeam'][i]==team_wins:
        if new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            wins+=1
            x.append(1)
        elif new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            losses+=1
            x.append(-1)
        else:
            draw +=1
            x.append(0)
    else:
        if new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            wins+=1
            x.append(1)
        elif new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            losses+=1
            x.append(-1)
        else:
            draw +=1
            x.append(0)
    
    
labels = ['Wins','Losses','Draws']
values = [wins, losses, draw]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

colors =['red','brown','orange']                 
fig.update_traces(hoverinfo="label+percent+name",marker=dict(colors=colors))


st.plotly_chart(fig)
#fig2 = go.Figure()
#fig2.add_trace(go.Scatter(x=list(new_df_wins['Date']), y=x))
# Add range slider

#st.plotly_chart(fig2)


wins_h = 0
losses_h = 0
draw_h = 0
wins_a = 0
losses_a = 0
draw_a = 0
for i in range(len(new_df_wins)):
    if new_df_wins['HomeTeam'][i]==team_wins:
        if new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            wins_h+=1
        elif new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            losses_h+=1
        else:
            draw_h+=1
for i in range(len(new_df_wins)):
    if not new_df_wins['HomeTeam'][i]==team_wins:
        if new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            wins_a+=1
        elif new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            losses_a+=1
        else:
            draw_a +=1
values_home = [wins_h, losses_h, draw_h]
values_away = [wins_a, losses_a, draw_a]
fig3 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])




#fig3.upDate_layout(
 #   title_text="Wins, losses and draws home vs away",
  #  annotations=[dict(text='Home', x=0.18, y=0.5, font_size=20, showarrow=False),
   #              dict(text='Away', x=0.82, y=0.5, font_size=20, showarrow=False)])
#fig3.upDate_traces(hole=.4, hoverinfo="label+percent+name")


#st.plotly_chart(fig3)



wins_h = 0
losses_h = 0
draw_h = 0
wins_a = 0
losses_a = 0
draw_a = 0
for i in range(len(new_df_wins)):
    if new_df_wins['HomeTeam'][i]==team_wins:
        if new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            wins_h+=1
        elif new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            losses_h+=1
        else:
            draw_h+=1
for i in range(len(new_df_wins)):
    if not new_df_wins['HomeTeam'][i]==team_wins:
        if new_df_wins['FTHG'][i]<new_df_wins['FTAG'][i]:
            wins_a+=1
        elif new_df_wins['FTHG'][i]>new_df_wins['FTAG'][i]:
            losses_a+=1
        else:
            draw_a +=1
values_home = [wins_h, losses_h, draw_h]
values_away = [wins_a, losses_a, draw_a]
fig3 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig3.add_trace(go.Pie(labels=labels, values=values_home, name="Home"),
              1, 1)
fig3.add_trace(go.Pie(labels=labels, values=values_away, name="Away"),
              1, 2)
fig3.update_layout(
    title_text="Wins, losses and draws home vs away",
    annotations=[dict(text='Home', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='Away', x=0.82, y=0.5, font_size=20, showarrow=False)])
colors =['red','brown','orange']                  
fig3.update_traces(hole=.4, hoverinfo="label+percent+name",marker=dict(colors=colors))
st.plotly_chart(fig3)









st.header('Best and wrost performance of the choosen team')


st.subheader('Top score')
t = []
for i in range(len(new_df_wins)):
    if new_df_wins['HomeTeam'][i]==team_wins:
        t.append(new_df_wins['FTHG'][i])
    else:
        t.append(new_df_wins['FTAG'][i])
        
        
m = np.argmax(np.array(t), axis=0)
out = new_df_wins.iloc[m]
st.write(out)


st.subheader('Lowest score')
t = []
for i in range(len(new_df_wins)):
    if new_df_wins['HomeTeam'][i]==team_wins:
        t.append(new_df_wins['FTHG'][i])
    else:
        t.append(new_df_wins['FTAG'][i])
        
        
m = np.argmin(np.array(t), axis=0)
out = new_df_wins.iloc[m]
st.write(out)


