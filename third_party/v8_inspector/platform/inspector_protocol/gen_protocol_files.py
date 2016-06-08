# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os.path
import sys
import string
import optparse
import collections
import re
try:
    import json
except ImportError:
    import simplejson as json

input_file = open("../../devtools/protocol.json", "r")
json_string = input_file.read()
parsed_json = json.loads(json_string, object_pairs_hook=collections.OrderedDict)

js_protocol = collections.OrderedDict()
js_protocol["domains"] = []
browser_protocol = collections.OrderedDict()
browser_protocol["domains"] = []

for domain in parsed_json["domains"]:
    if domain["domain"] in ["Runtime", "Debugger", "Profiler", "HeapProfiler"]:
        js_protocol["domains"].append(domain)
    else:
        browser_protocol["domains"].append(domain)
browser_protocol["version"] = parsed_json["version"]
js_protocol["version"] = parsed_json["version"]

output_file = open("../../core/inspector/browser_protocol.json", "w")
json.dump(browser_protocol, output_file, indent=4, sort_keys=False, separators=(',', ': '))
output_file = open("../../platform/v8_inspector/js_protocol.json", "w")
json.dump(js_protocol, output_file, indent=4, sort_keys=False, separators=(',', ': '))





input_file = open("../../devtools/Inspector-1.1.json", "r")
json_string = input_file.read()
parsed_json = json.loads(json_string, object_pairs_hook=collections.OrderedDict)

js_protocol = collections.OrderedDict()
js_protocol["domains"] = []
browser_protocol = collections.OrderedDict()
browser_protocol["domains"] = []

for domain in parsed_json["domains"]:
    if domain["domain"] in ["Runtime", "Debugger", "Profiler", "HeapProfiler"]:
        js_protocol["domains"].append(domain)
    else:
        browser_protocol["domains"].append(domain)
browser_protocol["version"] = parsed_json["version"]
js_protocol["version"] = parsed_json["version"]

output_file = open("../../core/inspector/browser_protocol-1.1.json", "w")
json.dump(browser_protocol, output_file, indent=4, sort_keys=False, separators=(',', ': '))
output_file = open("../../platform/v8_inspector/js_protocol-1.1.json", "w")
json.dump(js_protocol, output_file, indent=4, sort_keys=False, separators=(',', ': '))
