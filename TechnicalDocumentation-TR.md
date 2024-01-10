# Teknik Dökümantasyon

[English](/TechnicalDocumentation-EN.md) | **Türkçe**

### Hakkında

Python Flask tabanlı, açık kaynak kodlu, Burhaniye bölgesini çocuklara eğlenceli bir şekilde oyun formatında tanıtmak için yapılmış bir web uygulaması.

### Kullanılan Diller

- Python v3.12.0
- JavaScript vES14
- HTML5
- CSS3

### Kullanılan Kütüphaneler

- Flask v3.0.0
- Jinja2 v3.1.2 
- Socket v1.0.0
- Secrets v1.0.0
- TailwindCSS v3.4.1

### Geliştirme Sürecinde Kullanılan Programlar

- Visual Studio Code v1.85.1 (kod editörü)
- GitHub Desktop v3.3.6 (Git arayüzü)
- Windows Terminal v1.18.3181.0 (terminal arayüzü)
- Git Bash v5.2.15 (terminal)

### Arayüz

Uygulamanın arayüzünde HTML5 ve Jinja2 kullanılmıştır. Arayüzün stillendirilmesinde arka plan görseli hariç TailwindCSS kullanılmıştır yalnızca arka plan görseli için CSS3 kullanılmıştır. Arayüzdeki ses efektlerini oynatmak için JavaScript kullanılmıştır. Ayrıca JavaScript, “404 Page Not Found” hatası alındığı taktirde kullanıcıyı başlangıç sayfasına otomatik olarak yönlendirmesi için de kullanılmıştır.

### Arka Uç

Sunucu tarafında bir Python web kütüphanesi olan Flask kullanılmıştır. Flask tercih edilmesinin sebebi, basit ve hızlı bir kütüphane olmasıdır. Flask dışında Python’ın kendi içinde dahil olan “secrets” ve “socket” kütüphaneleri de kullanılmıştır. Socket, uygulamanın çalıştığı yerel bilgisayarın IP adresine ulaşmak için kullanılmıştır. Secrets, 32 karakterli rastgele gizli bir şifre oluşturmak için kullanılır. Bu şifre Flask uygulamasının gizli anahtarıdır.

### Yayınlanma

Flask tabanlı uygulamamız [PythonAnyWhere.com](https://www.pythonanywhere.com/) sayesinde ücretsiz bir şekilde yayınlanmıştır. Uygulama geliştirme sürecinde Python’ın 3.12.0 sürümünü kullanmasına rağmen, PythonAnyWhere’deki yayınlanma sürümünde Python’ın 3.10.0 sürümünü kullanmıştır. Bunun sebebi PythonAnyWhere sitesinin desteklediği en güncel Python sürümünün 3.10.0 olmasıdır.

### Sürüm Kontrol

Sürüm kontrol için Git kullanılmıştır. Uygulama tamamen açık kaynak kodludur. [GitHub’dan tüm kodlara erişebilirsiniz.](https://github.com/DogukanUrker/BurhaniyeAPP)

### QR Kod

QR kod için [QR Code Generator](https://www.qr-code-generator.com/) kullanılmıştır. QR kod içinde “<https://burhaniyem.pythonanywhere.com/>” bağlantısı gömülüdür.

### Ses Dosyaları/Efektleri

Bütün ses dosyaları ve efektleri “mp3” formatındadır. Bunun sebebi mp3 dosya uzantısının neredeyse tüm web tarayıcıları tarafından desteklenmesidir. Ses efektleri (alkış, doğru ve yanlış cevap) [pixabay](https://pixabay.com/sound-effects/) sitesinden alınmıştır. Ses dosyaları (sesli anlatımlar) ise Samsung Note 10, HUAWEI MateBook D 15 ve iPhone 11 cihazlarıyla kayıt alınmıştır. Alınan kayıtlar “m4a” veya “ogg” formatından [Convertio](https://convertio.co/) sitesinden yararlanılarak “mp3” formatına dönüştürülmüştür.

### Görseller

Arkaplan görseli [Creative Fabrica](https://www.creativefabrica.com/) sitesinden alınmıştır. Diğer görseller için [Google Images](https://images.google.com/) ve [Bing Images](https://www.bing.com/images) kullanılmıştır. Dosya formatı olarak “png”, “jpeg”, “webp” ve “jfif” kullanılmıştır.


