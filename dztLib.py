# -*- coding: utf-8 -*-


def download_file(driver):
    cookies = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookies)

    import urllib2
    headers = {'cookie':cookiestr}
    req = urllib2.Request(file_url, headers = headers)
    try:
        response = urllib2.urlopen(req)
        text = response.read()
        fd = open('test.csv', 'w')
        fd.write(text)
        fd.close()
        print '###get home page html success!!'
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

