# Welcome to Rey's PBP Tugas 2 Github Repository!

Berikut link menuju aplikasi:

[![LINKS](https://img.shields.io/badge/LIHAT%20APLIKASI-0054F7?style=for-the-badge&logoColor=white)](https://pbptugas2.herokuapp.com/katalog/)

Alternatif lain, Anda bisa kunjungi url berikut: https://pbptugas2.herokuapp.com/katalog/


![Django Chart - Compressed](static/Django%20Chart%20-%20Compressed.jpg)

## Kaitan urls.py, views.py, models.py, dan HTML
Terdapat 2 jenis urls.py pada proyek Django: project urls dan app urls. Saat user melakukan request dengan mengunjungi url halaman web, project urls akan tertrigger untuk menentukan urls.py pada app mana yang akan dieksekusi.

App urls.py tersebut akan menentukan fungsi pada views.py untuk dipangil berdasarkan url path yang dimasukkan user. Selanjutnya, jika diperlukan, views.py akan mengambil data dari models.py yang kemudian dikirim ke berkas html. Terkahir, berkas html akan menampilkan halaman web secara visual kepada user berdasarkan data-data yang diambil dari views.


## Virtual Environment
Virtual environment adalah environment yang digunakan Python atau Django dalam mengeksekusi program. Penggunaan virtual environment ini direkomendasikan untuk memisahkan dependency seperti code library atau package suatu project dengan project yang lain agar tidak tercampur. 

Akibat ruang virtual ini, perubahan pada project satu akan terisolasi dan tidak berpengaruh pada project lainnya. Namun, virtual environment ini bersifat "rekomendasi". Kita tetap bisa membuat project Django tanpa virtual environtment dan kita harus siap dengan konsekuensi yang mungkin terjadi.


## Penjelasan Implementasi
Berikut penjelasan bagaimana saya melakukan implementasi:

1. Saya mengimport class CatalogItem dari models di folder aplikasi katalog. Kemudian, setiap objek pada CatalogItem saya masukkan ke variable data_katalog. Lalu, saya membuat dictionary "context" untuk menyimpan data yang akan dirender. Selanjutnya, saya membuat fungsi show_katalog yang mengembalikan pemanggilan fungsi render yang diberikan argumen req, berkas html, dan data pada dictionary context. Fungsi ini akan memberikan instruksi agar html menampilkan data yang sesuai.

2. Pertama, saya import fungsi path dari library Django dan fungsi show_katalog dari views.py aplikasi katalog. Lalu membuat application namespace yang disimpan pada variabel "app_name". Selanjutnya, saya membuat urlpatterns untuk menentukan path url dan menghubungkannya dengan pemanggilan fungsi dari views.py. Lalu, saya tambahkan path baru pada project urls.py agar app urls terhubung dengan project secara keseluruhan.

3. Saya lakukan iterasi tiap data pada katalog_item (dari context views.py), lalu memanggil atribut dari data tersebut agar ditampilkan pada tabel. Tempat block for loop ini berada di dalam block table.

4. Git push, lalu saya hubungkan heroku dan github melalui API code yang disediakan oleh heroku. API tersebut diinput pada menu repository secret dengan variabel yang sesuai. Selanjutnya, saya pastikan isi berkas Procfile sudah benar (sesuai dengan nama project). Kemudian, saya jalankan workflow di github. Aplikasi berhasil berjalan.

<br>
<hr>
2022 | reyv
<hr>
<br>
