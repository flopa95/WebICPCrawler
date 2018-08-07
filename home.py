from flask import Flask, render_template, url_for, request
from bs4 import BeautifulSoup
import re
import requests

#------------------------------------------------------------------------------------#
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def return_result():

    testurl = request.form['testurl']
    testurl_list = testurl.split(',')
    print (testurl_list)
    results_list = {}

    for i in range(len(testurl_list)):
        
        a = str(testurl_list[i])

        try:
            page = requests.get(testurl_list[i])
            soup = BeautifulSoup(page.content,"html.parser")
            
            if (bool(soup.find_all(text=re.compile("ICP"))) == True):
                results_list[a]="Y"
            else:
                results_list[a]="N"
       
        except:
            results_list[a]="Invalid"

    print (results_list)
    return render_template("results2.html", results=results_list)
    
'''
    if (bool(soup.find_all(text=re.compile("ICP"))) == True):
        return render_template("results.html", website=testurl, test_result="a")
    else:
        return render_template("results.html", website=testurl, test_result="no")
'''


if __name__ == "__main__":
    app.run()   