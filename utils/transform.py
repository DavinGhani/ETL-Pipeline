import pandas as pd
import re  
import datetime  

# Fungsi untuk mengonversi harga dari USD ke IDR
def convert_price_to_idr(price_usd):
    try:
        # Menghapus simbol dolar dan mengonversi ke angka
        price = float(price_usd.replace('$', '').replace(',', '').strip())
        # Asumsi nilai tukar 1 USD = 16,000 IDR
        return price * 16000
    except ValueError:
        return None

# Fungsi untuk membersihkan dan mentransformasi data
def transform_data(data):
    # Membuat DataFrame dari data yang diekstraksi
    df = pd.DataFrame(data, columns=['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender'])
    
    # Menangani data invalid
    df = df[~df['Title'].isin(["Unknown Product"])]  # Menghapus produk yang tidak dikenal
    df = df[~df['Rating'].str.contains("Invalid Rating / 5|Not Rated", na=False)]  # Menghapus rating yang invalid
    df = df[~df['Price'].isin(["Price Unavailable", None])]  # Menghapus harga yang tidak tersedia
    
    # Mengonversi harga menjadi IDR
    df['Price'] = df['Price'].apply(convert_price_to_idr)
    
    # Menghapus duplikat
    df = df.drop_duplicates()

    # Mengonversi Rating menjadi float dengan regex (hanya jika valid)
    df['Rating'] = df['Rating'].apply(
        lambda x: float(re.search(r'(\d+\.\d+)', x).group(1)) if isinstance(x, str) and re.search(r'(\d+\.\d+)', x) else None
    )

    # Membersihkan kolom Colors (mengambil angka saja)
    df['Colors'] = df['Colors'].str.extract('(\d+)').astype(float)

    # Membersihkan kolom Size (menghapus "Size: " jika ada)
    df['Size'] = df['Size'].str.replace('Size: ', '')

    # Menghapus teks "Gender: " di kolom Gender
    df['Gender'] = df['Gender'].str.replace('Gender: ', '')

    # Menambahkan kolom timestamp
    df['Timestamp'] = datetime.datetime.now()  # Menambahkan timestamp saat data diproses

    # Menjamin tipe data sesuai harapan
    df['Price'] = df['Price'].astype(float)  # Tipe data untuk Price
    df['Rating'] = df['Rating'].astype(float)  # Tipe data untuk Rating
    df['Colors'] = df['Colors'].astype(int)  # Tipe data untuk Colors
    df['Size'] = df['Size'].astype(str)  # Tipe data untuk Size
    df['Gender'] = df['Gender'].astype(str)  # Tipe data untuk Gender

    # Mengembalikan DataFrame yang sudah dibersihkan
    return df
