function calculateFactorial () {
    const number = document.getElementById("number").value;

    const baseUrl = 'http://127.0.0.1:5000';

    // Fetch the result from the imperative approach
    fetch(`${baseUrl}/factorial_imperative?number=${number}`)
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            if (data.result !== undefined) {
                document.getElementById("result").innerText = `Imperative approach: ${data.result}`;
            } else {
                document.getElementById("result").innerText = `Imperative approach: Error calculating factorial.`;
            }
        });

    // Fetch the result from the declarative approach
    fetch(`${baseUrl}/factorial_declarative?number=${number}`)
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            if (data.result !== undefined) {
                document.getElementById("result").innerText += `\nDeclarative approach: ${data.result}`;
            } else {
                document.getElementById("result").innerText += `\nDeclarative approach: Error calculating factorial.`;
            }
        });
}