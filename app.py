from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "fuegey4te9gu8e9ighe849w722018nfgboerighpe59ieo85bgei478ubwo339"

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/calculator', methods=['POST', 'GET'])
def calc():
    if 'display' not in session:
        session['display'] = 0.0
        session['status'] = 0
        session['number'] = 0
        session['number1'] = 0
        session['number2'] = 0
    session['display'] = request.form.get('current', '')
    current = request.form.get('current','')
    if "clear" in request.form:
        session['display'] = ''
    else:
        digit = str(request.form.get("digit"))
        if digit:
            session['display'] = current + digit
    try:
        session['number'] = float(session['display'])
    except:
        pass
    if "zarb" in request.form:
        session['number1'] = session['number']
        session['display'] = ''
        session['status'] = 1
    if "taghsim" in request.form:
        session['number1'] = session['number']
        session['display'] = ''
        session['status'] = 2
    if "jam" in request.form:
        session['number1'] = session['number']
        session['display'] = ''
        session['status'] = 3
    if "tafrigh" in request.form:
        session['number1'] = session['number']
        session['display'] = ''
        session['status'] = 4
    if "tavan" in request.form:
        session['number1'] = session['number']
        session['display'] = ''
        session['status'] = 5
    if "dot" in request.form:
        if "." not in session['display']:
            session['display'] += "."
    if "manfi" in request.form:
        session['display'] = str(session['display'])
        session['display'] = "-"+session['display']
        session['display'] = session['display'][:-4]
        # session['display'] = int(session['display'])
        print(session['display'])
    if "back" in request.form:
        session['display'] = str(session['display'])[:-5]
        if session['display'] != '' and "." not in session['display'] and session['display'] != "-":
            session['display'] = int(session['display'])
    
    if "equals" in request.form:
        session['number2'] = session['number']
        match session['status']:
            case 0:
                session['display'] = ''
            case 1:
                session['display'] = session['number1'] * session['number2']
            case 2:
                if session['number2'] == 0:
                    session['display'] = "ERROR"
                else:
                    session['display'] = session['number1'] / session['number2']
            case 3:
                session['display'] = session['number1'] + session['number2']
            case 4:
                session['display'] = session['number1'] - session['number2']
            case 5:
                session['display'] = session['number1'] ** session['number2']
            
    try:
        session['display'] = session['display'].replace("None","")
    except:
        pass
    
    return render_template('calc.html', display=session['display'])

@app.route('/select-dimension')
def select_dimension():
    return render_template('select-dimension.html')

@app.route('/select-shape2')
def select_shape2():
    return render_template('select-shape2.html')

@app.route('/select-shape3')
def select_shape3():
    return render_template('select-shape3.html')

@app.route('/geometry2', methods=['POST', 'GET'])
def geometry2():
    disabled = []
    op = request.args.get('op')
    if op is not None:
        session['shape'] = op
    if 'tool' not in session:
        session['tool'] = 0
        session['arz'] = 0
        session['shoaa'] = 0
        session['ghaede'] = 0
        session['ertefa'] = 0
        session['area'] = 0
        session['env'] = 0
    global pi 
    pi = 3.14
    match session['shape']:
        case "1":
            session['env'] = ''
            session['area'] = ''
            session['tool'] = request.form.get('tool')
            disabled = ['arz', 'ertefa', 'shoaa', 'ghaede']
            if session['tool']:
                if float(session['tool']):
                    try:
                        session['env'] = float(session['tool']) * 4
                        session['area'] = float(session['tool'])**2
                    except:
                        pass
        case "2":
            session['env'] = '---'
            session['area'] = ''
            session['ertefa'] = request.form.get('ertefa')
            session['ghaede'] = request.form.get('ghaede')
            disabled = ['arz', 'tool', 'shoaa']
            if session['ertefa'] and session['ertefa']:
                if float(session['ertefa']) and float(session['ghaede']):
                    try:
                        session['area'] = (float(session['ertefa']) * float(session['ghaede']))/2
                    except:
                        pass
        case "3":
            session['env'] = ''
            session['area'] = ''
            session['tool'] = request.form.get('tool')
            session['arz'] = request.form.get('arz')
            disabled = ['shoaa', 'ghaede', 'ertefa']
            if session['tool'] and session['arz']:  
                if float(session['tool']) and float(session['arz']):
                    try:
                        session['area'] = float(session['tool']) * float(session['arz'])
                        session['env'] = (float(session['tool']) + float(session['arz']))*2
                    except:
                        pass
        case "4":
            session['env'] = ''
            session['area'] = ''
            session['shoaa'] = request.form.get('shoaa')
            disabled = ['arz', 'ertefa', 'tool', 'ghaede']
            if session['shoaa']:
                if float(session['shoaa']):
                    try:
                        session['env'] = float(session['shoaa'])*2*pi 
                        session['area'] = float(session['shoaa'])**2*pi
                    except:
                        pass
    session['env'] = str(session['env'])
    session['area'] = str(session['area'])

    return render_template('geometry2.html', env=session['env'], area=session['area'], disabled=disabled)

@app.route('/geometry3', methods=['POST', 'GET'])
def geometry3():
    disabled = []
    op = request.args.get('op')
    if op is not None:
        session['shape'] = op
    if 'tool' not in session:
        session['tool'] = 0
        session['arz'] = 0
        session['shoaa'] = 0
        session['ghaede'] = 0
        session['ertefa'] = 0
        session['vol'] = 0
        session['formula'] = ""
    global pi 
    pi = 3.14
    match session['shape']:
        case "1":
            session['vol'] = ''
            session['tool'] = request.form.get('tool')
            disabled = ['arz', 'ertefa', 'shoaa']
            session['formula'] = "حجم    = طول × عرض × ارتفاع "
            if session['tool']:
                if float(session['tool']):
                    try:
                        session['vol'] = float(session['tool']) ** 3
                    except:
                        pass
        case "2":
            session['vol'] = ''
            session['ertefa'] = request.form.get('ertefa')
            session['shoaa'] = request.form.get('shoaa')
            disabled = ['arz', 'tool']
            session['formula'] = "حجم مخروط = [مساحت قاعده × ارتفاع] ÷ ۳"
            if session['ertefa'] and session['shoaa']:
                if float(session['ertefa']) and float(session['shoaa']):
                    try:
                        session['vol'] = (float(session['ertefa']) * ((float(session['shoaa'])**2)*pi))/3
                    except:
                        pass
        case "3":
            session['vol'] = ''
            session['tool'] = request.form.get('tool')
            session['arz'] = request.form.get('arz')
            session['ertefa'] = request.form.get('ertefa')
            disabled = ['shoaa',]
            session['formula'] = " حجم مکعب مستطیل = طول × عرض × ارتفاع "
            if session['tool'] and session['arz'] and session['ertefa']:  
                if float(session['tool']) and float(session['arz']) and float(session['ertefa']):
                    try:
                        session['vol'] = (float(session['tool']) * float(session['arz'])) * float(session['ertefa'])
                    except:
                        pass
        case "4":
            session['vol'] = ''
            session['shoaa'] = request.form.get('shoaa')
            disabled = ['arz', 'ertefa', 'tool']
            session['formula'] = "حجم کره = ۴/۳ × عدد پی × شعاع × شعاع × شعاع"
            if session['shoaa']:
                if float(session['shoaa']):
                    try:
                        session['vol'] = (float(session['shoaa'])**3)*(4/3)*pi
                    except:
                        pass
    session['vol'] = str(session['vol'])

    return render_template('geometry3.html', volume=session['vol'], disabled=disabled , formula=session['formula'])

@app.route('/average', methods=["POST","GET"])
def average():
    session['average'] = 0
    try:
        if "number_A" in request.form:
            session['number_A'] = request.form.get("number_A")
                
            numbers_A = session['number_A'].split()
            len_A = len(numbers_A)
            total_A = 0
            for i in numbers_A:
                i = float(i)
                total_A += i
                session['average'] = total_A/len_A
    except:
        return render_template('average.html',out=session['average'])
    return render_template('average.html',out=session['average'])

@app.route('/bmi', methods=["POST","GET"])
def bmi():
    session['height'] = 0
    session['weight'] = 0
    session['bmi'] = 0
    if "height" in request.form:
        session['height'] = request.form.get("height")
        session['weight'] = request.form.get("weight")
        session['height'] = float(session['height']) / 100
        bmi = float(session['weight']) / (float(session['height'])**2)
        session['bmi'] = bmi
        return render_template('bmi.html', bmi=session['bmi'])
    return render_template('bmi.html')
    
app.run(debug=True, host='0.0.0.0', port=5555)
