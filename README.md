# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di seluruh Indonesia. Meskipun telah berkembang pesat, perusahaan ini masih menghadapi tantangan dalam pengelolaan sumber daya manusia, terutama dalam hal retensi karyawan.

Tingkat attrition (keluar/mundurnya karyawan) yang tinggi, yaitu lebih dari 10%, menjadi perhatian utama karena dapat berdampak pada efisiensi operasional dan biaya rekrutmen. Untuk mengatasi hal ini, manajemen HR ingin memahami faktor-faktor apa saja yang mempengaruhi keputusan karyawan untuk keluar dari perusahaan.

### Permasalahan Bisnis

Beberapa permasalahan bisnis utama yang ingin diselesaikan dalam proyek ini antara lain:

- Mengidentifikasi faktor-faktor yang mempengaruhi tingginya tingkat attrition.

- Menyediakan informasi visual kepada tim HR untuk memantau kondisi karyawan secara komprehensif.

- Memberikan rekomendasi berbasis data untuk menurunkan angka attrition di masa depan.

### Cakupan Proyek

Proyek ini akan mencakup:

- Analisis eksploratif terhadap data karyawan untuk menemukan pola dan insight.

- Pembuatan dashboard interaktif sebagai alat bantu pengambilan keputusan bagi tim HR.

- Pembangunan model prediktif sederhana untuk memprediksi potensi attrition.

- Dokumentasi hasil analisis dalam format laporan markdown (.md).

### Persiapan

Sumber data:    
Dataset karyawan dari perusahaan Jaya Jaya Maju yang berisi informasi demografi, pekerjaan, kepuasan kerja, dan status attrition.

Setup environment:

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

```

## Business Dashboard

Dashboard yang dibuat bertujuan untuk membantu perusahaan Jaya Jaya Maju dalam memahami dan memantau tingkat attrition (keluar/berhenti) karyawan secara lebih efektif. Melalui tampilan visual yang interaktif, dashboard ini memberikan kemudahan dalam mengeksplorasi data karyawan berdasarkan berbagai karakteristik seperti jenis kelamin, status pernikahan, departemen, tingkat pendapatan, serta lama bekerja di perusahaan.

Dashboard ini dibangun menggunakan Streamlit dan memanfaatkan visualisasi dari Plotly untuk menampilkan data dalam bentuk grafik batang, grafik lingkaran, dan histogram. Pengguna dapat menyaring data berdasarkan kategori tertentu melalui panel filter di sisi kiri, sehingga analisis dapat difokuskan pada kelompok karyawan tertentu sesuai kebutuhan.

Beberapa fitur utama dalam dashboard:

- Ringkasan Kunci:   
Menampilkan jumlah karyawan, tingkat attrition, dan rata-rata usia secara langsung.

- Analisis Perbandingan:   
Menampilkan perbandingan rata-rata usia, gaji, atau karakteristik lainnya antara karyawan yang keluar dan yang bertahan.

- Distribusi Karakteristik:   
Menunjukkan komposisi karyawan berdasarkan atribut tertentu (misalnya jabatan, departemen, dll).

- Pola Penyebaran:   
Menjelaskan pola attrition berdasarkan sebaran nilai seperti pendapatan atau lama bekerja.

Dashboard ini dirancang untuk digunakan oleh manajemen dan tim HR dalam pengambilan keputusan berbasis data, seperti merancang program retensi, mengevaluasi kebijakan kesejahteraan karyawan, serta mengidentifikasi kelompok yang berisiko tinggi untuk keluar dari perusahaan.

## Conclusion

Berdasarkan analisis yang dilakukan pada data karyawan perusahaan Jaya Jaya Maju, tujuan utama proyek ini adalah untuk mengidentifikasi faktor-faktor yang mempengaruhi tingginya tingkat attrition (keluarnya karyawan) dan memberikan rekomendasi berbasis data untuk membantu mengurangi tingkat attrition di masa depan. Berikut adalah beberapa kesimpulan utama yang dapat diambil dari hasil analisis ini:

1. Faktor-faktor yang Mempengaruhi Attrition    
Berdasarkan analisis data, ditemukan bahwa beberapa faktor numerik dan kategorikal memiliki hubungan dengan attrition. Secara umum, karyawan dengan pengalaman kerja yang lebih lama (lebih banyak TotalWorkingYears), usia yang lebih tua (Age), serta jabatan yang lebih tinggi (JobLevel) cenderung memiliki tingkat attrition yang lebih rendah. Sebaliknya, karyawan yang lebih muda dan baru dalam perusahaan memiliki kemungkinan lebih besar untuk keluar. Selain itu, faktor DistanceFromHome (jarak dari rumah ke kantor) juga menjadi indikasi bahwa karyawan yang tinggal lebih jauh dari lokasi perusahaan cenderung lebih sering keluar.

2. Visualisasi Data yang Mencerminkan Potensi Penyebab Attrition    
Hasil visualisasi menunjukkan bahwa jarak rumah ke kantor (DistanceFromHome) merupakan salah satu faktor yang berhubungan erat dengan keputusan karyawan untuk keluar dari perusahaan. Karyawan yang tinggal jauh dari kantor mungkin menghadapi kesulitan terkait dengan waktu dan biaya perjalanan, yang dapat meningkatkan keinginan mereka untuk mencari pekerjaan yang lebih dekat atau lebih fleksibel. Meskipun fitur kategorikal seperti Department, BusinessTravel, dan Gender menunjukkan distribusi yang berbeda antara karyawan yang keluar dan yang tidak, tidak ditemukan adanya kategori tunggal yang secara jelas mendominasi tingkat attrition. Hal ini menunjukkan bahwa keputusan untuk keluar lebih dipengaruhi oleh kombinasi beberapa faktor daripada satu faktor tunggal.

3. Kesimpulan Akhir    
Proyek ini memberikan wawasan yang berharga bagi tim HR perusahaan Jaya Jaya Maju dalam memahami faktor-faktor yang berkontribusi terhadap tingginya tingkat attrition. Dengan memanfaatkan hasil analisis ini, manajemen dapat lebih memahami tantangan yang dihadapi dalam retensi karyawan dan mengimplementasikan kebijakan yang lebih tepat untuk menurunkan tingkat attrition di masa depan. Analisis ini menunjukkan bahwa masalah attrition tidak dapat diselesaikan hanya dengan satu pendekatan, melainkan membutuhkan kebijakan yang berbasis data dan mempertimbangkan berbagai faktor yang mempengaruhinya.

Dengan adanya business dashboard yang dibuat dalam proyek ini, tim HR dapat secara efektif memantau berbagai faktor yang mempengaruhi karyawan dan mengambil langkah-langkah preventif untuk menjaga kepuasan dan loyalitas karyawan.

### Rekomendasi Action Items

Berikut adalah beberapa rekomendasi berbasis data yang dapat dilakukan oleh perusahaan Jaya Jaya Maju untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan:

1. Implementasi Kebijakan Kerja Fleksibel atau Hybrid    
Karyawan yang tinggal jauh dari kantor cenderung memiliki tingkat attrition lebih tinggi. Perusahaan dapat mempertimbangkan untuk menerapkan opsi kerja dari rumah (WFH) atau hybrid guna mengurangi beban perjalanan bagi karyawan yang tempat tinggalnya jauh.

2. Program Pengembangan Karier dan Promosi Internal    
Karyawan dengan level jabatan rendah dan pengalaman kerja singkat cenderung lebih mudah keluar. Maka, perusahaan perlu menyediakan jalur karier yang jelas, pelatihan keterampilan, serta sistem promosi yang transparan agar karyawan merasa dihargai dan memiliki masa depan di perusahaan.

3. Evaluasi dan Peningkatan Kepuasan Kerja    
Fitur-fitur seperti JobInvolvement, EnvironmentSatisfaction, dan WorkLifeBalance menunjukkan korelasi negatif terhadap attrition. Artinya, semakin puas karyawan terhadap pekerjaan dan lingkungannya, semakin kecil kemungkinan mereka keluar. Maka dari itu, survey rutin kepuasan karyawan serta tindak lanjut konkret perlu dilakukan secara berkala.

4. Program Retensi untuk Karyawan Baru dan Muda    
Karyawan yang lebih muda dan baru bergabung memiliki risiko keluar lebih tinggi. Oleh karena itu, perusahaan bisa menjalankan mentoring program atau onboarding program yang intensif agar mereka lebih cepat beradaptasi dan merasa terhubung dengan budaya perusahaan.

5. Monitoring Proaktif dengan Business Dashboard    
Gunakan dashboard yang telah dibuat untuk memonitor metrik penting seperti turnover rate, kepuasan kerja, jarak tempat tinggal, dan performa karyawan secara berkala. Dengan visualisasi yang tepat, tim HR dapat mengambil keputusan yang lebih cepat dan berbasis data.
