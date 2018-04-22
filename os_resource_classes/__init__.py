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

import pbr.version

THIS_NAME = __name__

__version__ = pbr.version.VersionInfo(THIS_NAME).version_string()

VERSION_HISTORY = (
    # "original" resource classes before custom resource classes existed
    # Only the VCPU, MEMORY_MB and DISK_GB resource classes were used.
    '1.0',
    # Addition of VGPU and VGPU_DISPLAY_HEAD resource classes.
    # VGPU_DISPLAY_HEAD resource class was a mistake and never used.
    '1.1',
    # Initial version of os_resource_classes library when broken out of Nova.
    # The VCPU, MEMORY_MB, DISK_GB and VGPU resource classes were used in the
    # Nova codebase. All other resource classes were deprecated and their codes
    # tombstoned.
    '1.2',
)

# Any user-specified resource class name is prefixed with the custom namespace
CUSTOM_NAMESPACE = 'CUSTOM_'


class ResourceClass(object):

    def __init__(self, name, code=None, version_added=None,
                 version_deprecated=None):
        """A resource class is something that can be consumed from a resource
        provider.

        :param name: String name for the resource class
        :param code: Integer code for the resource class
        :param version_added: String version ("$MAJOR.$MINOR") that the
                              resource class was introduced to the
                              os_resource_classes library
        :param version_deprecated: Optional version ("$MAJOR.MINOR") that the
                                   resource class was deprecated. When a
                                   resource class is deprecated, its code is
                                   essentially tombstoned. No future resource
                                   class may use that code.
        """
        self.name = name
        self.code = code
        self.version_added = version_added
        self.version_deprecated = version_deprecated

    def is_custom(self):
        return self.name.startswith(CUSTOM_NAMESPACE)

    def is_deprecated(self):
        return self.deprecated_version is not None

    def __repr__(self):
        return "<ResourceClass(name={0}, code={1})".format(self.name,
                                                           self.code)


VCPU = ResourceClass('VCPU', code=0, version_added='1.0')
MEMORY_MB = ResourceClass('MEMORY_MB', code=1, version_added='1.0')
DISK_GB = ResourceClass('DISK_GB', code=2, version_added='1.0')

# Deprecated - never used in the codebase
PCI_DEVICE = ResourceClass('PCI_DEVICE', code=3, version_added='1.0',
                           version_deprecated='1.2')
# Deprecated - never used in the codebase
SRIOV_NET_VF = ResourceClass('SRIOV_NET_VF', code=4, version_added='1.0',
                             version_deprecated='1.2')
# Deprecated - never used in the codebase
NUMA_SOCKET = ResourceClass('NUMA_SOCKET', code=5, version_added='1.0',
                            version_deprecated='1.2')
# Deprecated - never used in the codebase
NUMA_CORE = ResourceClass('NUMA_CORE', code=6, version_added='1.0',
                          version_deprecated='1.2')
# Deprecated - never used in the codebase
NUMA_THREAD = ResourceClass('NUMA_THREAD', code=7, version_added='1.0',
                            version_deprecated='1.2')
# Deprecated - never used in the codebase
NUMA_MEMORY_MB = ResourceClass('NUMA_MEMORY_MB', code=8, version_added='1.0',
                               version_deprecated='1.2')
# Deprecated - never used in the codebase
IPV4_ADDRESS = ResourceClass('IPV4_ADDRESS', code=9, version_added='1.0',
                             version_deprecated='1.2')

VGPU = ResourceClass('VGPU', code=10, version_added='1.1')
# Deprecated - This was a mistake. The display heads are not consumable
# resources. Never used in the codebase
VGPU_DISPLAY_HEAD = ResourceClass('VGPU_DISPLAY_HEAD', code=11,
                                  version_added='1.1',
                                  version_deprecated='1.2')
