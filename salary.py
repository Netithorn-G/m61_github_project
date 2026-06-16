salary = float(input("กรอกเงินเดือน: "))

tax = salary * 0.03
net_salary = salary - tax

print("ภาษีที่ต้องจ่าย =", tax, "บาท")
print("เงินเดือนสุทธิ =", net_salary, "บาท")
