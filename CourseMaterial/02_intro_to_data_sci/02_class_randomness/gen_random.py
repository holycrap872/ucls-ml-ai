def generate_sequence(seed, length):
    """
    Generates a sequence using the formula: f(n) = (f(n-1) * 3) % 7
    
    Args:
        seed (int): Starting number
        length (int): How many numbers to generate
    
    Returns:
        list: The generated sequence
    """
    sequence = [seed]
    for _ in range(length - 1):
        next_num = (sequence[-1] * 3) % 7
        sequence.append(next_num)
    return sequence


print(generate_sequence(9, 10))
