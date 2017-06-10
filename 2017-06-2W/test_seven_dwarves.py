from seven_dwarves import SevenDwarves

def test_dfs():
    sd = SevenDwarves()
    print()
    sd.dfs([], list(range(6)), 4, 0)

