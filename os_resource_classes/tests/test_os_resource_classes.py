# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os_resource_classes as orc
from os_resource_classes.tests import base


class TestSymbols(base.TestCase):

    def test_resource_classes(self):
        vcpu = orc.VCPU
        self.assertEqual("VCPU", vcpu.name)
        self.assertEqual(0, vcpu.code)
        self.assertEqual("1.0", vcpu.version_added)
        self.assertIsNone(vcpu.version_deprecated)
