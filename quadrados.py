from collections import Counter

def soma_quadrados(n):
    res = {0: [0]}
    quad = []
    maximo = 1
    if n == 0:
        return [0]
    else:
        while maximo*maximo <= n:
            quad.append(maximo*maximo)
            maximo = maximo + 1
            
        while len(quad) > 0:
            valor = n
            quadrado = quad.copy()
            n1 = quadrado.pop()
            resp=[]
            
            while valor > 0:
                if valor in res.keys() and valor is not n:
                    resp = resp + res[valor]
                    valor = 0
                else:
                    if len(quadrado) > 0:
                        n2 = valor - n1
                        if n2 < 0: n1 = quadrado.pop()
                        else:
                            valor = valor - n1
                            resp.append(n1)
                    else:
                        valor = valor - n1
                        resp.append(n1)
                        
            if n not in res.keys() and n != 0:
                res[n] = resp.copy()
            elif len(resp) < len(res[n]): res[n] = resp.copy()
            quad.pop()
        return res[n]


import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
if __name__ == '__main__':
    unittest.main()
