import unittest
import numpy as np
import pandas as pd
from utils.transform import transform_data

class TestTransformData(unittest.TestCase):

    def setUp(self):
        # Setup data contoh
        self.data = [
            ['T-shirt 2', '$1634400', 'Rating: ⭐ 3.9 / 5', '3 Colors', 'Size: M', 'Gender: Women'],
            ['Hoodie 3', '$7950080', 'Rating: ⭐ 4.8 / 5', '5 Colors', 'Size: L', 'Gender: Unisex']
        ]

    def test_transform_data(self):
        df = transform_data(self.data)
        
        # Pastikan kolom yang ada sudah benar
        self.assertEqual(df.shape[1], 7, "Harus ada 7 kolom setelah transformasi termasuk timestamp")
        
        # Pastikan harga sudah dalam IDR dan bertipe float
        self.assertIsInstance(df['Price'].iloc[0], float, "Harga seharusnya bertipe float")
        
        # Pastikan rating sudah menjadi float
        self.assertIsInstance(df['Rating'].iloc[0], float, "Rating seharusnya bertipe float")
        
        # Pastikan Colors sudah bertipe np.int64 (bukan pd.Int64Dtype atau int)
        self.assertIsInstance(df['Colors'].iloc[0], np.int64, "Colors seharusnya bertipe np.int64")
        
        # Pastikan Size dan Gender bertipe string
        self.assertIsInstance(df['Size'].iloc[0], str, "Size seharusnya bertipe string")
        self.assertIsInstance(df['Gender'].iloc[0], str, "Gender seharusnya bertipe string")
        
        # Pastikan Timestamp ada
        self.assertTrue('Timestamp' in df.columns, "Timestamp tidak ditemukan")

    def test_invalid_rating(self):
        # Menguji kasus rating yang invalid
        invalid_data = [['T-shirt 2', '$1634400', 'Rating: Invalid Rating / 5', '3 Colors', 'Size: M', 'Gender: Women']]
        df = transform_data(invalid_data)
        self.assertEqual(len(df), 0, "Data seharusnya dihapus jika rating invalid")
