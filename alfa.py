import unittest
from itertools import product

regra = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wzyz'}


def gerar_alfa(s):
    """
    Fazer análise de tempo e espaço
    Função recebe string com números de 2 a 9 e responde todas sequencias possíveis de letras
    Reg
    O tempo é O(n^2)
    O espaço é O(n)
    """
    res = [tuple()]
    for k in s:
        size = len(res) - 1
        while size >= 0:
            atual = res.pop(size)
            re = regra.__getitem__(k)
            for i in re:
                res.append(atual + tuple(i,))
            size -= 1
    return res
            


class Testes(unittest.TestCase):
    def testes_string_vazia(self):
        self.assertListEqual([tuple()], list(gerar_alfa('')))

    def testes_string_2(self):
        self.assertListEqual([('a',), ('b',), ('c',)], list(gerar_alfa('2')))

    def testes_string_3(self):
        self.assertListEqual([('d',), ('e',), ('f',)], list(gerar_alfa('3')))

    def testes_string_com_2_numeros(self):
        self.assertSetEqual(set((('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
                                 ('c', 'e'), ('c', 'f'))), set(gerar_alfa('23')))

    def testes_com_5_numeros(self):
        resultado = set(gerar_alfa('73696'))
        self.assertIn(tuple('renzo'), resultado)
        self.assertSetEqual(set(product('pqrs', 'def', 'mno', 'wzyz', 'mno')), resultado)
if __name__ == '__main__':
    unittest.main()
