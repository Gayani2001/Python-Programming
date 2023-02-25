#making sentences
subject_list=['I','We']
verb_list=['play','watch']
sports=input()
sport_list=sports.strip().split(" ")#putting sports into a list
for subject in subject_list:
    for verb in verb_list:
        for sport in sport_list:
            output=subject+" "+verb+" "+sport+'.'#concatanating words
            print(output)
