import pickle

def unpickle_data(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    print(f"Data has been unpickled from {filename}:")
    print(data)
    return data

if __name__ == "__main__":
    filename = 'data.pkl'
    data = unpickle_data(filename)
