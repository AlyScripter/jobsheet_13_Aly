def weight_conversion():
    berat = int(input("masukkan berat badan anda = "))
    satuan = input("masukkan satuan kg (k) atau lbs (l)")

    if satuan.lower() == 'l':
        print(f"berat badan anda dikonversi ke kilogram adalah {round(berat * 0.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"berat badan anda dikonversi ke pounds adalah {round(berat * 2.20462)} lbs")

weight_conversion()
