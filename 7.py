# Вариант 2

products = ["Keyboard", "Mouse", "Cable", "Monitor", "Trackball", "Gamepad"]
amounts = [8, 11, 3, 7, 15, 12]
print(f"products = {products}; amounts = {amounts}")

order = [k for k, v in zip(products, amounts) if v < 10]
print(order)
