# Bước chuẩn bị: Tạo file demo_file1.txt
content = "Thuc \nhanh \nvoi \nfile\nIO\n"
with open('demo_file1.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("--- Câu a: In trên một dòng ---")
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    noi_dung = f.read()
    
    mot_dong = noi_dung.replace('\n', ' ')
    print(mot_dong)


print("\n--- Câu b: In theo từng dòng ---")
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())