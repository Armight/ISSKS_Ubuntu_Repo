def xor_fluxu_zifraketa(mezua_str, gakoa_str):


    mezua_bytes = mezua_str.encode('utf-8')
    gakoa_bytes = gakoa_str.encode('utf-8')

    gakoa_egokituta = (gakoa_bytes * ((len(mezua_bytes) // len(gakoa_bytes)) + 1))[:len(mezua_bytes)]

    kriptograma_bytes = bytes(b ^ k for b, k in zip(mezua_bytes, gakoa_egokituta))

    deszifratuta_bytes = bytes(b ^ k for b, k in zip(kriptograma_bytes, gakoa_egokituta))

    print(f"Jatorrizko mezua (testua): {mezua_str}")
    print(f"Jatorrizko mezua (hex):    {mezua_bytes.hex()}")
    print(f"Gakoa (hex):               {gakoa_egokituta.hex()}")
    print(f"Kriptograma (hex):         {kriptograma_bytes.hex()}")
    print("-" * 50)

    deszifratutako_testua = deszifratuta_bytes.decode('utf-8')
    print(f"Deszifratutako mezua:      {deszifratutako_testua}")

    egiaztapena = (mezua_bytes == deszifratuta_bytes)
    print(f"Egiaztapena zuzena da?:    {egiaztapena}")

mezua = "GURE MEZUA HAU DA" 
gakoa = "GAKO01234567890"

xor_fluxu_zifraketa(mezua, gakoa)
