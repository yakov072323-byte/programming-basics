signal = int(input("Введіть рівень сигналу (0-100): "))

if signal >= 90:
    status = "Відмінний сигнал"
elif signal >= 70:
    status = "Хороший сигнал"
elif signal >= 40:
    status = "Слабкий сигнал"
else:
    status = "Критично низький сигнал"

mode = "Штатний режим" if signal >= 40 else "Режим підсилення сигналу"

print(f"Рівень сигналу: {signal}%")
print(f"Стан: {status}")
print(f"Режим роботи: {mode}")
