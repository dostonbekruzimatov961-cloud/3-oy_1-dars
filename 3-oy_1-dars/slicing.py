ism = input("Ism kiriting: ").lower()
familiya = input("Familiyangizni kiriting: ").lower()

matn = f"{ism}_{familiya[:4:]}"
print(f"Esername: {matn}")