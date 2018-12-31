import urllib.request, json


def main():
    with urllib.request.urlopen("https://demo1684309.mockable.io/names") as url:
        data = json.loads(url.read().decode())
        print(data)
        names_in_alphabetical_order = arrange(data)
        print('---Names is---')
        print(names_in_alphabetical_order)
        n_first_names = n_names(names_in_alphabetical_order, 4)
        print(n_first_names)

def arrange(names):
        arranged_names = []
        for x in names:
                arranged_names.append(x['name'])
        return sorted(arranged_names)

def n_names(names, n):
        return names[0:n]


if __name__ == '__main__':
    main()