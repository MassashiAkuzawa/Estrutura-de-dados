import unittest
#O tempo é O(n²) pois tem um while dentro de outro while
#A memória é O(1) pois há apenas a lista e três variáveis

def insertion_sort(seq):
    a = len(seq)
    b = 0
    c = 0
    if a <= 1:
        return seq
    else:
        while c < a:
            d = b
            if seq[c] > seq[b]:
                b = b + 1
                c = c + 1
            else:
                b = b + 1
                c = c + 1
                while d > 0:
                    if seq[d - 1] > seq[d]:
                        seq[d - 1], seq[d] = seq[d], seq[d - 1]
                    d = d - 1
    return seq
        
    pass


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
