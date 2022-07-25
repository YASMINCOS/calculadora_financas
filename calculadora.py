from tkinter import*
from tkinter import Tk, ttk
from PIL import Image,ImageTk


cor0="#2e2d2b"
cor1="#feffff"
cor2="#4fa882"
cor3="#38576b"
cor4="#403d3d"
cor5="#e06636"
cor6="#038cfc"
cor7="#efbfb9"
cor8="#263238"
cor9="#e9edf5"

janela=Tk()
janela.title("")
janela.geometry("500x350")
janela.configure(background=cor9)
janela.resizable(width=False,height=False)



frame_cima=Frame(janela,width=1043,height=60,pady=5,bg=cor1)
frame_cima.grid(row=0,column=0)

frame_baixo=Frame(janela,width=1043,height=400,pady=0,bg=cor1)
frame_baixo.grid(row=1,column=0)

#configurando framecima


app_logo_img=Image.open('salario.png')
app_logo_img=app_logo_img.resize((25,25))
app_logo_img=ImageTk.PhotoImage(app_logo_img)
app_logo=Label(frame_cima,image=app_logo_img,width=500,text='Calculadora de Salário',compound=LEFT,relief=RAISED,anchor=NW,font=('Verdana 15'),bg=cor1,fg=cor4)
app_logo.place(x=0,y=0)




#funcoes

def calcular():
    anos=365

    semanas=52

    nome=e_nome.get()

    #total de horas trabalhadas por dia

    T_H_de_Tr_por_dias=int(e_horas_trabalhadas.get())
    T__dias_Tr_por_semana=int(e_dias_semana.get())
    Salario_anual=float(e_salario.get())

    #horas de trabalho anual
    T_H_Semanalmente_por_ano=T_H_de_Tr_por_dias*T__dias_Tr_por_semana
    T_H_Tr_por_ano=semanas*T_H_Semanalmente_por_ano

    #salario por horas
    Salario_por_horas=Salario_anual/T_H_Tr_por_ano

    #salario diario
    Salario_diario=Salario_por_horas*T_H_de_Tr_por_dias

    #salario semanal
    Salario_semanal= Salario_anual/semanas

    #salario mensal

    Salario_mensal=Salario_anual/12

    #salario anual
    Salario_bruto_anual=Salario_mensal*12
    
    l_mostrar_nome=Label(frame_baixo,text=''+str(nome),width=25,pady=5,padx=5,relief=RAISED,font=('Ivy 10'),anchor=NW,bg=cor9,fg=cor0)
    l_mostrar_nome.place(x=10,y=150)
    l_mostrar_dias=Label(frame_baixo,text='Horas de trabalho por dia: ' + str(T_H_de_Tr_por_dias),width=25,pady=5,padx=5,relief=RAISED,font=('Ivy 10'),anchor=NW,bg=cor9,fg=cor0)
    l_mostrar_dias.place(x=10,y=180)
    l_mostrar_horas=Label(frame_baixo,text='Dias trabalhados por semana: '+str(T__dias_Tr_por_semana),width=25,pady=5,padx=5,relief=RAISED,font=('Ivy 10'),anchor=NW,bg=cor9,fg=cor0)
    l_mostrar_horas.place(x=10,y=210)
    l_mostrar_salario_anual=Label(frame_baixo,text='R$ {:,.2f}'.format(Salario_anual),width=25,pady=5,padx=5,relief=RAISED,font=('Ivy 10 bold'),anchor=NW,bg=cor9,fg=cor0)
    l_mostrar_salario_anual.place(x=10,y=240)



   
   
   
    
    
    app_r_hora['text']=' Salario por horas: R$ {:,.2f}'.format(Salario_por_horas)
    app_r_diario['text']='Salario por dia: R$ {:,.2f}'.format(Salario_diario)
    app_r_semanal['text']='Salario por semana: R$ {:,.2f}'.format(Salario_semanal)
    app_r_mensal['text']='Salario por mes: R$ {:,.2f}'.format(Salario_mensal)
    app_r_anual['text']=' Salario anual: R$ {:,.2f}'.format(Salario_anual)

    







#configurando frame baixo

l_nome=Label(frame_baixo,text='Digite seu nomme completo:',font=('Ivy 10'),anchor=NW,bg=cor1,fg=cor4)
l_nome.place(x=10,y=10)
e_nome=Entry(frame_baixo,width=25, justify='left',relief='solid')
e_nome.place(x=200,y=11)

l_horas_trabalhadas=Label(frame_baixo,text='Quantas horas você trabalha por dia:',font=('Ivy 10'),anchor=NW,bg=cor1,fg=cor4)
l_horas_trabalhadas.place(x=10,y=40)
e_horas_trabalhadas=Entry(frame_baixo,width=15, justify='left',relief='solid')
e_horas_trabalhadas.place(x=260,y=41)

l_dias_trabalhados_semana=Label(frame_baixo,text='Quantos dias você trabalha por semana:',font=('Ivy 10'),anchor=NW,bg=cor1,fg=cor4)
l_dias_trabalhados_semana.place(x=10,y=70)
e_dias_semana=Entry(frame_baixo,width=15, justify='left',relief='solid')
e_dias_semana.place(x=260,y=71)

l_salario=Label(frame_baixo,text='Digite seu salario anual:',font=('Ivy 10'),anchor=NW,bg=cor1,fg=cor4)
l_salario.place(x=10,y=100)
e_salario=Entry(frame_baixo,width=15, justify='left',relief='solid')
e_salario.place(x=260,y=101)


app_logo_imagem=Image.open('salario.png')
app_logo_imagem=app_logo_imagem.resize((90,90))
app_logo_imagem=ImageTk.PhotoImage(app_logo_imagem)
app_logo_=Label(frame_baixo,image=app_logo_imagem,bg=cor1,fg=cor4)
app_logo_.place(x=380,y=0)


app_img=Image.open('salario.png')
app_img=app_img.resize((20,20))
app_img=ImageTk.PhotoImage(app_img)
b_calcular=Button(frame_baixo,command=calcular,image=app_img,width=100,text=' CALCULAR',compound=LEFT,relief=RAISED,overrelief=RIDGE,anchor=NW,font=('Ivy 8 bold'),bg=cor1,fg=cor4)
b_calcular.place(x=370,y=92)

app_img_horas=Image.open('imgs/1.png')
app_img_horas=app_img_horas.resize((20,20))
app_img_horas=ImageTk.PhotoImage(app_img_horas)
app_r_hora=Label(frame_baixo,image=app_img_horas,width=300,compound=LEFT,anchor=NW,font=('Ivy 10'),bg=cor1,fg=cor0)
app_r_hora.place(x=253,y=140)

app_img_diario=Image.open('imgs/2.png')
app_img_diario=app_img_diario.resize((20,20))
app_img_diario=ImageTk.PhotoImage(app_img_diario)
app_r_diario=Label(frame_baixo,image=app_img_diario,width=300,compound=LEFT,anchor=NW,font=('Ivy 10'),bg=cor1,fg=cor0)
app_r_diario.place(x=253,y=165)

app_img_semanal=Image.open('imgs/3.png')
app_img_semanal=app_img_semanal.resize((20,20))
app_img_semanal=ImageTk.PhotoImage(app_img_semanal)
app_r_semanal=Label(frame_baixo,image=app_img_semanal,width=300,compound=LEFT,anchor=NW,font=('Ivy 10'),bg=cor1,fg=cor0)
app_r_semanal.place(x=253,y=190)

app_img_horas_mensal=Image.open('imgs/4.png')
app_img_horas_mensal=app_img_horas_mensal.resize((20,20))
app_img_horas_mensal=ImageTk.PhotoImage(app_img_horas_mensal)
app_r_mensal=Label(frame_baixo,image=app_img_horas_mensal,width=300,compound=LEFT,anchor=NW,font=('Ivy 10'),bg=cor1,fg=cor0)
app_r_mensal.place(x=253,y=215)

app_img_anual=Image.open('imgs/6.png')
app_img_anual=app_img_anual.resize((20,20))
app_img_anual=ImageTk.PhotoImage(app_img_anual)
app_r_anual=Label(frame_baixo,image=app_img_anual,width=300,compound=LEFT,anchor=NW,font=('Ivy 10'),bg=cor1,fg=cor0)
app_r_anual.place(x=253,y=240)







janela.mainloop()