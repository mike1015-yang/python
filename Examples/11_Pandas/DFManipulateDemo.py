import pandas as pd


def create():
    print("--create()----------------")
    # 建立一個有欄位名的DataFrame
    df = pd.DataFrame(columns=['name', 'age'])
    print("依序新增John, Mary二列資料")
    df.loc[0] = ['John', 30]
    df.loc[1] = ['Mary', 25]
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("新增city欄位")
    df['city'] = ['Taipei', 'Taichung']
    print(f"df:\n{df}")
    print("-----------------------------------")


def read():
    print("--read()----------------")
    df = pd.DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"df:\n{df}")
    print("-----------------------------------")
    # 取欄位名=name該欄資料
    print(f"df['name']:\n{df['name']}")
    print("-----------------------------------")
    # 取欄位名=name, age資料
    print(f"df[['name', 'age']]:\n{df[['name', 'age']]}")
    print("-----------------------------------")
    # 取列index=0該列資料
    print(f"df.loc[0]:\n{df.loc[0]}")
    print("-----------------------------------")
    # 取列index=0, 1資料
    print(f"df.loc[[0, 1]]:\n{df.loc[[0, 1]]}")
    print("-----------------------------------")
    # 取列index=0以及欄位名=name的資料
    print(f"df.at[0, 'name']: {df.at[0, 'name']}")
    print("-----------------------------------")
    # 取age>=30資料
    print(f"df[df['age'] >= 30]:\n{df[df['age'] >= 30]}")
    print("-----------------------------------")
    # 只讀前2筆
    print(f"df.head(2):\n{df.head(2)}")
    print("-----------------------------------")
    # 只讀後2筆
    print(f"df.tail(2):\n{df.tail(2)}")
    print("-----------------------------------")
    print("走訪DataFrame")
    for column, values in df.items():
        print(f"{column}:", end=" ")
        for value in values:
            print(value, end=" ")
        print()
    print("-----------------------------------")


def update():
    print("--update()----------------")
    df = pd.DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("John年齡改成33")
    df.loc[0, 'age'] = 33
    print(f"df:\n{df}")
    print("-----------------------------------")
    print("Ken居住城市改成Hualien")
    # 依照條件修改
    condition = df['name'] == 'Ken'
    df.loc[condition, 'city'] = 'Hualien'
    # 依照指定位置修改
    # df.loc[2, 'city'] = 'Hualien'
    print(f"df:\n{df}")
    print("-----------------------------------")


def delete():
    print("--delete()----------------")
    df = pd.DataFrame({
        'name': ['John', 'Mary', 'Ken'],
        'age': [30, 25, 35],
        'city': ['Taipei', 'Taichung', 'Kaohsiung']
    })
    print(f"df:\n{df}")
    print("-----------------------------------")
    print(f"df.drop(1):\n{df.drop(1)}\n")
    print(f"df.drop([0, 2]):\n{df.drop([0, 2])}\n")
    print(f"df.drop([0, 2, 1]:\n{df.drop([0, 2, 1])}\n")
    print("-----------------------------------")
    print("刪除city欄位資料")
    print(f"df.drop('city', axis=1):\n{df.drop('city', axis=1)}")
    print("-----------------------------------")
    print("移除所有資料(只剩欄位名稱)")
    print(f"df.drop(df.index):\n{df.drop(df.index)}")
    print("-----------------------------------")
    print("移除所有資料")
    print("df.drop(df.index, inplace=True)")
    df.drop(df.index, inplace=True)
    print("移除所有欄位名稱")
    print("df.drop(columns=df.columns, inplace=True)")
    df.drop(columns=df.columns, inplace=True)
    print(f"df:\n{df}")
    print("-----------------------------------")

def main():
    create()
    read()
    update()
    delete()


main()
