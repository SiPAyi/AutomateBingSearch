import webbrowser


f = open('./keywords.txt', 'r')
keywords = f.read()
queries = []
word = "https://www.bing.com/search?q="
for keyword in keywords:
    if(keyword == '\n'):
        queries.append(word)
        word = "https://www.bing.com/search?q="
    else:
        word = word+keyword


for query in queries:
    webbrowser.open_new_tab(query)
    print("opened a tab with query", query, "\n")


f.close()

