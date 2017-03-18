
    import facebook
    import time
    from bs4 import BeautifulSoup
    import schedule
    import os
    from datetime import datetime
    from selenium.webdriver import Firefox
    from selenium import webdriver
    from selenium.webdriver.common.by import By


    import facebook_graph_application


    def getExtendToken(user_token,app_id,app_secret):

        graphMe = facebook.GraphAPI(user_token)
        long_token = graphMe.extend_access_token(app_id, app_secret)
        return long_token['access_token']

    def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""


    def postFB():

        user_token = ''
        app_id = ''
        app_secret = '앱 시크릿키 등록'
        longToken = getExtendToken(user_token,app_id,app_secret)

        graphMe = facebook.GraphAPI(longToken)

        profile = graphMe.get_object("me")
        posts = graphMe.get_connections(profile['id'],'posts')

        graphMe.put_wall_post(message='입력할 문자열', attachment=attachment)
        print "Post Done at "+   str(datetime.now())



    schedule.every().day.at("18:30").do(postFB)      #주기적 으로 올릴때는 일정 설정


    while 1:
        schedule.run_pending()
        time.sleep(1)

    os.system("pause")