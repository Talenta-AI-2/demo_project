# user.py
import streamlit as st
from database import get_nutritional_info

def input_food():
    foods = []
    st.sidebar.title('Masukkan Makanan')

    input_counter = 0  # Inisialisasi counter untuk membuat kunci unik

    while True:
        input_counter += 1
        food_name = st.sidebar.text_input(f"Masukkan nama makanan {input_counter} (atau ketik 'selesai' untuk mengakhiri): ")
        if food_name.strip().capitalize().lower() == 'selesai':
            break
        if food_name.strip():  # Cek apakah input tidak kosong
            nutrition_info = get_nutritional_info(food_name.strip().capitalize())
            if nutrition_info:
                # Convert nutritional values to float
                nutrition_info = (nutrition_info[0], nutrition_info[1], float(nutrition_info[2]), float(nutrition_info[3]),
                                  float(nutrition_info[4]), float(nutrition_info[5]), float(nutrition_info[6]), float(nutrition_info[7]))
                foods.append(nutrition_info)
            else:
                st.sidebar.warning("Makanan tidak ditemukan di database.")
        else:
            st.sidebar.warning("Nama makanan tidak boleh kosong.")

    if st.sidebar.button("Tambah Makanan"):
        foods.extend(input_food())

    return foods

def input_user_data():
    st.sidebar.title('Masukkan Data Pengguna')

    st.sidebar.subheader('Pilih kelompok umur:')
    age_group_option = st.sidebar.selectbox(
        "Pilih kelompok umur:",
        ["16 - 18 Tahun", "19 - 29 tahun", "30 - 49 tahun"]
    )
    age_group_mapping = {
        "16 - 18 Tahun": 1,
        "19 - 29 tahun": 2,
        "30 - 49 tahun": 3
    }
    age_group = age_group_mapping.get(age_group_option)

    st.sidebar.subheader('Pilih trimester kehamilan:')
    trimester_option = st.sidebar.selectbox(
        "Pilih trimester kehamilan:",
        ["Trimester 1", "Trimester 2", "Trimester 3"]
    )
    trimester_mapping = {
        "Trimester 1": 1,
        "Trimester 2": 2,
        "Trimester 3": 3
    }
    trimester = trimester_mapping.get(trimester_option)

    return age_group, trimester
