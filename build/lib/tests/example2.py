import os

def example2():
    current_path = os.getcwd()
    return current_path

if __name__ == '__main__':
    print(f'Current Directory: {example2()}')