# Great War History Timeline
This app was created as part of my coursework for CS361 - Software Development I at Oregon State University.
The project guidelines were relatively open-ended, allowing for students to pursue apps that would align with their
interests both inside and outside of software development topics. I am passionate about 19th and 20th century history, 
particularly European history. As such, I sought to educate users on the events of World War I as the outcomes had
lasting impacts which still greatly influence our world today. The app consists of three pages: 
* A timeline of the events
themselves, using the TimelineJS plugin
* A _This Day In History_ page, allowing users to view a table populated with events which occurred / were
occurring on a selected date
* Backgrounds of key nations involved in the conflict, accessible via a dropdown


# Running the Application
The server used to run the WW1 events service exists in the server.py file. In this file, the server is started with the following code block:
```python
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```
To execute this and start the app via command line, simply run: python app.py

Additionally, the server is preset to run locally on port 5000. To change the server host value, simply change the host value in app.py to your 
desired host. To change the server port value simply change the port value in app.py to your desired port 
(it is currently set to 5000).

# This Day in History 
As part of my CS361 coursework, I worked with a classmate to develop microservices which would work within our
individual apps. My partner was tasked with developing the backend functionality for _This Day in History_ which
is featured in this repo. **Other than some minor modifications made to incorporate the microservice into my app, the work
within date_parser.py and events_service.py is the work of my partner.**