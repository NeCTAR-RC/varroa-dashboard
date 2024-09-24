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

from django.conf import settings
from horizon.utils.memoized import memoized
from keystoneauth1.identity import Token
from keystoneauth1 import session

from varroaclient import client as varroa_client


@memoized
def varroaclient(request, version="1"):
    """Initialization of Varroa client."""
    auth_url = getattr(settings, "OPENSTACK_KEYSTONE_URL", None)
    auth = Token(
        auth_url,
        token=request.user.token.id,
        project_id=request.user.project_id,
        domain_id=request.user.domain_id,
    )
    keystone_session = session.Session(auth=auth)

    return varroa_client.Client(
        version,
        session=keystone_session,
    )


def get_security_risks(request, **kwargs):
    """
    Retrieve security risks using the Varroa client.
    """
    return varroaclient(request).security_risks.list(**kwargs)
