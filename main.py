from trimmer_py.trimmer_py import search_max_score_tag 
from urllib import request

# テストコード
# 適当にはてなブログのトップにあった記事を選択.
if __name__ == '__main__':
    url = 'http://teenssexandwarmode.hatenablog.com/entry/2018/10/10/042129'
    with request.urlopen(url) as f:
        html = f.read()
        tag = search_max_score_tag(html)
        print(tag.text)
