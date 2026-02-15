import pandas
csv_path = "0_UDEMY_ANGELA_YU/3_projects/26_nato_alphabet_project/nato_phonetic_alphabet.csv"

data = pandas.read_csv(csv_path)

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

print(nato_dict['A'])

user_input = input('Enter a word: ').strip().upper()

output_lists = [nato_dict[letter] for letter in user_input]
""" for i in user_input:
    if i in nato_dict[i]:
        output_lists.append(nato_dict[i]) """

print(output_lists)


