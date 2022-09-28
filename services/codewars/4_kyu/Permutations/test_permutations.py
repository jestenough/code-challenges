from solution_permutations import permutations


def test_permutations():
    assert sorted(permutations('a')) == ['a']
    assert sorted(permutations('ab')) == ['ab', 'ba']
    assert sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    assert sorted(permutations('abcd')) == ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
