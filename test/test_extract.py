import unittest
from utils.extract import extract_data

class TestExtractData(unittest.TestCase):

    def test_extract_data_valid(self):
        # Menguji pengambilan data dari halaman yang valid (misalnya halaman 1)
        data = extract_data(1)
        self.assertGreater(len(data), 0, "Data tidak ditemukan atau kosong")
        self.assertEqual(len(data[0]), 6, "Format data salah, harus ada 6 kolom")

    def test_extract_data_invalid(self):
        # Menguji halaman yang tidak ada (misalnya halaman 1000)
        data = extract_data(1000)
        self.assertEqual(len(data), 0, "Data seharusnya kosong untuk halaman yang tidak ada")
    
    def test_extract_data_format(self):
        # Menguji format data yang diambil, memastikan data memiliki kolom yang benar
        data = extract_data(1)
        self.assertEqual(len(data[0]), 6, "Data harus memiliki 6 kolom")
        self.assertIsInstance(data[0][0], str, "Kolom Title harus berisi string")
        self.assertIsInstance(data[0][1], str, "Kolom Price harus berisi string")
        self.assertIsInstance(data[0][2], str, "Kolom Rating harus berisi string")
        self.assertIsInstance(data[0][3], str, "Kolom Colors harus berisi string")
        self.assertIsInstance(data[0][4], str, "Kolom Size harus berisi string")
        self.assertIsInstance(data[0][5], str, "Kolom Gender harus berisi string")
