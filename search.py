import walmart_class
import pickle

with open('allProducts.pkl', 'rb') as handle:
    data = pickle.load(handle)

search = input('Search: ')


def search(searchString):
    results = []
    terms = [searchString.capitalize(),searchString.lower(),searchString.upper(),searchString.title(),searchString.strip()]
    for search in terms:
        for product in data:
            if search in data[product].getName():
                results.append(product)
            elif search in data[product].getUrl():
                results.append(product)
            elif search in data[product].getID():
                results.append(product)

    results = list(set(results))
    return results

print(search(search))
