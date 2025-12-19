---
title: "［AtCoder］ABC-424｜B - Perfect"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-424 B - Perfect](https://atcoder.jp/contests/abc424/tasks/abc424_b)

## 提出結果

```python
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M, K = getIntMap()
    AB = getIntListRow(K)

    ans = [0] + [0 for _ in range(N)]
    p = []
    for a, _ in AB:
        ans[a] += 1
        if ans[a] == M:
            p.append(a)

    if len(p) > 0:
        print(" ".join(map(str, p)))


if __name__ == "__main__":
    main()
```
