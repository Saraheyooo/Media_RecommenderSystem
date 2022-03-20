import streamlit as st
import pandas as pd
from random import random


st.set_page_config(layout='wide')

df_movies = pd.read_csv('./dataset/TVNZ_movies_v3.csv')
#print(df_movies[df_movies['index']==0])

if 'ID' not in st.session_state:
  st.session_state['ID'] = 0

df_movie = df_movies[df_movies['ID'] == st.session_state['ID']].iloc[0]



col1, col2 = st.columns(2)


with col1: 
  st.image(df_movie['image'])


with col2:
  st.title(df_movie['title'])
  st.markdown(df_movie['GenreType']+ " Movie")
  st.caption('Mood' + ' : ' + str(df_movie['mood']) + '  |  ' + 'Distributor' + ' : ' + str(df_movie['distributor']))
  st.caption(df_movie['description'])

summary_choice = st.selectbox(' ',["Movie Language","German", "French", "Spanish", 'Japanese','Mandarin', 'Bulgarian','English'])


# genre type
# "Drama", "Comedy", "Action", "Thriller",'Mystery', "Romance","Real Life Story"
st.subheader('Movie Genre')
st.markdown("""
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
  Drama  
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="right" title="Tooltip on right">
  Comedy
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip on bottom">
  Action
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip on bottom">
  Thriller
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip on bottom">
  Mystery
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip on bottom">
  Romance    
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="left" title="Tooltip on left">
  Real Life Story
</button>
""", unsafe_allow_html=True)




st.markdown("***")

def select_movie(movie_id):
  st.session_state['ID'] = movie_id

def tile_item(column, item):
  with column:
    st.button('🍿', key=random(), on_click=select_movie, args=(item['ID'], ))
    st.image(item['image'], use_column_width='always')
    st.caption(item['title'])


def recommendations(df):

  # check the number of items
  nbr_items = df.shape[0]

  if nbr_items != 0:

    # create columns with the corresponding number of items
    columns = st.columns(nbr_items)

    # convert df rows to dict lists
    items = df.to_dict(orient='records')

    # apply tile_item to each column-item tuple (created with python 'zip')
    any(tile_item(x[0], x[1]) for x in zip(columns, items))



st.markdown("***")
# similar content
st.subheader('Similar Content to ' + df_movie['title'])
df_recommendations = df_movies[df_movies['k_means'] == df_movie['k_means']].head(7)
recommendations(df_recommendations)



#same genre of movie
st.subheader('Guess You May Also Like')
df_recommendations = df_movies[df_movies['k_genre'] == df_movie['k_genre']].head(7)
recommendations(df_recommendations)



#diff genre: diversity
st.subheader('Explore More')
df_recommendations = df_movies[df_movies['k_genre'] != df_movie['k_genre']].head(7)
recommendations(df_recommendations)


#top
st.subheader("This Week's Top New Zealand Movies")
top = df_movies[df_movies['Local'] == 1].tail(7)
recommendations(top)
#df_rating = df_movies[df_movies['Rating'] == df_movie['Rating']].head(7)
#df1 = pd.read_csv('ratings.csv')
#df_rating = df1.merge(df_movies, on='ID')
#recommendations(df_rating)


st.markdown("***")
fb1, fb2 = st.columns(2)
with fb1:
  st.subheader('We love hearing from your feedback')
  st.text_area('Feel free to share your feeling with us!').split("\n")

with fb2:
  st.markdown("***")
  st.markdown("***")
  st.radio("The recommended lists match your preference: ",('Yes', 'No'))
  st.markdown("Contact us:  feedback@tvnz.co.nz")

st.markdown("***")
st.info('Your privacy always comes first for us: We secure your data properly and only use them for our services. We will not share your data with third parties for marketing purposes, unless we have received your explicit permission. You decide whether we can use your data for additional TVNZ services. You can modify or delete your data for these services. You can read all about it in our privacy statement.')


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #1a1a5c;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">TVNZ OnDemand</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Movie <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">Live TV</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">News</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://sales.tvnz.co.nz/about-us/" target="_blank">About us</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Channels
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
    <form class="navbar-nav ml-auto">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </ul>  
      <div class="collapse navbar-collapse" id="navbar-collapse-01">    
        <ul class="nav navbar-right">
          <li><a href="#">Login</a></li>
        </ul>
      </div>
    </form>
  </div>
</nav>
""", unsafe_allow_html=True)



st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
