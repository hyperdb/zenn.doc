---
title: "［AtCorder］ABC-045｜Ｂ 3人でカードゲームイージー"
emoji: "⌨️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ['python', 'atcorder', 'abc']
published: true
---

## 設問ページ

- 🔗[ABC-045 B - 3人でカードゲームイージー](https://atcoder.jp/contests/abc045/tasks/abc045_b)

## 提出結果

```python
def getString():
    return input()


player_name = ['A', 'B', 'C']


def play(p, d):
    if (len(d[p]) == 0):
        print(player_name[p])
        return (-1)
    else:
        v = d[p].pop(0)
        return 0 if v == 'a' else 1 if v == 'b' else 2


def main():
    d = [
        list(getString()),
        list(getString()),
        list(getString())
    ]

    p = 0
    while p >= 0:
        p = play(p, d)


if __name__ == "__main__":
    main()
```
