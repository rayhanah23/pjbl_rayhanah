import streamlit as st
import math

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="📐",
    layout="wide"
)

with st.sidebar:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image("image/logo.png", width=180)
        st.title("📐 Matematika Geometri")
        pilihan = st.selectbox(
            "Pilih Bangun Datar",
            [
                "Persegi",
                "Persegi Panjang",
                "Lingkaran",
                "Segitiga",
                "Jajar Genjang"
            ]
        )
        st.caption("Dibuat oleh Rayhanah Salsabila Kamal ✨")

st.title("📚 Kalkulator Geometri")
st.write("Pilih bangun datar pada sidebar lalu hitung luas dan kelilingnya.")

match pilihan:

    case "Persegi":

        st.title("⬜ Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("Masukkan Sisi", min_value=0.0)
        if st.button("Hitung Persegi", type="primary"):
            luas = sisi ** 2
            keliling = 4 * sisi
            # st.success(f"✅ Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True) 
            with col2:
                st.metric("Keliling", value=keliling, border=True) 
            st.balloons()

    case "Persegi Panjang":

        st.title("▭ Persegi Panjang")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi panjang")
        panjang = st.number_input("Masukkan Panjang", min_value=0.0)
        lebar = st.number_input("Masukkan Lebar", min_value=0.0)

        if st.button("Hitung Persegi Panjang", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"✅ Luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Lingkaran":

        st.title("⚪ Lingkaran")
        st.markdown("Menghitung 'luas' dan 'keliling' lingkaran")
        r = st.number_input("Masukkan Jari-jari", min_value=0.0)
        if st.button("Hitung Lingkaran"):
            luas = 3.14 * r * r
            keliling = 2 * 3.14 * r
            st.success(f"✅ Luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Segitiga":

        st.title("🔺 Segitiga")
        st.markdown("Menghitung 'luas' dan 'keliling' segitiga")
        alas = st.number_input("Masukkan Alas", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi", min_value=0.0)
        if st.button("Hitung Segitiga"):
            luas = 0.5 * alas * tinggi
            st.success(f"✅ Luas segitiga adalah {luas:.2f}")
            st.balloons()

    case "Jajar Genjang":

        st.title("🔷 Jajar Genjang")
        st.markdown("Menghitung 'luas' dan 'keliling' jajar genjang")
        alas = st.number_input("Masukkan Alas", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi", min_value=0.0)
        sisi = st.number_input("Masukkan Sisi Miring", min_value=0.0)
        if st.button("Hitung Jajar Genjang"):               
            luas = alas * tinggi
            keliling = 2 * (alas + sisi)
            st.success(f"✅ Luas jajar genjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()
        
    case _:
        st.error("Pilihan tidak ditemukan") 