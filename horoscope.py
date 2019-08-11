import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []
    i = 0
    while i < total_num:
        j = 0
        forecast = ""
        while j < num_sentences:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = t.title() + " " + a + " " + p + "."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1

        prophecies.append(forecast)
        i = i + 1

    return prophecies
a = generate_prophecies()
# def generate_body(header, paragraphs):
#     body = "<h1>" + header + "</h1>"
#     for p in paragraphs:
#         body +="<p>"+p+"</p>"
#     return "<body>" + body + "</body>"
# def generate_page(head,body):
#     page = "<html>" + head + body + "</html>"
#     return page
# def generate_head(title):
#     head = "<meta charset="'utf-8'">" + "<title>" + title + "</title>"
#     return head




# fp = open("index.html", 'w')
# print(generate_page(generate_head('Horoscope'),generate_body(header="Гороскоп на сегодня",paragraphs=a)), file=fp)
# fp.close()
