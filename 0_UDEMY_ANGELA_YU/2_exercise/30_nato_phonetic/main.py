import pandas

phonetic_data = pandas.read_csv(r"0_UDEMY_ANGELA_YU/2_exercise/30_nato_phonetic/phonetic.csv")

data_dict = {row.letter:row.code for (index,row) in phonetic_data.iterrows()}

def generate_phonetic():
    user_input = input("Type your word: ").strip().upper()
    try:
        phonetic_lists = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry! Only letters in the alphabets please")
        generate_phonetic()
    else:
        print(phonetic_lists)
        
generate_phonetic()





        