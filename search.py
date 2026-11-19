def search_by_title(books, query):
    return [b for b in books if query.lower() in b.title.lower()]

def search_by_author(books, query):
    return [b for b in books if query.lower() in b.author.lower()]
