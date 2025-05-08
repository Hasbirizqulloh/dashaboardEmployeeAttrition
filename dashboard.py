import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv("data_cleaned.csv")

nama_fitur = {
    "Age": "Usia",
    "Attrition": "Status Attrition",
    "BusinessTravel": "Perjalanan Dinas",
    "DailyRate": "Tarif Harian",
    "Department": "Departemen",
    "DistanceFromHome": "Jarak dari Rumah",
    "Education": "Tingkat Pendidikan",
    "EducationField": "Bidang Pendidikan",
    "EnvironmentSatisfaction": "Kepuasan Lingkungan Kerja",
    "Gender": "Jenis Kelamin",
    "HourlyRate": "Tarif per Jam",
    "JobInvolvement": "Keterlibatan dalam Pekerjaan",
    "JobLevel": "Level Pekerjaan",
    "JobRole": "Jabatan",
    "JobSatisfaction": "Kepuasan Kerja",
    "MaritalStatus": "Status Pernikahan",
    "MonthlyIncome": "Pendapatan Bulanan",
    "MonthlyRate": "Tarif Bulanan",
    "NumCompaniesWorked": "Jumlah Perusahaan Sebelumnya",
    "OverTime": "Lembur",
    "PercentSalaryHike": "Persentase Kenaikan Gaji",
    "PerformanceRating": "Penilaian Kinerja",
    "RelationshipSatisfaction": "Kepuasan Hubungan Sosial",
    "StockOptionLevel": "Level Opsi Saham",
    "TotalWorkingYears": "Total Tahun Bekerja",
    "TrainingTimesLastYear": "Jumlah Pelatihan Tahun Ini",
    "WorkLifeBalance": "Keseimbangan Kerja-Hidup",
    "YearsAtCompany": "Lama Bekerja di Perusahaan",
    "YearsInCurrentRole": "Lama di Posisi Sekarang",
    "YearsSinceLastPromotion": "Tahun Sejak Promosi Terakhir",
    "YearsWithCurrManager": "Tahun Bersama Manajer Saat Ini"
}

# Kamus terjemahan nilai kategorikal
kategori_terjemahan = {
    "Gender": {
        "Male": "Laki-laki",
        "Female": "Perempuan"
    },
    "MaritalStatus": {
        "Single": "Lajang",
        "Married": "Menikah",
        "Divorced": "Cerai"
    }
}

# Filter DataFrame berdasarkan input di sidebar
df_filtered = df.copy()

# Simpan nilai asli (backup) untuk filter
for col, mapping in kategori_terjemahan.items():
    df[col + "_ID"] = df[col]  # Backup kolom asli
    df[col] = df[col].map(mapping)

# Sidebar filters
st.sidebar.title("Filter Data")

# Status Attrition
attrition_status = st.sidebar.selectbox(nama_fitur["Attrition"], ["Semua", "Keluar", "Tidak Keluar"])

# Departemen (langsung, karena sudah readable)
department = st.sidebar.selectbox(nama_fitur["Department"], ["Semua"] + df["Department"].unique().tolist())

# Jenis Kelamin
gender = st.sidebar.selectbox(nama_fitur["Gender"], ["Semua"] + df["Gender"].unique().tolist())

# Status Pernikahan
marital_status = st.sidebar.selectbox(nama_fitur["MaritalStatus"], ["Semua"] + df["MaritalStatus"].unique().tolist())

# Rentang Gaji Bulanan
min_income, max_income = int(df["MonthlyIncome"].min()), int(df["MonthlyIncome"].max())
salary_range = st.sidebar.slider(
    nama_fitur["MonthlyIncome"],
    min_value=min_income,
    max_value=max_income,
    value=(min_income, max_income),
    step=1000
)

# Lama Bekerja di Perusahaan
years_at_company = st.sidebar.slider(
    nama_fitur["YearsAtCompany"],
    min_value=int(df["YearsAtCompany"].min()),
    max_value=int(df["YearsAtCompany"].max()),
    value=(int(df["YearsAtCompany"].min()), int(df["YearsAtCompany"].max()))
)

# Filtering berdasarkan hasil terjemahan ke ID asli
df_filtered = df.copy()

# Filter DataFrame
if attrition_status == "Keluar":
    df_filtered = df[df["Attrition"] == 1]
elif attrition_status == "Tidak Keluar":
    df_filtered = df[df["Attrition"] == 0]
else:
    df_filtered = df.copy()

if department != "Semua":
    df_filtered = df_filtered[df_filtered["Department"] == department]

if gender != "Semua":
    gender_id = {v: k for k, v in kategori_terjemahan["Gender"].items()}[gender]
    df_filtered = df_filtered[df_filtered["Gender_ID"] == gender_id]

if marital_status != "Semua":
    marital_id = {v: k for k, v in kategori_terjemahan["MaritalStatus"].items()}[marital_status]
    df_filtered = df_filtered[df_filtered["MaritalStatus_ID"] == marital_id]

df_filtered = df_filtered[(df_filtered["MonthlyIncome"] >= salary_range[0]) & (df_filtered["MonthlyIncome"] <= salary_range[1])]
df_filtered = df_filtered[(df_filtered["YearsAtCompany"] >= years_at_company[0]) & (df_filtered["YearsAtCompany"] <= years_at_company[1])]
# Title
st.title("Attrition Monitoring Dashboard Perusahaan Jaya Jaya Maju ")
st.markdown("Visualisasi interaktif untuk memahami faktor penyebab *attrition* karyawan.")

card_style = """
    background-color:#1e1e1e;
    padding:20px;
    border-radius:12px;
    text-align:center;
    color:white;
    box-shadow:0 4px 6px rgba(0,0,0,0.3);
    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    margin-bottom: 20px;
    margin-top: 20px;
    border: 2px solid #2e2e2e;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease-in-out;
    cursor: pointer;
"""

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="{card_style}">
        <h5 style="font-size:22px;margin:0;">Jumlah Karyawan</h4>
        <p style="font-size:24px;font-weight:bold;margin:3px 0 0 0;">{len(df_filtered)}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="{card_style}">
        <h4 style="margin:0;">Tingkat Attrition</h4>
        <p style="font-size:24px;font-weight:bold;margin:4px 0 0 0;">{df_filtered['Attrition'].mean() * 100:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="{card_style}">
        <h4 style="font-size:24px;margin:0;">Rata-rata Usia</h4>
        <p style="font-size:24px;font-weight:bold;margin:30px 0 0 0;">{df_filtered['Age'].mean():.1f} tahun</p>
    </div>
    """, unsafe_allow_html=True)


# Fungsi untuk mencocokkan nama dalam nama_fitur ke nama kolom asli
def get_column_from_nama_fitur(nama_fitur_value):
    # Membalikkan dictionary nama_fitur untuk mendapatkan kolom asli dari nama bahasa Indonesia
    inverted_nama_fitur = {v: k for k, v in nama_fitur.items()}
    return inverted_nama_fitur.get(nama_fitur_value, nama_fitur_value)  # Kembalikan nama kolom yang sesuai

# ===================== 
# SECTION 1: Bar Chart Rata-rata Fitur
# =====================

st.subheader(f"Perbandingan Rata-Rata antar Kelompok")
numeric_cols = df.select_dtypes(include='number').columns.drop('Attrition')

# Menggunakan nama_fitur untuk menampilkan label yang lebih mudah dimengerti
selected_bar_feature = st.selectbox("Pilih fitur numerik:", [nama_fitur.get(col, col) for col in numeric_cols])

# Menemukan nama kolom asli yang sesuai dengan fitur yang dipilih
selected_bar_feature_col = get_column_from_nama_fitur(selected_bar_feature)

# Mengganti nama kolom yang tampil di grafik dengan nama_fitur
bar_df = df.groupby("Attrition")[selected_bar_feature_col].mean().reset_index()
bar_df['Attrition'] = bar_df['Attrition'].map({0: "Tidak Keluar", 1: "Keluar"})

bar_fig = px.bar(
    bar_df, x="Attrition", y=selected_bar_feature_col, color="Attrition",
    title=f"Rata-rata {selected_bar_feature} per Status Attrition", 
    text=selected_bar_feature_col
)
st.plotly_chart(bar_fig, use_container_width=True)

# ===================== 
# SECTION 2: Pie Chart untuk Fitur Kategorikal
# =====================
st.subheader("Sebaran Karakteristik Karyawan")
cat_cols = df.select_dtypes(include='object').columns

# Ganti dengan nama yang lebih mudah dimengerti
selected_pie_feature = st.selectbox("Pilih fitur kategorikal:", [nama_fitur.get(col, col) for col in cat_cols])

# Menemukan nama kolom asli yang sesuai dengan fitur yang dipilih
selected_pie_feature_col = get_column_from_nama_fitur(selected_pie_feature)

# Update pie chart dengan label yang lebih mudah dimengerti
pie_df = df_filtered[selected_pie_feature_col].value_counts().reset_index()
pie_df.columns = [selected_pie_feature_col, "Jumlah"]
pie_fig = px.pie(pie_df, values='Jumlah', names=selected_pie_feature_col,
                 title=f"Distribusi {selected_pie_feature} pada data {attrition_status}")
st.plotly_chart(pie_fig, use_container_width=True)

# ===================== 
# SECTION 3: Histogram Distribusi Nilai Fitur
# =====================

st.subheader("Pola Penyebaran Data")

# Pilih fitur numerik
selected_hist_feature = st.selectbox(
    "Pilih fitur numerik untuk histogram:",
    [nama_fitur.get(col, col) for col in numeric_cols],
    key='hist'
)

# Menemukan nama kolom asli yang sesuai dengan fitur yang dipilih
selected_hist_feature_col = get_column_from_nama_fitur(selected_hist_feature)

# Membuat histogram dengan pengaturan yang lebih baik
hist_fig = px.histogram(
    df,
    x=selected_hist_feature_col,
    color='Attrition',
    barmode='overlay',  # Overlay untuk membandingkan distribusi antara dua kelompok attrition
    nbins=30,  # Menentukan jumlah bins (disesuaikan untuk visualisasi yang lebih halus)
    title=f"Distribusi {nama_fitur.get(selected_hist_feature, selected_hist_feature)} berdasarkan Status Attrition",
    labels={'Attrition': 'Status Attrition', selected_hist_feature_col: f"{nama_fitur.get(selected_hist_feature_col, selected_hist_feature_col)}"},
    opacity=0.75,  # Mengatur transparansi agar lebih mudah dilihat ketika ada tumpang tindih
)

# Memperjelas visualisasi dengan menyesuaikan desain
hist_fig.update_traces(
    marker=dict(line=dict(width=0.5, color='black')),  # Menambahkan outline pada batang untuk kontras
)

# Update layout untuk meningkatkan desain
hist_fig.update_layout(
    xaxis_title=f"{nama_fitur.get(selected_hist_feature_col, selected_hist_feature_col)}",  # Menambahkan label sumbu x
    yaxis_title="Jumlah Karyawan",  # Menambahkan label sumbu y
    legend_title="Status Attrition",  # Menambahkan judul legend
    legend=dict(title="Status Attrition", x=0.8, y=1, bgcolor="rgba(255, 255, 255, 0.7)"),  # Menambahkan legenda yang jelas
    barmode='overlay',
    bargap=0.05,  # Gap antara bar untuk menghindari overlap yang terlalu banyak
    template="plotly_white"  # Menggunakan template putih untuk meningkatkan kontras dan keterbacaan
)

# Menampilkan histogram
st.plotly_chart(hist_fig, use_container_width=True)


