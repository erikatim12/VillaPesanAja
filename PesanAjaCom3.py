import streamlit as st 

st.image("https://www.linkpicture.com/q/Pesanaja.png")
st.write ("---------------------------- Selamat Datang di PesanAja --------------------------")
st.write ("**********Jadikan Harimu Lebih Bermakna dengan Penginapan Kelas Executive di Bandung**********")
st.write ("------------------------ Silahkan Pesan Villa yang Anda Inginkan -----------------------------")

nama=st.text_input("Masukkan Nama Anda: ")
tci=st.date_input("Masukkan Tanggal Check-in: ")
tco=st.date_input("Masukkan Tanggal Check-out: ")
jumlah_booking = int(st.text_input("Jumlah Hari Pemesanan: "))

st.write("------- PILIHAN VILLA ---------")
st.write("1. Villa Mawar     @1,199,000")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHK0iQ9kRXW6heEZdemH5blCph7fQjvihQsg&usqp=CAU")

st.write("2. Villa Melati    @1,399,000")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRShzYO2Sy7v6rpskNb9vEQN-CNrLFAqPLMTg&usqp=CAU")

st.write("3. Villa Mentari   @1,599,000")
st. image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcHg0Vbml9_6Y30nCnzm5Y4FxF0r9WAc2TcQ&usqp=CAU")

st.write("4. Villa Tulip     @1,799,000")
st.image("http://jktgo.com/wp-content/uploads/2020/03/DSC08378.jpg")

st.write("5. Villa Anggrek   @1,999,000")
st.image("https://pix10.agoda.net/hotelImages/461/4611246/4611246_18030716140062609877.jpg?ca=6&ce=1&s=1024x768")

booking_villa = int(st.text_input("Masukan Nomor Villa yang Diinginkan:"))

if booking_villa==1:
     harga = 1199000
elif booking_villa==2:
     harga = 1399000
elif booking_villa==3:
     harga = 1599000
elif booking_villa==4:
     harga = 1799000
elif booking_villa==5:
     harga = 1999000
else :
    while True:
        booking_villa = int(st.text_input("Masukan Nomor Villa yang Diinginkan:"))
        if booking_villa==1 or booking_villa==2 or booking_villa==3 or booking_villa==4 or booking_villa==5:
            if booking_villa==1:
                harga = 1199000
            elif booking_villa==2:
                harga = 1399000
            elif booking_villa==3:
                harga = 1599000
            elif booking_villa==4:
                harga = 1799000
            elif booking_villa==5:
                harga = 1999000
            break

bayar = jumlah_booking * harga

submit = st.button("Pesan")
if submit : st.write("-----Bukti Pemesanan-----"), st.write("Nama : ",nama), st.write("Tanggal Check-in : ",tci), st.write("Tanggal Check-out : ",tco), st.write("Jumlah Hari Pemesanan : ",jumlah_booking), st.write("Nomor Villa : ",booking_villa), st.write("Jumlah yang Harus Dibayar: Rp.{}".format(bayar)), st.write("Silahkan bawa bukti ini saat anda mengunjungi Villa!")