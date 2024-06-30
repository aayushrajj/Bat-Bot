// first we fetched all the variables ( INPUT , OUTPUT , BUTTON ) required ahead 
console.log(typeof marked); // should output 'function'
var btnSend = document.querySelector("#btn-send");
var audioID = document.querySelector("#click-sound");
var btnRefresh = document.querySelector("#btn-refresh");


// button click audio
function playClickSound() {
    var clickSound = audioID;
    clickSound.play();
}

// there can be error sometimes , so a function for handling errors
function errorHandler(error){
    console.log("error occured",error);
    alert("There has been a problem with your fetch operation; Error processing request");
    const loadingPlaceholder = document.getElementById('loadingPlaceholder');
        if (loadingPlaceholder) {
                loadingPlaceholder.remove();
        }
    // Clear the input field
    userInput.value = '';
    userInput.focus();
}

function refreshPage(){
    // Logic to refresh the chat messages
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.innerHTML = ''; // Clear the chat messages
    userInput.value = '';
    userInput.focus();
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

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');

    if (userInput.value.trim() === '') return;

    // Create user message element
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message', 'text-right');
    userMessage.textContent = userInput.value;
    chatMessages.appendChild(userMessage);

    // Create loading spinner placeholder
    const loadingPlaceholder = document.createElement('div');
    loadingPlaceholder.id = 'loadingPlaceholder';
    loadingPlaceholder.classList.add('message', 'bot-message', 'text-left');

    const loadingSpinner = document.createElement('div');
    loadingSpinner.classList.add('spinner-border', 'text-primary', 'spinner');
    loadingSpinner.role = 'status';
    loadingSpinner.innerHTML = '<span class="sr-only">Loading...</span>';


    loadingPlaceholder.appendChild(loadingSpinner);
    chatMessages.appendChild(loadingPlaceholder);

    // Scroll to the bottom of the chat
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // get response from Gemini
    const botResponse = await processText(userInput.value);
    console.log('Bot Response:', botResponse);

    // Remove loading spinner
    loadingPlaceholder.remove();

    // Create bot message element
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot-message', 'text-left');

    // Use marked to parse the response
    botMessage.innerHTML = marked.parse(botResponse); 
    chatMessages.appendChild(botMessage);

    // Clear the input field
    userInput.value = '';
    userInput.focus();

    // Scroll to the bottom of the chat
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function KeyboardEvent(event) {
    if (event.key==='Enter'){
        sendMessage();
        playClickSound();
    }
}

// Add Event Listeners...
btnSend.addEventListener("click" , playClickSound);
btnSend.addEventListener("click" , sendMessage);
userInput.addEventListener("keypress", KeyboardEvent);
btnRefresh.addEventListener("click", refreshPage);


