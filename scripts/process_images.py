# NOTE: written for the pre-restructure layout (items/ + Gallery/ at repo root, pre 2026-09-16).
# Do not re-run as-is: it would inject broken image paths. Layout is now assets/ + docs/.
import os
import glob
from PIL import Image
from rembg import remove

ITEMS_DIR = r"e:\himros web\items"
HTML_FILES = glob.glob(r"e:\himros web\*.html")

product_image_files = [
    "Acytron Forte.png", "Acytron KD.png", "Alpha KD DS.png", "Alpha KD.png",
    "Androwin.png", "Curepcos.jpeg", "Curepcos.png", "Durahaim 60.png",
    "Durahim 30.png", "Durahim gel.png", "Embroyshield.png", "Eractlong.png",
    "Erectlong.jpeg", "Foligaurd.png", "Himdrol.png", "Himeract pro.png",
    "Himract Gold med .png", "Himract Gold med.png", "Himract Gold.png",
    "Himract capsule.png", "Himract gel.png", "Himtam D.png", "Libart caupsule.png",
    "Librt pro.png", "Pro-kd45.jpeg", "ProdkD 15.png", "Prodky45.png",
    "Rekover.jpeg", "Rekover.png", "Stoxlate.jpeg", "Stoxlate.png",
    "Tadox 10.png", "Tadox 2.25.png", "Tadox 5.png", "Tadox DP.png",
    "acytron-forte.jpeg", "acytron-kd.jpeg", "androwin.jpeg", "aplha-kd ds.jpeg",
    "aplha-kd.jpeg", "durahim-30.jpeg", "durahim-gel.jpeg", "durahim.jpeg",
    "embry-s.jpeg", "foliguard.jpeg", "himdriol.jpeg", "himract-gold-med.png",
    "himract-pro.jpeg", "himract.jpeg", "himrect gel.jpeg", "hitam-d.jpeg",
    "librt capsule.jpeg", "librt-pro.jpeg", "pro-kd15.jpeg", "tadox-10.jpeg",
    "tadox-2'5.jpeg", "tadox-5.jpeg", "tadox-dp.jpeg"
]

replacement_map = {}

print("Starting background removal...")

for img_name in sorted(list(set(product_image_files))):
    input_path = os.path.join(ITEMS_DIR, img_name)
    if not os.path.exists(input_path):
        print(f"Skipping (not found): {img_name}")
        continue
    
    base_name = os.path.splitext(img_name)[0]
    output_name = base_name + "_nobg.png"
    output_path = os.path.join(ITEMS_DIR, output_name)
    
    try:
        print(f"Processing: {img_name} -> {output_name}")
        with open(input_path, 'rb') as f_in:
            input_bytes = f_in.read()
            output_bytes = remove(input_bytes)
        
        with open(output_path, 'wb') as f_out:
            f_out.write(output_bytes)
            
        replacement_map[img_name] = output_name
        print(f"Successfully converted: {output_name}")
    except Exception as e:
        print(f"Error processing {img_name}: {e}")

print("\nUpdating HTML file image references...")

for html_path in HTML_FILES:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old_img, new_img in replacement_map.items():
        old_ref = f"items/{old_img}"
        new_ref = f"items/{new_img}"
        if old_ref in content:
            content = content.replace(old_ref, new_ref)
            modified = True
            print(f"In {os.path.basename(html_path)}: {old_ref} -> {new_ref}")
            
    if modified:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("\nAll done!")
