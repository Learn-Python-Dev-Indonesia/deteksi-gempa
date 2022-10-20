import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    """
    Tanggal : 19 Oktober 2022,
    Waktu : 13:27:28 WIB
    Magnitudo : 3.4
    Kedalaman : 5 km
    Lokasi : LU = 2.06 LU BT 98.98
    Pusat Gempa : Pusat gempa berada di darat 5 km TimurLaut Tapanuli Utara
    Dirasakan : Dirasakan (Skala MMI): III Sipoholon, III Tarutung
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception :
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tanggal = soup.find('span', {'class':'waktu'})
        waktu = tanggal.text.split(', ')[1]
        tanggal = tanggal.text.split(', ')[0]


        hasil = dict()
        hasil['tanggal'] = tanggal #'19 Oktober 2022'
        hasil['waktu'] = waktu #'13:27:28 WIB'
        hasil['magnitudo'] = 3.4
        hasil['kedalaman'] = '5 km'
        hasil['lokasi'] = {'ls': 2.06, 'bt': 98.98}
        hasil['pusat'] = 'Pusat gempa berada di darat 5 km TimurLaut Tapanuli Utara'
        hasil['dirasakan']= 'Dirasakan (Skala MMI): III Sipoholon, III Tarutung'
        return hasil
    else:
        return None
def tampilkan_data(result):
    if result is None:
        print('Tidak Bisa menampilkan Data BMKG')
        return
    print('Gempa Terahkir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat {result['pusat']}")
    print(f"dirasakan {result['dirasakan']}")