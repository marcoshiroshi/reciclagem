from itertools import groupby


def cpf_verification(cpf):
    if not cpf or len(cpf) < 11:
        return False

    cpfs_block = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444',
                  '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']

    if cpf in cpfs_block:
        return False

    antigo_cpf = [int(d) for d in cpf]  # Remove verification digits
    novo_cpf = antigo_cpf[:9]

    # Generates new verification digits
    while len(novo_cpf) < 11:
        resto = sum([v * (len(novo_cpf) + 1 - i) for i, v in enumerate(novo_cpf)]) % 11
        digito_verificador = 0 if resto <= 1 else 11 - resto
        novo_cpf.append(digito_verificador)

    if novo_cpf == antigo_cpf:
        return cpf

    return False


def cnpj_verification(cnpj):
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
    cnpj_block = ['00000000000000', '11111111111111', '22222222222222', '33333333333333', '44444444444444',
                  '55555555555555', '66666666666666', '77777777777777', '88888888888888', '99999999999999']

    if cnpj in cnpj_block:
        return False

    if not cnpj or len(cnpj) < 14:
        return False

    antigo_cnpj = [int(d) for d in cnpj]
    novo_cnpj = antigo_cnpj[:12]
    weight = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = sum([novo_cnpj[i] * weight[1:][i] for i in range(12)]) % 11
    dv1 = dv1 if dv1 < 10 else 0
    novo_cnpj.append(dv1)
    dv2 = sum([novo_cnpj[i] * weight[i] for i in range(13)]) % 11
    dv2 = dv2 if dv2 < 10 else 0
    novo_cnpj.append(dv2)

    if novo_cnpj == antigo_cnpj:
        return True

    return False


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
