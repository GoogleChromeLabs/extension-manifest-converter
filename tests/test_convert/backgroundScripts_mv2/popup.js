/**
 * Copyright 2021 Google Inc. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

document.addEventListener('DOMContentLoaded', setup, false);

let key = "todoListItems";
var items = {};

function getFontSize() {
  chrome.storage.local.get({
    todoListFontSize: '90'
  }, function(items) {
    document.body.style.fontSize = items.todoListFontSize + '%';
  });
}

var port;

function setup() {
  port = chrome.runtime.connect({ name: "popup" });
  port.onMessage.addListener(function(msg) {
    let element = document.getElementById("addText");
    element.value = msg.text;
  });

  getFontSize();
  getItems();
  let element = document.getElementById("addText");
  element.focus();
  element.addEventListener("keyup", event => {
    if (event.key === 'Enter') {
      addItem();
    }
  });
  element.addEventListener("input", event => {
    let element = document.getElementById("addText");
    port.postMessage({text: element.value});
  });
}

function addItem() {
  let addItemElement = document.getElementById("addText");
  let text = addItemElement.value.slice(0, -1);
  if (text === ''|| text == null || text == undefined) {
    addItemElement.value = "";
    return;
  }
  document.getElementById("todoList").innerHTML += text + '<br/>';
  addItemElement.value = "";
  items[generateKey(text)] = text;
  save();
  port.postMessage({text: ""});
}

function hash(str) {
  return str.split("").reduce(function(a,b){a=((a<<5)-a)+b.charCodeAt(0);return a&a},0);              
}

function generateKey(text) {
  return `${Date.now().toString()}.${hash(text)}`;
}

function getItems() {
  chrome.storage.local.get([key], function(result) {
    if (!result[key]) return;
    items = JSON.parse(result[key]);
    document.getElementById("todoList").innerHTML = "";
    for (var item in items) {
      let todoList = document.getElementById("todoList");
      let div = document.createElement('div');
      let button = document.createElement('button');
      button.setAttribute('id', item);
      button.setAttribute('class', 'button');
      button.innerHTML = '&check;';
      button.addEventListener('click', (event) => removeItem(event));
      let clipboardButton = document.createElement('button');
      clipboardButton.innerHTML = '&boxbox;';
      clipboardButton.setAttribute('class', 'margin-right-half button');
      addListenerForClipboardButton(clipboardButton, items[item]);
      div.append(button);
      div.append(clipboardButton);
      div.append(items[item]);
      todoList.append(div);
    }
  });
}

function removeItem(event) {
  delete items[event.srcElement.id];
  save();
}

function save() {
  let elements = JSON.stringify(items);
  chrome.storage.local.set({[key]: elements}, () => {});
  getItems();
}

function addListenerForClipboardButton(button, value) {
  button.addEventListener("click", () => {
    let tmp = document.createElement("textarea");
    tmp.value = value;
    tmp.style.height = "0";
    tmp.style.overflow = "hidden";
    tmp.style.position = "fixed";
    document.body.appendChild(tmp);
    tmp.focus();
    tmp.select();
    document.execCommand("copy");
    document.body.removeChild(tmp);
  });
}
