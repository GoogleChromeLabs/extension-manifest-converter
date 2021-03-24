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

var items = [];
var textarea = "";

chrome.runtime.onConnect.addListener(function(port) {
  if (port.name === "popup") {
    chrome.storage.local.get([key], function(result) {
      if (result[key]) {
        textarea = result[key];
        port.postMessage({text: textarea});
      }
    });

    port.onDisconnect.addListener(function() {
      save();
    });

    port.onMessage.addListener(function(msg) {
      textarea = msg.text;
    });
  }
});

var key = 'todoListTextarea';

function save() {
  chrome.storage.local.set({[key]: textarea}, () => {});
}
