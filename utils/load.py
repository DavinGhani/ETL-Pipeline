import pandas as pd
from sqlalchemy import create_engine

# Fungsi untuk menyimpan data ke CSV
def save_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename}")

# Fungsi untuk menyimpan data langsung ke PostgreSQL (tanpa perlu tabel manual)
def save_to_postgresql(df, db_url="postgresql://davin:1213@localhost:5432/fashion_db", table_name="products"):
    try:
        # Membuat koneksi ke database PostgreSQL
        engine = create_engine(db_url)
        
        # Menyimpan DataFrame ke PostgreSQL, jika tabel belum ada maka akan dibuat otomatis
        df.to_sql(table_name, engine, if_exists='replace', index=False)  # Ganti 'replace' dengan 'append' jika ingin menambahkan ke tabel yang ada
        print(f"Data berhasil disimpan ke tabel {table_name} di PostgreSQL")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data ke PostgreSQL: {e}")

