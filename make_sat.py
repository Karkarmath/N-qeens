from satispy import Variable
from satispy.solver import Minisat


def find_sat(n):
    assert n > 0

    # Проверка, что ферзей хотя бы n
    check_n = Variable('True')
    for i in range(n):
        row = -Variable('True')
        for j in range(n):
            row = row | Variable(str(i) + 'v' + str(j))
        check_n = check_n & row

    # Проверка, что нет 2 ферзей в одной строчке или столбце
    check_row_and_col = Variable('True')
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j != k:
                    check_row_and_col = check_row_and_col & (
                            (- Variable(str(i) + 'v' + str(j))) | (- Variable(str(i) + 'v' + str(k))))
                    check_row_and_col = check_row_and_col & (
                            (- Variable(str(j) + 'v' + str(i))) | (- Variable(str(k) + 'v' + str(i))))

    # Проверка, что нет 2 ферзей на одной из главных диагоналей
    check_main_dia = Variable('True')
    for sum in range(2 * n):
        for i in range(n):
            for j in range(n):
                k1 = sum - i
                k2 = sum - j
                if n > k1 > -1 and n > k2 > -1 and i != j:
                    check_main_dia = check_main_dia & (
                            (- Variable(str(i) + 'v' + str(k1))) | (- Variable(str(j) + 'v' + str(k2))))

    # Проверка, что нет 2 ферзей на одной из побочных диагоналей
    check_side_dia = Variable('True')
    for neg in range(-n, n):
        for i in range(n):
            for j in range(n):
                k1 = i + neg
                k2 = j + neg
                if n > k1 > -1 and n > k2 > -1 and i != j:
                    check_side_dia = check_side_dia & (
                            (- Variable(str(i) + 'v' + str(k1))) | (- Variable(str(j) + 'v' + str(k2))))

    full_check = check_n & check_row_and_col & check_main_dia & check_side_dia
    solver = Minisat()
    sat_solution = solver.solve(full_check)

    if sat_solution.success:
        solution = [[int(sat_solution[Variable(str(i) + 'v' + str(j))]) for j in range(n)] for i in range(n)]
        return solution
    else:
        return None




if __name__ == "__main__":
    n = int(input())

    find_sat(n)
    solution = find_sat(n)

    if solution is not None:
        print('Found a solution:')
        for i in solution:
            for j in i:
                print(j, end=" ")
            print()
    else:
        print('There is no such an arrangement')
