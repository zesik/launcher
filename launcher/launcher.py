#!/usr/bin/env python3
import sys
import os
import argparse
import difflib
import subprocess
from collections import OrderedDict


DEFAULT_CONFIG = 'launcher.conf'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name',
                        nargs='?',
                        help='name of the launcher')
    parser.add_argument('-q', '--query',
                        action='store_true',
                        help='query launchers instead of running')
    parser.add_argument('--limit',
                        type=int,
                        default=0,
                        help='max items to display')
    parser.add_argument('--config',
                        default=DEFAULT_CONFIG,
                        help='config file name')
    args = parser.parse_args()
    if not args.name:
        name = ''
    else:
        name = args.name.strip()
    if args.query:
        return query(args.config, name, args.limit)
    else:
        if not name:
            print("Error: launcher name empty")
            return 1
        return launch(args.config, name)


def read_source(file_name):
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             file_name)
    result = {}
    if not os.path.isfile(file_name):
        return OrderedDict()
    with open(file_name) as f:
        title = None
        for line in f:
            if title is None:
                title = line
            else:
                result[title.strip()] = line.strip()
                title = None
    return OrderedDict(sorted(result.items(), key=lambda t: t[0]))


def launch(config, keyword):
    source = read_source(config)
    for title, action in source.items():
        if title == keyword:
            print(action)
            return subprocess.call(action, shell=True)
    print("Error: no launcher matching provided name")
    return 1


def query(config, keyword, limit):
    source = read_source(config)
    matches = get_match(source, keyword)
    if len(matches):
        if limit > 0 and len(matches) > limit:
            matches = matches[:limit]
        print('\n'.join(['%s' % r['title'] for r in matches]))
    return 0


def get_match(source, keyword):
    result = []
    keyword = keyword.strip()
    index = 0
    for title, action in source.items():
        if len(keyword) == 0:
            result.append({
                'title': title,
                'titleHighlight': [],
                'rank': -index
                })
            index += 1
            continue
        r = compare_difflib(keyword, title)
        if r:
            result.append({
                'title': title,
                'titleHighlight': r['highlight'],
                'rank': r['rank'],
                })
    return sorted(result, key=lambda x:-x['rank'])


def compare_difflib(keyword, target, case_sensitive=False):
    def get_rank(s1, s2):
        if len(s1) != len(s2):
            return 0
        rank = 0
        for i in range(0, len(s1)):
            if s1[i] == s2[i]:
                rank += 2
            else:
                rank += 1
        return rank

    keyword = keyword.strip()
    if len(keyword) == 0:
        return None

    if case_sensitive:
        compare_keyword = keyword
        compare_target = target
    else:
        compare_keyword = keyword.lower()
        compare_target = target.lower()

    m = difflib.SequenceMatcher(None, compare_keyword, compare_target)
    highlight = []
    rank = 0
    for (op, i1, i2, j1, j2) in m.get_opcodes():
        if op == 'equal':
            highlight.append((j1, j2 - j1))
            rank += ((j2 - j1) ** 2)
            rank += get_rank(keyword[i1:i2], target[j1:j2])
        elif op == 'replace' or op == 'delete':
            rank = 0
            break
    if rank > 0:
        return {
            'highlight': highlight,
            'rank': rank
        }
    return None


if __name__ == '__main__':
    sys.exit(main())
