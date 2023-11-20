print("Градус Цельсія | Градус Фаренгейта")
print("---------------------------------")

for celsius in range(0, 1001, 20):
    fahrengeit=(celsius*9/5)+32
    print(f"{celsius:^10} | {fahrengeit:^16}")
