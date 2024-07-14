import pickle_data
import unpickle_data

def main():
    filename = 'data.pkl'
    
    # Get user input for data
    sample_data = {
        'name': input("Enter your name: "),
        'age': int(input("Enter your age: ")),
        'city': input("Enter your city: "),
        'is_student': input("Are you a student? (yes/no): ").lower() == 'yes'
    }
    
    # Pickle the data
    pickle_data.pickle_data(sample_data, filename)
    
    # Unpickle the data
    data = unpickle_data.unpickle_data(filename)
    print("Unpickled data:")
    print(data)

if __name__ == "__main__":
    main()
