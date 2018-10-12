from bs4 import BeautifulSoup, Comment
import math


def filter_n_upper(soup, n=200):
    """html tagだけ取得."""
    filtered_tags = []
    for idx, child in enumerate(soup.recursiveChildGenerator()):
        # Tag　objectの確認
        # 確認するには`name`があるか確認すればよい
        name = getattr(child, 'name', None)

        if name is not None:  # タグじゃない
            if len(list(child.descendants)) < n: continue
            filtered_tags.append(child)
    
    return filtered_tags


def count_depth(tag, count=0):
    """タグの深さを取得."""
    if tag.parent is not None:
        count += 1
        return count_depth(tag.parent, count)
    
    return count


def calc_score(child):
    """スコアを計算する."""
    depth_count = count_depth(child)
    text_lenght = len(child.get_text())
    child_count = len(list(child.descendants))
    
    return round(text_lenght * math.sqrt(text_lenght) * depth_count / math.sqrt(2 * child_count))


def preprocessing(soup):
    """前処理."""
    # コメントタグの除去
    for comment in soup(text=lambda x: isinstance(x, Comment)):
        comment.extract()

    # scriptタグの除去
    for script in soup.find_all('script', src=False):
        script.decompose()


    # styleタグの除去
    for style in soup.find_all('style', src=False):
        style.decompose()

    return soup


def search_max_score_tag(html):
    soup = BeautifulSoup(html, 'lxml')
    soup2 = preprocessing(soup)
    filtered_tags = filter_n_upper(soup2)

    max_score = 0
    max_score_child = None
    for child in filtered_tags:
        score = calc_score(child)
        if (max_score < score):
            max_score = score
            max_score_child = child
    
    return max_score_child
