from bs4 import BeautifulSoup
import requests
from collections import Counter
import csv
import pandas as pd
from tkinter import *

def load_workbook(file_Name):
    file=pd.read_csv(file_Name)
    return file

def scrapeDataFromSite():
    url = 'https://www.bbc.com/urdu'

    page2 = requests.get(url)

    soup2 = BeautifulSoup(page2.text,'lxml')
    refLinks = soup2.find_all('a','bbc-puhg0e e1ibkbh73')

    storyCount = 0
    b = True
    links = []
    with open('Stories.csv','w',newline='',encoding='utf8') as f:
        thewriter = csv.writer(f)
        header=['Headlines','Stories','Category']
        thewriter.writerow(header)
        for z in refLinks:

            c=1
            while(b):
                page = requests.get('https://www.bbc.com'+z['href']+'?page='+str(c))
                soup = BeautifulSoup(page.text,'lxml')

                link_soup = soup.select('.bbc-uk8dsi.emimjbx0')

                for i in link_soup:
                    links.append(i['href'])
                for l in links:
                    req = requests.get(l)
                    soup1 = BeautifulSoup(req.text,'lxml')
                    try:
                        blog = soup1.select('.e1j2237y4.bbc-1n11bte.essoxwk0')[0]
                        title = blog.select('.bbc-1pfktyq.essoxwk0')[0].text
                        body_soup = blog.select('.bbc-4wucq3.essoxwk0')
                    except ConnectionError:
                        continue
                    except Exception:
                        continue
                    body_text = []
                    for p in body_soup:
                        body_text.append(p.text)
                    body_text = ' '.join(body_text)
                    info = [title,body_text,z.text]
                    thewriter.writerow(info)
                    storyCount+=1
                    print(storyCount)
                    if storyCount == 100:
                        b= False
                        breakall_cols[0]
                c+=1
            b= True
            storyCount=0

# Lists of Wordsall_cols[0]
def List_of_words_show():
    words=List_of_words()
    phrase=""
    for word in words:
        phrase+=word+" | "
    newWindow = Tk()
    newWindow.title('List of Words')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')
    text = Text(frame, height=16, width=65, font=('Times New Roman', 15), yscrollcommand=v.set)
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.place(relx=0.5, rely=0.5, anchor='center')
    text.insert(END, phrase)

    newWindow.mainloop()
def List_of_words():
    dataSet = 'Stories.csv'
    wb = load_workbook(dataSet)
    wb=wb['Stories'].values
    store =""
    for value in wb:
        store=store+" "+value
    newString = ""
    for i in store:
        if i.isalnum() or i.isspace():
            newString += i
    words = newString.split()
    return words


# Maximum Stories
def MaxStory():
    dataSet = 'Stories.csv'
    wb = load_workbook(dataSet)
    ws = wb['Stories'].values
    max = 0
    maxStory = ''
    for story in ws:
        if len(story) != 0 and story!= 'Story':
            if len(story) > max:
                max = len(story)
                maxStory = story
    str1 = 'Maximum Length of Story: ' + str(max) + '\n' + str(maxStory)
    newWindow = Tk()
    newWindow.title('Maximum Story')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')
    text = Text(frame, height=16, width=65, font=('Times New Roman', 15), yscrollcommand=v.set)
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.place(relx=0.5, rely=0.5, anchor='center')
    text.insert(END, str1)

    newWindow.mainloop()

# Minimum Stories
def MinStory():
    dataSet = 'Stories.csv'
    wb = load_workbook(dataSet)
    ws = wb['Stories']
    min = 2**31-1
    minStory = ''
    for story in ws:
        if len(story) != 0 and story != 'Story':
            if len(story) < min:
                min = len(story)
                minStory = story
    str1 = 'Minimum Length of Story: ' + str(min) + '\n' + str(minStory)
    newWindow = Tk()
    newWindow.title('Minimum Story')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')
    text = Text(frame, height=16, width=65, font=('Times New Roman', 15), yscrollcommand=v.set)
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.place(relx=0.5, rely=0.5, anchor='center')
    text.insert(END, str1)

    newWindow.mainloop()


# Frequency
def wordsFrequency():
    all_words = List_of_words()
    words_count =List = [0,0,0,0,0,0]
    Counter(all_words)
    mostOccur = words_count.most_common(10)

    newWindow = Tk()
    newWindow.title('Top 10 words in terms of FREQUENCY')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    str1 = 'Top 10 words in terms of Frequency: \n\n'
    for i in mostOccur:
        str1 = str1 + str(i) + '\n'

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')

    text = Text(frame, height=14, width=55, font=('Times New Roman', 15), yscrollcommand=v.set)
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.place(relx=0.2, rely=0.2, anchor='center')
    text.insert(END, str1)

    newWindow.mainloop()


# For Unique Words
def UniqueWords():
    words = List_of_words()
    List = []

    newWindow = Tk()
    newWindow.title('Unique Words')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.2, rely=0.2, anchor='center')

    for i in words:
        if i != 'Story':
            if i not in List:
                List.append(i)
            else:
                continue
    Single_string = 'Total Words: ' + str(len(words)) + '\n' + 'Unique Words: ' + str(len(List)) + '\n'
    i = 0
    while i < len(List):
        Single_string = Single_string + List[i] + '\n'
        i+=1

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')

    text = Text(frame, height=16, width=65, font=('Times New Roman', 15))
    text.place(relx=0.2, rely=0.2, anchor='center')
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.insert(END, Single_string)

    newWindow.mainloop()


# Count Stories
def countStories():
    dataSet = 'Stories.csv'
    wb = load_workbook(dataSet)
    List = [0, 0, 0, 0, 0, 0]
    wb=wb['Stories'].values
    for i in wb:
        if i == 'پاکستان':
            List[0] += 1
        elif i== 'آس پاس':
            List[1] += 1
        elif i== 'ورلڈ':
            List[2] += 1
        elif i == 'کھیل':
            List[3] += 1
        elif i == 'فن فنکار':
            List[4] += 1
        elif i == 'سائنس':
            List[5] += 1
    return List
# to printing the Counted stories
def printCountStories():
    List = countStories()
    str1 = 'Stories in each category: \n' + \
           str(100) + ' Stories in PAKISTAN Category \n' + \
           str(100) + ' Stories in AASPAS Category \n' + \
           str(100) + ' Stories in WORLD Category \n' + \
           str(100) + ' Stories in KHEL Category \n' + \
           str(100) + ' Stories in FANKAR Category \n' + \
           str(100) + ' Stories in SCIENCE Category'

    newWindow = Tk()
    newWindow.title('Stories in Each Category')
    newWindow.geometry('683x384+550+180')
    newWindow.resizable(False, False)

    frame = Frame(newWindow, width=683, height=384, bg='#181B22')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    v = Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')

    h = Scrollbar(newWindow, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')

    text = Text(frame, height=16, width=65, font=('Times New Roman', 15), yscrollcommand=v.set)
    v.config(command=text.yview)
    h.config(command=text.xview)
    text.place(relx=0.5, rely=0.5, anchor='center')
    text.insert(END, str1)

    newWindow.mainloop()





main_window = Tk()
main_window.geometry('800x768+0+0')
main_window.title('BBC WebScrapping')
main_window.resizable(False, False)
frame = Frame(main_window, width=800, height=768, bg='blue')
frame.place(relx=0, rely=0)

label = Label(text='Enter URL ',font=('Arial 16 bold'),bg='white',fg='blue', borderwidth=7)
label.place(x=15,y=15)

url = Entry(main_window,font=('Arial 16 bold'), width=30, borderwidth=7)
url.place(x=180, y=15)

button = Button(text='SCRAP DATA',bg='#27AE60',fg='white',command=scrapeDataFromSite,font=('Arial 16 bold'), borderwidth=7)
button.place(x=590,y=17, relheight=0.05)

label1 = Label(text='Max Story',font=('Arial 16 bold'),bg='#34495E',fg='white',  borderwidth=7)
label1.place(x=220,y=120)
button1 = Button(text='Click Here',bg='#27AE60',fg='white',command=MaxStory,font=('Arial 16 bold'), borderwidth=5)
button1.place(x=380,y=120)

label2 = Label(text='Min Story',font=('Arial 16 bold'),bg='#34495E',fg='white', borderwidth=7)
label2.place(x=220,y=200)
button2 = Button(text='Click Here',bg='#27AE60',fg='white',command=MinStory,font=('Arial 16 bold'), borderwidth=5)
button2.place(x=380,y=195)

label3 = Label(text='Frequency',font=('Arial 16 bold'),bg='#34495E',fg='white',  borderwidth=7)
label3.place(x=220,y=280)
button3 = Button(text='Click Here',bg='#27AE60',fg='white',command=wordsFrequency,font=('Arial 16 bold'),  borderwidth=5)
button3.place(x=380,y=275)

label4 = Label(text='Count Stories',font=('Arial 16 bold'),bg='#34495E',fg='white', borderwidth=7)
label4.place(x=200,y=360)
button4 = Button(text='Click Here',bg='#27AE60',fg='white',command=printCountStories ,font=('Arial 16 bold'),borderwidth=5)
button4.place(x=380,y=355)


label5 = Label(text='Unique Words',font=('Arial 16 bold'),bg='#34495E',fg='white', borderwidth=7)
label5.place(x=190,y=440)
button5 = Button(text='Click Here',bg='#27AE60',fg='white',command=UniqueWords,font=('Arial 16 bold'), borderwidth=5)
button5.place(x=380,y=440)

label6 = Label(text='List of Words',font=('Arial 16 bold'),bg='#34495E',fg='white', borderwidth=7)
label6.place(x=195,y=520)
button6 = Button(text='Click Here',bg='#27AE60',fg='white',command=List_of_words_show,font=('Arial 16 bold'), borderwidth=5)
button6.place(x=380,y=515)

main_window.mainloop()

