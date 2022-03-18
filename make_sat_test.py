from make_sat import find_sat


class TestSat:
    def test_one(self):
        solution = find_sat(1)
        assert solution == [[1]]

    def test_small(self):
        for i in range(2, 4):
            solution = find_sat(i)
            assert solution is None

    def test_rows(self):
        for i in range(4, 15):
            solution = find_sat(i)
            assert solution is not None
            assert len(solution) == i
            for row in solution:
                assert sum(row) == 1

    def test_columns(self):
        for i in range(4, 15):
            solution = find_sat(i)
            assert solution is not None
            assert len(solution[0]) == i
            for row in zip(*solution):
                assert sum(row) == 1
