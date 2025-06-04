import time
from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_postgresql

# Fungsi utama untuk menjalankan pipeline ETL
def run_etl_pipeline():
    all_data = []
    
    # Ekstraksi data dari halaman 1 hingga 50
    for page in range(1, 51):  # Halaman 1 sampai 50
        print(f"Scraping halaman {page}...")
        page_data = extract_data(page)
        all_data.extend(page_data)
        time.sleep(2)  # Memberi jeda antara permintaan ke server
    
    print(f"Total data yang diambil: {len(all_data)}")
    
    # Transformasi data
    transformed_data = transform_data(all_data)
    
    # Menyimpan data ke CSV
    save_to_csv(transformed_data)
    
    # Menyimpan data ke PostgreSQL
    save_to_postgresql(transformed_data)
    
    print("ETL Pipeline selesai.")

# Menjalankan pipeline
if __name__ == "__main__":
    run_etl_pipeline()
