def bilangan_terkecil(A, B, C):
    if  A <= B and A <= C:
        return A
    elif  B <= A and B <= C:
        return B
    else:
        return C
    
def main():
    A = int(input("Masukkan nilai A: "))
    B = int(input("Masukkan nilai B: "))
    C = int(input("Masukkan nilai C: "))
    
    terkecil =  bilangan_terkecil(A, B, C)

    print(f"Bilangan terkecil {A}, {B}, {C} adalah {terkecil}")
    
main()
