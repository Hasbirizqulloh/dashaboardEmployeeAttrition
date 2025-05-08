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

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Berdasarkan analisis yang dilakukan pada data karyawan perusahaan Jaya Jaya Maju, tujuan utama proyek ini adalah untuk mengidentifikasi faktor-faktor yang mempengaruhi tingginya tingkat attrition (keluarnya karyawan) dan memberikan rekomendasi berbasis data untuk membantu mengurangi tingkat attrition di masa depan. Berikut adalah beberapa kesimpulan utama yang dapat diambil dari hasil analisis ini:

1. Faktor-faktor yang Mempengaruhi Attrition    
Berdasarkan analisis data, ditemukan bahwa beberapa faktor numerik dan kategorikal memiliki hubungan dengan attrition. Secara umum, karyawan dengan pengalaman kerja yang lebih lama (lebih banyak TotalWorkingYears), usia yang lebih tua (Age), serta jabatan yang lebih tinggi (JobLevel) cenderung memiliki tingkat attrition yang lebih rendah. Sebaliknya, karyawan yang lebih muda dan baru dalam perusahaan memiliki kemungkinan lebih besar untuk keluar. Selain itu, faktor DistanceFromHome (jarak dari rumah ke kantor) juga menjadi indikasi bahwa karyawan yang tinggal lebih jauh dari lokasi perusahaan cenderung lebih sering keluar.

2. Visualisasi Data yang Mencerminkan Potensi Penyebab Attrition    
Hasil visualisasi menunjukkan bahwa jarak rumah ke kantor (DistanceFromHome) merupakan salah satu faktor yang berhubungan erat dengan keputusan karyawan untuk keluar dari perusahaan. Karyawan yang tinggal jauh dari kantor mungkin menghadapi kesulitan terkait dengan waktu dan biaya perjalanan, yang dapat meningkatkan keinginan mereka untuk mencari pekerjaan yang lebih dekat atau lebih fleksibel.

3.Keterkaitan Fitur-fitur dengan Attrition    
Meskipun fitur kategorikal seperti Department, BusinessTravel, dan Gender menunjukkan distribusi yang berbeda antara karyawan yang keluar dan yang tidak, tidak ditemukan adanya kategori tunggal yang secara jelas mendominasi tingkat attrition. Hal ini menunjukkan bahwa keputusan untuk keluar lebih dipengaruhi oleh kombinasi beberapa faktor daripada satu faktor tunggal.


4. Kesimpulan Akhir    
Proyek ini memberikan wawasan yang berharga bagi tim HR perusahaan Jaya Jaya Maju dalam memahami faktor-faktor yang berkontribusi terhadap tingginya tingkat attrition. Dengan memanfaatkan hasil analisis ini, manajemen dapat lebih memahami tantangan yang dihadapi dalam retensi karyawan dan mengimplementasikan kebijakan yang lebih tepat untuk menurunkan tingkat attrition di masa depan. Analisis ini menunjukkan bahwa masalah attrition tidak dapat diselesaikan hanya dengan satu pendekatan, melainkan membutuhkan kebijakan yang berbasis data dan mempertimbangkan berbagai faktor yang mempengaruhinya.

Dengan adanya business dashboard yang dibuat dalam proyek ini, tim HR dapat secara efektif memantau berbagai faktor yang mempengaruhi karyawan dan mengambil langkah-langkah preventif untuk menjaga kepuasan dan loyalitas karyawan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
