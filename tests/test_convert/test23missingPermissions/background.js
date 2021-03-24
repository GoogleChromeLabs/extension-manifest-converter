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

chrome.browserAction.onClicked.addListener(tab => {
  chrome.tabs.executeScript(
    null,
    {
      code: 'alert("1 from code.");'
    }
  );
});

/*
The logic to handle a convenience method would be trickier.
Each of the callsites would need to do something different.
Maybe it would work anyway, but it's unlikly without care. e.g.

function execute(tab, code) {
  chrome.tabs.executeScript(
    tab,
    {code: code},
  );
}
*/
