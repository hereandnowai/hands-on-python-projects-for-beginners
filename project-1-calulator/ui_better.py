from flask import Flask, request, jsonify
from calculator import calculate

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>iPhone Style Calculator</title>
<style>
body{
    margin:0;
    background:#0b0f1a;
    display:flex;
    align-items:center;
    justify-content:center;
    height:100vh;
    font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto;
}

.phone{
    width:320px;
    background:black;
    padding:20px;
    border-radius:40px;
    box-shadow:0 20px 60px rgba(0,0,0,.8);
}

.display{
    width:100%;
    height:80px;
    color:white;
    font-size:48px;
    text-align:right;
    border:none;
    background:transparent;
}

.grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
}

button{
    height:70px;
    border-radius:50%;
    border:none;
    font-size:26px;
    cursor:pointer;
}

.num{background:#333;color:white}
.op{background:#ff9f0a;color:white}
.spec{background:#a5a5a5}

.zero{
    grid-column:span 2;
    border-radius:40px;
    text-align:left;
    padding-left:28px;
}
</style>
</head>

<body>

<div class="phone">

<input id="display" class="display" value="0" readonly>

<div class="grid">

<button class="spec" onclick="clearDisplay()">AC</button>
<button class="spec" onclick="toggleSign()">+/-</button>
<button class="spec" onclick="percent()">%</button>
<button class="op" onclick="setOp('/')">÷</button>

<button class="num" onclick="press(7)">7</button>
<button class="num" onclick="press(8)">8</button>
<button class="num" onclick="press(9)">9</button>
<button class="op" onclick="setOp('*')">×</button>

<button class="num" onclick="press(4)">4</button>
<button class="num" onclick="press(5)">5</button>
<button class="num" onclick="press(6)">6</button>
<button class="op" onclick="setOp('-')">-</button>

<button class="num" onclick="press(1)">1</button>
<button class="num" onclick="press(2)">2</button>
<button class="num" onclick="press(3)">3</button>
<button class="op" onclick="setOp('+')">+</button>

<button class="num zero" onclick="press(0)">0</button>
<button class="num" onclick="dot()">.</button>
<button class="op" onclick="equals()">=</button>

</div>
</div>

<script>

let current="0"
let previous=null
let op=null

const display=document.getElementById("display")

function update(){display.value=current}

function press(n){
 if(current=="0") current=n.toString()
 else current+=n
 update()
}

function dot(){
 if(!current.includes(".")){
 current+="."
 update()
 }
}

function clearDisplay(){
 current="0"
 previous=null
 op=null
 update()
}

function toggleSign(){
 current=(parseFloat(current)*-1).toString()
 update()
}

function percent(){
 current=(parseFloat(current)/100).toString()
 update()
}

function setOp(o){
 previous=current
 current="0"
 op=o
}

async function equals(){
 if(previous==null||op==null) return

 const res=await fetch("/calculate",{
 method:"POST",
 headers:{"Content-Type":"application/json"},
 body:JSON.stringify({a:previous,b:current,op:op})
 })

 const data=await res.json()

 current=data.result.toString()
 previous=null
 op=null
 update()
}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return HTML_PAGE


@app.route("/calculate", methods=["POST"])
def calc():
    data = request.json

    a = float(data["a"])
    b = float(data["b"])
    op = data["op"]

    result = calculate(a, op, b)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)