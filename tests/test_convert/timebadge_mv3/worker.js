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

chrome.alarms.onAlarm.addListener(function( alarm ) {
  setBadgeText();
});

function setBadgeText() {
  let today = new Date();
  let h = maybePrependZero(today.getHours());
  let m = maybePrependZero(today.getMinutes());
  chrome.action.setBadgeText({text: `${h}${m}`});
}

function maybePrependZero(x) {
  return x < 10 ? "0" + x : x;
}

function clearBadgeText() {
  chrome.action.setBadgeText({text: ""});
}

function toggleAlarm() {
  chrome.alarms.getAll(function(alarms) {
    if (alarms.length > 0) {
      chrome.alarms.clearAll();
      clearBadgeText();
    } else {
      setBadgeText();
      createAlarm();
    }
  });
}

function createAlarm() {
  let date = new Date();
  let seconds = date.getSeconds();
  chrome.alarms.create("time", {
    periodInMinutes: 1,
    when: Date.now() + (60-seconds*1000)
  });
}

chrome.action.onClicked.addListener(() => toggleAlarm());
