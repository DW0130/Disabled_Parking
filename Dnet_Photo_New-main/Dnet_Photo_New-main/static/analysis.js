window.addEventListener('DOMContentLoaded', function() { 

})

function time(a){
    switch(a){
        case 0:
        case 1:
        case 2:
            return 0
        case 2:
        case 3:
        case 4:
            return 1

        case 4:
        case 5:
        case 6:
            return 2

        case 6:
        case 7:
        case 8:
            return 3

        case 8:
        case 9:
        case 10:
            return 4

        case 10:
        case 11:
        case 12:
            return 5

        case 12:
        case 13:
        case 14:
            return 6

        case 14:
        case 15:
        case 16:
            return 7

        case 16:
        case 17:
        case 18:
            return 8

        case 18:
        case 19:
        case 20:
            return 9

        case 20:
        case 21:
        case 22:
            return 10

        case 22:
        case 23:
        case 24:
            return 11


    }
}


function search(){
    var locatan = [0,0,0,0,0,0]
    var atime = [0,0,0,0,0,0,0,0,0,0,0,0]
    var btime = [0,0,0,0,0,0,0,0,0,0,0,0]
    var ctime = [0,0,0,0,0,0,0,0,0,0,0,0]
    var dtime = [0,0,0,0,0,0,0,0,0,0,0,0]
    var etime = [0,0,0,0,0,0,0,0,0,0,0,0]
    var ftime = [0,0,0,0,0,0,0,0,0,0,0,0]


    console.log("search")
    var startdate = document.getElementById('startdate').value
    var enddate = document.getElementById('enddate').value
    var lim = '0'

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/searchDBAn", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        startdate : startdate,
        enddate : enddate,
        lim : lim
    }));
    xhr.onload = function() {
    var data = JSON.parse(this.responseText)

    for(i in data){
        var date1 = new Date(data[i][2])
        switch(data[i][0]){
            case 'A':
                locatan[0] += 1
                atime[time(data[i][2])] +=1
                break
            case 'B':
                locatan[1] += 1
                btime[time(data[i][2])] +=1
                break
            case 'C':
                locatan[2] += 1
                ctime[time(data[i][2])] +=1
                break
            case 'D':
                locatan[3] += 1
                dtime[time(data[i][2])] +=1
                break
            case 'E':
                locatan[4] += 1
                etime[time(data[i][2])] +=1
                break
            case 'F':
                locatan[5] += 1
                ftime[time(data[i][2])] +=1
                break
            }

        

    }

    var ctx = document.getElementById("myChart").getContext('2d');
/*
- Chart를 생성하면서, 
- ctx를 첫번째 argument로 넘겨주고, 
- 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
*/
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["센서 1", "센서 2", "센서 3", "센서 4", "센서 5", "센서 6"],
        datasets: [{
            label: '단속 수',
            data: locatan,
            backgroundColor: [
                'rgba(6, 0, 47)',
                'rgba(6, 0, 47)',
                'rgba(6, 0, 47)',
                'rgba(6, 0, 47)',
                'rgba(6, 0, 47)',
                'rgba(6, 0, 47)',
            ],

        }]
    },
    options: {
        maintainAspectRatio: false, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});


console.log(locatan)
console.log(time)
var ctx2 = document.getElementById('aa').getContext('2d');

var myChart = new Chart(ctx2,{
    type: 'line',
    data: {
        labels: ['00~02', '02~04', '04~06' ,'06~08', '08~10', '10~12', '12~14','14~16', '16~18', '18~20', '20~22', '22~24'],
        datasets: [
            {
                label: '센서1',
                data: atime,
                borderColor: 'red',
                fill : false
            },
            {
                label: '센서2',
                data: btime,
                borderColor: 'blue',
                fill : false
            },
            {
                label: '센서3',
                data: ctime,
                borderColor: 'green',
                fill : false
            },
            {
                label: '센서4',
                data: dtime,
                borderColor: 'black',
                fill : false
            },
            {
                label: '센서5',
                data: etime,
                borderColor: 'gray',
                fill : false
            },
            {
                label: '센서6',
                data: ftime,
                borderColor: 'orange',
                fill : false
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        bezierCurve: false,
        elements: {
            line: {
                tension: 0
            }
        }
    }
});


}
}