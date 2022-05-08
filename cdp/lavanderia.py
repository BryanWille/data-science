entr = ""
while entr != "0 0":
    entr = input()
    entrada = entr.split(" ")
    num_part = int(entrada[0])
    num_probl = int(entrada[1])

    if num_part != 0 and num_probl != 0:
        if 3 <= num_part and num_probl <= 100:
            cont = 0
            dicionario = {}

            for c in range(0, num_probl):
                rodada_jogador = input().split(" ")
                array = []
                try:
                    array = [int(x) for x in rodada_jogador]
                except:
                    exit()
                dicionario.update({c: array})
                cont += 1

            checklist = 0

            resolvidos = [0 for x in range(0, num_probl)]
            ngm_resolveu_todos = True
            todos_resolveram_mesmo = False
            alguem_acertou_nada = False

            for key in dicionario:
                cont = 0
                quant_ganhado = 0
                for x in dicionario[key]:
                    if x == 1:
                        resolvidos[cont] += 1
                        quant_ganhado += 1
                    cont += 1
                if quant_ganhado == 0:
                    alguem_acertou_nada = True
                elif quant_ganhado == num_probl:
                    ngm_resolveu_todos = False

            for x in resolvidos:
                if x == num_part:
                    todos_resolveram_mesmo = True

            if ngm_resolveu_todos:
                checklist += 1
            if all(resolvidos):
                checklist += 1
            if not todos_resolveram_mesmo:
                checklist += 1
            if not alguem_acertou_nada:
                checklist += 1

            print(checklist)
