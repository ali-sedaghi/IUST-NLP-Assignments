import re


def is_accepted(string, pattern):
    result = re.match(pattern, string)
    if result:
        return True
    return False


if __name__ == '__main__':
    pattern = '^Dr. |^Doctor |.* M\.D\.$'
    samples = open('Q1-input.txt').read().split('\n')
    for sample in samples:
        print(f"{sample}: {is_accepted(sample, pattern)}")
