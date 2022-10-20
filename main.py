"""
Aplikasi Deteksi Gempa
MODULARISASI DENGAN FUNCTION
"""
from gempaterkini import ekstrasi_data, tampilkan_data

if __name__ == '__main__' :
    print('Aplikasi Utama')
    result = ekstrasi_data()
    tampilkan_data(result)