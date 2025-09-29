from PIL import Image
import os

# folder utama semua tier
base_folder = r"C:\Providd\Portofolio\mythclaw_characters"

for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith(".png"):
            path = os.path.join(root, file)
            print(f"Memproses {path} ...")
            
            img = Image.open(path).convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                # jika pixel hampir putih -> buat transparan
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)
            img.save(path)
            print(f"{file} → selesai, background putih dihapus")

print("Selesai semua gambar di semua folder!")