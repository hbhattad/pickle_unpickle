import pickle

def pickle_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f"Data has been pickled and saved to {filename}")

if __name__ == "__main__":
    filename = 'data.pkl'
    sample_data = {
        'name': input("Enter your name: "),
        'age': int(input("Enter your age: ")),
        'city': input("Enter your city: "),
        'is_student': input("Are you a student? (yes/no): ").lower() == 'yes'
    }
    pickle_data(sample_data, filename)
