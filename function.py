# 消費税の計算関数
# 金額は整数
# 税率は少数　10% -> 0.1
def add_tax(price, tax_rate):
    return int(price + price * tax_rate)

# このファイルを実行すると動く。インポートされたときは動かない。
if __name__ == "__main__":
    # TEST
    # print(add_tax(1000, 0.1))   # 一般
    # print(add_tax(1000, 0.08))  # 軽減税率
    # assertは正しいときは何も言わず、間違ってるときは教えてくれる
    assert add_tax(1000, 0.1) == 1100
    assert add_tax(1000, 0.08) == 1080