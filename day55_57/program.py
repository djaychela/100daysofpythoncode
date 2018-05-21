import datetime

import blog_client


def main():
    val = 'RUN'

    while val:
        print('What would you like to do?')
        val = input('[w]rite a post or [r]ead them?')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_post()


def read_post():
    svc = blog_client.BlogClient()
    response = svc.all_entries()

    posts = response.json()
    for idx, p in enumerate(posts,1):
        print(f"{idx} : {p['view_count']} - {p['title']}")

    print()
    selected = int(input('Which post to view?'))
    selected_id = posts[selected - 1].get('id')
    print(selected_id)

    response = svc.entry_by_id(selected_id)

    selected_post = response.json()
    print(f"Details for selected post:{selected_post.get('id')}")
    print(f"Title: {selected_post.get('title')}")
    print(f"Written: {selected_post.get('published')}")
    print(f"Content: {selected_post.get('content')}")
    print()


    print()



def write_post():
    svc = blog_client.BlogClient()

    title = input('Title: ')
    content = input('Content: ')
    view_count = int(input('view_count (int): '))
    published = datetime.datetime.now().isoformat()

    resp = svc.create_new_entry(title=title, content=content, views=view_count, published=published)

    print()
    print(f"Created new entry successfully: {resp.json().get('id')}")
    print()



if __name__ == '__main__':
    main()