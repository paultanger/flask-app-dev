# make html that gives us a button to go back to the home page
    go_to_home_html = '''
        <form action="/" >
            <input type="submit" value = "Go home"/>
        </form>
    '''


    # formatting dictionary keys and values to be displayed in html
def dict_to_html(d):
    return '<br>'.join('{0}: {1}'.format(k, d[k]) for k in sorted(d))


# Form page to submit text
@app.route('/')
def submission_page():
    # in this form, method = 'POST' means that data entered into
    # the 'user_input' variable will be sent to the /word_counter routing
    # block when the 'Enter text' submit button is pressed
    return '''
        <form action="/word_counter" method='POST' >
            <input type="text" name="user_input" />
            <input type="submit" value = 'Enter text'/>
        </form>
        '''


# My word counter app
# this routing block accepts data in variable 'user_input' from the form
# and then processes it on the server and returns word counts to the browser
@app.route('/word_counter', methods=['GET', 'POST'])
def word_counter():
    text = str(request.form['user_input']) #gets the value entered in the input type="text", name="user_input"
    word_counts = Counter(text.lower().split())
    
    # formatted output string
    page = 'There are {0} words.<br><br>Individual word counts:<br> {1}'
    
    # make html that gives us a button to go back to the home page
    go_to_home_html = '''
        <form action="/" >
            <input type="submit" value = "Enter more text"/>
        </form>
    '''
    
    return page.format(len(word_counts), dict_to_html(word_counts)) + go_to_home_html


    @app.route('/')
def index():
    # img in the html specifies the presence of an image
    # however, the src of the image is a routing block instead of
    # a .jpg or .png
    return '''
        <h2>Here's my plot!</h2>
        <img src='/plot.png'>
        '''

@app.route('/plot.png')
def get_graph():
    fig = Figure()
    ax = fig.subplots()
    n = 10
    ax.plot(range(n), [random() for i in range(n)])
    image = BytesIO()
    fig.savefig(image)  #the plot is saved
    return image.getvalue(), 200, {'Content-Type': 'image/png'}