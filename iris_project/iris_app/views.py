# Import render from django shortcuts
from django.shortcuts import render

#Import check_email function, cv, model from Email_Spaming_Model.py
from Iris_data import model

# Create your views here.

# Making prediction function.
def predict_iris(value):

    # Then Predict the email (spam or ham)
    iris_post = model.predict(value)

    # return the output.
    return iris_post[0]


def irishit(request):
    if request.method == 'POST':

        # receive input by post function.
        check_value1 = request.POST['T1']
        check_value2 = request.POST['T2']
        check_value3 = request.POST['T3']
        check_value4 = request.POST['T4']

        list = [[check_value1,check_value2,check_value3,check_value4]]

        # checking output is spam or not.
        if predict_iris(list) == 0:
            data = 'Iris-Setosa'

            #           return Iris-Setosa to html file.
            return render(request, 'home.html', {'data': '0'})
        elif predict_iris(list) == 1:
            data = 'Iris-Versicolour'

            #           return Iris-Versicolour to html file.
            return render(request, 'home.html', {'data': '1'})
        else:
            data = 'Iris-Virginica'
            #           return Iris-Virginica to html file.
            return render(request, 'home.html', {'data': '2'})
    else:
        #       return error if page is not load.
        return render(request, 'home.html', {'data': "Page Loading Fail"})
