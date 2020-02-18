io = open("prob04.txt").read().splitlines()

for i in range(1, len(io), 2):
    tax_rate = float(io[i]) / 100
    total = float(io[i + 1])
    pretax_price = total / (1.0 + tax_rate)
    tax_amount = pretax_price * tax_rate
    print(f"On your ${format(total, '.2f')} purchase, the tax amount was ${format(tax_amount, '.2f')}")
