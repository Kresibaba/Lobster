// Appending <a href= > tag to elements in the periodic table.

textField = function () {

    let allElements = document.getElementsByClassName('table-element');
    let element_abbr = null;
    let element_name = null;

        for (let item of allElements) {

            let children = item.childNodes;
            for (let child of children) {
                if (child.className === 'element-abbr') {
                    element_abbr = child.innerHTML;
                }
                if (child.className === 'element-name') {
                    element_name = child.innerHTML;
                }
            }

            var aTag = document.createElement('a');
            aTag.setAttribute('onclick', 'overlay_window_on("overlay-window", "'+element_abbr+'", "'+element_name+'")');
            aTag.setAttribute('class', 'element-anchor');
            /*var aTag = document.createElement('input');
            aTag.setAttribute('type', 'submit');
            aTag.setAttribute('value','');
            aTag.setAttribute('name','H');*/


           while (item.hasChildNodes())
                aTag.appendChild(item.firstChild);
            item.appendChild(aTag);
        }
    };

try {
    window.onload = textField();
} catch (e) {
    alert("Exception raised")
}

// Open overlay window
function overlay_window_on(window, element_abbr, element_name) {
    //document.getElementById('radDataElement').submit();
    document.getElementById(window).style.display = "block";
    document.getElementById('test').textContent = element_abbr;
    document.getElementById('overlay-title').innerHTML = element_name;
    }

// Close overlay window
function overlay_window_off(window) {
    document.getElementById(window).style.display = "none";
}