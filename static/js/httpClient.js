let makeHttpClient = function (baseUrl) {
    let HttpClient = function (baseUrl) {
        this.baseUrl = '/r01/sensor-';
    };
    //get
    HttpClient.prototype.get = function (param, callback) {
        let url = `${this.baseUrl}` + param;
        let r = new XMLHttpRequest();
        r.responseType = 'json';
        r.open('GET', url, true);
        r.onreadystatechange = function () {
            if (r.readyState === 4) {
                callback(r.response);
            }
        };
        r.send();
    };
    return new HttpClient();
};