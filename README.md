# AI Chat with Streamlit
Aplikasi ini memungkinkan Anda berinteraksi dengan asisten AI menggunakan model bahasa GPT-3.5 Turbo dari OpenAI. Anda dapat mengajukan pertanyaan kepada asisten AI dan menerima responsnya dalam waktu nyata.

## Fitur

- Memuat model bahasa GPT-3.5 Turbo dari OpenAI
- Menggunakan antarmuka pengguna berbasis web dengan Streamlit
- Menampilkan pesan-pesan hasil interaksi dengan asisten AI
- Menggunakan kunci API OpenAI yang aman dan terenkripsi

## Penggunaan

1. Pastikan Anda telah menginstal Streamlit di lingkungan pengembangan lokal Anda. Jika belum, Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal:
   ```python
   pip install streamlit
   ```
2. Pastikan Anda telah mengatur kunci API OpenAI Anda dalam variabel lingkungan "OPENAI_API_KEY". Jika belum, atur kunci API tersebut di [OpenAI Developer Portal](https://openai.com/)

3. Jalankan aplikasi ini di lingkungan pengembangan lokal Anda dengan menjalankan perintah berikut di terminal:
   ```python
   streamlit run main.py
   ```
4. Akses aplikasi melalui browser Anda dengan mengunjungi alamat [http://localhost:8501](http://localhost:8501)

5. Tanyakan apa saja kepada asisten AI melalui kotak `chat_input` di aplikasi

6. Lihat dan ikuti balasan dari asisten AI dalam kotak `chat_message`

Dengan mengikuti langkah-langkah di atas, Anda dapat menggunakan aplikasi ini dan berinteraksi dengan asisten AI melalui browser Anda tanpa perlu melakukan instalasi Streamlit secara manual sebelumnya.

## Kontribusi

Kontribusi dan masukan diterima dengan senang hati! Jika Anda ingin menyempurnakan aplikasi ini atau melaporkan masalah, silakan buat "issue" baru atau ajukan "pull request".

Terima kasih telah menjelajahi AI Chat with Streamlit! Semoga bisa menemukan pengalaman interaktif dengan asisten AI yang menarik dan bermanfaat.

## Sumber

[Streamlit](https://streamlit.io/)
