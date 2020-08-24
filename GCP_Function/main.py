def send_email(request):
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    payload = eval(request.get_data(as_text=True))
    
    #request_json = request.get_json()
    #print(request_json)

    html='<table border="2" style="background-color: snow; border-color: black;"><tr><th>Name</th><th>Age</th><th>Gender</th><th>Major</th><th>Program</th><th>Preference One</th><th>Preference Two</th><th>Min Rent</th><th>Max Rent</th><th>Food Preference</th><th>Description</th><th>Email</th></tr>'

    email_body=eval(payload['email_body'])

    for y in email_body:
        html+="<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(y['name'],y['age'],y['gender'],y['major'],y['program'],y['preferenceone'],y['preferencetwo'],y['minrent'],y['maxrent'],y['foodpreference'],y['description'],y['email'])

    html+='</table>'

    message = Mail(
        from_email='spuranda@asu.edu',
        to_emails=str(payload['receiver']),
        subject='Greetings from Sun Devils Roommate Recommender!',
        html_content=html)
    SENDGRID_API_KEY='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'
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return payload['receiver']
        # request_json = request.get_json()
        # if request.args and 'body' in request.args:
        #     return request.args.get('body')
        # elif request_json and 'body' in request_json:
        #     return request_json['body']
        #print(response.body)
        #print(response.headers)
    except Exception as e:
        return str(e)