from flask import Flask, render_template
from flask.globals import request
import func

app=Flask("__name__")

@app.route('/')
def welcome() :
    return render_template('welcome.html')

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/operation_result/',methods=['POST'])
def operation_result() :
    first_input=request.form['Input1']
    second_input=request.form['Input2']
    operation=request.form['operation']
    try:
        input1=int(first_input)
        input2=int(second_input)
        while True:
            if operation== 'a' :
                num, den=func.constant(input1,input2);
                break;
            elif operation=='b' :
                num, den=func.expo(input1,input2);
                break;
            elif operation=='c' :
                num, den=func.sine(input1,input2);
                break;
            elif operation=='d' :
                num, den=func.cos(input1,input2)
                break;
            elif operation=='e' :
                num, den=func.tfunc(input1,input2)
                break;
            elif operation=='f' :
                num, den=func.expo_cos(input1,input2)
                break;
            elif operation=='g' :
                num, den=func.expo_sin(input1,input2)
                break;
            elif operation=='h' :
                num, den=func.t_expo(input1,input2)
                break;
            elif operation=='i' :
                num, den=func.expo_sinh(input1,input2)
                break;
            elif operation=='j' :
                num, den=func.expo_cosh(input1,input2)
                break;
            elif operation =='k' :
                num, den=func.sinh(input1,input2)
                break;
            elif operation =='l' :
                num, den=func.cosh(input1,input2)
                break;
    
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result_num=num,
            result_den=den,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result2='Bad Input',
            calculation_success=False,
            error="You cannot divide by zero"
        )
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result3='Bad Input',
            calculation_success=False,
            error="Cannot perform operations with provided inputs"
        )

@app.route('/information')
def info() :
    return render_template('information.html')

@app.route('/about')
def about() :
    return render_template('about.html')

        
if __name__=="__main__" :
    app.run(debug=True,host="localhost")
