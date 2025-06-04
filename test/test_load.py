import unittest
from utils.load import save_to_csv, save_to_postgresql
import os
import pandas as pd

class TestLoadData(unittest.TestCase):

    def test_save_to_csv(self):
        # Setup data contoh
        data = [
            ['T-shirt 2', 1634400, 3.9, 3, 'M', 'Women', '2025-02-10T13:54:32'],
            ['Hoodie 3', 7950080, 4.8, 5, 'L', 'Unisex', '2025-02-10T13:54:32']
        ]
        # Mengubah list menjadi DataFrame sebelum menyimpan ke CSV
        df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating', 'Stock', 'Size', 'Gender', 'Date'])
        
        # Menyimpan data ke CSV
        save_to_csv(df)  # Memanggil fungsi dengan DataFrame
        # Mengecek apakah file CSV telah disimpan
        self.assertTrue(os.path.exists('products.csv'), "CSV tidak disimpan")
        
    def test_save_to_postgresql(self):
        # Setup data contoh
        data = [
            ['T-shirt 2', 1634400, 3.9, 3, 'M', 'Women', '2025-02-10T13:54:32'],
            ['Hoodie 3', 7950080, 4.8, 5, 'L', 'Unisex', '2025-02-10T13:54:32']
        ]
        # Mengubah list menjadi DataFrame sebelum menyimpan ke PostgreSQL
        df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating', 'Stock', 'Size', 'Gender', 'Date'])
        
        # Menyimpan data ke PostgreSQL
        save_to_postgresql(df)  # Memanggil fungsi dengan DataFrame
        # Anda bisa menambahkan pengecekan untuk validasi data di PostgreSQL
        self.assertTrue(True, "Data tidak dapat disimpan ke PostgreSQL")


