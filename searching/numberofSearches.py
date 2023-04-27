import webbrowser

n = int(input("how many tabs: "))

for i in range(n):
    webbrowser.open_new_tab("https://www.bing.com/search?q=query")