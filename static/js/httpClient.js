// 封装 Ajax 数据请求
let makeHttpClient = function () {
    //创建对象
    let HttpClient = function () {
        this.baseUrl = '/r01/sensor-';
    };

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