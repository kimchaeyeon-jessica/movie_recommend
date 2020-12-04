import pandas as pd #✨중요 pandas 다운로드 받아야함 ✨중요

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

    print(title)

    for i in range(len(genres)):
        genres[i] = modify_data(genres[i])
        keywords[i] = modify_data(keywords[i])
    
    #write your code here... ok ok~
    favorite_movies = []
    for i in range(2): #나중에 입력 개수 바꾸기!
        favorite_movies.append(input("좋아하는 영화를 입력하세요:"))
    gen_dict, kw_dict, len_dict = create_BOW(favorite_movies, title.tolist(), [genres.tolist(),keywords.tolist(),ori_lan.tolist()])
    
    print(gen_dict, kw_dict, len_dict) #확인용
    
def modify_data(list_df):
    list_df = list_df.split(",")
    new_df = []
    for i in range(len(list_df)):
        if i%2 == 1:
            list_df[i] = list_df[i].lstrip(' "name": "').rstrip('"}]')
            new_df.append(list_df[i])
    return new_df

def create_BOW(movies, title, features):
    gen_dict, kw_dict, len_dict = {}, {}, {}
    
    for m in movies:
        mindex = title.index(m)
        genre = features[0][mindex]
        #keyword, len 정의
        
        for gen in genre:
            if gen not in gen_dict:
                gen_dict[gen] = 1
            else :
                gen_dict[gen] += 1
        #위의 gen_dict처럼 kw_dict생성
        """if leng not in len_dict:
            len_dict[leng] = 1
        else :
            len_dict[leng] += 1"""
        
    return gen_dict, kw_dict, len_dict

if __name__ == "__main__":
    main()
