import streamlit as st
import urllib.request
import json
import os
import ssl
import time

def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

def call_azure_ml_service(age, gender, height):
    data = {
        "input_data": {
            "columns": [
                "Umur (bulan)",
                "Jenis Kelamin",
                "Tinggi Badan (cm)"
            ],
            "index": [0],
            "data": [
                [age, gender, height]
            ]
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://mlw-automl-stuntingapps-dsjxl.southeastasia.inference.ml.azure.com/score'
    api_key = 'bXMLS1MTI2gwsqgtRuEQLMXfPMTVsR8y'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
        'azureml-model-deployment': 'stunting-v1'
    }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        return json.loads(result)
    except urllib.error.HTTPError as error:
        st.error(f"The request failed with status code: {error.code}")
        st.error(error.read().decode("utf8", 'ignore'))
        return None

def main():
    st.title("Prediksi Stunting")

    st.header("Masukkan Data")
    age = st.number_input("Umur (bulan)", min_value=0)
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    height = st.number_input("Tinggi Badan (cm)", min_value=0.0)

    if st.button("Prediksi"):
        with st.spinner('Memproses...'):
            result = call_azure_ml_service(age, gender, height)
            time.sleep(2)
            if result:
                st.success("Prediksi berhasil!")
                try:
                    prediction = result[0]  # Mengakses elemen pertama dari list prediksi
                    st.markdown(f"<h1 style='text-align: center; color: green; font-size: 60px; font-weight: bold;'>{prediction}</h1>", unsafe_allow_html=True)
                except (KeyError, IndexError, TypeError) as e:
                    st.error("Struktur data hasil tidak sesuai.")
            else:
                st.error("Gagal mendapatkan prediksi. Coba lagi.")

if __name__ == "__main__":
    main()
