BIKE SHARING DATASET
Ini adalah proyek pertama saya dalam menganalisis data yang berasal dari Dicoding berjudul "Belajar Analisis Data Dengan Python." File notebook ini mencakup hasil pembersihan dan visualisasi yang telah saya lakukan, dengan data yang diambil dari: https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view

Analysis Data dengan Jupyter Notebook
Untuk dapat running file Notebook dapat mengikuti langkah-langkah berikut ini:
1) Buka file di IDE seperti VS Code atau bisa buka di Google Colaboratory
2) Install requirement
3) Install extensions jika memakai VS CODE
4) Buka file yang telah di download
5) Rubah terlebih dahulu path dan dari fata dan juga image
6) Jalankan coding tersebut

Pertanyaan
1) Bagaimana tren penggunaan layanan dari waktu ke waktu?
2) Apa faktor-faktor yang paling mempengaruhi penggunaan layanan?

*Conclution*

Conclution pertanyaan 1 "Bagaimana tren penggunaan layanan dari waktu ke waktu?"
1) Peningkatan penggunaan signifikan terlihat pada bulan Mei hingga Oktober setiap tahun, yang mencerminkan musim panas dengan cuaca yang lebih baik.
2) Penggunaan layanan tertinggi terjadi pada Sabtu, dengan rata-rata sekitar 4,200 pengguna per hari.
3) Hari kerja seperti Senin hingga Jumat memiliki rata-rata penggunaan lebih rendah, dengan sekitar 3,100 pengguna per hari.
4) Pada hari kerja, puncak penggunaan terjadi pada jam 8 pagi dan jam 5 sore, dengan lebih dari 450 pengguna rata-rata pada waktu-waktu ini, menunjukkan penggunaan untuk keperluan komuter.
5) Pada akhir pekan, penggunaan tersebar lebih merata dari pukul 10 pagi hingga 4 sore, dengan rata-rata 350-400 pengguna per jam.

Conclution pertanyaan 2 "Apa faktor-faktor yang paling mempengaruhi penggunaan layanan?"

1) Cuaca yang baik (Clear/Partly Cloudy) memiliki rata-rata penggunaan 3,600 pengguna per hari, sedangkan cuaca buruk (Heavy Rain/Snow) memiliki rata-rata penggunaan yang jauh lebih rendah, hanya sekitar 1,800 pengguna per hari.
2) Hari kerja memiliki rata-rata 3,200 pengguna per hari, dengan puncak pada jam sibuk pagi dan sore.
3) Hari libur rata-rata lebih rendah, dengan hanya 2,100 pengguna per hari, tetapi penggunaan layanan oleh pengguna kasual meningkat pada hari-hari ini.

Kesimpulan: Faktor-faktor utama yang mempengaruhi penggunaan layanan adalah cuaca dan hari dalam minggu. Cuaca cerah dapat meningkatkan penggunaan, sementara hari libur menunjukkan penurunan penggunaan yang signifikan karena peminjam didominasi untuk keperluan komuter.

Dashboard with Streamlit
Acces via webStreamlit
Anda dapat melihat Dashboard Streamlit melalui Link yang tertera di file url.txt dimana dasboard tersebut berisi mulai dari; data rides berdasarkan perjam, hari, bulan dan musim pada tahun 2011-2012.

Untuk mengecek data di tanggal yang lain anda tinggal memilih batas awal dan akhir lewat fitur calender di sidebar dimana untuk tombol pertama sebagai batas awal dan tombol kedua sebagai batas akhir dari data.

Setelah memilih data akan terganti/terbarui sesuai dengan batas awal dan akhir yang dipilih.

Run Streamlit on Local
Install Dependencies

Aktifkan virtual environtment :
pip install streamlit babel

Install file requirement
pip install -r requirements.txt

Run Dashboard
streamlit run [dasboard.py]