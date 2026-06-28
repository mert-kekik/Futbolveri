​⚽ Spor Veri Sorgulama ve İstatistik Sistemi
​Bu proje, Türkiye Süper Ligi başta olmak üzere çeşitli liglerdeki futbol takımlarının temel verilerine (şampiyonluk sayıları, teknik direktör, başkan vb.) hızlıca erişmeyi sağlayan, açık kaynaklı bir veri sorgulama sistemidir.
​🚀 Projenin Amacı
​Sistemin amacı, karmaşık web sayfalarında vakit kaybetmeden, sadece takım ismi girerek o takıma ait en güncel verileri "çat" diye ekrana yansıtmaktır. Kullanıcılar veriyi sorgular, sistem GitHub üzerindeki JSON dosyasından en güncel bilgiyi çeker ve Streamlit arayüzü ile sunar.
​🛠️ Nasıl Çalışır?
​Veri Kaynağı: Tüm takım bilgileri GitHub üzerinde barındırılan merkezi bir takimlar.json dosyasında tutulur.
​Sorgulama: Python/Streamlit tabanlı arayüz, kullanıcıdan aldığı takım ismini JSON dosyasında "sözlük araması" yöntemiyle saniyeler içinde bulur.
​Güncellik: Veri dosyasında yapılan herhangi bir değişiklik, uygulamaya yansıtılır.
​🤝 Katkıda Bulunma Rehberi
​Bu projeye yeni takımlar, ligler veya eksik verileri ekleyerek katkıda bulunabilirsiniz. Süreç tamamen güvenli ve kontrol altındadır:
​Fork Edin: Bu repoyu sağ üstteki "Fork" butonuna basarak kendi hesabınıza kopyalayın.
​Düzenleyin: Kendi kopyanızdaki takimlar.json dosyasını açıp gerekli verileri ekleyin.
​Commit Yapın: Değişiklikleri kendi kopyanıza kaydedin.
​Pull Request Gönderin: "Contribute" > "Open pull request" yolunu izleyerek değişikliklerinizi bana gönderin.
​Onay: Gönderdiğiniz veriler tarafımca incelenecek ve uygun bulunursa ana sisteme dahil edilecektir.
​🛡️ Güvenlik ve Denetim
​Sistem, verilerin bütünlüğünü korumak adına "Protected Branch" kuralı ile yönetilmektedir. Hiçbir dış müdahale doğrudan ana dosyayı etkileyemez; her değişiklik sizin onayınızdan geçmek zorundadır.
​Bu sistem, spor istatistiklerine hızlı ve şeffaf bir erişim sağlamak amacıyla geliştirilmiştir.
