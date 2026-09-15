import sqlite3

def init_db():
    # SQLite veri tabanına bağlan (yoksa otomatik oluşturulur)
    conn = sqlite3.connect("career_bot.db")
    cursor = conn.cursor()

    # Meslekler tablosunu oluştur
    # Tablo Formatı:
    # - id: Benzersiz kimlik
    # - field: Sektör/Alan (ör. Teknoloji, Sanat, Sağlık)
    # - title: Meslek Adı
    # - description: Meslek Açıklaması
    # - skills: Gereken Yetenekler
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS careers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            field TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            skills TEXT NOT NULL
        )
    ''')

    # Örnek demo verileri ekle (Eğer tablo boşsa)
    cursor.execute("SELECT COUNT(*) FROM careers")
    if cursor.fetchone()[0] == 0:
        demo_careers = [
            ("Teknoloji", "Yapay Zeka Mühendisi", "Makine öğrenimi modelleri ve yapay zeka sistemleri geliştirir.", "Python, Matematik, Veri Analizi"),
            ("Teknoloji", "Siber Güvenlik Uzmanı", "Sistemlerin ve ağların güvenliğini sağlar, sızma testleri yapar.", "Ağ Bilgisi, Linux, Problem Çözme"),
            ("Sanat", "Dijital İllüstratör", "Oyunlar, kitaplar ve medya için dijital çizimler hazırlar.", "Çizim Yeteneği, Photoshop, Yaratıcılık"),
            ("Sanat", "UI/UX Tasarımcısı", "Kullanıcı dostu web ve mobil arayüzler tasarlar.", "Figma, İletişim, Empati"),
            ("Sağlık", "Biyoenformatik Uzmanı", "Biyolojik verileri analiz etmek için yazılım araçları geliştirir.", "Biyoloji, Python, İstatistik")
        ]
        cursor.executemany('''
            INSERT INTO careers (field, title, description, skills)
            VALUES (?, ?, ?, ?)
        ''', demo_careers)
        conn.commit()

    conn.close()

# Seçilen alana göre meslek getiren yardımcı fonksiyon
def get_careers_by_field(field_name):
    conn = sqlite3.connect("career_bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, skills FROM careers WHERE field = ?", (field_name,))
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    init_db()
    print("Veri tabanı başarıyla başlatıldı ve demo verileri yüklendi.")
