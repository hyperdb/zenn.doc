# 解答のマークダウンを読み込んで解答済みの問題を抽出するスクリプト
# CSV形式で出力するため、`check.py > result.csv` のように実行してください
#
import glob
import os
import re


def main():
    result = dict()

    files = glob.glob(os.path.join(os.getcwd(), "articles", "*.md"))
    for file in files:
        if not os.path.isfile(file):
            continue
        with open(file, "r", encoding="UTF-8") as f:
            content = f.read()
            f.close()

            pattern = r"- 🔗\[(.*)\]\((.*)\)\n"
            m = re.search(pattern, content)

            if m:
                t = m.group(1).split(" - ")[0].strip()
                titles = t.split(" ")
                key = titles[0]
                submission = titles[1] if len(titles) > 1 else ""
                result.setdefault(key, []).append(
                    f'"{submission}"' if submission else ""
                )

    result = dict(sorted(result.items()))
    for key, submissions in result.items():
        if len(submissions) > 1:
            submissions = list(set(submissions))
            submissions.sort()
            print(f'"{key}", {", ".join(submissions)}')


if __name__ == "__main__":
    main()
