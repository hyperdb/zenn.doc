---
title: "［AtCoder］ABC-311｜C - Find it!"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'AtCoder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-311 C - Find it!](https://atcoder.jp/contests/abc311/tasks/abc311_c)

## 提出結果

```python
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = [x - 1 for x in getIntList()]

    pt = 0
    route = [pt]
    reached = [0 for _ in range(n)]
    reached[pt] = 1

    while True:
        nextPt = a[pt]
        if reached[nextPt] == 1:
            startIdx = route.index(nextPt)
            route = route[startIdx:]
            break
        else:
            pt = nextPt
            route.append(pt)
            reached[pt] = 1

    print(len(route))
    print(" ".join(map(str, [x + 1 for x in route])))


if __name__ == "__main__":
    main()
```
