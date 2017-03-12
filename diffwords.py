def main():
    commandline_args = get_commandline_args()
    file1_path = commandline_args.file1
    file2_path = commandline_args.file2

    file1 = open_file1(file1_path)
    file2 = open_file2(file2_path)

    file1_lines = read_lines(file1)
    file2_lines = read_lines(file2)

    line_pairs = zip(file1_lines, file2_lines)

    for line_no, (f1_line, f2_line) in enumerate(line_pairs):
        f1_words = f1_line.split()
        f2_words = f2_line.split()
        word_pairs = zip(f1_words, f2_words)
        for word_no, (f1w, f2w) in enumerate(word_pairs):
            if f1w != f2w:
                print(line_no, word_no, f1w, f2w)

    file1.close()
    file2.close()


def get_commandline_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", type=str)
    parser.add_argument("file2", type=str)
    return parser.parse_args()


def open_file1(file1_path):
    import sys
    if file1_path == '-':
        file1 = sys.stdin
    else:
        file1 = open(file1_path)
    return file1


def open_file2(file2_path):
    import sys
    if file2_path is None or file2_path == '-':
        file2 = sys.stdin
    else:
        file2 = open(file2_path)
    return file2


def read_lines(a_file):
    for line in a_file:
        yield line


if __name__ == '__main__':
    main()
