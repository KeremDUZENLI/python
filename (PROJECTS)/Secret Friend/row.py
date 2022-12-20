import random
import smtplib
import ssl


####################     ALGORITHM     ####################
file1 = open('names_email.txt', 'r')
Lines = file1.readlines()

count = 0

liste1 = []
liste2 = []

for line in Lines:
    count += 1
    liste1.append(line.strip())
    liste2.append(line.strip())


limit = len(liste1) - 1


while len(liste1) > 1:
    randomNumber1 = random.randint(0, limit)
    randomNumber2 = random.randint(0, limit)

    while True:
        if randomNumber1 == randomNumber2:
            randomNumber2 = random.randint(0, limit)
        else:
            break

    print(
        f"Sender: {liste1[randomNumber1]} >> Receiver: {liste2[randomNumber2]}"
    )

    liste1.remove(liste1[randomNumber1])

    liste2.remove(liste2[randomNumber2])

    limit -= 1


print(
    f"Sender: {liste1[0]} >> Receiver: {liste2[0]}"
)


####################     E-MAIL     ####################

# port, smtp_server = Hangi mail sunucusu kullanılıyorsa (gmail, hotmail, yandex) bu değer google da bulunup değştirilecek
port = 587
smtp_server = "smtp.gmail.com"

# sender_email = göndericinin mail adresi
# receiver_email = alıcılar virgül işareti ile ayrılacak şekilde çoğaltılıp listeye eklenebilir
# password = göndericinin mail şifresi, bu kısım kod çalıştırılınca çıkan input ekranında girilecek
sender_email = "anafen6041@gmail.com"
receiver_email = "ghdznl09@gmail.com"
password = input("Type your password and press enter:")

# message = Subject kısmında konu yazılacak, this message ..... bölümü silinip yazılacaklar eklenecek
message = """\
Subject: Hi there

This message is sent from Python."""

# bu kısım mail foksiyonların çalıştırıldığı kısım
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
