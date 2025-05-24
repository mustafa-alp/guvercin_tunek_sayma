from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Modeli yükleme (model yolunu buraya girin)
model = YOLO("best.pt")  # Eğitilmiş model dosyanızın adı

# Resmi yükleyin
image_path = "IMG_8506.JPG"  # JPEG dosyanızın yolunu buraya girin
image = cv2.imread(image_path)

# YOLOv8 ile algılama
results = model(image_path,  iou=0.5)

# Algılanan nesne sayısını hesapla
detected_count = len(results[0].boxes)  # Algılanan kutucukların sayısı

# Algılama sonuçlarını görselleştir
annotated_image = results[0].plot()

text = f"Tunek sayisi: {detected_count}"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 10  # Yazı boyutunu büyük yapmak için ölçeği artırdık
color = (0, 255, 0)  # Yeşil renk
thickness = 10  # Kalınlığı artırarak okunabilirliği sağlıyoruz

# Sağ alt köşe koordinatlarını hesapla
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = annotated_image.shape[1] - text_size[0] - 50  # Sağdan 50 piksel boşluk
text_y = annotated_image.shape[0] - 50  # Alttan 50 piksel boşluk

cv2.putText(annotated_image, text, (text_x, text_y), font, font_scale, color, thickness)
# Sonuç görüntüsünü kaydet
cv2.imwrite("sonuc.jpg", annotated_image)

# Sonucu göster
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()