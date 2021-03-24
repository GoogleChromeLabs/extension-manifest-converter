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

// Saves options to chrome.storage
function save_options() {
  var fontSize = document.getElementById('font-size').value;
  chrome.storage.local.set({
    todoListFontSize: fontSize
  }, function() {
    setFontSize(fontSize);
    // Update status to let user know options were saved.
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function() {
      status.textContent = '';
    }, 1000);
  });
}

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
function restoreFontSize() {
  chrome.storage.local.get({
    todoListFontSize: '90'
  }, function(items) {
    setFontSize(items.todoListFontSize);
  });
}

function setFontSize(size) {
  document.body.style.fontSize = size + '%';
}

document.addEventListener('DOMContentLoaded', restoreFontSize());
document.getElementById('save').addEventListener('click',
    save_options);
