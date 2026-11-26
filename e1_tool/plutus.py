"""plutus.py - ONE command per week / pair -> ONE Pine v6 script (S6): Engine 1 map + Engine 2 shape chain + Engine 3 trade setups, every number from data closed before the Monday anchor.
usage: python3 plutus.py MONDAY PAIR [out.pine]      (PAIR = DXY | EURUSD | GBPUSD; default output e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine)"""
import sys, os
import e1_pine as EP, e2_chain as E2

HERE = os.path.dirname(os.path.abspath(__file__))


def run(pair, monday):
    X = EP.run(pair, monday)
    lead = E2.build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None      # DXY = master direction (P533:1899-1917; GS Law 7)
    chain = E2.build(pair, monday, X, lead)
    setups = []
    try:
        import e3_trades as E3
        setups = E3.build(pair, monday, X, chain)
    except ImportError:
        E3 = None
    extra = E2.pine(pair, monday, chain) + (E3.pine(pair, monday, setups) if E3 else [])
    return X, chain, setups, EP.generate(pair, monday, X, extra, EP.reach(X, chain))


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, 'out', f'PLUTUS_{pair}_{monday}.pine')
    X, chain, setups, src = run(pair, monday)
    open(out, 'w').write(src)
    print(out)
