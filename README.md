Repositori ini merupakan tugas saya yang berisikan proyek yang saya kerjakan. Website ini dibuat menggunakan Django.

Cara menjalankan proyeknya:
Pertama, pastikan Django sudah terinstal dengan mengeceknya di terminal lalu ketikkan "python -m django --version".
Jika sudah, pergi ke direktori mana saja sebagai tempat dimana proyek itu ingin diletakkan. Setelah cd kedalam direktori tersebut, jalankan perintah "django-admin startproject mysite" untuk membuat proyek didalam direktori tadi. ("mysite" adalah nama direktori/folder yang akan digunakan sebagai proyek yang bisa diganti sesuka kita, disini saya menggunakan "website")
Setelah berhasil membuat proyek baru maka susunan folder seharusnya akan terlihat seperti ini:
website/
    manage.py
    website/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
Sekarang kita tinggal mengecek apakah proyek Django bekerja dengan cara menjalankan perintah "python manage.py runserver" pada terminal. *pastikan posisi terminal berada pada akar direktori proyek
Nantinya terminal akan mendirect kita ke browser yang akan memunculkan page jika Django berhasil terpasang dan siap untuk diotak-atik.
