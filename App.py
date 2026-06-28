import streamlit as st
import requests

# GitHub'daki JSON dosyanın linki
URL = 'https://raw.githubusercontent.com/mert-kekik/Futbolveri/refs/heads/main/Veri.json'

st.title("Spor Veri Sorgulama")

# 1. Kullanıcıdan takım ismini al
arama = st.text_input("Takım adını girin (Örn: galatasaray, fenerbahce):").lower().strip()

if arama:
    try:
        # Veriyi çek
        response = requests.get(URL)
        data = response.json()
        
        # 2. Doğrudan eşleşen anahtarı bul (lookup)
        if arama in data:
            takim_bilgileri = data[arama]
            
            # 3. Verileri ekrana şık bir şekilde bas
            st.subheader(f"{takim_bilgileri['takimIsmi']} Verileri")
            
            # Her bir veriyi liste olarak yazdır
            for key, value in takim_bilgileri.items():
                st.write(f"**{key.capitalize()}:** {value}")
        else:
            st.error("Böyle bir takım sistemde bulunamadı. Lütfen ismini kontrol et.")
            
    except Exception as e:
        st.error("Veri çekilirken bir hata oluştu.")

