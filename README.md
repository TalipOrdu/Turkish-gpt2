# Türkçe Şiir Üretimi - turkish-gpt2 Modeli ile

Bu proje, Yıldız Teknik Üniversitesi'nin geliştirdiği **"turkish-gpt2-large-750m-instruct-v0.1"** modelini kullanarak Türkçe şiir üretmeyi amaçlamaktadır. 
Huggingface Transformers kütüphanesi ile GPT-2 tabanlı bu dil modeli, verilen başlangıç metninden yola çıkarak anlamlı ve yaratıcı Türkçe şiir dizeleri üretmektedir.

## Proje Özellikleri

- **Model:** ytu-ce-cosmos/turkish-gpt2-large-750m-instruct-v0.1 (Türkçe GPT-2 büyük boyutlu model)
- **Girdi:** Kullanıcı tarafından belirlenen başlangıç şiir satırı veya kelime grubu
- **Çıktı:** Modelin oluşturduğu, anlamlı ve akıcı şiir dizeleri
- **Teknik:** Huggingface Transformers, PyTorch kullanılarak metin tokenizasyonu ve üretimi  
- **Özelleştirme:** Sampling parametreleri (top_k, top_p, temperature, repetition_penalty) ile üretim çeşitliliği ve tekrar kontrolü sağlanır
- **Sonuç:** Üretilen şiirler konsola yazdırılır ve tarih damgası ile birlikte `poem.txt` dosyasına kaydedilir

## Kullanım

Projede örnek olarak şu başlangıç metni verilmiştir: Kenetlenmişsin kalbime, ilmek ilmek,

Bu metin model tarafından işlenerek yaklaşık 100 token uzunluğunda şiir üretimi yapılır.

## Amaç

Türkçe doğal dil işleme alanında yaratıcı metin üretimi için yerli kaynakların kullanılması ve geliştirilmesi hedeflenmektedir. 
Bu çalışma, Türkçe dilinde şiir üretimi yapan modellerin pratik kullanımını göstermektedir.

## Geliştirici Ekip

Bu projede kullanılan GPT-2 tabanlı Türkçe dil modeli, Yıldız Teknik Üniversitesi Cosmos ekibi tarafından geliştirilmiştir. 
Daha fazla bilgi ve projeleri incelemek için:

🔗 [https://cosmos.yildiz.edu.tr/](https://cosmos.yildiz.edu.tr/)
