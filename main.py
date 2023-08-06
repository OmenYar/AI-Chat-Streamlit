import streamlit as st
import openai


def main():
    # Menetapkan judul halaman dan menampilkan teks yang dibuat oleh pengembang
    st.markdown("<h3 style='text-align: center; color: white;'>AI Chat with Streamlit 🤖 </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white;'>Built by <a href='https://github.com/OmenYar'>Bachtiar ❤️</a> </h6>", unsafe_allow_html=True)


    # Menginisialisasi kunci API OpenAI menggunakan variabel lingkungan yang tersimpan di dalam secrets Streamlit
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Memeriksa status model OpenAI yang digunakan dan pesan-pesan yang ada dalam sesi. Jika tidak ada, sesi dan pesan kosong dibuat.
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mengulangi setiap pesan dalam sesi dan menampilkannya menggunakan chat_message
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Meminta input pengguna melalui kotak chat_input
    if prompt := st.chat_input("Silakan Tanyakan Apa Saja?"):
        # Menambahkan pesan pengguna ke sesi menggunakan role "user" dan konten input pengguna
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Menampilkan pesan pengguna menggunakan komponen chat_message dengan role "user"
        with st.chat_message("user"):
            st.markdown(prompt)

        # Menjalankan chat dengan model OpenAI menggunakan pesan-pesan yang ada dalam sesi
        # Menampilkan pesan assistan menggunakan komponen chat_message dengan role "assistant"
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Menambahkan pesan assistan ke dalam sesi menggunakan role "assistant" dan konten respons penuh dari model
        st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == '__main__':
    main()