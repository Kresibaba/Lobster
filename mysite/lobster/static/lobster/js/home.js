
// Selection of all the text inside this object

var project_name = document.getElementById("id_project_name");


window.onload = function () {
    project_name.placeholder = 'Enter a name...';
    project_name.onclick = function () {
    project_name.setSelectionRange(0, this.value.length);
    }
};
