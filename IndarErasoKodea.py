def programa_interaktiboa(testua):

    maiztasunak = {}
    for c in testua:
        if "a" <= c.lower() <= "z":  
            maiztasunak[c] = maiztasunak.get(c, 0) + 1

    print("--- ZIFRATUAREN LETREN MAIZTASUNAK ---")
    for letra in sorted(
        maiztasunak, key=lambda x: maiztasunak[x], reverse=True
    ):
        print(f"'{letra}': {maiztasunak[letra]} aldiz")

    
    eguneratuta = testua
    while True:
        print("\n" + "=" * 50)
        print("UNEKO TESTUA:")
        print(eguneratuta)
        print("=" * 50)

        zahar = input(
            "\nZein letra aldatu nahi duzu? (idatzi 'irten' amaitzeko): "
        )
        if zahar.lower() == "irten" or not zahar:
            break

        berri = input(f"Zein letra jarri nahi duzu '{zahar}'ren ordez?: ")

        
        eguneratuta = eguneratuta.replace(zahar, berri)



mezua = "JIYQ WQIEtYLP YtXLLW OPLP! CWXYM SPMQPLtP YEYQWtP CPOX PLZP SBPJPQX bPBQXWYtPQX bPtYPM. JYLYM bPW, XLPWM HYMCY PEQX PtYLPtJYM CP HPWJQWbYB WQIEtYLP; tRPBXPQ YtP tRPBXPQ, YtP «PISP, HPWJQWbYB!» XWFIPQ WJPM CWLP MPOIEW WbWBbWCY XEXPM. QPBY MPOIEWP YLY HPCP YJ CP BYFYM bYJPWM OPtPJQPtEIP, bPWMP, XLPWMCWQ YLY, JYMbPWt YZPQIZY OPtJYQ SPEPYLPM bWJQPLLP YZPM CWXtY HPWJQWbYBW, SPLtY FPLtJYP bPWZYMtJYM CWYM QXMSPWMWP bPQPLLPW."

programa_interaktiboa(mezua)
