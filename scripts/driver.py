#!/usr/bin/python3
#
# Simple driver to demonstrate usage
#
# Author: Jeanderson Candido
#
import json
import urllib.request

from ghwrappers.search import RepositoryQuery


def run(queryable):
    with urllib.request.urlopen(queryable.query()) as response:
        return json.loads(response.read().decode())


data = run(RepositoryQuery().lang("java").stars(">=100"))
print(data['total_count'])
