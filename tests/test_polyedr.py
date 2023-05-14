from pytest import approx
from common.r3 import R3
from shadow.polyedr import Segment, Edge, Polyedr

# polyedr строчка 147, удаление дубликатов ребер

# polyedr строчка 181, сумма длин нехороших ребер

# r3 строчка 46, хорошая ли точка


class TestR3_1:

    # r3 строчка 46, хорошая ли точка
    def test_is_good01(self):
        a = R3(0.0, 0.0, -1.0)
        assert not a.is_good()

    def test_is_good02(self):
        a = R3(-1.0, 1.0, 0.0)
        assert a.is_good()

    def test_is_good03(self):
        a = R3(0.0, 3.0, -1.0)
        assert not a.is_good()


class TestEdge_1:

    # polyedr строчка 46, является ли нехорошим отрезок
    def test_is_not_good01(self):
        s = Edge(R3(0.0, 0.0, -1.0), R3(2.0, 0.0, -1.0))
        assert s.is_not_good(1)

    def test_is_not_good02(self):
        s = Edge(R3(0.0, 0.0, -1.0), R3(1.0, -1.0, 0.0))
        assert not s.is_not_good(1)

    def test_is_not_good03(self):
        s = Edge(R3(0.0, 0.0, -1.0), R3(2.0, 0.0, 0.0))
        assert s.is_not_good(1)

#         python3 -B -m pytest -p no:cacheprovider tests/


class TestPolyedr:

    def test_sum_of_lens01(self):
        p = Polyedr(f"data/file_1.geom")
        assert p.sum_of_lens() == 3

    def test_sum_of_lens02(self):
        p = Polyedr(f"data/file_2.geom")
        assert p.sum_of_lens() == approx(11.31371)

    def test_sum_of_lens03(self):
        p = Polyedr(f"data/file_3.geom")
        assert p.sum_of_lens() == 0

    def test_sum_of_lens04(self):
        p = Polyedr(f"data/file_4.geom")
        assert p.sum_of_lens() == approx(12.32456)
