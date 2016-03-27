import unittest
#O tempo é O(n²) pois tem um for dentro de outro for
#A memória é O(1) pois há apenas a lista e uma variável

def bubble_sort(seq):
    a = len(seq) - 1
    flag = 0
    for b in range(len(seq) - 1):
        for c in range(len(seq) - 1):
            if seq[c] > seq[c+1]:
                seq[c+1], seq[c] = seq[c], seq[c+1]
        if (flag):
            break
    return seq
    pass


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
