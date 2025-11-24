# Baseline Model Raporu 

24 Kasım 2025


## 1) Amaç

Bu aşamada veri setindeki ilk analizimi referans alarak model oluşturdum.  
Amacım “Bu ürün tekrar alınır mı?” sorusuna ilk cevabı verecek basit bir model üretmek.


# 2) Kullanılan Veri

Bu bölümde yalnızca:

- ürünün geçmişte ne kadar tekrar alındığını temsil eden feature, train_data[['reorder_ratio']]   
- hedef değişken olarak train_data['reordered']'i kullandım.

Sadece reorder_ratio kullanmamın sebebi: EDA sürecinde datasetimi analiz ederken `order`, `products` ve `prior` tablo incelememde:

- reorder oranının %60 civarında olması,  
- en çok alınan ürünlerin bir kısmının süt, muz, yumurta gibi ürünleri olması,  
- kullanıcıların belirli ürünleri tekrar alma eğiliminin yüksek olduğunu gözlemledim.  

Bu yüzden ilk modelde gözlemlerimi kontrol etmek ettim.  


# 3) Model Kurulumu

Basit bir Lojistik Regresyon kullanıldı.

- random_state = 42  
- test_size = 0.2  
- stratify = y (sınıf yapısını korumak için)  

Amacım tek feature ile modelin nerede durduğunu ve “bu ürün tekrar alınır mı?” sorusunun modele nasıl yansıdığını görmekti.  

# 4) Sonuçlar

Aşağıdaki metrikler validation set üzerinden hesaplandı:

- F1-Score :  0.7452
- Precision: 0.6614
- Recall   : 0.8535

Confusion matrix de görselleştirilip kaydedildi:  figures/baseline_confusion_matrix.png


# 5) Çıkarımlar

- Tek feature olmasına rağmen modelin performansı çok iyi, `reorder_ratio` güçlü bir feature olduğunu, bu ürün tekrar alınır mı sorusunun bu dataset için önemli olduğunu gördüm.  
- Recall 0.8535 değeri :  %85 model tekrar alınacak ürünleri güçlü şekilde anlıyor, model, tekrar alınacak ürünleri yakalama konusunda güçlü olması, baseline için iyi bir başlangıç gibi görünüyor.  
- Precision’ın düşük kalmasının sebebi: 72,436 ürün “tekrar alınır” diye tahmin edilmiş ama alınmamış, FE ile düzeltilebilir.  


6) Veri Kaçağı (Data Leakage) Kontrolü

- şimdilik problem görünmüyor ama FE aşamasında daha detaylı kontrol yapılacak  


7) Sonraki Adım

- Kullanıcı tabanlı özellikler (user-level features)
- Ürün + kullanıcı etkileşimi (user-product interaction)
- Sepet içi davranışlar (add_to_cart_order, order_number)


Baseline tamamlandı.
Bir sonraki aşama: **Feature Engineering**