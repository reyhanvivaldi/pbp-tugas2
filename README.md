# Welcome to Rey's PBP Assignment Github Repository!

Berikut link aplikasi untuk Assignment 4:

[![TODOLIST](https://img.shields.io/badge/TodoList%20Heroku-298D46?style=for-the-badge&logoColor=white)](https://pbptugas2.herokuapp.com/todolist/)


## Kegunaan {% csrf_token %} pada elemen form
CSRF token adalah kode alphanumeric acak yang unik pada site terkait, sehingga tidak ada site yang memiliki kode CSRF yang sama. Fungsi CSRF token adalah untuk membangun proteksi terhadap serangan CSRF (Cross Site Request Forgeries), yaitu serangan yang terjadi saat suatu website menyimpan link, tombol, form, atau elemen lain yang bisa mengeksekusi malicious action dalam website dengan menggunakan credential dari logged-in user. Apabila CSRF token tidak ada, maka tidak ada proteksi terhadap serangan ini sehingga user bisa saja melakukan action yang sebenarnya tidak ingin dia lakukan.


## Apakah bisa membuat form manual tanpa menggunakan generator?
Ya, kita bisa membuat form secara manual tanpa generator. Kelebihannya adalah kita bisa memberikan efek CSS pada form tersebut.

Gambaran besarnya, kita bisa buat section pada template html untuk menampilkan tiap field form secara manual dengan membuat label tiap field form, misalnya "Nama", kemudian buat form field sesuai yang didefinisikan pada forms.py dengan memanggil {{ form.< formfield > }}. Kemudian buat tombol yang mentrigger pemrosesan data yang dimasukkan pada form.

Step pembuatan form manual: https://www.geeksforgeeks.org/render-django-form-fields-manually/


## Proses alur submisi dari HTML form, penyimpanan ke database, hingga munculnya data di HTML
User mengisi form, kemudian browser akan men-generate request, method, dan argumen ke server. Pastikan request tersebut adalah POST request agar bisa disimpan di database. Setelah request diterima oleh server, views.py akan memproses data dengan semua logic yang dibuat, misalnya dengan menyimpan data form tersebut pada models dengan form.save(). Data yang tersimpan di database ini lalu bisa ditampilkan di HTML sesuai yang didefinisikan oleh fungsi terkait pada views.py


## Penjelasan Pengerjaan Checklist Assignment 4
Berikut penjelasan bagaimana saya melakukan implementasi:

1. Saya menjalankan command "python manage.py startapp todolist" untuk membuat aplikasi baru bernama todolist pada project_django. Daftarkan nama aplikasi mywatchlist pada INSTALLED_APPS yang ada di settings.py project_django. 

2. Menambahkan path baru pada urlpatterns di project urls.py agar bisa mengakses localhost:8000/todolist

3. Membuat class Task serta atribut-atributnya. Lalu saya lakukan makemigrations dan migrate.

4. Membuat fungsi baru untuk login, register, add task, dan logout, pada views.py serta template html yang bersesuaian untuk tiap fungsi.

5. Membuat table task, tombol task baru, dan logout pada template html. Tombol task baru akan meredirect ke halaman create-task, dan logout akan memanggil fungsi logout pada views.py.

6. Untuk membuat halaman add new task, pertama saya membuat file baru bernama forms.py. Di file ini, berisi class modelform yang menghubungkan antara form secara visual dengan class pada models.py, sehingga data yang dimasukkan di form dapat disimpan di database. Kemudian, class form diintegrasikan dengan template HTML dengan logic dan pemrosesan yang didefisinikan pada views.py, tepatnya di fungsi get_add_task. Kemudian, saya buat template HTML yang menampilkan form tersebut sebagai table.

7. Menambahkan path baru pada app urls.py agar bisa mengakses /login, /register, /create-task, dan /logout.

8. Git add, commit, push. Aplikasi otomatis terdeploy pada heroku (appname: pbptugas2)

9. Membuat 2 user dan 3 dummy data tiap user pada app heroku.


<br>
<hr>
2022 | reyv
<hr>
<br>
