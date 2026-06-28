# ⚽ Spor Veri Sorgulama ve İstatistik Sistemi

Bu proje, Türkiye Süper Ligi başta olmak üzere çeşitli liglerdeki futbol takımlarının temel verilerine (şampiyonluk sayıları, teknik direktör, başkan vb.) hızlıca erişmeyi sağlayan, **açık kaynaklı** bir veri sorgulama sistemidir.

## 🚀 Projenin Amacı
Sistemin amacı, karmaşık web sayfalarında vakit kaybetmeden, sadece takım ismi girerek o takıma ait en güncel verileri "çat" diye ekrana yansıtmaktır. Kullanıcılar veriyi sorgular, sistem GitHub üzerindeki JSON dosyasından en güncel bilgiyi çeker ve `Streamlit` arayüzü ile sunar.

## 🛠️ Nasıl Çalışır?
* **Veri Kaynağı:** Tüm takım bilgileri GitHub üzerinde barındırılan merkezi bir `takimlar.json` dosyasında tutulur.
* **Sorgulama:** Python/Streamlit tabanlı arayüz, kullanıcıdan aldığı takım ismini JSON dosyasında "sözlük araması" yöntemiyle saniyeler içinde bulur.
* **Güncellik:** Veri dosyasında yapılan herhangi bir değişiklik, uygulamaya anında yansıtılır.



## 🤝 Katkıda Bulunma Rehberi
Bu projeye yeni takımlar, ligler veya eksik verileri ekleyerek katkıda bulunabilirsiniz. Süreç tamamen güvenli ve kontrol altındadır:

1.  **Fork Edin:** Bu repoyu sağ üstteki "Fork" butonuna basarak kendi hesabınıza kopyalayın.
2.  **Düzenleyin:** Kendi kopyanızdaki `takimlar.json` dosyasını açıp gerekli verileri ekleyin.
3.  **Commit Yapın:** Değişiklikleri kendi kopyanıza kaydedin.
4.  **Pull Request Gönderin:** "Contribute" > "Open pull request" yolunu izleyerek değişikliklerinizi bana gönderin.
5.  **Onay:** Gönderdiğiniz veriler tarafımca incelenecek ve uygun bulunursa ana sisteme dahil edilecektir.



---
*Bu sistem, spor istatistiklerine hızlı ve şeffaf bir erişim sağlamak amacıyla geliştirilmiştir.*
