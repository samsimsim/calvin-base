# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import umsgpack
from message_coder import MessageCoderBase
import json

umsgpack.compatibility = True

# set of functions to encode/decode data tokens to/from a json description
class MessageCoder(MessageCoderBase):

    def encode(self, data):
        print "Encode: %s" % json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        return umsgpack.packb(data)

    def decode(self, data):
        data = umsgpack.unpackb(data)
        print "Decode: %s" % json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        return data
