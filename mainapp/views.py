import pandas as pn
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from django.contrib import messages
import os
# import difflib

# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=="POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        c_password = request.POST.get("C_password")
        if password==c_password:
            if User_Reg.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
            else:
                data = User_Reg(name=name, email=email, password=password)
                data.save()
                return redirect("log")   
        else:
            messages.info(request, 'Passwords do not match')
    return render(request,'registration.html')

def log(request):
    if request.method=="POST":
        try:
            email=request.POST.get('Email')
            password=request.POST.get('Password')
            # username=request.POST.get('Name')
            logdata=User_Reg.objects.get(email=email, password=password)
            request.session['Email']=logdata.email
            request.session['id']=logdata.id
            return redirect('user')
        except User_Reg.DoesNotExist as e:
            messages.info(request,'Incorrect password or email')
    return render(request,'login.html')


def user(request):
    
    return render(request, 'user.html')


def editprofile(request):
    e = User_Reg.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            e.Image = request.POST.get("Images")
            e.name = request.POST.get("Name")
            e.email = request.POST.get("Email")
            e.password = request.POST.get("Password")
            e.save()
    # f=get_object_or_404(userreg, e)

    # g=f.Email

    # p=f.Password

    return render(request, 'editprofile.html',{'e':e})

def searchs(request):
    product = []
    query=''
    se = search.objects.all()
    if request.method=="POST":
        query = request.POST.get('que','') 
    
    if query: 
        product = search.objects.filter(Item=query)

    return render(request, 'search.html',{'query':query, 'products':product})

def addrec(request):
    if request.method=="POST":
         i = request.session['id']
         e = request.session["Email"]
         iem = request.POST.get('item', '')
         data = request.POST.get('desc', '')
         if not id or not e or not iem or not data:
             return redirect('search')
         dat = Buy(e,iem,data)
         dat.save()
    return redirect(request, 'addrec.html')


def recommend(request):
    data = pn.read_csv('/content/Items.csv', encoding='ISO-8859-1')

    # Convert to DataFrame
    df = pn.DataFrame(data)

    # Step 1: Preprocess descriptions using TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['description'])

    # Step 2: Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Step 3: Define a function to recommend items
    def recommend_item(item_name, top_n=3):
        # Get index of the item
        idx = df.index[df['name'] == item_name].tolist()[0]
        
        # Get pairwise similarity scores for the item
        sim_scores = list(enumerate(cosine_sim[idx]))
        
        # Sort items based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get the top N most similar items (excluding the item itself)
        sim_scores = sim_scores[1:top_n+1]
        
        # Get the item indices and names
        recommended_indices = [i[0] for i in sim_scores]
        recommended_names = df['name'].iloc[recommended_indices].values
        
        return recommended_names

    # Test the recommendation system
    item_to_recommend = 'Bose 27028 161 Bookshelf Pair Speakers In White - 161WH'
    recommended_items = recommend_item(item_to_recommend, top_n=3)
    print(f"Items similar to '{item_to_recommend}':")
    for item in recommended_items:
        print(item)