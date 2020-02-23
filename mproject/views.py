from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .form import signupform,contactForm
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from PIL import Image
from scipy import misc
import imageio
import img2pdf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img 




# Create your views here.

def home(request):
    title = 'welcome'

    #if request.user.is_authenticated:
        #title="The user is  %s " %(request.user)
    #if request.method == "POST":
        #print  request.POST   
    form = signupform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance) 
    context = { 
        "template_title":title,"form":form 
    }
    return render(request,"index.html",context)

def contact_form(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        for key,value in form.cleaned_data.items():
            print(key,value)

       
        #form_mail = form.cleaned_data.get('email')
        #form_message = form.cleaned_data.get('telephone')
        #form_fullname = form.cleaned_data.get('fullname')

        #subject = 'mail from django'

        #from_email = settings.EMAIL_HOST_USER
        #to_email = [form_mail,'khalid.rami.1996@gmail.com']
        #contact_message =" %s : %s via %s " %(
        #form_fullname,
        #form_message,
        #form_mail)
        #some_html_message = """ <h1>  Hello</h1>   """
        #send_mail(subject,contact_message,from_email,to_email,fail_silently=False)

    context = { "form":form
    }    
    return render(request,"contact_form.html",context)

def login(request):
    return render(request,"login.html")

def registerform(request):
    return render(request,"registerform.html")

def acc(request):
    return render(request,"acc.html")

def upload(request):
    return render(request,"model_form_upload.html")    

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        df = pd.read_excel (myfile,sheet_name=0, index_col=0)
        maxx=df.max(axis=0)
        minn=df.min(axis=0)
        #plt.title("first")
        #plt.scatter(minn,maxx)
        #plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\un.png')
        sorted_by_gross = df.sort_index(axis = 1).head(10).plot(kind="bar")
        plt.title("histchart")
        plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.png')
        im1=Image.open('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.png')
        rgb_im1 = im1.convert('RGB')
        rgb_im1.save('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.jpg')
        sorted_by_gross2 = df.sort_index(axis = 1).head(10).plot(kind="hist")
        plt.title("Barchart")
        plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.png')
        im2=Image.open('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.png')
        rgb_im2 = im2.convert('RGB')
        rgb_im2.save('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.jpg')
        moy=df.mean()
        counts = moy.value_counts()
        counts.plot.pie(autopct='%.2f%%')
        plt.title("Pie Chart")
        plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.png')
        im3=Image.open('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.png')
        rgb_im3 = im3.convert('RGB')
        rgb_im3.save('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.jpg')
        #movies_sheet1 = pd.read_excel(myfile, sheet_name=0, index_col=0)
        sorted_by_grossi = df.sort_index(axis = 1) 
        res=df.head()
        clm=df.columns
        #clm.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\clm.html")
        ind=df.index
        #ind.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\ind.html")
        trans=df.T
        trans.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\trans.html")
        pourc=(df / df.sum())
        pourc.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\pourc.html")
        pourl=(df.T / df.T.sum()).T
        pourl.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\pourl.html")
        varr=df.var(axis=0)
        #varr.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\var.html")
        media=df.median()
        #media.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\mediane.html")
        rang=df.rank() 
        rang.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\rank.html")
        tr=df.sort_index(axis = 0, ascending = False)#trie
        tr.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\trie.html")
        con=pd.concat([pourc,pourl])
        cums=df.apply(np.cumsum)
        cums.to_html("C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\cumsum.html")
        res.to_html('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\head_df.html') #.items()
        res1=df.tail() #.items()
        res1.to_html('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\tail_df.html')
        moviess = pd.DataFrame(df)
        moviess.to_html('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\indexxx.html')
        res2=df.describe()
        res2.to_html('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\templates\\static.html')
        res3=df.plot()
        plt.title("Simple chart")
        plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.png')
        im4=Image.open('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.png')
        rgb_im4 = im4.convert('RGB')
        rgb_im4.save('C:\\Users\\Khalid-Rami\\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.jpg')
        #plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\suine.png')
        #res4= df['CKDTVOL'].value_counts()
        #res6=df['Region'].value_counts()
        #res7=res6.plot.pie(autopct='%.2f%%')
        #res5=res4.plot.pie(autopct='%.2f%%')
        print('****sort with index****')
        print(sorted_by_grossi)
        print(" **** Statics ****   ")
        print(res2) 
        print("**** DATA FRAME **** ")
        print(moviess)
        print("*****Data head*****")
        print(res)
        print("****Data tail*****")
        print(res1)
        print("****columns****")
        print(clm)
        print("****index*****")
        print(ind)
        print("*****transposé****")
        print(trans)
        print("*****pourc****")
        print(pourc)
        print("*****pourcl****")
        print(pourl)
        print("variance")
        print(varr)
        print("le mediane")
        print(media)
        print("trie decroissant")
        print(tr)
        print("le rang de le group")
        print(rang)
        print("***** concateni ******")
        print(con)
        print("*****cumsum*****")
        print(cums)
    return render(request,'acc.html') 
      #print(plt.show())
    #plt.savefig('C:\\Users\\Khalid-Rami\\Desktop\\ilkoe.png')
    #return render(request,'acc.html', {'res1' : res1})
    #return render(request,'acc.html', {'res2' : res2})

def exporthtml(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        movies = pd.read_excel(myfile)
        movies.to_html('C:\\Users\\Khalid-Rami\\Desktop\\dataframe.html')
    return render(request,'acc.html') 

def exportjson(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        movies = pd.read_excel(myfile)
        movies.to_json('C:\\Users\\Khalid-Rami\\Desktop\\dataframe.json')
    return render(request,'acc.html')

def exportpdf(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        movies = pd.read_excel(myfile)
        movies.to_pdf('C:\\Users\\Khalid-Rami\\Desktop\\indexxx.json')
    return render(request,'acc.html')
    
def dataframe(request):
    return render(request,"indexxx.html")

def head(request):
    return render(request,"head_df.html")

def tail(request):
    return render(request,"tail_df.html")

def statics(request):
    return render(request,"static.html")

def dataframecss(request):
    return render(request,"dataframe_css.html")

def graphes(request):
    return render(request,"graphes.html")
    
def images_1(request):
    if request.method == 'POST':
        image11 = Image.open(r'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.jpg')
        im1 = image11.convert('RGB')
        im1.save(r'C:\\Users\\Khalid-Rami\\Desktop\\1.pdf')
        return render(request,"graphes.html")

def images_2(request):
    if request.method == 'POST':
        image22 = Image.open(r'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.jpg')
        im2 = image22.convert('RGB')
        im2.save(r'C:\\Users\\Khalid-Rami\\Desktop\\2.pdf')
        return render(request,"graphes.html")  

def images_3(request):
    if request.method == 'POST':
        image33 = Image.open(r'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.jpg')
        im3 = image33.convert('RGB')
        im3.save(r'C:\\Users\\Khalid-Rami\\Desktop\\3.pdf')
        return render(request,"graphes.html") 

def images_4(request):
    if request.method == 'POST':
        image44 = Image.open(r'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.jpg')
        im4 = image44.convert('RGB')
        im4.save(r'C:\\Users\\Khalid-Rami\\Desktop\\4.pdf')
        return render(request,"graphes.html")   

def images_5(request):
    if request.method == 'POST':
        with open( 'C:\\Users\\Khalid-Rami\\Desktop\\outputtzi.pdf', 'wb' ) as f:
            img = Image.open( 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.jpg' )
            my_layout_fun = img2pdf.get_layout_fun(
                pagesize = ( img2pdf.px_to_pt( img.width, 96 ), img2pdf.px_to_pt( img.height, 96 ) ),
                fit = img2pdf.FitMode.into
            )
            f.write( img2pdf.convert( [ 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.jpg','C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.jpg', 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.jpg', 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.jpg' ], layout_fun = my_layout_fun ))
            return render(request,"graphes.html")

def detail_1(request):
    if request.method == 'POST':
        img = Image.open( 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.png' )
        imageio.imwrite('C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\cinq.png',img)
        plt.imshow(img)
        plt.show()
        return render(request,"graphes.html")
        
def detail_2(request):
    if request.method == 'POST':
        img = Image.open( 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.png' )
        imageio.imwrite('C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\deux.png',img)
        plt.imshow(img)
        plt.show()
        return render(request,"graphes.html")

def detail_3(request):
    if request.method == 'POST':
        img = Image.open( 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.png' )
        imageio.imwrite('C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\quatre.png',img)
        plt.imshow(img)
        plt.show()
        return render(request,"graphes.html")        

def detail_4(request):
    if request.method == 'POST':
        img = Image.open( 'C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.png' )
        imageio.imwrite('C:\\Users\\Khalid-Rami\Desktop\\mywebsite\\static_file\\our_static\\images\\trois.png',img)
        plt.imshow(img)
        plt.show()
        return render(request,"graphes.html")  

#def plot (request):
        #data = pd.read_excel('C:\\Users\\Khalid-Rami\\Desktop\\COLA.xls')
        #data_old=data.columns
        #fig = go.Figure([go.Scatter(x=df['CKREGWT'], y=df['PPREGWT'])])
        #fig.show()
        #return render(request,"plot.html",{'res':data_old})





        
















 




