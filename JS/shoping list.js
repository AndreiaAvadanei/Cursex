function adaugProdus(){
    var check_box = document.createElement(tagName:"input")
    check_box.type="checkbox"
    var produs = document.createElement(tagName:"lable")
    var spaces = document.createElement(tagName:"br")

    var parinte = document.getElementById(elementId:"text_box")
    var inputed_text = document.getElementById(elementId:"text_box")
    parinte.appendChild(spaces)
    parinte.appendChild(check_box)
    parinte.appendChild(produs)
}