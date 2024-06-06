// first we fetched all the variables ( INPUT , OUTPUT , BUTTON ) required ahead 
var btntranslate = document.querySelector("#btn-translate");
var textInput = document.querySelector("#user-input");
var outputDiv = document.querySelector("#output");


// there can be error sometimes , so a function for handling errors
function errorHandler(error){
    console.log("error occured",error);
    alert("There has been a problem with your fetch operation; Error processing request");
}


// what to do when button clicks happens..
async function processText(inputText) {
    // const inputText = textInput.value;
    try {
        const response = await fetch('http://127.0.0.1:5000/api/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: inputText }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data.result;
    } catch (error) {
        errorHandler(error);
    }
}

async function conversation() {
    const userInput = textInput.value;
    if (userInput.trim() !== '') {
        // Append user's message to the chat list
        const userMessageElement = document.createElement('li');
        userMessageElement.textContent = 'User: ' + userInput;
        document.getElementById('chat-list').appendChild(userMessageElement);

        // Get chatbot response
        const botResponse = await processText(userInput);
        console.log(botResponse)

        // Check if botResponse is not null before appending
        if (botResponse !== null) {
            const botResponseElement = document.createElement('li');
            botResponseElement.textContent = 'Batman: ' + botResponse;
            document.getElementById('chat-list').appendChild(botResponseElement);
        }

        // Scroll to the bottom of the chat list
        document.getElementById('chat-list').scrollTop = document.getElementById('chat-list').scrollHeight;

        // Clear the input field
        document.getElementById('user-input').value = '';
    }
}


// what to do when a click happens...
// btntranslate.addEventListener("click" , processText);
btntranslate.addEventListener("click" , conversation);


