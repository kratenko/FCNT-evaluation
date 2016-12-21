#!/usr/bin/env python
"""
Script for evaluation of FCNT results.

Simple quick'n'dirty python script to evaluate results produced by 
my fork of the FCNT tracking program
https://github.com/kratenko/FCNT

Created on 2016-12-14

@author: Peer Springstübe
"""
from rect import Rect

RUN_DIR = "/data/FCNT-evaluation/run3"
GT_DIR = "/data/data/tb100_unzipped"
ENDING = '.position.mat'

import os
import scipy.io
import numpy as np
import re
from matplotlib import pyplot as plt

tb50 = """Ironman
Matrix
MotorRolling
Soccer
Skiing
Freeman4
Freeman1
Skating1
Tiger2
Liquor
Coke
Football
FleetFace
Couple
Tiger1
Woman
Bolt
Freeman3
Basketball
Lemming
Singer2
Subway
CarScale
David3
Shaking
Sylvester
Girl
Jumping
Trellis
David
Boy
Deer
FaceOcc2
Dudek
Football1
Suv
Jogging.1
Jogging.2
MountainBike
Crossing
Singer1
Dog1
Walking
Walking2
Doll
Car4
David2
CarDark
Mhyang
FaceOcc1
Fish"""


def build_dist_fun(dists):
    def f(thresh):
        return (dists <= thresh).sum() / len(dists)
    return f


def build_over_fun(overs):
    def f(thresh):
        return (overs >= thresh).sum() / len(overs)
    return f


def load_rects(sname):
    a = scipy.io.loadmat(os.path.join(RUN_DIR, sname + ENDING))
    mrects = a['rects']
    r = []
    for i in range(len(mrects[0])):
        mr = mrects[0][i], mrects[1][i], mrects[2][i], mrects[3][i]
        r.append(Rect(mr))
    return r


def load_gt(sname):
    path = os.path.join(GT_DIR, sname, 'groundtruth_rect.txt')
    r = re.compile(r"(\d+)\D+(\d+)\D+(\d+)\D+(\d+)")
    rects = []
    with open(path, 'r') as tf:
        for line in tf:
            m = r.match(line)
            if m:
                rect = Rect(tuple(int(m.group(n)) for n in (1, 2, 3, 4)))
            else:
                rect = None
            rects.append(rect)
    return rects

all_rs = []
all_gts = []

for fname in os.listdir(RUN_DIR):
    if not fname.endswith(ENDING):
        continue
    sname = fname[:-len(ENDING)]

for sname in tb50.split("\n"):
    rs = load_rects(sname)
    gts = load_gt(sname)
    if sname == 'Football1':
        rs = rs[0:74]
    elif sname == 'Freeman4':
        rs = rs[0:283]
    elif sname == 'Freeman3':
        rs = rs[0:460]
    elif sname == 'Diving':
        rs = rs[0:215]
    elif sname == 'David':
        rs = rs[299:]
        gts = gts[299:]
    all_rs.extend(rs)
    all_gts.extend(gts)
    print("Sample:", sname, len(rs), len(gts), len(all_gts))
    assert len(rs) == len(gts)

# print(all_rs)
# print(all_gts)
cd = np.empty(len(all_rs))
ov = np.empty(len(all_gts))
print(len(cd), len(ov))
for n, (r, gt) in enumerate(zip(all_rs, all_gts)):
    if gt is None:
        print(n)
    cd[n] = r.center_distance(gt)
    ov[n] = r.overlap_score(gt)

dim = np.arange(1, len(cd) + 1)

dfun = build_dist_fun(cd)
ofun = build_over_fun(ov)

f = plt.figure()
x = np.arange(0., 50.1, .1)
y = [dfun(a) for a in x]
at20 = dfun(20)
tx = "prec(20) = %0.4f" % at20
plt.text(5.05, 0.05, tx)
plt.xlabel("center distance [pixels]")
plt.ylabel("occurrence")
plt.xlim(xmin=0, xmax=50)
plt.ylim(ymin=0.0, ymax=1.0)
plt.plot(x, y)
plt.show()

f = plt.figure()
x = np.arange(0., 1.001, 0.001)
y = [ofun(a) for a in x]
auc = np.trapz(y, x)
tx = "AUC = %0.4f" % auc
plt.text(0.05, 0.05, tx)
plt.xlabel("overlap score")
plt.ylabel("occurrence")
plt.xlim(xmin=0.0, xmax=1.0)
plt.ylim(ymin=0.0, ymax=1.0)
plt.plot(x, y)
plt.show()

exit()

