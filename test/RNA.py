transcription = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}



def transcribe_rna(dna):
    rna = ''
    if len(dna) != 4:
        return None
    for letter in dna:
        rna += transcription[letter]
    return rna


def validate_dna(dna):
    return set(dna).issubset(set('GCTA'))


def main():
    while True:
        input_data = input('Enter DNA ')
        input_data = input_data.upper()
        if not validate_dna(input_data):
            answer = input('Invalid DNA, please enter DNA again ([y]/[n]')
            if answer.lower() != 'y':
                break
            continue
        rna = transcribe_rna(input_data)
        print(f' Your RNA {rna}')
        return 


if __name__ == '__main__':
    main()

