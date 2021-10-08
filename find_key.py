
import re
import statistics
from statistics import mode
from typing import Counter

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY_DICT = {'A': None,'B': None,'C': None,'D': None,'E': None,'F': None,'G': None,'H': None,'I': None,'J': None,'K': None,'L': None,'M': None,'N': None,'O': None,'P': None,'Q': None,'R': None,'S': None,'T': None,'U': None,'V': None,'W': None,'X': None,'Y': None,'Z': None}


def set_the_and(freq_words):
    KEY_DICT[freq_words[2][0][0].upper()] = 'T'
    KEY_DICT[freq_words[2][0][1].upper()] = 'H'
    KEY_DICT[freq_words[2][0][2].upper()] = 'E'
    KEY_DICT[freq_words[2][1][0].upper()] = 'A'
    KEY_DICT[freq_words[2][1][1].upper()] = 'N'
    KEY_DICT[freq_words[2][1][2].upper()] = 'D'
    
def set_i(freq_words):
    if KEY_DICT[freq_words[0][0].upper()] != None:
        KEY_DICT[freq_words[0][1].upper()] = 'I'
    else:
        KEY_DICT[freq_words[0][0].upper()] = 'I'

def set_w(words_by_len):

    four_letter_ith_words = []
    freq_four_letter_ith_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('T')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('H')].lower()
    for w in words_by_len[3]:
        if str in w:
            four_letter_ith_words.append(w)

    cnt = Counter()
    for x in four_letter_ith_words:
        cnt[x] += 1

    freq_four_letter_ith_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_four_letter_ith_words[0][0][0][0].upper()] = 'W'

def set_o_f(freq_words):
    if KEY_DICT[freq_words[1][0][0].upper()] != None:
        KEY_DICT[freq_words[1][1][0].upper()] = 'O'
        KEY_DICT[freq_words[1][1][1].upper()] = 'F'
    else:
        KEY_DICT[freq_words[1][0][0].upper()] = 'O'
        KEY_DICT[freq_words[1][0][1].upper()] = 'F'

def set_k(words_by_len):

    four_letter_now_words = []
    freq_four_letter_now_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('N')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('W')].lower()
    for w in words_by_len[3]:
        if str in w:
            four_letter_now_words.append(w)

    cnt = Counter()
    for x in four_letter_now_words:
        cnt[x] += 1

    freq_four_letter_now_words.append([cnt.most_common(1)[0]])

def set_r(words_by_len):
    three_letter_fo_words = []
    freq_three_letter_fo_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('F')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower()
    for w in words_by_len[2]:
        if str in w:
            three_letter_fo_words.append(w)

    cnt = Counter()
    for x in three_letter_fo_words:
        cnt[x] += 1

    freq_three_letter_fo_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_three_letter_fo_words[0][0][0][2].upper()] = 'R'

def set_m(words_by_len):
    four_letter_fro_words = []
    freq_four_letter_fro_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('F')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('R')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower()
    for w in words_by_len[3]:
        if str in w:
            four_letter_fro_words.append(w)

    cnt = Counter()
    for x in four_letter_fro_words:
        cnt[x] += 1

    freq_four_letter_fro_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_four_letter_fro_words[0][0][0][3].upper()] = 'M'

def set_b(words_by_len):
    two_letter_e_words = []
    freq_two_letter_e_words = []
    for w in words_by_len[1]:
        if list(KEY_DICT.keys())[list(KEY_DICT.values()).index('E')].lower() in w:
            two_letter_e_words.append(w)

    cnt = Counter()
    for x in two_letter_e_words:
        cnt[x] += 1

    freq_two_letter_e_words.append([cnt.most_common(4)[0], cnt.most_common(4)[1], cnt.most_common(4)[2], cnt.most_common(4)[3]])

    if KEY_DICT[freq_two_letter_e_words[0][0][0][0].upper()] == None:
        KEY_DICT[freq_two_letter_e_words[0][0][0][0].upper()] = 'B'

    elif KEY_DICT[freq_two_letter_e_words[0][1][0][0].upper()] == None:
        KEY_DICT[freq_two_letter_e_words[0][1][0][0].upper()] = 'B'

    elif KEY_DICT[freq_two_letter_e_words[0][2][0][0].upper()] == None:
        KEY_DICT[freq_two_letter_e_words[0][2][0][0].upper()] = 'B'

    else:
        KEY_DICT[freq_two_letter_e_words[0][3][0][0].upper()] = 'B'

def set_s(words_by_len):
    two_letter_i_words = []
    freq_two_letter_i_words = []
    for w in words_by_len[1]:
        if list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')].lower() in w:
            two_letter_i_words.append(w)

    cnt = Counter()
    for x in two_letter_i_words:
        cnt[x] += 1

    freq_two_letter_i_words.append([cnt.most_common(4)[0], cnt.most_common(4)[1], cnt.most_common(4)[2], cnt.most_common(4)[3]])

    if KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] = 'S'

    elif KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] = 'S'

    elif KEY_DICT[freq_two_letter_i_words[0][2][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][2][0][1].upper()] = 'S'

    else:
        KEY_DICT[freq_two_letter_i_words[0][3][0][1].upper()] = 'S'


def get_digraphs(m):

    digraph_list = []

    for i in range(0, len(m) - 1):
        if m[i].upper() in LETTERS and m[i + 1].upper() in LETTERS:
            digraph_list.append(m[i] + m[i + 1])

    return digraph_list

def get_key(key_dict):
    l = key_dict.values()
    key_str = ''
    for x in l:
        if x != None:
            key_str += x
        else:
            key_str += '@'
    print(key_str)

def read_input_files():

    f_name = ''
    input_messages = []

    for i in range(1, 8):

        f_name = 'encr_output' + str(i) + '.txt'

        f = open(f_name, 'r')
        encr_text = f.read()

        input_messages.append(encr_text.lower())

    return input_messages

def get_letter_freq(message):

    freq_dict = {'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}

    for x in message:
        if x.upper() in LETTERS:
            freq_dict[x.upper()] += 1

    return freq_dict


#Input: List of messages
#Output: List of lists where each list contains all the words that have 1, 2, 3, 4 letters respectively 

def get_all_words(message):
    
    raw_words = message.split()
    stripped_words = []
    word_list_by_len = []


    for w in raw_words:
        stripped_words.append(re.sub(r'\W+', '', w))

    one_l_words = []
    two_l_words = []
    three_l_words = []
    four_l_words = []
    
    
    for w in stripped_words:

        word_len = len(w)

        if word_len == 1:
            one_l_words.append(w)
        elif word_len == 2:
            two_l_words.append(w)
        elif word_len == 3:
            three_l_words.append(w)
        elif word_len == 4:
            four_l_words.append(w)

    word_list_by_len.append(one_l_words)
    word_list_by_len.append(two_l_words)
    word_list_by_len.append(three_l_words)
    word_list_by_len.append(four_l_words)

    return word_list_by_len

def print_file_data(freq_words, file_num):

    print(f'Input {file_num} | MC1: {freq_words[0]} | MC2: {freq_words[1]} | MC3: {freq_words[2]} | MC4: {freq_words[3]} | ')

def reset_key_dict():
    keys = KEY_DICT.keys()
    for k in keys:
        KEY_DICT[k] = None

#Input: List of messages
#Ouput: Prints the name of each input file as well as the top 3 most common words of length 1, 2, 3, 4

def get_key(messages):

    file_num = 0

    for m in messages:

        reset_key_dict()

        freq_words = []
        words_by_len = get_all_words(m)
        freq_dict = get_letter_freq(m)
        
        for l in words_by_len:
            cnt = Counter()
            for w in l:
                cnt[w] += 1

            freq_words.append([cnt.most_common(4)[0][0], cnt.most_common(4)[1][0], cnt.most_common(4)[2][0], cnt.most_common(4)[3][0]])

        print_file_data(freq_words, file_num)

        if file_num == 0:
            file_num += 1
            continue

        set_the_and(freq_words)
        set_i(freq_words)
        set_w(words_by_len)
        set_o_f(freq_words)
        set_k(words_by_len)
        set_r(words_by_len)
        set_m(words_by_len)
        set_b(words_by_len)
        set_s(words_by_len)

        file_num += 1

        continue

        KEY_DICT[freq_four_letter_now_words[0][0][0][0].upper()] = 'K'

        two_letter_e_words = []
        freq_two_letter_e_words = []
        for w in words_by_len[1]:
            if list(KEY_DICT.keys())[list(KEY_DICT.values()).index('E')].lower() in w:
                two_letter_e_words.append(w)

        cnt = Counter()
        for x in two_letter_e_words:
            cnt[x] += 1

        freq_two_letter_e_words.append([cnt.most_common(5)[0], cnt.most_common(5)[1], cnt.most_common(5)[2], cnt.most_common(5)[3], cnt.most_common(5)[4]])



       
        #this will work to get 's' and 'm'
        two_letter_i_words = []
        freq_two_letter_i_words = []
        for w in words_by_len[1]:
            if list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')].lower() in w:
                two_letter_i_words.append(w)

        cnt = Counter()
        for x in two_letter_i_words:
            cnt[x] += 1

        freq_two_letter_i_words.append([cnt.most_common(5)[0], cnt.most_common(5)[1], cnt.most_common(5)[2], cnt.most_common(5)[3], cnt.most_common(5)[4]])
        
        continue

        if KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] == None:
            KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] = 'S'

        elif KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] == None:
            KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] = 'S'

        else:
            KEY_DICT[freq_two_letter_i_words[0][2][0][1].upper()] = 'S'
        
        if KEY_DICT[freq_two_letter_i_words[0][3][0][1].upper()] == None:
            KEY_DICT[freq_two_letter_i_words[0][3][0][1].upper()] = 'M'
        else:
            KEY_DICT[freq_two_letter_i_words[0][4][0][1].upper()] = 'M'


        #setting 'of'
        if KEY_DICT[freq_words[1][0][0].upper()] != None:
            KEY_DICT[freq_words[1][1][0].upper()] = 'O'
            KEY_DICT[freq_words[1][1][1].upper()] = 'F'
        else:
            KEY_DICT[freq_words[0][0][0].upper()] = 'O'
            KEY_DICT[freq_words[0][0][1].upper()] = 'F'

        
        

        


        

        #this will attempt to get 'R'
        three_letter_fo_words = []
        freq_three_letter_fo_words = []
        str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('F')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower()
        for w in words_by_len[2]:
            if str in w:
                three_letter_fo_words.append(w)

        cnt = Counter()
        for x in three_letter_fo_words:
            cnt[x] += 1

        freq_three_letter_fo_words.append([cnt.most_common(1)[0]])

        KEY_DICT[freq_three_letter_fo_words[0][0][0][2].upper()] = 'R'

        print(freq_three_letter_fo_words)

        print(get_key_str(KEY_DICT))

        

        

    # we now know 'the' and 'and'
    KEY_DICT[freq_words[2][0][0].upper()] = 'T'
    KEY_DICT[freq_words[2][0][1].upper()] = 'H'
    KEY_DICT[freq_words[2][0][2].upper()] = 'E'
    KEY_DICT[freq_words[2][1][0].upper()] = 'A'
    KEY_DICT[freq_words[2][1][1].upper()] = 'N'
    KEY_DICT[freq_words[2][1][2].upper()] = 'D'

    #setting 'i'
    if KEY_DICT[freq_words[0][0][0].upper()] != None:
        KEY_DICT[freq_words[0][0][1].upper()] = 'I'
    else:
        KEY_DICT[freq_words[0][0][0].upper()] = 'I'

    #setting 'of'
    if KEY_DICT[freq_words[1][0][0].upper()] != None:
        KEY_DICT[freq_words[1][1][0].upper()] = 'O'
        KEY_DICT[freq_words[1][1][1].upper()] = 'F'
    else:
        KEY_DICT[freq_words[0][0][0].upper()] = 'O'
        KEY_DICT[freq_words[0][0][1].upper()] = 'F'

    
    #this will work to get 's' and 'm'
    two_letter_i_words = []
    freq_two_letter_i_words = []
    for w in words_by_len[1]:
        if list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')].lower() in w:
            two_letter_i_words.append(w)

    cnt = Counter()
    for x in two_letter_i_words:
        cnt[x] += 1

    freq_two_letter_i_words.append([cnt.most_common(5)[0], cnt.most_common(5)[1], cnt.most_common(5)[2], cnt.most_common(5)[3], cnt.most_common(5)[4]])
    

    if KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][0][0][1].upper()] = 'S'

    elif KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][1][0][1].upper()] = 'S'

    else:
        KEY_DICT[freq_two_letter_i_words[0][2][0][1].upper()] = 'S'
    
    if KEY_DICT[freq_two_letter_i_words[0][3][0][1].upper()] == None:
        KEY_DICT[freq_two_letter_i_words[0][3][0][1].upper()] = 'M'
    else:
        KEY_DICT[freq_two_letter_i_words[0][4][0][1].upper()] = 'M'

    #this will attempt to get 'w'
    four_letter_ith_words = []
    freq_four_letter_ith_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('T')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('H')].lower()
    for w in words_by_len[3]:
        if str in w:
            four_letter_ith_words.append(w)

    cnt = Counter()
    for x in four_letter_ith_words:
        cnt[x] += 1

    freq_four_letter_ith_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_four_letter_ith_words[0][0][0][0].upper()] = 'W'


    #this will attempt to get 'K'
    four_letter_now_words = []
    freq_four_letter_now_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('N')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('W')].lower()
    for w in words_by_len[3]:
        if str in w:
            four_letter_now_words.append(w)

    cnt = Counter()
    for x in four_letter_now_words:
        cnt[x] += 1

    freq_four_letter_now_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_four_letter_now_words[0][0][0][0].upper()] = 'K'

    #this will attempt to get 'R'
    three_letter_fo_words = []
    freq_three_letter_fo_words = []
    str = list(KEY_DICT.keys())[list(KEY_DICT.values()).index('F')].lower() + list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')].lower()
    for w in words_by_len[2]:
        if str in w:
            three_letter_fo_words.append(w)

    cnt = Counter()
    for x in three_letter_fo_words:
        cnt[x] += 1

    freq_three_letter_fo_words.append([cnt.most_common(1)[0]])

    KEY_DICT[freq_three_letter_fo_words[0][0][0][2].upper()] = 'R'

    print(freq_three_letter_fo_words)

    print(get_key_str(KEY_DICT))

def get_key_str(key_dict):

    #sorted_key_dict = {k: v for k, v in sorted(key_dict.items(), key=lambda item: item[1])}

    l = key_dict.values()

    out_str = ''

    if 'A' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('A')]
    if 'B' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('B')]
    if 'C' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('C')]
    if 'D' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('D')]
    if 'E' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('E')]
    if 'F' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('F')]
    if 'G' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('G')]
    if 'H' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('H')]
    if 'I' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('I')]
    if 'J' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('J')]
    if 'K' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('K')]
    if 'L' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('L')]
    if 'M' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('M')]
    if 'N' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('N')]
    if 'O' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('O')]
    if 'P' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('P')]
    if 'Q' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('Q')]
    if 'R' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('R')]
    if 'S' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('S')]
    if 'T' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('T')]
    if 'U' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('U')]
    if 'V' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('V')]
    if 'W' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('W')]
    if 'X' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('X')]
    if 'Y' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('Y')]
    if 'Z' in l:
        out_str += list(KEY_DICT.keys())[list(KEY_DICT.values()).index('Z')]    

    return out_str

def main():

    messages = read_input_files()

    get_key(messages)

        

#freq_dict = {'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}
if __name__ == "__main__":
    main()