def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)
    
def main():
    a = int(input("Masukkan bilangan pertama (A): "))
    b = int(input("Masukkan bilangan kedua  (B): "))
    
    hasil_fpb = fpb(a, b)
    
    print(f"FPB dari {a} dan {b} adalah {hasil_fpb}")
    
main()
