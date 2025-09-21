def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total de compra.

    Args:
        monto_total (float): El monto total de la compra
        porcentaje_descuento (float, optional): Porcentaje de descuento. Por defecto es 10.

    Returns:
        float: El monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # Primera función: solo monto total, usa descuento por defecto (10%)
    monto1 = 1000
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra 1: Monto total = ${monto1:.2f}")
    print(f"Descuento (10%) = ${descuento1:.2f}")
    print(f"Monto final a pagar = ${monto_final1:.2f}\n")

    # Segunda función: monto total y porcentaje de descuento personalizado
    monto2 = 2000
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Compra 2: Monto total = ${monto2:.2f}")
    print(f"Descuento ({porcentaje2}%) = ${descuento2:.2f}")
    print(f"Monto final a pagar = ${monto_final2:.2f}")


if __name__ == "__main__":
    main()