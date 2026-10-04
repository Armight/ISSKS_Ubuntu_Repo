def cesar_indarra_erasoa(testu_zifratua):
    minus = "abcdefghijklmnopqrstuvwxyz"
    maius = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for gakoa in range(1, 26):
        deszifratuta = ""
        for letra in testu_zifratua:
            if letra in minus:
                deszifratuta += minus[(minus.index(letra) - gakoa) % 26]
            elif letra in maius:
                deszifratuta += maius[(maius.index(letra) - gakoa) % 26]
            else:
                deszifratuta += letra

        print(f"Gakoa {gakoa}: {deszifratuta}")


mezua = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"
cesar_indarra_erasoa(mezua)
