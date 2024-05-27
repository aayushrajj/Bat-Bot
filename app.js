
// first we fetched all the variables ( INPUT , OUTPUT , BUTTON ) required ahead 
var btntranslate = document.querySelector("#btn-translate");
var textInput = document.querySelector("#text-input");
var outputDiv = document.querySelector("#output");


// we fetched the server url , to which we want to talk or get our data
var serverURL = "https://api.funtranslations.com/translate/minion.json"


// then we defined a function for whenever we want to convert a text or use server URL for the text
function getTranslationURL(text){
    var encodedText = encodeURI(text);
    return serverURL + "?" + "text=" + encodedText
}

// there can be error sometimes , so a function for handling errors
function errorHandler(error){
    console.log("error occured",error);
    alert("Too Many Requests! Rate limit of 5 requests per hour exceeded. Please try again after sometime");
}


// what to do when button clicks happens..
function clickHandler(){
    // read the input
    var input = textInput.value; 

    // calling server for processing
    var finalURL = getTranslationURL(input);
    
    // go fetch the response we got from the server --> then convert it to json --> 
    // then  get that translated text and show this as the main output
    fetch(finalURL)
        .then( response => response.json() )
        .then(json => {
            var translatedText = json.contents.translated;
            outputDiv.innerText = translatedText; //main output
        })
        .catch(errorHandler) 

}


// what to do when a click happens...
btntranslate.addEventListener("click" , clickHandler);


