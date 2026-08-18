def add(a, b):
    return a + b

if __name__ == '__main__':
    n = int(input('Enter N: '))
    numbers = [float(input(f'Enter number {i+1}: ')) for i in range(n)]
    print('The sum is:', sum(numbers))
