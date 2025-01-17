#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import horizon
from openstack_dashboard.test import helpers as test

from varroa_dashboard.content.security import panel as security_panel


class TestVarroaDashboard(test.TestCase):
    def test_registered(self):
        project_dashboard = horizon.get_dashboard('project')

        panel_1 = project_dashboard.get_panel('security')
        self.assertEqual(security_panel.SecurityRisks, panel_1.__class__)
