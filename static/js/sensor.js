let initColor = function () {
    let activeElement = document.getElementsByClassName('nav-link')[0];
    activeElement.style.color = '#9a9a9a';
};

let HttpClient = function () {
    let client = function () {
        this.baseUrl = '/r01/sensor-';
    };

    client.prototype.get = function (param, callback) {
        let url = `${this.baseUrl}` + param;
        let r = new XMLHttpRequest();
        r.responseType = 'json';
        r.onreadystatechange = function () {
            if (r.readyState === 4) {
                callback(r.response);
            }
        };
        r.open('GET', url, true);
        r.send();
    };
    return new client();
};

let bindLinkClickEvent = function () {
    let links = document.getElementsByClassName('item');
    for (let i = 0; i < links.length; i++) {
        let link = links[i];
        link.addEventListener('click', function (event) {
            let param = event.target.parentNode.getAttribute('value');
            //发送get请求
            doGetRequest(param, function (response) {
                if (response.status) {
                    doTableHead(response.tabs);
                    doTableBody(response.content);
                } else {
                    alert(response.error)
                }
            })
        });
    }
};

let doGetRequest = function (param, callback) {
    let client = HttpClient();
    client.get(param, callback);
};

//生成table的内容
let doTableBody = function (contentList) {
    let bodyElement = document.getElementsByTagName('tbody')[0];
    bodyElement.innerHTML = '';
    for (let i = 0; i < contentList.length; i++) {
        let trElement = document.createElement('tr');
        let firTd = document.createElement('td');
        firTd.classList.add('td-content');
        firTd.innerHTML = contentList[i]['id'];
        trElement.appendChild(firTd);
        let dataDict = contentList[i]['data'];
        for (let key in dataDict) {
            let tdElement = document.createElement('td');
            tdElement.classList.add('td-content');
            //check property exist
            if (dataDict.hasOwnProperty(key)) {
                tdElement.innerHTML = dataDict[key];
            } else {
                console.log('没有此key值')
            }
            trElement.appendChild(tdElement);
        }
        bodyElement.appendChild(trElement);
    }
};

//生成table表头
let doTableHead = function (tabNames) {
    let elem = document.getElementsByTagName('thead')[0];
    elem.innerHTML = '';
    //获取当前宽度
    let newWidth = getNewWidth(tabNames);
    //读取信息生成th插入到table中
    let elemTr = document.createElement('tr');
    for (let j = 0; j < tabNames.length; j++) {
        let elemTh = document.createElement('th');
        let elemDiv = document.createElement('div');
        elemDiv.style.width = newWidth + 'px';
        elemDiv.innerHTML = `${tabNames[j]}`;
        elemDiv.classList.add('th-content');
        elemTh.appendChild(elemDiv);
        elemTr.appendChild(elemTh);
    }
    let elemThead = document.getElementsByTagName('thead')[0];
    elemThead.appendChild(elemTr);
};

//处理table和container边框适配问题
let getNewWidth = function (tabNames) {
    let container = document.getElementsByClassName('table-container')[0];
    let itemWidth = container.clientWidth / tabNames.length;
    if (itemWidth <= 110) {
        itemWidth = 110;
    }
    return Math.ceil(itemWidth);
};

let __main = function () {
    initColor();
    doGetRequest('InfraredSensor', function (response) {
        if (response.status) {
            doTableHead(response.tabs)
        } else {
            alert(response.error)
        }
    });
    bindLinkClickEvent();
};

__main();