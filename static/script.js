"use strict";

let editBtn = document.getElementsByClassName("editBtn")
let form_title = document.getElementById("form_title")
let form_desc = document.getElementById("formDesc")
let submit_button = document.getElementById("form_button")
let form = document.getElementsByTagName("form")[0]


for (let one of editBtn) {
 one.addEventListener("click", (e) => {

  // let title = e.target.parentNode.firstElementChild.innerText
  // let desc = e.target.parentNode.firstElementChild.nextElementSibling.innerText
  let title = e.target.parentNode.firstElementChild.innerText
  let desc = e.target.parentNode.firstElementChild.nextElementSibling.innerText


  form_title.value = title
  form_desc.value = desc
  submit_button.innerText = "📑 Update Note"
  let clean_id = e.target.id.split("_")[1]
  form.action = `update_note/${clean_id}`
  // form.method = "PATCH"
  // form.method = "get"




  // console.log(title + ": " + desc);



 })
}

