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
"""Rest API over the warre api"""

from django.views import generic

from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils

from varroa_dashboard.api import security as api


@urls.register
class SecurityRisks(generic.View):
    """API for SecurityRisks."""

    url_regex = r'varroa/security-risks/$'

    @rest_utils.ajax()
    def get(self, request):
        """List security risks"""
        risks = api.get_security_risks(request)
        return {'items': [s.to_dict() for s in risks]}
