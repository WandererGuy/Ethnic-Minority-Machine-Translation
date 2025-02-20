def read_first_1000_lines(file_path):
    """
    Reads the first 1000 lines from the file at file_path.
    
    Parameters:
        file_path (str): The path to the file.
        
    Returns:
        list: A list containing up to 1000 lines from the file.
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= 1000:
                    break
                lines.append(line)
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

# Example usage:
if __name__ == "__main__":
    input_file = 'data/src-test-token.txt'
    first_1000_lines = read_first_1000_lines(input_file)
    print(f"Read {len(first_1000_lines)} lines from {input_file}")
    output_file = "data/fake-src-test-token.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(first_1000_lines)

    input_file = 'data/tgt-test-token.txt'
    first_1000_lines = read_first_1000_lines(input_file)
    print(f"Read {len(first_1000_lines)} lines from {input_file}")
    output_file = "data/fake-tgt-test-token.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(first_1000_lines)