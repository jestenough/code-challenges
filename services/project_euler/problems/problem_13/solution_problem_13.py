def problem_13():
    import os
    with open(os.path.join(os.path.dirname(__file__), 'number.txt'), 'r') as f:
        return int(str(sum(int(i) for i in f.readlines()))[:10])
