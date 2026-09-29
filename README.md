# 🚀 Kariyer Danışmanı Discord Botu

Bu projede ilginizi çeken bir alanı seçiyorsunuz ve bot size o alanla ilgili popüler meslekleri ve kariyer önerilerini getiriyor. Bot ayrıca Gemini AI entegrasyonuna ve SQL veri tabanı altyapısına sahiptir.

Botu çalıştırmak için !kariyer komutunu kullanabilirsiniz.

# 📌 Botun Özellikleri ve Kullanımı

## 1. Etkileşimli Kariyer Arayüzü (!kariyer)

Açılır Menü (Dropdown): Teknoloji, Sanat veya Sağlık alanlarından birini seçtiğinizde SQL veri tabanından ilgili meslekleri, açıklamalarını ve gerekli yetenekleri listeler.
![Kariyer Görünümü](https://github.com/Ygz312629/Mezuniyet-Python-Level-3/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-09-29%20191559.png?raw=true)


Detaylı Rehber İste Butonu: Seçtiğiniz alanla ilgili online kurs ve proje tavsiyeleri verir.

Danışmanla Görüş Butonu: Destek, istek ve şikayetlerinizi iletebileceğiniz e-posta adresini paylaşır.

## 2. Yapay Zeka Danışmanı (!ai [sorunuz])

Gemini AI modeli entegrasyonu sayesinde kullanıcıların sadece kariyer, meslek ve yetenek gelişimi ile ilgili sorularını yanıtlar.

Kariyer dışındaki genel sohbet veya alakasız soruları otomatik olarak filtreler ve nazikçe reddeder.

## 3. Diğer Komutlar

!ara [alan_adı] : Doğrudan metin ile alan araması yapmanızı sağlar (Örn: !ara Teknoloji).

!yardim : Tüm komutları ve özellikleri anlatan yardım rehberini kanala gönderir.

# 🛠️ Kurulum ve Çalıştırma

Gerekli kütüphaneleri yükleyin:

pip install discord.py google-genai


bot.py dosyasındaki DISCORD_BOT_TOKEN_BURAYA ve GEMINI_API_KEY_BURAYA kısımlarına kendi anahtarlarınızı ekleyin.

Botu başlatın:

python bot.py
