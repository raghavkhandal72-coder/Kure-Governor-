"""
KURE Governor — Mars Rover Image Compression Demo
Simulates autonomous algorithm selection for a Mars rover.
Invented by Raghav Khandal
"""

import sys
import math
sys.path.insert(0, '..')

from kure_governor import KUREGovernor


def wavelet_compress_recursive(n):
    """Recursive wavelet compression — O(n) extra space."""
    if n <= 1:
        return 0
    mid = n // 2
    return wavelet_compress_recursive(mid) + wavelet_compress_recursive(n - mid) + n


def run_length_compress_iterative(n):
    """Iterative run-length encoding — O(1) extra space."""
    total = 0
    for i in range(n):
        total += i % 256  # Simulated compression work
    return total


# Mars Rover Configuration (very tight constraints)
rover_gov = KUREGovernor(
    alpha=1.5,    # Higher recursion penalty (stack is precious)
    beta=1.0,     # Standard container weight
    gamma=0.5,    # Energy exponent
    threshold=80  # Strict safe threshold for rover
)

print("=" * 65)
print("  🚜  MARS ROVER — Autonomous Algorithm Selection")
print("  KURE Governor by Raghav Khandal")
print("=" * 65)

image_sizes = [64, 256, 1024, 4096]  # Image resolution sizes

for size in image_sizes:
    print(f"\n{'─' * 55}")
    print(f"📸 Image Size: {size}×{size} pixels")

    res_wavelet = rover_gov.evaluate(wavelet_compress_recursive, size)
    res_runlength = rover_gov.evaluate(run_length_compress_iterative, size)

    print(f"\n🔴 Wavelet Compression (Recursive):")
    print(f"   SpaceCode: {res_wavelet['SpaceCode']}")
    print(f"   KURE Score: {res_wavelet['KURE Score']}")
    print(f"   Status: {res_wavelet['Status']}")

    print(f"\n🟢 Run-Length Encoding (Iterative):")
    print(f"   SpaceCode: {res_runlength['SpaceCode']}")
    print(f"   KURE Score: {res_runlength['KURE Score']}")
    print(f"   Status: {res_runlength['Status']}")

    comparison = rover_gov.compare(
        wavelet_compress_recursive,
        run_length_compress_iterative,
        size
    )

    print(f"\n🏆 Rover Decision: Use '{comparison['Winner']}'")

    if res_wavelet['Status'] == 'UNSAFE':
        print("   ⚠️  Recursive method rejected — memory overflow risk!")
        print("   🚀 Rover autonomously selected safe iterative method.")

print(f"\n{'=' * 65}")
print("  ✅ Mars Rover Demo Complete")
print("  KURE Governor — Protecting Space Missions")
print("=" * 65)