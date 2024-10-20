import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def filter_and_sort_data(df: pd.DataFrame, gender: str, age: str, education: str, fav_animals: str, fav_place: str) -> pd.DataFrame: 

    df_copy = df.copy()
    if gender != "Wszyscy":
        df_copy = df_copy[df_copy['gender'] == gender]
    if gender == "Mężczyźni":
        df_copy = df[df['gender'] == 0.0 ]
    elif gender == "Kobiety":
        df_copy = df[df['gender'] == 1.0 ]
    elif gender == "Płeć nieznana":
        df_copy = df[df['gender'] == 'nan']

    if age != "Wszyscy":
        df_copy = df_copy[df_copy['age'] == age]    
    if education != "Wszystkie":
        df_copy = df_copy[df_copy['edu_level'] == education]
    if Ulubione_zwierzę != "Wszystkie":
        df_copy = df_copy[df_copy['fav_animals'] == fav_animals]
    if Ulubione_miejsce != "Wszystkie":
        df_copy = df_copy[df_copy['fav_place'] == fav_place]
        
    df_copy = df_copy.sort_values(by="gender")
    df_copy = df_copy.sort_values(by="age")
    df_copy = df_copy.sort_values(by="edu_level") 
    df_copy = df_copy.sort_values(by="fav_animals") 
    df_copy = df_copy.sort_values(by="fav_place")
    return df_copy


df = pd.read_csv("35__welcome_survey_to_Homework1.csv", sep=";")


col1, col2= st.columns([1, 7])
with col1:
    st.image("https://previews.123rf.com/images/alexmas/alexmas1610/alexmas161000003/67144356-3d-cz%C5%82owiek-z-lup%C4%85-i-znakiem-zapytania-obraz-3d-bia%C5%82e-t%C5%82o.jpg")
with col2:
    st.title('Łowca Danych')


with st.sidebar.title("Złów dane"):
    gender = st.sidebar.selectbox("Wybierz płeć", ["Wszyscy", "Kobiety", "Mężczyźni", "Płeć nieznana"], index=0)
    if gender:
        Wiek = st.sidebar.selectbox("Wybierz wiek", ["Wszyscy", "<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">=65"], index=0)
        Wykształcenie = st.sidebar.selectbox("Wybierz wykształcenie", ["Wszystkie", "Podstawowe", "Średnie", "Wyższe"], index=0)
        Ulubione_zwierzę = st.sidebar.selectbox("Wybierz zwierzę", ["Wszystkie", "Psy", "Koty", "Inne"], index=0)
        Ulubione_miejsce = st.sidebar.selectbox("Wybierz miejsce", ["Wszystkie", "Nad wodą", "W lesie", "W górach", "Inne"], index=0)



filtered_data = filter_and_sort_data(df, gender, Wiek, Wykształcenie, Ulubione_zwierzę, Ulubione_miejsce)

if not filtered_data.empty:
    fig, ax = plt.subplots()
    ax.bar(filtered_data['gender'], range(len(filtered_data)))
    ax.set_title('Liczba osób z wybranymi atrybutami')
    ax.set_xlabel(gender)
    ax.set_xticks([])
    ax.set_ylabel('Liczba urzytkowników')
    st.pyplot(fig)
else:
    st.write("Brak danych spełniających wybrane kryteria.")

