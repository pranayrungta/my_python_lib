def main(fileCriteria, nonCriteria):
    import os
    ls = os.listdir('./')
    files = [i for i in ls if( all(x in i for x in fileCriteria) )
                        and not any(x in i for x in nonCriteria)]
    already_exist = []
    for i in files:
        folder_path = i.split('_')[:-1]
        folder_path = '/'.join(folder_path)
        new_path = '/'.join([folder_path, i])

        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        if os.path.isfile(new_path):
            already_exist += [i]
        else: os.rename(i, new_path)

    if(len(already_exist)>0):
        print("Following files already exists :\n")
        for filename in already_exist:
            print(filename)
        input()
