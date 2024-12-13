def main():
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    ai.sort()
    bi.sort(reverse=True)
    s = 0
    i0 = 0
    i1 = n - 1
    j0 = 0
    j1 = m - 1
    while i0 <= i1:
        s0 = abs(ai[i0] - bi[j0])
        s1 = abs(ai[i1] - bi[j1])
        if s0 > s1:
            s += s0
            i0 += 1
            j0 += 1
        else:
            s += s1
            j1 -= 1
            i1 -= 1
    return s
"""
Registering simulator runtime with CoreSimulator failed.
Domain: DVTDownloadableErrorDomain
Code: 29
User Info: {
    DVTErrorCreationDateKey = "2024-01-16 13:32:01 +0000";
}
--
Cannot copy the image because the disk is almost full
Domain: com.apple.CoreSimulator.simdiskimaged.SimDiskImageError
Code: 14
--


System Information

macOS Version 14.1 (Build 23B74)
Xcode 15.2 (22503) (Build 15C500b)
Timestamp: 2024-01-16T16:32:01+03:00
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
