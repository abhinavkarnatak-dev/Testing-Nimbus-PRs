// Function declarations are available before their definition.
showMessage();

function showMessage() {
    console.log("JavaScript functions can be called before they are declared.");
}

// Variables declared with var are hoisted, but their assignment is not.
console.log("Before assignment:", message);
var message = "The variable now has a value.";
console.log("After assignment:", message);
