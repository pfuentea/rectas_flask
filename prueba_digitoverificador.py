from itertools  import cycle

def validar_rut(rut: str, verificador: str) -> bool:
        rut = rut.replace(".", "").replace(",", "")
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        check_digit = (-s) % 11
        if check_digit == 10:
            check_digit = 'K'
        return str(check_digit) == str(verificador).upper()

rut="13460498"
dv="0"

print(validar_rut(rut,dv))  