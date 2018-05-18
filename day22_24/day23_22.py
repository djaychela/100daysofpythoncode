from functools import wraps


def make_html(parameter):
    def make_html_inner(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start_text = f"<{parameter}>"
            text = function(*args, **kwargs)
            end_text = f"</{parameter}>"
            return start_text + text + end_text
        return wrapper
    return make_html_inner


@make_html('p')
@make_html('strong')
def get_text(text):
    return text


print(get_text('hello'))