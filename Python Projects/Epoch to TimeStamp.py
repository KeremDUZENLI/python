def corrigedata(contactStartedDate, contactFinishedDate):
    import time
    d1 = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(contactStartedDate)))
    d2 = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(contactFinishedDate)))
    return d1, d2


corrigedata(1347517370, 1347517375)
