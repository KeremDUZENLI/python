import smtplib
import ssl

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
