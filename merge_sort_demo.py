"""
KURE Governor — Merge Sort Space Analysis
Analyzes divide-and-conquer algorithms for space missions.
Invented by Raghav Khandal
"""

import sys
import math
sys.path.insert(0, '..')

from kure_governor import KUREGovernor


def merge_sort(arr):
    """Standard merge sort — O(n) extra space."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge — creates temporary array of size n
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr, left=0, right=None):
    """In-place merge sort simulation — O(1) extra space."""
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return arr
    mid = (left + right) // 2
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)
    # In-place merge would go here (simplified)
    return arr


# Satellite Configuration (balanced constraints)
sat_gov = KUREGovernor(
    alpha=1.0,
    beta=1.2,    # Slightly higher container penalty
    gamma=0.5,
    threshold=200
)

print("=" * 60)
print("  🛰️  SATELLITE — Merge Sort Space Analysis")
print("  KURE Governor by Raghav Khandal")
print("=" * 60)

for n in [8, 64, 1024]:
    print(f"\n{'─' * 50}")
    print(f"📊 Array Size n = {n}")

    res_merge = sat_gov.evaluate(merge_sort, n)
    print(f"\n🔴 Standard Merge Sort:")
    print(f"   SpaceCode: {res_merge['SpaceCode']}")
    print(f"   Big-O:     {res_merge['Space Complexity (Big-O)']}")
    print(f"   KURE:      {res_merge['KURE Score']}")
    print(f"   Decision:  {res_merge['Decision']}")

    res_inplace = sat_gov.evaluate(merge_sort_inplace, n)
    print(f"\n🟢 In-Place Merge Sort:")
    print(f"   SpaceCode: {res_inplace['SpaceCode']}")
    print(f"   Big-O:     {res_inplace['Space Complexity (Big-O)']}")
    print(f"   KURE:      {res_inplace['KURE Score']}")
    print(f"   Decision:  {res_inplace['Decision']}")

    if res_merge['Status'] == 'UNSAFE':
        print(f"\n   ⚠️  Standard merge sort EXCEEDS safe threshold at n={n}!")
        print(f"   🚀 Satellite switched to in-place merge sort.")

print(f"\n{'=' * 60}")
print("  ✅ Satellite Merge Sort Demo Complete")
print("=" * 60)