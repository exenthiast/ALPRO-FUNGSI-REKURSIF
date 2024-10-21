def rata_rata(daftar_bilangan):
    total  = 0
    count = 0
    
    for bilangan in  daftar_bilangan:
        total += bilangan
        count += 1
        
    if count == 0:
        return 0
    return total / count

def main():
    N = int(input("Masukkan jumlah bilangan (N): "))
    
    daftar_bilangan =  []
    for i in range (N):
        bilangan = float(input(f"Masukkan bilangan ke-{i+1}: "))
        daftar_bilangan.append(bilangan)
        
    rata2 =  rata_rata(daftar_bilangan)
    
    print(f"Rata - rata dari {N} bilangan tersebut adalah: {rata2:.2f}")

main()
