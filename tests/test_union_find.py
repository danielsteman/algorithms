from algorithms.union_find import QuickFindUF


def test_quick_find_connected():
    N = [0, 1, 1, 8, 8, 0, 0, 1, 8, 8]
    qf = QuickFindUF(N)
    res_true = qf.connected(6, 5)
    res_false = qf.connected(4, 5)
    assert res_true == True
    assert res_false == False


def test_quick_find_union():
    N = [0, 1, 1, 8, 8, 0, 0, 1, 8, 8]
    qf = QuickFindUF(N)
    qf.union(4, 5)
    assert qf.id == [0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
