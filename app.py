import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d2d206d805cf81572b43a90d2bb4084b&language=en-US'.format(movie_id))
    data=response.json()
    # print(data)
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recomend(movie):
    print("")
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity_matrix[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recomended_movies_list=[]
    recomended_movies_poster=[]
    for i in movie_list:
        movie_id=new_df.iloc[i[0]].movie_id
        movie_name=new_df.iloc[i[0]].title
        movie_poster=fetch_poster(movie_id)

        recomended_movies_list.append(movie_name)
        recomended_movies_poster.append(movie_poster)
    return recomended_movies_list,recomended_movies_poster

# movies dataframe....
new_df=pickle.load(open('movies.pkl','rb'))

# similarity_matrix...
similarity_matrix=pickle.load(open('similarity.pkl','rb'))

# movies list....
movies_list=new_df['title'].values





st.title("Movie Recomendation System")
option = st.selectbox('Select a Movie',movies_list)


if st.button('Recomend'):
    names,posters=recomend(option)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])




