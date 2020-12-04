import pandas as pd #✨중요 pandas 다운로드 받아야함 ✨중요
import re

def main():

    data = pd.read_csv("tmdb_5000_movies.csv", encoding = "CP949")
    #data 갯수 4799개
    
    genres = data.pop("genres") #장르(여러개로 되어있음)
    keywords = data.pop("keywords") #키워드(여러개로 되어있음)
    ori_lan = data.pop("original_language") #언어
    popularity = data.pop("popularity") #인기도
    title = data.pop("title") #제목
    vote_aver = data.pop("vote_average") #평균 평점
    vote_count = data #평점 갯수

    for i in range(len(genres)):
        genres[i] = modify_data(genres[i])
        keywords[i] = modify_data(keywords[i])

    #write your code here... ok ok~
    favorite_movies = input()
    BOW_dict, BOW = create_BOW(favorite_movies)

    print(BOW_dict) #확인용
    print(BOW) #확인용
    
def modify_data(list_df):
    list_df = list_df.split(",")
    new_df = []
    for i in range(len(list_df)):
        if i%2 == 1:
            list_df[i] = list_df[i].lstrip(' "name": "').rstrip('"}]')
            new_df.append(list_df[i])
    return new_df

def create_BOW(favorite_movies):
    favorite_movies = favorite_movies.lower() #입력받은 문장 모두 소문자로 변환
    favorite_movies = replace_non_alphabetic_chars_to_space(favorite_movies) #정규식으로 변환
    word_list = favorite_movies.split() #space 기준으로 자름
    #단어 리스트 안에 단어들의 길이를 검사해 1 이상이 안되면 삭제
    for word in word_list:
        if len(word) < 1:
            word_list.remove(word)
    #해당 단어의 중복을 체크해가며 bow_dict 라는 사전에 단어를 추가
    bow_dict = {}  # 빈 사전
    #sentence를 bow_dict 에 있는 index 의 값들로 채움

    i = 0
    for word in word_list:
        if word not in bow_dict:
            bow_dict[word] = i
            i = i + 1

    bow = [0 for i in range(len(bow_dict))]

    for word in word_list:
        bow[bow_dict[word]] += 1

    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(favorite_movies):
    return re.sub(r'[^a-z]+', ' ', favorite_movies)
    
if __name__ == "__main__":
    main()
