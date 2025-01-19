document.getElementById('quiz-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    try {
        const response = await fetch('/submit_quiz', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);
        } else {
            alert(`Error: ${result.message}`);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
});
