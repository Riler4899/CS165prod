function gotoedit() {
	window.location.href = "{{url_for('edit')}}";
}
function unhide() {
	var hidden = document.getElementById("hid");
	hidden.style.display = "block";
}
