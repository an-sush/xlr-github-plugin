#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
from org.eclipse.egit.github.core import Reference
from org.eclipse.egit.github.core.client import GitHubClient
from org.eclipse.egit.github.core.client import GitHubRequest

if not host:
  github_client = GitHubClient().setCredentials(user, password)
elif (not port) and (not scheme):
  github_client = GitHubClient(host).setCredentials(user, password)
elif port and scheme:
  github_client = GitHubClient(host, port, scheme).setCredentials(user, password)
else:
  print "Valid combinations for host, port, scheme are:\n"
  print "(1) host not given, port not given, scheme not given:  public GitHub (https://github.com)\n"
  print "(2) host given, port not given, scheme not given:  GitHub Enterprise (https://host)\n"
  print "(3) host given, port given, scheme given:  GitHub Enterprise (scheme://host:port)\n"
  sys.exit(1)

if organization:
  geturi = "/repos/%s/%s/git/refs/heads/%s" % (organization, repositoryName, oldBranch)
  posturi = "/repos/%s/%s/git/refs" % (organization, repositoryName)
else:
  geturi = "/repos/%s/%s/git/refs/heads/%s" % (user, repositoryName, oldBranch)
  posturi = "/repos/%s/%s/git/refs" % (user, repositoryName)

request = GitHubRequest()
request.setType(Reference)
request.setUri(geturi)
ref = github_client.get(request).getBody()
params = {"ref" : ref.getRef().replace(oldBranch, newBranch), "sha" : ref.getObject().getSha()}
github_client.post(posturi, params, Reference)
print "Branch %s has been created" % newBranch
