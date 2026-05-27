"""
KURE Governor — Factorial Demo
Compares recursive vs iterative factorial for space missions.
Invented by Raghav Khandal
"""

import sys
sys.path.insert(0, '..')

from kure_governor import KUREGovernor


def factorial_recursive(n):
    """Recursive factorial — O(n) stack space."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Iterative factorial — O(1) extra space."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# Initialize KURE Governor for a small satellite (tight memory)
gov = KUREGovernor(alpha=1.0, beta=1.0, gamma=0.5, threshold=50)

print("=" * 60)
print("  🛰️  KURE Governor — Factorial Space Analysis")
print("  Raghav Khandal — Space Technologist")
print("=" * 60)

for n in [5, 10, 20, 100]:
    print(f"\n{'─' * 50}")
    print(f"📊 Input Size n = {n}")

    res_rec = gov.evaluate(factorial_recursive, n)
    res_itr = gov.evaluate(factorial_iterative, n)

    print(f"\n🔴 Recursive Factorial:")
    print(f"   SpaceCode: {res_rec['SpaceCode']}")
    print(f"   Big-O:     {res_rec['Space Complexity (Big-O)']}")
    print(f"   KURE:      {res_rec['KURE Score']}")
    print(f"   Decision:  {res_rec['Decision']}")

    print(f"\n🟢 Iterative Factorial:")
    print(f"   SpaceCode: {res_itr['SpaceCode']}")
    print(f"   Big-O:     {res_itr['Space Complexity (Big-O)']}")
    print(f"   KURE:      {res_itr['KURE Score']}")
    print(f"   Decision:  {res_itr['Decision']}")

    if res_rec['Status'] == 'UNSAFE':
        print(f"\n   ⚠️  ALERT: Recursive factorial UNSAFE at n={n}!")
        print(f"   🚀 Rover auto-switched to iterative mode.")

print(f"\n{'=' * 60}")
print("  ✅ Demo Complete — KURE Governor Ready for Space")
print("=" * 60)