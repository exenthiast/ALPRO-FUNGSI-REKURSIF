import math

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return  2 * math.pi * jari_jari

def main():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    
    luas = luas_lingkaran(jari_jari)
    keliling =  keliling_lingkaran(jari_jari)
    
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah  {luas:.2f}")
    print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {keliling:.2f}")

main()
