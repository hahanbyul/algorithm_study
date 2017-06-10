from seven_dwarves import SevenDwarves

def test_dfs():
    sd = SevenDwarves()
    print()
    sd.dfs([], 0, list(range(6)), 4, 0)

