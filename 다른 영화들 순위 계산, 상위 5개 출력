import re
import os
import math
import pandas as pd #✨중요 pandas 다운로드 받아야함 ✨중요

def main():

    data = pd.read_csv("tmdb_5000_movies.csv", encoding = "CP949")
    #data 갯수 4799개
    print(data)


    data = data.sort_values(["popularity"], ascending=[False])
    print(data)


    
    genres = data.pop("genres") #장르(여러개로 되어있음)
    keywords = data.pop("keywords") #키워드(여러개로 되어있음)
    ori_lan = data.pop("original_language") #언어
    popularity = data.pop("popularity") #인기도
    title = data.pop("title") #제목
    vote_aver = data.pop("vote_average") #평균 평점
    vote_count = data.pop("vote_count") #평점 개수

    print(title)

    # id, name 구조형으로 되어 있는 형태에서 Value만 뽑아서 문자열로 만듬...
    for i in range(len(genres)):
        genres[i] = modify_data(genres[i])
        keywords[i] = modify_data(keywords[i])
    
    favorite_movies = []
    for i in range(3): #나중에 입력 개수 바꾸기!
        favorite_movies.append(input("재미있게 보았던 영화를 입력하세요:"))
    fgen_dict, fkw_dict, flan_dict = create_BOW(favorite_movies, title.tolist(), [genres.tolist(),keywords.tolist(),ori_lan.tolist()])


    boring_movies = []
    for i in range(3): #나중에 입력 개수 바꾸기!
        boring_movies.append(input("지루했던 영화를 입력하세요:"))
    bgen_dict, bkw_dict, blan_dict = create_BOW(boring_movies, title.tolist(), [genres.tolist(),keywords.tolist(),ori_lan.tolist()])

    print(fgen_dict, fkw_dict, flan_dict) #확인용
    print(bgen_dict, bkw_dict, blan_dict) #확인용


    # key = 영화제목, value = 스코어 (장르추천점수 - 장르비추천점수 + 키워드추천점수 - 키워드비추천점수)
    recommend_dict = {}

    for i in range(len(genres)):

        # 장르 점수 비교
        alpha = 0.1
        prob1 = 0.5
        prob2 = 0.5
        genres_prob_pair = naive_bayes(fgen_dict, bgen_dict, genres[i], alpha, prob1, prob2)

        # 키워드 점수 비교
        alpha = 0.1
        prob1 = 0.5
        prob2 = 0.5
        keyword_prob_pair = naive_bayes(fkw_dict, bkw_dict, keywords[i], alpha, prob1, prob2)

        recommend_dict[title[i]] = genres_prob_pair[0] - genres_prob_pair[1] + keyword_prob_pair[0] - keyword_prob_pair[1]

        if(i % 500 == 0):
            print(i)


    print("")
    print("")
    print("추천 영화를 알려드릴께요.... 영화제목(점수)")
    print("")
    
    i = 0
    for title,score in sorted(recommend_dict.items(), key =lambda recommend_dict:-recommend_dict[1]):

        if title in favorite_movies:
            i += 0
        else:
            i += 1
            print ("Top Rank ", i, "= [", title,"] (",score*50, "점)")
            
        if(i >= 20):
            break;


def naive_bayes(t1_dict, t2_dict, test_dict, alpha, prob1, prob2):
    t1_text = make_dictionary_to_text(t1_dict)
    t2_text = make_dictionary_to_text(t2_dict)
    test_text = make_list_to_text(test_dict)
    
    # Exercise
    training_model_pos = create_sentence_BOW(t1_text)
    training_model_neg = create_sentence_BOW(t2_text)
    testing_model = create_sentence_BOW(test_text)
    
    classify1 = calculate_doc_prob(training_model_pos, testing_model, alpha)
    classify2 = calculate_doc_prob(training_model_neg, testing_model, alpha)

    return normalize_log_prob(classify1, classify2)

def read_text_data(directory):
    # We already implemented this function for you

    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.txt')]
    all_text = ''
    for f in files:
        all_text += ' '.join(open(directory + f).readlines()) + ' '

    return all_text




def make_dictionary_to_text(dictionary):
    all_text = ''
    for key, value in dictionary.items():
        all_text = all_text + ' ' + key

    return all_text

def make_list_to_text(vlist):
    all_text = ''

    for i in range(len(vlist)):
        all_text = all_text + ' ' + vlist[i]
        
    return all_text


def read_text(directory):
    all_text = ''
    for f in files:
        all_text += ' '.join(open(directory + f).readlines()) + ' '

    return all_text

def normalize_log_prob(prob1, prob2): #계산 간단하게
    maxprob = max(prob1, prob2)

    prob1 -= maxprob
    prob2 -= maxprob
    prob1 = math.exp(prob1)
    prob2 = math.exp(prob2)

    normalize_constant = 1.0 / float(prob1 + prob2)
    prob1 *= normalize_constant
    prob2 *= normalize_constant

    return (prob1, prob2)

def calculate_doc_prob(training_model, testing_model, alpha): #베이즈정리에 의한 계산
    logprob = 0

    num_tokens_training = sum(training_model[1])
    num_words_training = len(training_model[0])

    for word in testing_model[0]:
        word_freq = testing_model[1][testing_model[0][word]]
        word_freq_in_training = 0
        if word in training_model[0]:
            word_freq_in_training = training_model[1][training_model[0][word]]
        for i in range(0, word_freq):
            logprob += math.log(word_freq_in_training + alpha)
            logprob -= math.log(num_tokens_training + num_words_training * alpha)

    return logprob

def create_sentence_BOW(sentence):
    bow_dict = {}
    bow = []

    sentence = sentence.lower()
    sentence = replace_non_alphabetic_chars_to_space(sentence)
    words = sentence.split(' ')
    for token in words:
        if len(token) < 1: continue
        if token not in bow_dict:
            new_idx = len(bow)
            bow.append(0)
            bow_dict[token] = new_idx
        bow[bow_dict[token]] += 1
    
    return bow_dict, bow


def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

    
def modify_data(list_df):
    list_df = list_df.split(",")
    new_df = []
    for i in range(len(list_df)):
        if i%2 == 1:
            list_df[i] = list_df[i].lstrip(' "name": "').rstrip('"}]')
            new_df.append(list_df[i])
    return new_df

def create_BOW(movies, title, features):
    gen_dict, kw_dict, lan_dict = {}, {}, {}
    
    for m in movies:
        mindex = title.index(m)
        genre = features[0][mindex]
        keyword = features[1][mindex]
        lan = features[2][mindex]

        for gen in genre:
            if gen not in gen_dict:
                gen_dict[gen] = 1
            else :
                gen_dict[gen] += 1
                
        for kw in keyword:
            if kw not in kw_dict:
                kw_dict[kw] = 1
            else :
                kw_dict[kw] += 1 
                
        for lang in lan:
            if lang not in lan_dict:
                lan_dict[lang] = 1
            else :
                lan_dict[lang] += 1
            
        
    return gen_dict, kw_dict, lan_dict

if __name__ == "__main__":
    main()
