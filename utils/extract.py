import requests
from bs4 import BeautifulSoup
import time

# Base URL untuk mengakses halaman
BASE_URL = "https://fashion-studio.dicoding.dev"  # Halaman pertama tanpa /page1

# Headers untuk meniru request dari browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

# Fungsi untuk mengambil data dari setiap halaman
def extract_data(page_number):
    # Menentukan URL berdasarkan halaman
    if page_number == 1:
        url = BASE_URL  # Halaman pertama tidak perlu /page1
    else:
        url = f"{BASE_URL}/page{page_number}"  # Halaman 2 dan seterusnya

    session = requests.Session()
    try:
        response = session.get(url, headers=HEADERS)
        
        # Cek jika status code adalah 200, berarti halaman tersedia
        if response.status_code == 200:
            # Parsing konten HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Debugging: Menampilkan halaman yang diambil untuk memeriksa elemen
            print(f"[INFO] Mengambil data dari {url}")
            
            # Ambil semua produk dari halaman
            products = soup.find_all('div', class_='collection-card')

            data = []
            for product in products:
                # Ambil semua elemen produk
                title_tag = product.find('h3', class_='product-title')
                price_tag = product.find('span', class_='price') or product.find('p', class_='price')

                # Menangani elemen rating, size, colors, dan gender
                rating_tag = product.find('p', string=lambda text: text and 'Rating' in text)
                colors_tag = product.find('p', string=lambda text: text and 'Colors' in text)
                size_tag = product.find('p', string=lambda text: text and 'Size' in text)
                gender_tag = product.find('p', string=lambda text: text and 'Gender' in text)

                # Debugging: Periksa apakah elemen-elemen ditemukan
                # if title_tag:
                #     print(f"[DEBUG] Title: {title_tag.text.strip()}")
                # else:
                #     print(f"[DEBUG] Title: NOT FOUND")
                    
                # if price_tag:
                #     print(f"[DEBUG] Price: {price_tag.text.strip()}")
                # else:
                #     print(f"[DEBUG] Price: NOT FOUND")

                # Jika semua elemen ditemukan, ambil data
                if title_tag and price_tag:
                    title = title_tag.text.strip()
                    
                    # Menangani harga yang tersedia dan tidak tersedia
                    price = price_tag.text.strip()
                    if "Price Unavailable" in price:
                        price = None  # Harga tidak tersedia

                    rating = rating_tag.text.strip() if rating_tag else "Not Rated"
                    colors = colors_tag.text.strip() if colors_tag else "Unknown"
                    size = size_tag.text.strip() if size_tag else "Unknown"
                    gender = gender_tag.text.strip() if gender_tag else "Unknown"
                    
                    # Menambahkan ke dalam list data
                    data.append([title, price, rating, colors, size, gender])
            
            return data
        else:
            print(f"[ERROR] Halaman {page_number} tidak ditemukan (Status Code: {response.status_code})")
            return []
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengambil halaman {url}: {e}")
        return []

# Fungsi untuk menjalankan ekstraksi data dari halaman 1 hingga 50
def run_extraction():
    all_data = []
    
    for page in range(1, 51):  # Halaman 1 sampai 50
        print(f"Scraping halaman {page}...")
        page_data = extract_data(page)
        if page_data:  # Jika data berhasil diambil, tambahkan ke all_data
            all_data.extend(page_data)
        time.sleep(2)  # Memberi jeda antara permintaan ke server
    
    print(f"Total data yang diambil: {len(all_data)}")
    return all_data

# Menjalankan fungsi utama
if __name__ == "__main__":
    all_data = run_extraction()
