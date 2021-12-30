function showList() {
	document.getElementsByClassName("menuList").className = "menuList hide";
	var x = document.activeElement;
  	document.getElementById("demo").innerHTML = x;
	x.className = "menuList show";
  }