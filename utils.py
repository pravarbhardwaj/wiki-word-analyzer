import requests
from bs4 import BeautifulSoup 

def get_words_count(word, number):
    word = word.lower()
    word_to_search = word.replace(" ", "_").capitalize()
    URL = f"https://en.wikipedia.org/wiki/{word_to_search}" 
    r = requests.get(URL) 
    
    #Used beautifulsoup to webscrape wikipedia
    soup = BeautifulSoup(r.content, 'html5lib') 

    div_tag = soup.find('div', attrs = {'class':'mw-content-ltr mw-parser-output'})  
    
    try:
        paragraphs = [p_tag.get_text() for p_tag in div_tag.find_all("p")]
    except:
        paragraphs = None
    
    if not paragraphs:
        return {"error": "Please input valid subject"}
    result = dict()
    
    for para in paragraphs:

        #All the replace below are used to remove garbage from string
        para = para.replace('"', "")
        para = para.replace('\n', " ")
        para = para.replace('  ', " ")
        para = para.replace('[', ' [')
        arr = para.split(" ")
        
        for w in arr:
            if result.get(w):
                result[w] += 1
            else:
                result[w] = 1
        
        #This creates the dictionary with all the words and their count in descending count value
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
        count = 1
        return_dic = dict()
        
        for i in result:
            
            if i == "":
                continue

            if i.startswith("[") and i.endswith("]"):
                skip = True
                
                for l in range(1, 1, len(i)-1):
                    if not i[l].isnumeric():
                        skip = False
                if skip:
                    continue

            return_dic[i] = result[i]
            
            if count == number:
                break
            count+=1
    return return_dic

