/*
      JavaScript 6th Edition
      Chapter 7
      Hands-on Project 7-5

      Author: Truc Huynh
      Date:   06/01/2018

      Filename: script.js
 */

var delivInfo = {};
var delivSummary = document.getElementById("deliverTo");
var foodInfo = {};
var foodSummary = document.getElementById("order");

function processDeliveryInfo() {
    //Declare variable
    var prop;
    delivInfo.name = document.getElementById("nameinput").value;
    delivInfo.addr = document.getElementById("addrinput").value;
    delivInfo.city = document.getElementById("cityinput").value;
    delivInfo.email = document.getElementById("emailinput").value;
    delivInfo.phone = document.getElementById("phoneinput").value;

    for (prop in delivInfo) {
        delivSummary.innerHTML += "<p>" + delivInfo[prop] + "</p>";
        document.getElementById("deliverTo").style.display = 'block';
    }

}

// create a function with the name processFood
function processFood() {
    //Declare variable
    var prop;
    var crustOpt = document.getElementsByName("crust");
    var toppings = 0;
    var toppingBoxes = document.getElementsByName("toppings");
    var instr = document.getElementById("instructions");

    //checks if thin crust or deep dish
    if (crustOpt[0].checked) {
        foodInfo.crust = crustOpt[0].value;
    } else {
        foodInfo.crust = crustOpt[1].value;
    }

    //Get the pizza size and assigned to foodInfo Object
    foodInfo.size = document.getElementById("size").value;

    //Get the pizza toppings and assigned them foodInfo Object
    for (var i = 0; i < toppingBoxes.length; i++) {
        if (toppingBoxes[i].checked) {
            toppings++;
            foodInfo["topping" + toppings] = toppingBoxes[i].value;
            // Assign array of topping boxes.
        }
    }

    // checks if the element referenced by the instr variable has any content
    if (!instr.value == " ") {
        foodInfo.instructions = instr.value;
    } else {
        foodInfo.instructions = "There is no instructions";
    }
    //Assign the detail of the food to foodSummary
    foodSummary.innerHTML += "<p><span>Crust</span>: " + foodInfo.crust + "</p>";
    foodSummary.innerHTML += "<p><span>Size</span>: " + foodInfo.size + "</p>";
    foodSummary.innerHTML += "<p><span>Topping(s)</span>: " + " </p>";
    foodSummary.innerHTML += "<ul>";
    //Assign the topping
    for (var i = 1; i < 6; i++) {
        if (foodInfo["topping" + i]) {
            foodSummary.innerHTML += "<li>" + foodInfo["topping" + i] + "</li>";
        }
    }
    foodSummary.innerHTML += "</ul>";
    foodSummary.innerHTML += "<p><span>Instructions</span>: " + foodInfo.instructions;
    //Display the food Summary
    document.getElementById("order").style.display = "block";
}

//create a function call to process DeliveryInfo and change the display style of the section element to prop
function previewOrder() {
    processDeliveryInfo();
    processFood();
    document.getElementsByTagName("section")[0].style.display = 'block';
}

//create the Event Listener function
function createEventListeners() {
    var previewButton = document.getElementById("previewBtn");
    if (previewButton.addEventListener) {
        previewButton.addEventListener("click", previewOrder, false);
    } else if (previewButton.attachEvent) {
        previewButton.attachEvent("onclick", previewOrder);
    }
}

if (window.addEventListener) {
    window.addEventListener("load", createEventListeners, false);
} else if (window.attachEvent) {
    window.attachEvent("onload", createEventListeners);
}

 
 