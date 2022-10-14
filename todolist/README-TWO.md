# Welcome to Rey's PBP Assignment Github Repository!

Berikut link aplikasi Todolist

[![TODOLIST](https://img.shields.io/badge/TodoList%20Heroku-298D46?style=for-the-badge&logoColor=white)](https://pbptugas2.herokuapp.com/todolist/)


## Perbedaan synchronous dan asynchronous programming
Perbedaan paling jelas dari kedua jenis programming tersebut adalah proses eksekusinya. Synchronous programming mengeksekusi program secara sekuensial, artinya langkah ke n tidak akan dieksekusi jika langkah sebelum n dieksekusi. Asynchronous programming memungkinkan program mengeksekusi langkah ke n tanpa harus mengeksekusi langkah sebelum n.


## Paradigma event-driven programming
Event-driven programming adalah paradigma yang mengeksekusi program berdasarkan event yang ter-trigger misalnya mouse click, hover, klik ke tombol tertentu, dll. Dengan kata lain, program dapat dieksekusi kapanpun selama event itu dipicu tanpa harus mengeksekusi program-program sebelumnya. Contoh dalam tugas ini adalah saat user mengirim task dengan klik tombol, program pembuatan card akan dieksekusi.


## Penerapan asynchronous programming pada AJAX 
AJAX dapat berkomunikasi dengan server, contohnya transaksi data, di belakang layar. AJAX juga bisa melakukan eksekusi program secara event-driven. Misalnya, pada tugas ini, saat tombol "Add task" diklik, AJAX melakukan transaksi data dengan server, lalu menampilkan data yang didapat dari server ke html tanpa harus mereload seluruh halaman. Hal ini memungkinkan halaman web diupdate secara asinkronus. 


## Penjelasan Pengerjaan Checklist Assignment 6
Pertama, saya membuat fungsi pada views yang mengembalikan data tasks dalam bentuk json beserta routingnya. Saya juga membuat fungsi baru untuk menerima data dari ajax (agar berbeda dengan tugas sebelumnya). Lalu, saya implementasi ajax dengan jQuery pada html yang mengeksekusi pembuatan Tasks Card layout berdasarkan data yang diambil dari json.

Dalam pembuatan AJAX POST, pertama, saya membuat fungsi baru pada views (add_task_ajax) sebagai media transfer data antara ajax dan server beserta routingnya. Lalu, saya membuat modal yang diambil dari bootstrap dan menambahkan kode blok form yang sesuai dengan field pada modelsForm. Dalam implementasi ini, saya juga menggunakan jQuery. Saya juga menambahkan code block pada atribut success yang membuat halaman tidak reload saat klik tombol Submit pada modal, mengeksekusi pembuatan tasks card layout, penutupan modal, dll.

<br>
<hr>
2022 | reyv
<hr>
<br>
