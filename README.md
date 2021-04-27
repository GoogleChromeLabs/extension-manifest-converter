Extension Manifest Converter is an open source tool to convert existing Chrome extensions to
Manifest V3. Use it to convert an entire directory, extension zip file, or just a manifest.json
file. All expected changes are applied to manifest.json.

## Features

* Performs conversions on
  * unpacked extension directories
  * zip files containing an extension
  * manifest.json
* General manifest.json conversions
  * Updates `manifest_version` field
  * Converts between host permissions declared in `permissions` or `optional_permissions` in MV2 and
    `host_permissions` in MV3
  * Converts between a `content_security_policy` string in MV2 and `content_security_policy` object
    with`extension_pages` and `sandbox` properties in MV3
  * Converts between `background.scripts` in MV2 and background service workers
    `background.service_worker` in MV3
* Scripting API conversions
  * Converts `chrome.tabs.executeScript` in MV2 to `chrome.scripting.executeScript` in MV3. If
    necessary, also adds `scripting` to the `permissions` array in manifest.json.
  * Converts `chrome.tabs.insertCSS` in Mv2 to `chrome.scripting.insertCSS` in MV3. If necessary,
    also adds `scripting` to the `permissions` array in manifest.json.
* Action API conversions
  * Converts calls to `chrome.browserAction` and `chrome.pageAction` in MV2 into `chrome.action` in
    MV3
  * Converts `browser_action` and `page_action` manifest entries in MV2 into `action` in MV3

## Limitations

This tool aims to simplify the MV3 conversion; it does not fully automate the process. Only search
and replace changes are applied to `.js` files.

This tool does not:

* update any service worker code that relies on a DOM

## Installation

To use this tool, you will first need Python 3 installed on your sytem.

Next, clone this repository locally.

```bash
git clone https://github.com/GoogleChromeLabs/extension-manifest-converter
```

cd into the project's directory and execute the following command to verify that you can run the
tool.

```bash
python3 extension.py
```

## Usage

Convert a directory

```bash
python3 extension.py dir/path/
```

Convert a manifest file

```bash
python3 extension.py manifest.json
```

Convert a .zip file

```bash
python3 extension.py extension.zip
```
