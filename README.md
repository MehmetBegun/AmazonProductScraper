# Amazon Product Scraper

Bu proje, Selenium kullanarak Amazon'daki belirli bir ürünün bilgilerini otomatik olarak çekip CSV dosyasına kaydeden basit bir web kazıyıcı (scraper) uygualamasıdır.

## Özellikler

- Amazon ürün sayfasından ürün adı, fiyat, açıklama maddeleri, kullanıcı değerlendirmesi ve ürünün ön plana çıkan görüntüsünün URL'sini çeker.
- Verileri yapılandırılmış şekilde CSV dosyasına yazar.
- Google Chrome için WebDriver yönetimini otomatik yapar.
- Tarayıcıyı arka planda (headless modda) çalıştırarak kullanıcı etkileşimi olmadan işlem yapar.

## Kullanım

1. Gerekli Python kütüphanelerini kurun:
   ```
   pip install selenium webdriver-manager
   ```

2. Scripti çalıştırın. Varsayılan olarak Logitech G502 ürün sayfasını kazıyacaktır.

3. İşlem tamamlandığında `product.csv` dosyasında ürün bilgilerini görüntüleyebilirsiniz.

## Proje Yapısı ve Fonksiyonlar

- `create_driver()`: Chrome tarayıcısını headless modda açar ve WebDriver'ı hazırlar.
- `scrape_product_data(driver, url)`: Verilen URL'deki ürünü ziyaret edip, gerekli bilgileri toplar.
- `write_to_csv(filename, data)`: Toplanan veriyi CSV formatında dosyaya kaydeder.

## Notlar

- Kodda kullanılan CSS ve ID seçiciler Amazon sayfa yapısına özeldir ve sayfa yapısı değişirse güncellenmesi gerekebilir.
- Headless mod sayesinde arka planda hızlıca çalışabilir.
- Daha fazla ürün için URL parametre olarak genişletilebilir.
---

Bu araç, temel web kazıma örneği olarak geliştirilmiş olup, istenilen çeşitli e-ticaret sayfalarına uyarlanabilir.
