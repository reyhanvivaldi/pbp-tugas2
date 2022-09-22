# Welcome to Rey's PBP Assignment Github Repository!

Berikut link aplikasi untuk Assignment 3:

[![HTML](https://img.shields.io/badge/DATA%20HTML-298D46?style=for-the-badge&logoColor=white)](static/3_postman_html.jpg)
[![JSON](https://img.shields.io/badge/DATA%20JSON-0054F7?style=for-the-badge&logoColor=white)](static/3_postman_json.jpg)
[![XML](https://img.shields.io/badge/DATA%20XML-F24E1E?style=for-the-badge&logo=github&logoColor=white)](static/3_postman_xml.jpg) 

### Postman - HTML
![Postman HTML](staticfiles/3_postman_html.jpg)
### Postman - JSON
![Postman JSON](staticfiles/3_postman_json.jpg)
### Postman - XML
![Postman XML](staticfiles/3_postman_xml.jpg)


## Perbedaan JSON, XML, dan HTML
Perbedaan yang paling jelas adalah JSON berbasis Javascript, sedangkan HTML dan XML adalah markup language. Dalam konteks fungsi, JSON berfungsi untuk merepresentasikan dan menyimpan data, sedangkan XML sejatinya berfungsi untuk menyimpan data. HTML tidak membawa/menyimpan data, melainkan hanya menampilkan data. Dalam segi kemudahan pembacaan, kita lebih mudah membaca data dalam JSON daripada XML, sedangkan HTML bergantung pada bagaimana kita membuat tampilannya. Struktur JSON yang simpel dan minim syntax membuat JSON lebih mudah dibaca oleh manusia dibanding XML. Sedangkan, karakter XML adalah old-fashioned dan kompleks akibat struktur tag yang memakan space. Namun, kompleksitas XML inilah yang membuat XML tidak hanya bisa untuk mengirim data, tetapi juga memproses/memformat objek dan dokumen. 

Dalam konteks keamanan, XML lebih aman daripada JSON. Namun, pengiriman data dengan format JSON bisa lebih cepat dibandingkan XML karena ukuran file yang lebih kecil. Perbedaan yang lain adalah XML dapat menghandle komentar, sedangkan JSON tidak. XML juga mendukung berbagai tipe data seperti gambar dan bagan, sedangkan JSON mendukung string, objek, angka, boolean, dan arrays. XML menyimpan data dalam tree structure, sedangkan JSON menyimpan data seperti map yang terdiri dari pasangan key-value.


## Mengapa kita memerlukan data delivery dalam implementasi platform?
Data delivery sangat diperlukan karena dalam suatu platform akan ada proses dimana pertukaran data itu terjadi. Misalnya, saat kita mengakses suatu halaman yang menampilakan data, user akan mengirimkan request yang ujungnya diterima oleh database. Kemudian database akan mengirimkan data yang diminta sebagai respon. Data delivery memiliki peran dalam proses ini.


## Penjelasan Pengerjaan Checklist Assignment 3
Berikut penjelasan bagaimana saya melakukan implementasi:

1. Saya menjalankan command "python manage.py startapp mywatchlist" untuk membuat aplikasi baru bernama mywatchlist pada project_django.

2. Kemudian, saya daftarkan nama aplikasi mywatchlist pada INSTALLED_APPS yang ada di settings.py project_django. Lalu saya lakukan command makemigrations dan dilanjutkan dengan migrate.

3. Membuat class MyWatchList yang memiliki atribut watched, title, rating, release_date, dan review. Setiap atribut memiliki field yang sesuai dengan fungsinya masing-masing.

4. Untuk membuat data, pertama saya buat folder fixtures pada direktori mywatchlist yang berisi file format JSON bernama initial_mywatchlist_data. Kemudian, saya isi file JSON ini dengan data yang fieldnya disesuaikan dengan class pada models. Lalu, saya lakukan command loaddata.

5. Dalam file views.py pada aplikasi mywatchlist, saya mengimport modul yang diperlukan dan membuat tiga fungsi yang masing-masing berfungsi untuk mengembalikan display data yang sesuai (HTML, JSON, dan XML).

6. Dalam file urls.py pada folder mywatchlist, saya buat routing agar data bisa diakses melalui URL dengan path yang berbeda (/html, /json, /xml). Tiap path itu akan terhubung pada fungsi pada views.py yang bersesuaian. Kemudian, saya tambahkan path baru (mywatchlist/) pada urls.py di folder project_django agar terhubung dengan urls.py aplikasi.

7. Git add, commit, dan push. Kemudian saya cek workflow pada github. Aplikasi bisa berjalan, tetapi database (initial_mywatchlist_data.json) tidak muncul. Lalu saya lakukan loaddata ulang di CLI Heroku Bash, kemudian aplikasi berjalan lancar.


<br>
<hr>
2022 | reyv
<hr>
<br>
