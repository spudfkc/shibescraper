import urllib2

from bs4 import BeautifulSoup as bs
from random import shuffle

def scrape_site(url):
    result = []
    soup = bs(urllib2.urlopen(url).read())
    for img in soup.find_all('img'):
        if img.has_attr('alt'):
            src = img.get('src')
            link = ''.join(['http:', src[:src.rindex('.')-1],
                    src[src.rindex('.'):]])
            title = img.get('title')
            if title is None:
                title = ''
            else:
                title = title[:title.index('<p>')]
            result.append((title, link))
    return result

def write_html(filename, links):
    towrite = ''
    for (title, link) in links:
        s = u'<br> <p>{}</p><img src="{}" style="max-width: 100%;"></img><br>'.format(title, link)
        towrite = ''.join([towrite, s])
    with open(filename, 'w') as f:
        f.write(towrite.encode('utf8'))

def main():

    sites = [
        'http://imgur.com/r/shibe',
        'http://imgur.com/r/supershibe',
        'http://imgur.com/r/dogecoin',
        'http://imgur.com/r/doge',
        'http://imgur.com/r/shiba'
#    'http://shibe-doge.tumblr.com'
    ]

    filename = 'link2.html'
    r = []
    for site in sites:
        r = r + scrape_site(site)
        shuffle(r)
        write_html(filename, r)

if __name__ == '__main__':
    main()
