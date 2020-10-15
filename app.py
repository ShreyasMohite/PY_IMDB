

from tkinter import *
import imdb 
import tkinter.messagebox
from tkinter.ttk import Combobox
import threading


class Imdbpro:
    def __init__(self,root):
        self.root=root
        self.root.title("IMDB")
        self.root.geometry("800x600")
        self.root.iconify()
        self.root.iconbitmap("logo602.ico")
        self.root.resizable(0,0)

        actor_name=StringVar()
        movie_name=StringVar()
        actor_code=StringVar()
        movie_code=StringVar()
        actor_category=StringVar()
        movie_category=StringVar()


    #============================================================================#
        def on_enter1(e):
            but_search_actor_name['background']="black"
            but_search_actor_name['foreground']="cyan"
  
        def on_leave1(e):
            but_search_actor_name['background']="SystemButtonFace"
            but_search_actor_name['foreground']="SystemButtonText"

        def on_enter2(e):
            but_search_movie_name['background']="black"
            but_search_movie_name['foreground']="cyan"
  
        def on_leave2(e):
            but_search_movie_name['background']="SystemButtonFace"
            but_search_movie_name['foreground']="SystemButtonText"

        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"
        
        def on_enter4(e):
            but_erase['background']="black"
            but_erase['foreground']="cyan"
  
        def on_leave4(e):
            but_erase['background']="SystemButtonFace"
            but_erase['foreground']="SystemButtonText"

        def on_enter5(e):
            but_search_actor_category['background']="black"
            but_search_actor_category['foreground']="cyan"
  
        def on_leave5(e):
            but_search_actor_category['background']="SystemButtonFace"
            but_search_actor_category['foreground']="SystemButtonText"

        def on_enter6(e):
            but_search_movie_category['background']="black"
            but_search_movie_category['foreground']="cyan"
  
        def on_leave6(e):
            but_search_movie_category['background']="SystemButtonFace"
            but_search_movie_category['foreground']="SystemButtonText"



    #==========================command===================================#

        def search_actor():
            try:

                text.delete("1.0","end")
                ia = imdb.IMDb()
                if actor_name.get()!="":

                    name=actor_name.get()
                    search = ia.search_person(name)
                    with open("C:\\TEMP\\imdb.txt","w") as f: 

                        for i in range(len(search)): 
                            
                            id = search[i].personID 

                            a=search[i]['name'] + " : " + id
                            f.write(a+"\n")
                    with open("C:\\TEMP\\imdb.txt","r") as f:
                        text.insert("end",f.read())
                
                else:
                    tkinter.messagebox.showerror("Error","Please enter Actor name")
 
            except:
                tkinter.messagebox.showerror("Error","No Internet Connection")


        def thread_actor():
            t1=threading.Thread(target=search_actor)
            t1.start()


        def clear():
            actor_name.set("")
            movie_name.set("")
            actor_code.set("")
            movie_code.set("")
            actor_category.set("Select Actor category")
            movie_category.set("Select Movie category")


        def erase():
            text.delete('1.0',"end")

        
        def movie_names():
            try:

                text.delete("1.0","end")
                ia = imdb.IMDb()
                if movie_name.get()!="":

                    name=movie_name.get()

                    search = ia.search_movie(name)

                    with open("C:\\TEMP\\imdb.txt","w") as f: 

                        for i in range(len(search)): 
                            
                            id = search[i].movieID 

                            a=search[i]['title'] + " : " + id
                            f.write(a+"\n")

                    with open("C:\\TEMP\\imdb.txt","r") as f:
                        text.insert("end",f.read())                
                else:
                    tkinter.messagebox.showerror("Error","Please enter Movie name")
 
            except:
                tkinter.messagebox.showerror("Error","No Internet Connection")



        def thread_movie_name():
            t1=threading.Thread(target=movie_names)
            t1.start()

                 

        def actor_categories():
            try:
                ia = imdb.IMDb()
                text.delete("1.0","end")
                with open("C:\\TEMP\\imdb.txt","w") as f:
                    if actor_category.get()=="Biography":
                        code=actor_code.get()
                        person = ia.get_person(code, info =['biography'])
                        person.infoset2keys
                        f.write(str(person['biography']))

                    if actor_category.get()=="Filmography":
                        code=actor_code.get()
                        person = ia.get_person(code, info =['filmography'])
                        person.infoset2keys
                        f.write(str(person['filmography']))

                    if actor_category.get()=="Awards":
                        code=actor_code.get()
                        person = ia.get_person(code, info =['awards'])
                        person.infoset2keys
                        f.write(str(person['awards']))

                    if actor_category.get()=="BirthDate":
                        person_id = actor_code.get()
                        search = ia.get_person(person_id)
                        a=search['name'] + "  " +search['birth date']
                        place = search['birth info']['birth place'] 
                        f.write(str(a)+"\n")
                        f.write(str(place))

                    if actor_category.get()=="OtherWorks":
                        code=actor_name.get()
                        persons = ia.search_person(code) 
                        person = persons[0] 
                        ia.update(person, info = ['other works'])
                        a=person['other works']
                        for x in a:
                            f.write(str(x)+"\n\n")

                    


                with open("C:\\TEMP\\imdb.txt","r") as f:
                        text.insert("end",f.read())
            except Exception as e:
                print(e)

        def thread_actor_categories():
            t=threading.Thread(target=actor_categories)
            t.start()


        def movie_categories():
            try:
                ia = imdb.IMDb()
                text.delete("1.0","end")
                with open("C:\\TEMP\\imdb.txt","w") as f: 
                    name=movie_name.get()
                    movies=ia.search_movie(name)
                    movie=movies[0]
                    ia.update(movie, info = [movie_category.get()]) 
                    a=movie[movie_category.get()]
                    f.write(str(a))

                    if movie_category.get()=="Information":
                        name=movie_name.get()
                        movies = ia.search_movie(name)  
                        movie = movies[0]
                        ia.update(movie, info = ['plot']) 
                        a=movie['plot']
                        f.write(str(a))


                       

                    if movie_category.get()=="Taglines":
                        name=movie_name.get()
                        movies = ia.search_movie(name)  
                        movie = movies[0]
                        ia.update(movie, info = ['taglines']) 
                        a=movie['taglines']
                        f.write(str(a))
                        

                    if movie_category.get()=="Title":
                        name=movie_name.get()
                        movies = ia.search_movie(name)  
                        f.write(str(movies)+"\n")
                        for i in range(len(movies)): 
                           a=movies[i]['title']
                           f.write(str(a)+"\n")

                    if movie_category.get()=="Year":
                        name=movie_name.get()
                        search = ia.search_movie(name)  
                        year = search[0]['year'] 
                        a=search[0]['title'] + " : " + str(year)
                        f.write(a)

                    if movie_category.get()=="Cast":
                        name=movie_code.get()
                        movie = ia.get_movie(name)  
                        f.write(str(movie)+"\n")
                        decot="===================="
                        f.write(decot+"\n")
                        cast = movie['cast'] 
                        for i in range(0,41):
                            actor = cast[i] 
                            f.write(str(actor)) 
                            role = actor.notes 
                            f.write(str(role)+"\n\n")

                        

                with open("C:\\TEMP\\imdb.txt","r") as f:
                    text.insert("end",f.read())
            except:
                tkinter.messagebox.showerror("Error","Information is not avaiable or Network Error")
                


        def thread_movie_categories():
            t1=threading.Thread(target=movie_categories)
            t1.start()



    #=========================frame======================================#

        mainframe=Frame(self.root,width=800,height=600,bd=4,relief="ridge",bg="#555b6e")
        mainframe.place(x=0,y=0)

        topframe=Frame(mainframe,width=793,height=350,bd=3,relief="ridge",bg="#555b6e")
        topframe.place(x=0,y=0)

        bottomframe=Frame(mainframe,width=793,height=241,bd=3,relief="ridge")
        bottomframe.place(x=0,y=350)

    #===========================topframe=========================================#
        
        lab_frame=LabelFrame(topframe,width=786,height=343,text="IMDB SEARCHES",bg="#555b6e",fg="white")
        lab_frame.place(x=0,y=0)

    #============================================================================#
       
        lab_actor=Label(lab_frame,text="Search Actor Name :",font=('times new roman',12,'bold'),bg="#555b6e",fg="white")
        lab_actor.place(x=20,y=20)

        lab_movie=Label(lab_frame,text="Search Movie Name :",font=('times new roman',12,'bold'),bg="#555b6e",fg="white")
        lab_movie.place(x=20,y=80)

        lab_movie=Label(lab_frame,text="Enter Actor Code :",font=('times new roman',12,'bold'),bg="#555b6e",fg="white")
        lab_movie.place(x=20,y=140)

        lab_movie=Label(lab_frame,text="Enter Movie Code :",font=('times new roman',12,'bold'),bg="#555b6e",fg="white")
        lab_movie.place(x=20,y=200)

    #=============================================================================#

        ent_actor_name=Entry(lab_frame,width=25,font=('times new roman',12,'bold'),bd=3,relief="ridge",textvariable=actor_name)
        ent_actor_name.place(x=200,y=20)
        

        ent_actor_name=Entry(lab_frame,width=25,font=('times new roman',12,'bold'),bd=4,relief="ridge",textvariable=movie_name)
        ent_actor_name.place(x=200,y=80)


        ent_actor_code=Entry(lab_frame,width=25,font=('times new roman',12,'bold'),bd=4,relief="ridge",textvariable=actor_code)
        ent_actor_code.place(x=200,y=140)

        ent_movie_code=Entry(lab_frame,width=25,font=('times new roman',12,'bold'),bd=4,relief="ridge",textvariable=movie_code)
        ent_movie_code.place(x=200,y=200)
         
        
        actor_list=["Biography","Filmography","Awards","OtherWorks","BirthDate"]
        actor_list_combo=Combobox(lab_frame,values=actor_list,font=('arial',10),width=19,state="readonly",textvariable=actor_category)
        actor_list_combo.set("Select Actor category")
        actor_list_combo.place(x=450,y=140)

        movie_list=["Information","Taglines","Title","Year","Cast","airing","akas","alternate versions","awards","connections",\
            "crazy credits","critic reviews","episodes","external reviews","external sites","faqs","full credits","goofs","keywords",\
            "locations","main","misc sites","news","official sites","parents guide","photo sites","plot","quotes","release dates",\
            "release info","reviews","sound clips","soundtrack","synopsis","taglines","technical","trivia","tv schedule","video clips","vote details"]
        movie_list_combo=Combobox(lab_frame,values=movie_list,font=('arial',10),width=19,state="readonly",textvariable=movie_category)
        movie_list_combo.set("Select Movie category")
        movie_list_combo.place(x=450,y=200)
        

    #==============================================================================#
       
        but_search_actor_name=Button(lab_frame,text="Search Actor Name",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=thread_actor)
        but_search_actor_name.place(x=450,y=15)
        but_search_actor_name.bind("<Enter>",on_enter1)
        but_search_actor_name.bind("<Leave>",on_leave1)

        but_search_movie_name=Button(lab_frame,text="Search Movie Name",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=thread_movie_name)
        but_search_movie_name.place(x=450,y=75)
        but_search_movie_name.bind("<Enter>",on_enter2)
        but_search_movie_name.bind("<Leave>",on_leave2)

        but_clear=Button(lab_frame,text="Clear",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=clear)
        but_clear.place(x=620,y=15)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)

        but_erase=Button(lab_frame,text="Erase",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=erase)
        but_erase.place(x=620,y=75)
        but_erase.bind("<Enter>",on_enter4)
        but_erase.bind("<Leave>",on_leave4)

        but_search_actor_category=Button(lab_frame,text="Search A Catagory",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=thread_actor_categories)
        but_search_actor_category.place(x=620,y=130)
        but_search_actor_category.bind("<Enter>",on_enter5)
        but_search_actor_category.bind("<Leave>",on_leave5)

        but_search_movie_category=Button(lab_frame,text="Search M Catagory",width=16,font=('times new roman',12,'bold'),bd=4,cursor="hand2",command=thread_movie_categories)
        but_search_movie_category.place(x=620,y=190)
        but_search_movie_category.bind("<Enter>",on_enter6)
        but_search_movie_category.bind("<Leave>",on_leave6)

        

    #=========================TEXT=======================================#
        
        scol=Scrollbar(bottomframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(bottomframe,height=12,width=95,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)

    #=====================================================================#

        






if __name__ == "__main__":
    root=Tk()
    app=Imdbpro(root)
    root.mainloop()
