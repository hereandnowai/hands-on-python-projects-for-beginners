let current = "0";
let previous = null;
let operator = null;
let waitingForNext = false;

const display = document.getElementById("display");

function update() {
    display.value = current;
}

function press(n) {
    if (current === "0" || waitingForNext) {
        current = n.toString();
        waitingForNext = false;
    } else {
        current += n.toString();
    }
    update();
}

function dot() {
    if (waitingForNext) {
        current = "0.";
        waitingForNext = false;
    } else if (!current.includes(".")) {
        current += ".";
    }
    update();
}

function clearDisplay() {
    current = "0";
    previous = null;
    operator = null;
    waitingForNext = false;
    update();
}

function toggleSign() {
    if (current === "0") return;
    current = (parseFloat(current) * -1).toString();
    update();
}

function percent() {
    current = (parseFloat(current) / 100).toString();
    update();
}

function setOperator(op) {
    if (operator && !waitingForNext) {
        equals();
    }
    previous = current;
    operator = op;
    waitingForNext = true;
}

async function equals() {
    if (previous === null || operator === null) return;

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ a: previous, b: current, op: operator })
        });

        if (!response.ok) {
            throw new Error("API response error");
        }

        const data = await response.json();
        current = data.result.toString();
        previous = null;
        operator = null;
        waitingForNext = true; 
        update();
    } catch (error) {
        console.error("Calculation failed:", error);
        current = "Error";
        update();
    }
}
