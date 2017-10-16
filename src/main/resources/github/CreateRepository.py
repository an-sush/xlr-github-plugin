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
from org.eclipse.egit.github.core import Repository
from org.eclipse.egit.github.core import User
from org.eclipse.egit.github.core.client import GitHubClient
from org.eclipse.egit.github.core.service import RepositoryService

if host is None:
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

rs = RepositoryService(github_client)
github_user = User().setLogin(user)
new_repository = Repository()
new_repository.setOwner(github_user)
new_repository.setName(repositoryName)

if organization:
  new_repository = rs.createRepository(organization, new_repository)
else:
  new_repository = rs.createRepository(new_repository)

repositoryId = new_repository.getId()
print "Successfully created %s\n" % new_repository.getName()