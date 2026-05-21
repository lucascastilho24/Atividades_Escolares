cpf = []
entrada = "09191148901"
print(entrada)
for i in entrada:
    cpf.append(int(i))

print(cpf)
dv = cpf[-2:]
nums = cpf[:9]
print(dv)
print(nums)
