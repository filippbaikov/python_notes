import json
import datetime

def create():
    title=input("введи название заметки: ")
    text=input("введи описание заметки: ")
    note={"id": str(datetime.datetime.now().timestamp), "title": title, "text": text, "dateCreate": str(datetime.datetime.now()),
          "dateMod": str(datetime.datetime.now())}
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("n")
        
def read():
    with open("notes.json", "r") as file:
        for line in file:
            note =json.loads(line)
            print (f"id: {note['id']}")
            print (f"название: {note['title']}")
            print (f"текст: {note['text']}")
            print (f"дата создания: {note['dateCreate']}")
            print (f"дата изменения: {note['dateMod']}")
            
def update():
    noteId= input("введи id заметки, которую хочешь помменять: ")
    with open("notes.json", "r+") as file:
        for line in file:
            note=json.loads(line)
            if noteId ==note["id"]:
                print (f"название: {note['title']}")
                print (f"текст: {note['text']}")
                choice=input("изменить заголовок нажми (1), изменить текст нажми (2)")
                if choice=="1" :
                    newTitle=input("введи новое название: ")
                    note["title"]=newTitle
                    note["dateMod"]= str(datetime.datetime.now())
                elif choice=="2":
                    newText=input("введи новый текст: ")
                    note["text"]=newText
                    note["dateMod"]= str(datetime.datetime.now())
                    
                file.seek(0)
                file.truncate()
                json.dump(note, file)
                file.write("n")
                break                  

def delete():
    noteId= input("введи id заметки, которую хочешь удалить: ")
    with open("notes.json", "r+") as file:
        lines=file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            note= json.loads(line)
            if noteId!=note["id"]:
                file.write(line)
                
def run():
    print("создать (1), смотреть(2), изменить(3), удалить(4)")
    choice=input("выбери действие: ")
    if choice=="1": create()
    elif choice=="2": read()
    elif choice=="3" : update()
    elif choice=="4" :delete()           
    else: SystemExit("неверное действие")            

run()