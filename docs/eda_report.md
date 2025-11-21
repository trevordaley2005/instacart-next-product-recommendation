# EDA Raporu  

22 Kasım 2025

## 1) Veri Seti Genel Görünüm

Instacart veri seti; kullanıcı sipariş geçmişi, ürün bilgisi ve ürün–kullanıcı etkileşimlerinden oluşan geniş bir e-ticaret datasıdır.

Kullandığım temel tablolar:

- **orders:** 3.4M sipariş --> kullanıcıların sipariş zaman bilgileri  
- **order_products_prior:** 32M satır --> geçmiş siparişlerde alınan ürünler  
- **order_products_train:** 1.38M satır --> modelin öğreneceği hedef etiket  
- **products:** ürün kataloğu  
- **aisles & departments:** ürün kategorileri  

Orders tablosunda yalnızca `days_since_prior_order` kolonunda **206.209 eksik satır** bulunuyor.  
Bunlar kullanıcıların ilk siparişleri olduğu için doğal bir eksiklik ve veri hatası olarak değerlendirilmedi.

---

## 2) Orders Tablosu – Kullanıcı Davranışı

Siparişlerin zaman dağılımına baktığımda:

- Sipariş yoğunluğu **10:00'da başlıyor** (Şekil 1: order_hour_distribution.png)  ve **15:00 arasında pik yapıyor**.  
- Gece saatlerinde sipariş neredeyse yok (özellikle **01:00–04:00**).  
- Haftanın en yoğun günleri **Pazar ve Pazartesi**, en düşük gün **Perşembe**.

Sipariş aralığı (`days_since_prior_order`) grafiğinde:

- En yoğun aralık **3–10 gün**.  
- **30 gün** civarında da belirgin bir tepe var (aylık alışveriş davranışı).  
- Bu tablo, kullanıcıların belirgin alışveriş ritimleri olduğunu gösterdi ve FE aşamasında zaman tabanlı özelliklere ağırlık verilmesi gerektiğini düşündürdü.

---

## 3) Products – Ürün Özellikleri

En çok satın alınan ürünlere baktığımda:

- Üst sıraların neredeyse tamamı **taze meyve–sebze** ve **organik ürünlerden** oluşuyor.  
- **Banana (muz)** açık ara en çok satın alınan ürün.  
- Organik ürünlerin yoğunluğu belirgin.  
- Ürün katalog tabloları (products, aisles, departments) temiz ve tutarlı.  
- Kategori tabanlı özellik üretmek için uygun bir yapı var.

---

## 4) Aisles ve Departments

Aisle ve department dağılımlarında:

- En yoğun kategoriler: **fresh fruits**, **fresh vegetables**, **packaged vegetables & fruits**  
- Departman düzeyinde **produce**, veri setinin en baskın bölümü.  
- Bu tablo, kullanıcıların temel gıda alışverişi ağırlıklı davrandığını doğruluyor.  
- Bu sebeple kategori bazlı FE’ler model için önemli olacak.

---

## 5) Order_Products_Prior – Asıl Bilgi Kaynağı

- Prior tablosu (32M satır), geçmiş alışveriş davranışını içerdiği için proje açısından en kritik tablo.  
- `reordered` oranı yaklaşık **%60**.  
- `add_to_cart_order`, ürünlerin sepette hangi sırayla eklendiğini gösteriyor --> ilk eklenen ürünlerin daha temel ürünler olduğu görülüyor.  
- Bu tablo ileride kullanıcı–ürün geçmişi, ürün popülerliği ve sepetteki pozisyon gibi güçlü feature’lar üretmek için kullanılacak.

---

## 6) Train Tablosu – Hedef Değişken

`order_products_train` tablosunda:

- `reordered` sınıf dağılımı **%60 / %40**  
- Hafif dengesizlik var ama aşırı bir imbalance değil.  
- Accuracy tek başına yeterli olmayacağı için değerlendirme metriği olarak **F1-score** daha uygun.

---

## 7) Genel Değerlendirme

EDA sonunda gördüğüm temel noktalar:

- Veri yapısı temiz ve tutarlı.  
- Kullanıcıların alışveriş davranışı oldukça düzenli → zaman tabanlı özellikler anlamlı.  
- Ürün ve kategori dağılımları, market alışverişi alışkanlıklarıyla uyumlu.  
- Prior tablosu, FE için en değerli kaynak.  
- Train seti dengeli --> baseline model kurmak için uygun.

---

## 8) Sonraki Adım

EDA tamamlandı.  
Bir sonraki aşama: **Feature Engineering + Baseline Model**.

