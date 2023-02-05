import glob
import re
import os


def main():

    files = glob.glob("./articles/*.md")

    index = []
    for file in files:
        f = open(file, 'r', encoding='UTF-8')
        content = f.read()
        f.close()

        pattern = r'title: \"［.*?］(.*?)\"'
        result = re.search(pattern, content)

        t = result.group(1) if result else ''
        i = os.path.splitext(os.path.basename(file))[0]

        index.append([t, i])

    index.sort()

    f = open('./article_list.md', 'w', encoding='UTF-8')
    for item in index:
        title = item[0]
        id = item[1]
        if title != '':
            line = "- [%s](https://zenn.dev/hyperdb/articles/%s)" % (title, id)
            f.write(line + "\n")
    f.close()


if __name__ == "__main__":
    main()
