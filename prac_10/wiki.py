import wikipedia

def main():
    title_information = input("Enter page title: ").strip()
    while title_information.strip() != "":
        try:
            page = wikipedia.page(title_information)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title_information}" does not match any pages. Try another id!\n')
        title_information = input("Enter page title: ").strip()
    print("Thank you")

main()
