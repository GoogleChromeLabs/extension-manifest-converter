# Extension Manifest Converter

Extension Manifest Converter is an open source tool that helps convert existing Chrome extensions to
Manifest V3. Use it to convert:

-  an entire unpacked directory
-  an extension zip file
-  just a manifest.json file.

After using the tool, complete the conversion using instructions in the [Migrate to Manifest
V3](https://developer.chrome.com/docs/extensions/migrating/) guide. This tool makes the conversions
listed below. To make completion of the upgrading easier, the titles and bullets below roughly
correspond to the wording of the headings and items in
[the migration guide's checklist](https://developer.chrome.com/docs/extensions/migrating/checklist/).

## Updates to the manifest

-  Changes the manifest version number. 
-  Updates the host permissions.

## Updates that migrate to a service worker

-  Upgrades the `"background"` field in the manifest.

## Updates to API calls

-  Replaces `tabs.executeScript()` with `scripting.executeScript()`. (If necessary, also adds
    `scripting` to the `permissions` array in the `manifest.json`.)
-  Replaces `tabs.insertCSS()` with `scripting.insertCSS()`. You will still need to
    [replace `tabs.removeCSS()` with `scripting.removeCSS()](https://developer.chrome.com/docs/extensions/migrating/api-calls/#replace-insertcss-removecss)`.
    (If necessary, also adds `scripting` to the `permissions` array in manifest.json.)
-  Replaces Browser Actions and Page Actions with Actions and makes related changes to the manifest.

## Improvement to extension security

-  Updates the content security policy.

## Limitations

This tool aims to simplify the MV3 conversion; it does not fully automate the process. Only search
and replace changes are applied to `.js` files.

This tool does not:

* update any service worker code that relies on the DOM.

## Installation

To use this tool, follow the steps below.

1. Make sure Python 3 is installed.

    ```bash
    python3 --version
    ```

    If you don't see a version number, follow your OS's guidance to install Python 3 or visit
    https://www.python.org/downloads/ to download a recent release.

2. Clone this repo using the below command.

    ```bash
    git clone https://github.com/GoogleChromeLabs/extension-manifest-converter
    ```

3. `cd` into the cloned project directory.

4. Execute the test command.

    ```bash
    python3 emc.py
    ```

    The tool logs basic usage information to the console.


## Usage

* Convert a directory

    ```bash
    python3 emc.py dir/path/
    ```

* Convert a manifest file

    ```bash
    python3 emc.py manifest.json
    ```

* Convert a .zip file

    ```bash
    python3 emc.py extension.zip
    ```
    
## License
[Apache 2.0](https://github.com/GoogleChromeLabs/extension-manifest-converter/blob/master/LICENSE)

This is not an official Google product.
