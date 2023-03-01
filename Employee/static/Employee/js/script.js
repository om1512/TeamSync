function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, menuOptions;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="menuOptions" and remove the class "active"
  menuOptions = document.getElementsByClassName("menuOptions");
  for (i = 0; i < menuOptions.length; i++) {
    menuOptions[i].className = menuOptions[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("Performance").click();