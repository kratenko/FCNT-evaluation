# FCNT-evaluation
Results of my executions of the FCNT visual tracker by Wang et al.

[TOC] 

## Benchmark and Data set
Basis for the evaluation is the visual tracker benchmark proposed by Wu et al., which is available at
http://cvlab.hanyang.ac.kr/tracker_benchmark/ or http://www.visual-tracking.net/

The data set of the benchmark originally consisted of 50 sequences and has later been extended 
to 100 samples. I refer to the original set of 50 sequences, as it has been introduced in 
the paper, as *tb-paper*, and to the full set of 100 sequences (as of writing) to *tb-100*. 

For reference, I'll list the names of the individual sequences for both sets.

### tb-paper sequences

    Basketball, Bolt, Boy, Car4, CarDark, CarScale, Coke, Couple, Crossing, David, David2, David3, Deer, Dog1, Doll, Dudek, FaceOcc1, FaceOcc2, Fish, FleetFace, Football, Football1, Freeman1, Freeman3, Freeman4, Girl, Ironman, Jogging.1, Jogging.2, Jumping, Lemming, Liquor, Matrix, Mhyang, MotorRolling, MountainBike, Shaking, Singer1, Singer2, Skating1, Skiing, Soccer, Subway, Suv, Sylvester, Tiger1, Tiger2, Trellis, Walking, Walking2, Woman

### tb-100 sequences

    Basketball, Biker, Bird1, Bird2, BlurBody, BlurCar1, BlurCar2, BlurCar3, BlurCar4, BlurFace, BlurOwl, Board, Bolt2, Bolt, Box, Boy, Car1, Car24, Car2, Car4, CarDark, CarScale, ClifBar, Coke, Couple, Coupon, Crossing, Crowds, Dancer2, Dancer, David2, David3, David, Deer, Diving, Dog1, Dog, Doll, DragonBaby, Dudek, FaceOcc1, FaceOcc2, Fish, FleetFace, Football1, Football, Freeman1, Freeman3, Freeman4, Girl2, Girl, Gym, Human2, Human3, Human4.2, Human5, Human6, Human7, Human8, Human9, Ironman, Jogging.1, Jogging.2, Jumping, Jump, KiteSurf, Lemming, Liquor, Man, Matrix, Mhyang, MotorRolling, MountainBike, Panda, RedTeam, Rubik, Shaking, Singer1, Singer2, Skater2, Skater, Skating1, Skating2.1, Skating2.2, Skiing, Soccer, Subway, Surfer, Suv, Sylvester, Tiger1, Tiger2, Toy, Trans, Trellis, Twinnings, Vase, Walking2, Walking, Woman

## Execution

My runs have been executed on an amd-64 pc running ubuntu linux 14.04, using five CPUs of model
*Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz* and a *GeForce GTX 980* GPU with 4GB memory.

The exact version of the software used can be found at https://github.com/kratenko/FCNT/releases/tag/evaluate1,
which is a tag in my fork of the [original FCNT repository](https://github.com/scott89/FCNT).

## Results

The following table lists the precission plot for 20 pixels (*proc(20)*) and the Area under Curve (*AUC*).
It includes the results claimed in the paper by Wang et al., three runs I performed, and the mean of all
my three runs (calculated at increased precision). My runs include results for both sets. The paper has
results only for the tb-paper data set.

| Run    | tb-paper proc(20) | tb-paper AUC | tb-100 proc(20) | tb-100 AUC |
|:-------|--------------:|---------:|---------------:|----------:|
| paper  | 0.856 | 0.599 | -- | -- |
| run1   | 0.837 | 0.638 | 0.753 | 0.553 |
| run2   | 0.831 | 0.631 | 0.766 | 0.555 |
| run3   | 0.857 | 0.644 | 0.765 | 0.558 |
| run1-3 | 0.842 | 0.638 | 0.761 | 0.555 |