from Par_code import get_info

for i in range(1, 7):
    url = "https://scrapingclub.com/exercise/list_basic/?page=" + str(i)

    get_info(url)
