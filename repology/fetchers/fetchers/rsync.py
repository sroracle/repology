# Copyright (C) 2017 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import os

from repology.fetchers import Fetcher
from repology.logger import NoopLogger
from repology.subprocess import RunSubprocess


class RsyncFetcher(Fetcher):
    def __init__(self, url, fetch_timeout=60):
        self.url = url
        self.fetch_timeout = fetch_timeout

    def fetch(self, statepath, update=True, logger=NoopLogger()):
        if os.path.exists(statepath) and not update:
            logger.Log('no update requested, skipping')
            return

        command = ['rsync', '--verbose', '--archive', '--compress', '--delete', '--delete-excluded', '--safe-links', '--timeout', str(self.fetch_timeout), self.url, statepath]
        RunSubprocess(command, logger)
