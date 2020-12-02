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

    for i in range(len(genres)):
        genres[i] = modify_data(genres[i])
        keywords[i] = modify_data(keywords[i])

    #write your code here...
    
def modify_data(list_df):
    list_df = list_df.split(",")
    new_df = []
    for i in range(len(list_df)):
        if i%2 == 1:
            list_df[i] = list_df[i].lstrip(' "name": "').rstrip('"}]')
            new_df.append(list_df[i])
    return new_df
    
if __name__ == "__main__":
    main()
