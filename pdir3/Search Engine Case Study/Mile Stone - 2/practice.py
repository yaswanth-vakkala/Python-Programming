mytitles = []
def create_index(filenames, index, file_titles):
    new_filenames = []
    for j in filenames:
        if j not in new_filenames:
            new_filenames.append(j)
    for i in new_filenames:
        f = open(i,'r')
        for line in f:
            for word in line.split():
                new_word = ''.join(char for char in word if char.isalnum())
                if new_word.lower() in index.keys():
                    lst = index[new_word.lower()]
                    lst.append(i)
                else:
                    index[new_word.lower()] = [i]
        f.seek(0)
        file_titles[i] = f.readline().strip()
        f.close()
    print(index)
    print(file_titles)
    global mytitles
    mytitles = file_titles
index = {}
file_titles = {}
create_index(['test1.txt','test2.txt','test2.txt'],index,file_titles)


def search(index, query):
    f_list = index.keys()
    q_list = query.split()
    new_list = []
    for i in f_list:
        for j in q_list:
            if i == j and i not in new_list:
                new_list.append(i)
    flst = []
    if len(new_list) < len(q_list):
        return []
        quit()
    if len(new_list) == 1:
        for k in new_list:
            flst.append(index[k])
        if flst != []:
            return flst[-1]
        else:
            return flst
    else:
        print(new_list)
        val = []
        for i in new_list:
            val.append(index.get(i))
        # print(val)
        comm = []
        # print(mytitles)
        for n in mytitles:
            comm.append(n)
        fcomm = []
        count = 0
        for i in comm:
            for j in val:
                if i in j:
                    count += 1
            if count == len(val):
                fcomm.append(i)
                count = 0
            else:
                count = 0
        return fcomm
        # for b in file_titles.keys():
        #     for j in val:
        #         for k in j:
        #             if k == b:
        #                 comm.append(k)
        # for b in file_titles.keys():
        #     for j in new_list:
        #         if b in index[j]
        # print(comm)


print(search(index,"apple carrot"))