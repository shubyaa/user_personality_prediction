
from django.shortcuts import render
from dashboard.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from.models import Student

import pandas as pd
import os

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

import pickle


loaded_model_1 = pickle.load(open("/media/shubham/Acer/Users/Shubham/Final Year Projects/user_personality_prediction/main/dashboard/trained_model_1.sav","rb"))
loaded_model_2 = pickle.load(open("/media/shubham/Acer/Users/Shubham/Final Year Projects/user_personality_prediction/main/dashboard/trained_model_2.sav","rb"))
loaded_model_3 = pickle.load(open("/media/shubham/Acer/Users/Shubham/Final Year Projects/user_personality_prediction/main/dashboard/trained_model_3.sav","rb"))
loaded_model_4 = pickle.load(open("/media/shubham/Acer/Users/Shubham/Final Year Projects/user_personality_prediction/main/dashboard/trained_model_4.sav","rb"))

postdf=pd.read_csv("/media/shubham/Acer/Users/Shubham/Final Year Projects/user_personality_prediction/main/dashboard/pickle_models/post.csv")


from .Algorithms import questionare as qt


# Create your views here.
def detailed_personality(trait) :
    
    if trait=="ISTJ":
        return("The Inspector:\nReserved and practical, they tend to be loyal, orderly, and traditional.\nCharacteristics: Responsible, sincere, analytical, reserved, realistic, systematic. Hardworking and trustworthy with sound practical judgment.")
    elif trait=="ISTP":
        return("The Crafter:\nHighly independent, they enjoy new experiences that provide first-hand learning.\nCharacteristics: Action-oriented, logical, analytical, spontaneous, reserved, independent. Enjoy adventure, skilled at understanding how mechanical things work.")
    elif trait =="ISFJ":
        return("The Protector:\nWarm-hearted and dedicated, they are always ready to protect the people they care about.\nCharacteristics: Warm, considerate, gentle, responsible, pragmatic, thorough. Devoted caretakers who enjoy being helpful to others.")
    elif trait =="ISFP":
        return("The Artist:\nEasy-going and flexible, they tend to be reserved and artistic.\nCharacteristics: Gentle, sensitive, nurturing, helpful, flexible, realistic. Seek to create a personal environment that is both beautiful and practical.")
    elif trait=="INFJ":
        return("The Advocate:\nreative and analytical, they are considered one of the rarest Myers-Briggs types.\nCharacteristics: Idealistic, organized, insightful, dependable, compassionate, gentle. Seek harmony and cooperation, enjoy intellectual stimulation.")
    elif trait=="INFP":
        return("The Mediator:\nIdealistic with high values, they strive to make the world a better place.\nCharacteristics: Sensitive, creative, idealistic, perceptive, caring, loyal. Value inner harmony and personal growth, focus on dreams and possibilities.")   
    elif trait=="INTJ":
        return("The Architect:\nHigh logical, they are both very creative and analytical.\nCharacteristics: Innovative, independent, strategic, logical, reserved, insightful. Driven by their own original ideas to achieve improvements.")
    elif trait=="INTP":
        return("The Thinker:\nQuiet and introverted, they are known for having a rich inner world.\nCharacteristics: Intellectual, logical, precise, reserved, flexible, imaginative. Original thinkers who enjoy speculation and creative problem solving.")
    elif trait=="ESTP":
        return("The Persuader:\nOut-going and dramatic, they enjoy spending time with others and focusing on the here-and-now.\nCharacteristics: Outgoing, realistic, action-oriented, curious, versatile, spontaneous. Pragmatic problem solvers and skillful negotiators.")
    elif trait=="ESTJ":
        return("The Director:\nAssertive and rule-oriented, they have high principles and a tendency to take charge.\nCharacteristics: Efficient, outgoing, analytical, systematic, dependable, realistic. Like to run the show and get things done in an orderly fashion.")
    elif trait=="ESFP":
        return("The Performer:\nOutgoing and spontaneous, they enjoy taking center stage.\nCharacteristics: Playful, enthusiastic, friendly, spontaneous, tactful, flexible. Have strong common sense, enjoy helping people in tangible ways.")
    elif trait=="ESFJ":
        return("The Caregiver:\nSoft-hearted and outgoing, they tend to believe the best about other people.\nCharacteristics: Friendly, outgoing, reliable, conscientious, organized, practical. Seek to be helpful and please others, enjoy being active and productive.")
    elif trait=="ENFP":
        return("The Champion:\nCharismatic and energetic, they enjoy situations where they can put their creativity to work.\nCharacteristics: Enthusiastic, creative, spontaneous, optimistic, supportive, playful, Value inspiration, enjoy starting new projects, see potential in others.")
    elif trait=="ENFJ":
        return("The Giver:\nLoyal and sensitive, they are known for being understanding and generous.\nCharacteristics: Caring, enthusiastic, idealistic, organized, diplomatic, responsible. Skilled communicators who value connection with people.")
    elif trait=="ENTP":
        return("The Debater:\nLoyal and sensitive, they are known for being understanding and generous.\nCharacteristics: Inventive, enthusiastic, strategic, enterprising, inquisitive, versatile. Enjoy new ideas and challenges, value inspiration.")
    elif trait=="ENTJ":
        return("The Commander:\nOutspoken and confident, they are great at making plans and organizing projects.\nCharacteristics: Strategic, logical, efficient, outgoing, ambitious, independent. Effective organizers of people and long-range planners.")



def detect_personality(sample_test):

    vector = CountVectorizer(stop_words='english', max_features=1500)
    vector = vector.fit(postdf.post_list)
    features = vector.transform(sample_test)
    transform = TfidfTransformer()
    finalfeatures = transform.fit_transform(features).toarray()
    sample_input = transform.fit_transform(features).toarray()
    vect = vector.transform(sample_test).toarray()
    loaded_model_1.predict(vect)
    if loaded_model_1.predict(vect) == 1:
        a = "I"
        A="Introversion"
    else:
        a = "E"
        A="Extraversion"
    vect = vector.transform(sample_test).toarray()
    loaded_model_2.predict(vect)
    if loaded_model_2.predict(vect) == 1:
        b = "N"
        B="Intuition"
    else:
        b = "S"
        B="Sensing"
    vect = vector.transform(sample_test).toarray()
    loaded_model_3.predict(vect)
    if loaded_model_3.predict(vect) == 1:
        c = "T"
        C="Thinking"
    else:
        c = "F"
        C="Feeling"
    vect = vector.transform(sample_test).toarray()
    loaded_model_4.predict(vect)
    if loaded_model_4.predict(vect) == 1:
        d = "J"
        D="Judging"
    else:
        d = "P"
        D="Perceiving"
    return (a+b+c+d+" ("+A+"-"+B+"-"+C+"-"+D+")")


def about_us(request):
    return render(request, 'about.html')


@csrf_exempt
def index(request):
    
    # The line below returns the list of students
    student =Student.objects.all()
    # print(student[0].gender)
   
    if request.method == 'POST':
        lame = str(request.POST['last_name'])
        fname = str(request.POST['first_name'])
        email = str(request.POST['email'])
        phone = int(request.POST['phone'])
        add1 = str(request.POST['area'])
        desc = str(request.POST['description'])
        exist = str(request.POST['exist'])
        
        if Student.objects.filter(first_name=fname, last_name=lame).exists():
            print('User Already exists')
            return redirect('dashboard:index')
        else:
            gender = 'M'
            if exist!='M':
                gender='F'
                
            student_ = Student(first_name=fname, last_name=lame, email=email, phone=phone, description=desc, gender=gender, area=add1)
            student_.save()

    context = {
        "first_name" : "Shubham",
        "students" :  student,
    }
    return render(request, "index.html", context=context)


def open_profile(request, id):
    
    # This line will give the student as a list by checking the entry with reference of id.
    student = Student.objects.all().filter(id=id)
    # print(student[0].description)

    desc = [student[0].description]

    vector = CountVectorizer(stop_words='english', max_features=1500)
    features = vector.fit_transform(desc)

    transform = TfidfTransformer()
    # sample_input = transform.fit_transform(features).toarray()
    
    final_result = ""
  
    
    if request.method == "POST":
        question = request.POST["question"]
        
        final_result = qt.answer_questions(question_text=question, context_text=student[0].description)
        
        # return redirect(request, 'userinfo.html', context=context)
    
    print("Final result is ",final_result)
    personality = detect_personality(desc)
        
    context = {
        'id' : id,
        'student' : student[0],
        'answer' : final_result,
        'personality' : personality,
        'personality_detailed' : detailed_personality(personality[0:4]),
    }
   
    return render(request, 'userInfo.html', context=context)

def run_data(request):
    return render(request, 'demo.html')