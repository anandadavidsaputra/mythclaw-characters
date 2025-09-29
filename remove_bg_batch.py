from PIL import Image
import os

# folder khusus SSR
ssr_folder = "C:\\Providd\\Portofolio\\mythclaw_characters\\ssr"

for file in os.listdir(ssr_folder):
    if file.lower().endswith(".png"):
        path = os.path.join(ssr_folder, file)
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

print("Selesai semua gambar SSR!")