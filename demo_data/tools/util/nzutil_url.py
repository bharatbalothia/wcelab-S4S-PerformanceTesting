import requests, urllib.parse


def join_url_fragements(*url_fragemets: [str]) -> str:

  url_to_return = None

  for frg in url_fragemets:

    if url_to_return is None:
      url_to_return = frg
    else:
      if not url_to_return.endswith('/'):
        url_to_return = url_to_return + '/'
      
      url_to_return = urllib.parse.urljoin(url_to_return, urllib.parse.quote(frg.encode('utf-8')))
  
  return url_to_return


# print(join_url_fragements('https://www.ibm.com', 'commerce', 'goood stuff', '^*^$%&**&^F'))
