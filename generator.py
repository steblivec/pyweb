# coding: utf-8
from sys import getdefaultencoding
getdefaultencoding()

from horoscope import generate_prophecies
from datetime import datetime as dt
def generate_page(head, body):
    page = f"<html>{head}{body}</html>"
    return page
def generate_head(title):
    head = f"""<head>
            <meta charset='utf-8'>
        <title>{title}</title>
        </head>
        """
    return head
def generate_body(header, paragraphs):
    body = f"<h2>{header}</h2>"
    for p in paragraphs:
        body = body + f"<li><p>{p}</p></li>"
    return f"<body><ul>{body}</ul></body>"
def save_page(title, header, paragraphs, output="index.html"):
    today = dt.now().date()
    page = generate_page(
          head=generate_head(title),
          body=generate_body(header=header, paragraphs=paragraphs)
    )
    with open(output, 'w', encoding='utf-8') as f:
        f.write(page)

#####################

today = dt.now().date()
save_page(
title="Гороскоп на сегодня",
header="Что день " + str(today) + " готовит",
paragraphs=generate_prophecies(),
)






















# from horoscope import generate_prophecies
# from datetime import datetime as dt
#
#
# a = generate_prophecies()
# def generate_head(title):
#     head = "<meta charset='utf-8'>" + "<title>" + title + "</title>"
#     return head
# def generate_body(header, paragraphs):
#     body = "<h2>" + header + "</h2>"
#     for p in paragraphs:
#         body +="<p>"+p+"</p>"
#     return "<body>" + body + "</body>"
# def generate_page(head,body):
#     page = "<html>" + head + body + "</html>"
#     return page
#
# def save_page(title, header, paragraphs, output="index.html"):
#     fp = open(output, "w")
#     page = generate_page(
#         head=generate_head(title),
#         body=generate_body(header=header, paragraphs=paragraphs)
#     )
#     print(page.encode('utf-8').decode('utf-8'), file=fp)
#     fp.close()
# today = dt.now().date()
# a = save_page(
#     title = 'Horoscope',
#     header = 'Что день'+ str(today) + "готовит...",
#     paragraphs= a)