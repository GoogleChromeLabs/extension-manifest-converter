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

document.addEventListener("DOMContentLoaded", ready);

function ready() {
  document.getElementById("btnGetLinksText").addEventListener('click', () => {
    let div = document.getElementById('divResult');
    div.innerHTML = '<br />';
    div.style.width = 600;
    chrome.tabs.query({currentWindow: true}, tabs => {
      tabs.forEach(tab => {
        div.innerHTML += tab.title + '. '  + tab.url + '<br />';
      });
    });
  });

  document.getElementById("btnGetLinksHtml").addEventListener('click', () => {
    let div = document.getElementById('divResult');
    div.innerHTML = '<br />';
    div.style.width = 600;
    chrome.tabs.query({currentWindow: true}, tabs => {
      tabs.forEach(tab => {
        div.innerHTML += '<a href="' + tab.url + '">' + tab.title + '</a><br />';
      });
    });
  });

  document.getElementById("btnCopyLinksText").addEventListener('click', () => {
    console.log('clicked2');
    let result = "";
    chrome.tabs.query({currentWindow: true}, tabs => {
      tabs.forEach(tab => {
        result += tab.title + '. '  + tab.url + '\n';
      });
      copyPlainTextToClipboard(result);
    });
  });
  
  document.getElementById("btnCopyLinksHtml").addEventListener('click', () => {
    console.log('clicked');
    let result = "";
    chrome.tabs.query({currentWindow: true}, tabs => {
      tabs.forEach(tab => {
        console.log(5);
        result += '<a href="' + tab.url + '">' + tab.title + '</a><br />';
      });
      copyRichTextToClipboard(result);
    });
  });
}

function copyRichTextToClipboard(text) {
  const listener = function(ev) {
    ev.preventDefault();
    ev.clipboardData.setData('text/html', text);
    ev.clipboardData.setData('text/plain', text); // is this line needed?
  };
  document.addEventListener('copy', listener);
  document.execCommand('copy');
  document.removeEventListener('copy', listener);
}

function copyPlainTextToClipboard(text) {
  const listener = function(ev) {
    ev.preventDefault();
    ev.clipboardData.setData('text/plain', text);
  };
  document.addEventListener('copy', listener);
  document.execCommand('copy');
  document.removeEventListener('copy', listener);
}
