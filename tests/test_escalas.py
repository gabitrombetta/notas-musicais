from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_com_notas_minusculas():
    tonica = 'c'
    tonalidade = 'maior'

    result = escala(tonica, tonalidade)

    assert result


def test_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    msg_erro = f'Essa nota não existe. Tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert msg_erro == error.value.args[0]


def test_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'

    msg_erro = f'Essa escala não existe ou não foi implementada. Tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert msg_erro == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_retorna_escalas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')

    assert resultado['notas'] == esperado


def test_graus():
    tonica = 'c'
    tonalidade = 'maior'

    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
