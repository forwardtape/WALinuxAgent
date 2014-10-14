# Windows Azure Linux Agent
#
# Copyright 2014 Microsoft Corporation
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
#
# Requires Python 2.4+ and Openssl 1.0+

import walinuxagent.utils.restutil as restutil
import walinuxagent.utils.osutil as osutil
from walinuxagent.protocol.contract import *

class ProtocolV1(Protocol):

    @staticmethod
    def Detect():
        #osutil.OpenPortForDhcp()
        pass

    @staticmethod
    def Init():
        return ProtocolV1()

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def getVmInfo(self):
        pass

    def getCerts(self):
        pass

    def getExtensions(self):
        pass

    def getOvf(self):
        pass

    def reportProvisionStatus(self):
        pass

    def reportAgentStatus(self):
        pass

    def reportExtensionStatus(self):
        pass

    def reportEvent(self):
        pass

