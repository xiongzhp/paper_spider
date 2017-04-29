#coding:utf-8
"""journal"""
JOURNAL = [
	'pra',
	'prb',
	'prd'
]
"""paper tag"""
PAPER_TAG = [
    # '',
    'highlights', # Editors' Suggestion
    # 'recent', 
    # 'accepted'
]

URL = [(x+'/'+y) for x in JOURNAL for y in PAPER_TAG]