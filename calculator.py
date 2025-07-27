import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter_pattern = ',|\n'
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter = re.escape(parts[0][2:])
        delimiter_pattern = f'{delimiter}|\n'
        numbers = parts[1]

    number_list = re.split(delimiter_pattern, numbers)
    negatives = [num for num in number_list if num and int(num) < 0]
    if negatives:
        raise Exception(f"negative numbers not allowed {','.join(negatives)}")
    return sum(int(num) for num in number_list if num)
