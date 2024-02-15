import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.gofundme.com/f/the-adeline-movement').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

value = soup.find('div', class_ = "hrt-disp-inline")

donation_value = [x.text.strip() for x in value]
print(donation_value)


from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", plswork = donation_value)