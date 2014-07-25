#!/usr/bin/python
from subprocess import check_output
import commands
import sys
import json
import os.path
import argparse

def getLatestCommit(repo, branch, path):
    command = "pushd %s > /dev/null; git log -n 1 %s %s; popd > /dev/null" % (repo, branch, path)
    log = commands.getoutput(command)
    if(log.startswith("commit ")):
        return log[7:47]
    else:
        return None

def getLatestCommitMap(repo, branch, paths):
    results = {}
    for path in paths:
        hash = getLatestCommit(repo, branch, path)
        if hash != None:
            results[path] = hash
    return results

def getResponse(repo, branch, paths, callback):
    map = getLatestCommitMap(repo, branch, paths)
    text = json.dumps(map)
    if callback == None:
        return text
    else:
        return "%s(%s);" % (callback, text)
    

def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", required=True, metavar="repo", help="path to the root of the git repo")
    parser.add_argument("-b", metavar="branch", default="master", help="branch to search for latest commit")
    parser.add_argument("-c", metavar="callback", help="callback to use for jsonp")
    parser.add_argument("paths", nargs="*", help="relative file paths to lookup")
    argument_map = parser.parse_args(arguments)
    repo = os.path.abspath(argument_map.r)
    branch = argument_map.b
    paths = argument_map.paths
    callback = argument_map.c
    print getResponse(repo, branch, paths, callback)
    
    
if(__name__ == "__main__"):
    main(sys.argv[1:])

    
