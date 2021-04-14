goods = []
features = {'product name': '', 'price': '', 'quantity': '', 'measure': ''}
analytics = {'product name': [], 'price': [], 'quantity': [], 'measure': []}
num = 0
while True:
    if input('To exit programme press "Q", tp continue press "Enter": ').upper() == 'Q':
        break
        num += 1
        features = features.copy()
        for f in features:
            pro = input(f'Enter name of product "{f}": ')
            features[f] = int(pro) if f == 'price' or f == 'quantity' else pro
            analytics[f].append(features[f])
        goods.append((num, features))
        print(f"\nGoods specification\n{goods}")
        print(f'\n Current product analytics: \n {"*" * 30}')
        for key, value in analytics.items():
            print(f'{key:>30}: {value}')
        print("*" * 30)