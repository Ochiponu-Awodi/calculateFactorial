function calculateFactorial () {
    const number = document.getElementById("number").value;
    fetch(`factorial_imperative.py?number=${number}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("result").innerText = `Imperative approach: ${data}`;
        });
    fetch(`factorial_declarative.py?number=${number}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("result").innerText += `\nDeclarative approach: ${data}`;
        });
}